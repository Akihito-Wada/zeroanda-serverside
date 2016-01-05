import time

def run_process(schedule):
    print('run_process')
    print(schedule.title)
    i = 0
    while i < 3:
        i += 1
        time.sleep(1)
        print(i)