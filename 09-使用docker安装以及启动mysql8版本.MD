```shell script
使用 docker 安装 mysql8 版本

# docker 中下载 mysql
docker pull mysql

# 启动
docker run --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=ruiyang -d mysql

# 进入容器
docker exec -it mysql bash

# 登录 mysql
mysql -u root -p
ALTER USER 'root'@'localhost' IDENTIFIED BY 'ruiyang';

# 添加远程登录用户
CREATE USER 'kailun'@'%' IDENTIFIED WITH mysql_native_password BY 'ruiyang';
GRANT ALL PRIVILEGES ON *.* TO 'kailun'@'%';

# 容器外部连接 
mysql -h 127.0.0.1  -uroot -p
```