import sys
from apscheduler.schedulers.blocking import BlockingScheduler

sys.path.append("../")
from send2kindle import main


def run():
    sched = BlockingScheduler()
    sched.add_job(main.run, 'cron', hour="7,11,17")
    # sched.add_job(main.run, 'interval', seconds=20)

    try:
        sched.start()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    run()
