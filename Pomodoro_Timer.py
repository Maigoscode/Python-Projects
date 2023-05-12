# Pomodoro Timer:
# Create a simple Pomodoro timer that helps users stay productive by breaking their work into 25-minute intervals,
# with short breaks in between.

import time


def pomodoro_timer():
    work_time = 25 * 60
    short_break_time = 5 * 60

    while True:
        print("Work for 25 minutes...")
        time.sleep(work_time)

        print("Take a short break for 5 minutes...")
        time.sleep(short_break_time)


pomodoro_timer()
