import schedule
import time


def foobar():
    print("Function foobar is executed.")


schedule.every(1).seconds.do(foobar)

while True:
    schedule.run_pending()
    time.sleep(1)
