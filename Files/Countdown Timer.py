import time


def countDown(t):
    while t:
        min_s, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(min_s, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Fire in the Hole")


t = int(input("enter the time"))
countDown(int(t))
