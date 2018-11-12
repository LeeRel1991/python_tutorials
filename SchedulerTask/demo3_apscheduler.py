#!/usr/bin/env python
# encoding: utf-8


# -------------------------------------------------------
# version: v0.1
# author: lirui
# license: Apache Licence
# project: 
# function:
# file: demo3_apscheduler.py
# time: 2017/11/24 0024 8:42
# -------------------------------------------------------

"""
Demonstrates how to use the background scheduler to schedule a job that executes on 3 second intervals.
"""

import time

from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler


def tick():
    print('Tick! The time is: %s' %  time.strftime('%Y-%m-%d %X',time.localtime()))


if __name__ == '__main__':
    # scheduler = BackgroundScheduler()
    # scheduler.add_job(tick, 'interval', seconds=1)
    # scheduler.start()
    # try:# This is here to simulate application activity (which keeps the main thread alive)
    #     while True:
    #         time.sleep(2)
    # except (KeyboardInterrupt, SystemExit):
    #     scheduler.shutdown()
    sched = BlockingScheduler()
    sched.add_job(tick, 'interval', seconds=5)
    sched.start()