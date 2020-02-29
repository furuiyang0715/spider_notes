初始化 redis 连接： 
直接连： r = redis.Redis(host='127.0.0.1',port=6379,password='123456',db=0,decode_responses=True) 
或者是：  r = redis.StrictRedis(host='10.10.2.14',port=6379,password='123456',decode_responses=True) 

使用连接池：
pool = redis.ConnectionPool(host='127.0.0.1',port=6379,password='123456',decode_responses=True)
r = redis.Redis(connection_pool=pool)  
或者是: r = redis.StrictRedis(connection_pool=pool) 


使用连接池的好处： 
管理对一个redis server的所有连接，避免每次建立，释放连接的开销。默认，每个redis实例都会维护一个自己的连接池，
可以直接建立一个连接池，作为参数传给redis，这样可以实现多个redis实例共享一个连接池。
