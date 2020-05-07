### 参考
# http://sinhub.cn/2018/11/apscheduler-user-guide/
# https://pypi.org/project/APScheduler/
# https://apscheduler.readthedocs.io/en/latest/
# https://github.com/agronholm/apscheduler/tree/master/examples/?at=master

### 安装
# pip install apscheduler

### 简介
# APScheduler ，全称是 Advanced Python Scheduler,
# APScheduler 内置了三种调度系统：
#
# Linux Cron 风格的调度系统（并有可选的开始和结束时间）
# 基于时间间隔的执行调度（周期性地运行作业 job ，并有可选的开始和结束时间）
# 只执行一次的延后执行作业调度（只执行一次作业 job ，在设定的日期 date 或时间 time 执行）
# APScheduler 可以配合多种不同的作业存储后端一起使用，目前支持以下的作业存储后端：
#
# 内存 Memory
# SQLAlchemy (任何 SQLAlchemy 支持的关系型数据库)
# MongoDB
# Redis
# RethinkDB
# ZooKeeper
# APScheduler 也可以集成到几个常见的 Python 框架中，如：
#
# asyncio
# gevent
# Tornado
# Twisted
# Qt（使用 PyQt 或 PySide）

### 基本组件
# APScheduler 有如下四种组件：
#
# triggers 触发器:
# 包含具体的角度逻辑。每个 job 都会有自己的触发器，由它来决定下一个要运行的 job 。在触发器被初始化配置之前，它们都是完全无状态（stateless）的。
# job stores 作业存储:
# 存放被调度的 job 。默认的作业存储只是简单地将作业存储在内存中，但也可以存储到各种数据库中。当一个 job 保存到一个持久化地作业存储中时，其数据必须要被序列化（serialized），当它们被加载回来时再执行反序列化（deserialized）。非默认的作业存储不会将作业数据保存到内存中，相反，内存会作为后端存储介质在保存、加载、更新和搜索 job 过程中的中间人。作业存储不会在调度器（scheduler）之间共享。
# executors 执行器:
# 负责处理运行中的作业。通常它们都是负责将 job 中指定的可调用的部分提交到线程或进程池。当 job 完成后，执行器会通知（notifies）调度器，由调度器随后发出（emits）一个恰当的事件（event）。
# schedulers 调度器:
# 调度器负责将以上的东西结合在一起。一般情况下，你的应用程序只会有一个调度器在运行。应用程序的开发者通常不用直接面对 trigger ， job stores 以及 executor ，相反，调度器会提供合适的接口让开发者去管理它们 —— 通过调度程序来配置 job stores 和 executor 来实现诸如添加、修该和删除 job 。

### 如何选择合适的 scheduler、job stores、executor 和 trigger
