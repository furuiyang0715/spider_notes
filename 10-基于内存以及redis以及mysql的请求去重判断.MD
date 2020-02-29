### 示例代码
```shell script
# 基于信摘要算法进行去重判断以及存储的几种存储容器实现方案。
# 但是未在存储容器中保留数据的状态。

# 1. 基于内存的存储
# 2. 基于redis的存储
# 3. 基于mysql的存储
import sys

import redis
import six
import hashlib


class BaseFilter(object):
    """基于信息摘要算法进行数据的去重以及判断"""
    def __init__(self, hash_func_name='md5',
                 redis_host='localhost',
                 redis_port=6379,
                 redis_db=15,
                 redis_key='filter',
                 mysql_url=None,

                 ):
        self.hash_func = getattr(hashlib, hash_func_name)
        self.redis_host = redis_host
        self.redis_port = redis_port
        self.redis_db = redis_db
        self.redis_key = redis_key
        self.mysql_url = mysql_url
        self.storage = self._get_storage()

    def _get_storage(self):
        """
        获取去重容器对象
        在具体的子类中实现
        :return:
        """
        pass

    def _safe_date(self, data):
        """
        python2 str --> python3 bytes
        python2 unicode --> python3 str
        :param data: 给定的原始数据
        :return: 二进制类型的字符串数据
        """
        if six.PY3:
            if isinstance(data, bytes):
                return data
            elif isinstance(data, str):
                return data.encode()
            else:
                raise Exception("请提供字符串数据")
        # elif six.PY2:
        #     if isinstance(data, str):
        #         return data
        #     elif isinstance(data, unicode):
        #         return data.encode()
        #     else:
        #         raise Exception("请提供字符串数据")

    def _get_hash_value(self, data):
        """
        根据给定的数据 返回对应的 hash 摘要信息
        :param data:
        :return:
        """
        # 创建一个 hash 对象
        hash_obj = self.hash_func()
        hash_obj.update(self._safe_date(data))
        hash_value = hash_obj.hexdigest()
        return hash_value

    def save(self, data):
        """
        根据 data 计算出对应的指纹进行存储
        :param data:
        :return:
        """
        hash_value = self._get_hash_value(data)
        return self._save(hash_value)

    def _save(self, hash_value):
        """
        交给对应的子类去具体实现
        :param hash_value:
        :return:
        """
    def is_exist(self, data):
        """
        判断给定的数据是否存在
        :param data:
        :return:
        """
        hash_value = self._get_hash_value(data)
        return self._is_exist(hash_value)

    def _is_exist(self, hash_value):
        """
        交给对应的子类去实现
        判断的结果是 True 或者是 False
        :param hash_value:
        :return:
        """


class MemoryFilter(BaseFilter):
    """
    基于 python 中的 set 结构进行去重判断依据的存储

    基于内存的存储数据是临时的，一次运行之后就会销毁
    """

    def _get_storage(self):
        return set()

    def _save(self, hash_value):
        """
        利用 set 进行存储
        :param hash_value:
        :return:
        """
        self.storage.add(hash_value)  # 向 set 中添加数据

    def _is_exist(self, hash_value):
        if hash_value in self.storage:
            return True
        else:
            return False


class RedisFilter(BaseFilter):
    """
    基于redis的持久化存储的去重判断依据的实现

    在一次存储之后数据将永久存在 方便起见增加了重启容器 即清空现有数据的接口
    """
    def restart(self):
        """
        重启存储容器
        """
        self.storage.delete(self.redis_key)

    def _get_storage(self):
        """
        返回一个 redis 连接对象
        :return:
        """
        # client = redis.StrictRedis(host='localhost', port=6379, db=15)
        # return client

        # 增加 redis 连接对象的复用性
        pool = redis.ConnectionPool(host=self.redis_host,
                                    port=self.redis_port,
                                    db=self.redis_db)
        client = redis.StrictRedis(connection_pool=pool)
        return client

    def _save(self, hash_value):
        """
        利用 redis 的无序集合进行存储
        :param hash_value:
        :return:
        """
        return self.storage.sadd(self.redis_key, hash_value)

    def _is_exist(self, hash_value):
        """
        判断 redis 的无序集合中是否有对应的判断依据
        :param hash_value:
        :return:
        """
        # if self.storage.sismember(self.redis_key, hash_value):
        #     return True
        # else:
        #     return False
        return self.storage.sismember(self.redis_key, hash_value)


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Filter(Base):
    __tablename__ = "filter"  # 对应mysql中的表名
    id = Column(Integer, primary_key=True)
    hash_value = Column(String(40), index=True, unique=True)  # 索引且唯一


class MqlFilter(BaseFilter):
    """
    基于 mysql 的去重判断依据的存储

    数据是持久化存储的 所以同样添加一个数据库重启的方法
    """

    def restart(self):
        """
        重启存储容器
        """
        session = self.storage()
        ret = session.query(Filter).delete()
        print(">>> ", ret)
        session.commit()
        session.close()

    def _get_storage(self):
        """
        返回一个 mysql 的连接对象 （在此处为 sqlalchemy 的连接对象）
        :return:
        """
        engine = create_engine(self.mysql_url)
        Base.metadata.create_all(engine)    # 创建表 如果已有就忽略
        session = sessionmaker(engine)
        return session

    def _save(self, hash_value):
        """
        利用 mysql 数据库进行存储
        :param hash_value:
        :return:
        """
        session = self.storage()
        _filter = Filter(hash_value=hash_value)
        session.add(_filter)
        session.commit()
        session.close()

    def _is_exist(self, hash_value):
        """
        判断 mysql 数据库中是否有对应的判断依据
        :param hash_value:
        :return:
        """
        session = self.storage()
        ret = session.query(Filter).filter_by(hash_value=hash_value).first()
        session.close()
        if ret is None:
            return False
        else:
            return True


def test_mysql():
    f = MqlFilter(mysql_url="mysql+pymysql://root:ruiyang@127.0.0.1:3306/test_db?charset=utf8")
    f.restart()
    datas = ['ruiyang', 'Ruiyang', '33', 'pwd', "11", "22", "33", "ruiyang"]
    for d in datas:
        if f.is_exist(d):
            print("{} 数据已经存在".format(d))
            # print(f.storage)
        else:
            f.save(d)
            print("添加数据 {}".format(d))


def test_redis():
    # 测试基于 redis 的去重过滤器
    f = RedisFilter()
    f.restart()
    datas = ['ruiyang', 'Ruiyang', '33', 'pwd', "11", "22", "33", "ruiyang"]
    for d in datas:
        if f.is_exist(d):
            print("{} 数据已经存在".format(d))
            # print(f.storage)
        else:
            f.save(d)
            print("添加数据 {}".format(d))


def test_memory():
    # 测试基于 memory 的去重过滤器
    f = MemoryFilter()
    datas = ['ruiyang', 'Ruiyang', '33', 'pwd', "11", "22", "33", "ruiyang"]
    for d in datas:
        if f.is_exist(d):
            print("{} 数据已经存在".format(d))
            # print(f.storage)
        else:
            f.save(d)
            print("添加数据 {}".format(d))


# test_memory()

# test_redis()

# test_mysql()

```