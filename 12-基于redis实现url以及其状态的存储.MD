改写自基于leveldb的情况
```python
import sys
import traceback
import redis

class RedisUrlDB(object):
    status_failure = "0"
    status_success = "1"

    def __init__(self, redis_db=0, redis_host="127.0.0.1", redis_port=6379):
        self.redis_db = redis_db
        self.redis_host = redis_host
        self.redis_port = redis_port
        self.storage = self._get_storage()

    def _get_storage(self):
        pool = redis.ConnectionPool(host=self.redis_host,
                                    port=self.redis_port,
                                    db=self.redis_db)
        client = redis.StrictRedis(connection_pool=pool)
        return client

        # pool = redis.ConnectionPool(host='127.0.0.1', port=6379, decode_responses=True)
        # r = redis.Redis(connection_pool=pool)
        # return r

    def set_success(self, url):
        """
        存储 url 并且设置 url 状态为成功
        """
        try:
            self.storage.set(url, self.status_success)
            s = True
        except Exception as e:
            print(">>> ", e)
            # traceback.print_exc()
            s = False
        return s

    def set_fail(self, url):
        """
        存储 url 并且设置 url 状态为失败
        """
        try:
            self.storage.set(url, self.status_failure)
        except Exception as e:
            print(">>> ", e)
            return False
        return True

    def has(self, url):
        try:
            ret = self.storage.get(url)
            # 插入的时候可以直接使用字符串 redis客户端会自己进行封装以及处理
            # 查询取出的时候, value 值是二进制的，需要自行解码
            # print("<<< ", ret)
            return bool(ret)
        except:
            return False


if __name__ == "__main__":
    rdb = RedisUrlDB()
    storage = rdb.storage
    ret = rdb.set_success("ruiyang")
    # ret = rdb.set_fail("失败的 url ")
    # print(ret)
    print(rdb.has("ruiyang"))

```