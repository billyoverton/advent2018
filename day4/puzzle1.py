#!/usr/bin/env python3

import sys
import re
from datetime import datetime

def main(input_file):
    pattern = re.compile("\[(.*)\] (.*)")

    records = [] # (date, message)
    with open(input_file) as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            m = pattern.match(line)
            date = m.group(1)
            message = m.group(2)

            date = datetime.strptime(date, "%Y-%m-%d %H:%M")
            records.append((date, message))

    # sort our found records
    records.sort(key=lambda x: x[0])

    guards = {} # guard -> [minutes when asleep]

    pattern = re.compile("^Guard \#(\d+)")
    current_guard = None
    sleep_start = None
    for date, message in records:
        m = pattern.match(message)
        if m is not None:
            current_guard = m.group(1)
            if current_guard not in guards:
                guards[current_guard] = [0] * 60
            continue

        if message == "falls asleep":
            sleep_start = date
        elif message == "wakes up":
            for i in range(sleep_start.minute, date.minute):
                guards[current_guard][i] = guards[current_guard][i] + 1
            #sleep_time = date.minute - sleep_start.minute
            #print("Guard {0} slept {1} minutes".format(current_guard, sleep_time))

    most_sleep_guard = -1
    most_sleep_value = 0

    for guard, sleeptimes in guards.items():
        total_sleep = sum(sleeptimes)
        if total_sleep > most_sleep_value:
            most_sleep_value = total_sleep
            most_sleep_guard = guard

    print("Guard the slept the most: #{0}".format(most_sleep_guard))

    most_sleep_minute = -1
    most_sleep_value = 0
    for minute, count in enumerate(guards[most_sleep_guard]):
        if count > most_sleep_value:
            most_sleep_value = count
            most_sleep_minute = minute

    print("Minute most asleep: {0}".format(most_sleep_minute))
    print("Answer 1: {0}".format(most_sleep_minute * int(most_sleep_guard)))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing input file argument")
    else:
        main(sys.argv[1])
