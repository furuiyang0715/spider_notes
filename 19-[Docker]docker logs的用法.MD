### docker logs 的常见用法 
基本用法: docker logs --help 
```shell script
$ docker logs [OPTIONS] CONTAINER
  Options:
        --details        显示更多的信息
    -f, --follow         跟踪实时日志
        --since string   显示自某个 timestamp 之后的日志, 或相对时间, 如 42m (即42分钟)
        --tail string    从日志末尾显示多少行日志, 默认是 all
    -t, --timestamps     显示时间戳
        --until string   显示自某个 timestamp 之前的日志, 或相对时间, 如 42m (即42分钟) 
```

查看指定的时间后固定的 100 行日志: 
```shell script
docker logs -ft --since='2020-04-23' --tail 1000 container_id  
```

查看最近 30 分钟的日志: 
```shell script
docker logs --since 30m container_id 
```

查看某个时间段内的日志: 
```shell script
docker logs --since='2020-04-23' --until='2020-04-24'  container_id
```
