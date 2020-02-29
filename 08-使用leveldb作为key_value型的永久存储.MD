LevelDB是Google开源的一个key-value数据库，速度非常快，同时自动压缩数据。我们用它先来实现一个UrlDB作为永久存储数据库。 

代码示例: 
```python 
import sys

import leveldb


class UrlDB:
    '''Use LevelDB to store URLs what have been done(succeed or faile)

    提供的功能： (1) 将成功或者失败状态的 url 存储到 key-value 数据库中
    (2) 判断给定的 url 在数据库中是否存在。
    '''
    status_failure = b'0'
    status_success = b'1'

    def __init__(self, db_name):
        self.name = db_name + '.urldb'
        # 生成一个文件夹 ..
        self.db = leveldb.LevelDB(self.name)

    def set_success(self, url):
        # 存储 url 状态为成功
        if isinstance(url, str):
            # 数据要编码为 二进制 才能进行存储以及查询
            url = url.encode('utf8')
        try:
            self.db.Put(url, self.status_success)
            s = True
        except:
            s = False
        return s

    def set_failure(self, url):
        # 存储 url 状态为失败
        if isinstance(url, str):
            url = url.encode('utf8')
        try:
            self.db.Put(url, self.status_failure)
            s = True
        except:
            s = False
        return s

    def has(self, url):
        # 查看数据库中是否已经存在该 url
        if isinstance(url, str):
            url = url.encode('utf8')
        try:
            attr = self.db.Get(url)
            return bool(attr)
        except:
            pass
        return False


if __name__ == "__main__":
    db = UrlDB("test.urldb")
    print(db.set_success("ruiyang"))
    print(db.set_failure("furuiyang"))
    print(db.has("kailun"))
    print(db.has("ruiyang"))
    sys.exit(0)
```