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
    # sched.add_job(child_job, trigger=DateTrigger(), id="123")
    sched.add_job(child_job, max_instances=10, trigger=DateTrigger(), id="123")


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