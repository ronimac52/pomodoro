#!/usr/bin/env python
# used with chmod +x to allow access from any folder by calling my_pom.py

from __future__ import print_function # allows use of python3 print() function syntax
import sys
import time
import subprocess
# Alarm sound files taken from http://www.soundjay.com/clock-sounds-1.html

my_alarm = "/home/inor/pomodero/alarm-clock-01.mp3"
dev_null  = open("/dev/null","w")

req_time = raw_input('Enter work time in minutes(use an integer): ')
# need to add 'try/except' so string input wont cause programme failure.



# The follwing function (alarm) adapted from http://code.activestate.com/recipes/577358-pomodoro-timer/
# and was originally written by Noufal Ibrahim
def alarm(alarm):
    "Plays the alarm sound specified by alarm"
    cmd = ["mpv", alarm]
    p = subprocess.Popen(cmd, stdout = dev_null, stderr = subprocess.PIPE)
    p.wait()


def countdown(work_time):
    while work_time:
        mins, secs = divmod(work_time, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        sys.stdout.flush()
        time.sleep(1)
        work_time -= 1
    alarm(my_alarm)
    print('Take a break!\n\n\n')
countdown(60 * int(req_time))

# need to add code for timing of break and 'back to work alarm
