# 解决 apscheduler 中出现警告"skipped: maximum number of running instances reached (1)"

### 参考:
https://blog.csdn.net/wyongqing/article/details/50320601

### 重现问题脚本
```python
import time
import tornado.ioloop
from apscheduler.triggers.date import DateTrigger
from apscheduler.schedulers.tornado import TornadoScheduler

sched = TornadoScheduler()


def child_job():
    """创建一个执行时间为 60 s 的任务"""
    print("start")
    time.sleep(60)
    print("end")


def main_job():
    sched.add_job(child_job, trigger=DateTrigger(), id="123")


if __name__ == "__main__":
    # 每 5 s 执行一次任务
    sched.add_job(main_job, 'interval', seconds=5)
    sched.start()
    tornado.ioloop.IOLoop.instance().start()


'''问题复现：
python sche1.py
start
WARNING:apscheduler.scheduler:Execution of job "child_job (trigger: date[2020-05-07 11:15:49 CST], next run at: 2020-05-07 11:15:49 CST)" skipped: maximum number of running instances reached (1)
WARNING:apscheduler.scheduler:Execution of job "child_job (trigger: date[2020-05-07 11:15:54 CST], next run at: 2020-05-07 11:15:54 CST)" skipped: maximum number of running instances reached (1)

'''
```

### 分析问题
缺乏资料，所以根据提示，分析 apscheduler 源码, 记录异常位置, 在源码目录下，搜索关键字maxinum，找到记录异常的位置:
```python
# apscheduler/schedulers/base.py
if run_times:
    try:
        executor.submit_job(job, run_times)
    except MaxInstancesReachedError:
        self._logger.warning(
            'Execution of job "%s" skipped: maximum number of running instances reached (%d)',
            job, job.max_instances)
    except:
        self._logger.exception('Error submitting job "%s" to executor "%s"', job, job.executor)

```
继续看submit_job函数，找到异常抛出位置:
```python
# apscheduler/executors/base.py
def submit_job(self, job, run_times):
    """
    Submits job for execution.

    :param Job job: job to execute
    :param list[datetime] run_times: list of datetimes specifying when the job should have been run
    :raises MaxInstancesReachedError: if the maximum number of allowed instances for this job has been reached
    """

    assert self._lock is not None, 'This executor has not been started yet'
    with self._lock:
        if self._instances[job.id] >= job.max_instances:
            raise MaxInstancesReachedError(job)

        self._do_submit_job(job, run_times)
        self._instances[job.id] += 1
```

_instances变量作用:
- 在 submit_job (提交任务)时加1，在 _run_job_success(任务运行成功)时减 1。 当 self._instances[job.id] 大于 job.max_instances 抛出异常。
- max_instances 默认值为 1，它表示 id 相同的任务实例数。

### 解决方案
通过设置max_instances参数
```
sched.add_job(child_job, max_instances=10, trigger=DateTrigger(), id="123")
```
