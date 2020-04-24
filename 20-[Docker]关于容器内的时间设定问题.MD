在 docker logs -t 查看容器日志的过程中遇到一个问题, 就是容器显示时间与当前时间不一致。 

但是进入容器中执行 date 命令，得到的时间是正确且经过调整的。 


linux 中 ln 的功能是为某一个文件在另外一个位置建立一个同步的链接。
常用的命令参数: 
```shell script
-b 删除, 覆盖以前建立的链接
-d 允许超级用户制作目录的硬链接
-f 强制执行
-i 交互模式, 文件存在则提示用户是否覆盖
-n 把符号链接视为一般目录
-s 软链接(符号链接)
-v 显示详细的处理过程
```

```
TZ=Asia/Shanghai 
ln -snf /usr/share/zoneinfo/$TZ /etc/localtime 
echo $TZ > /etc/timezone
```

