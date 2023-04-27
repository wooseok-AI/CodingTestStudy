"""
Author :  Wooseok Jung
Problem_linK : https://school.programmers.co.kr/learn/courses/30/lessons/92341
"""
import math

def charge(time, fees):
    # time is in minute
    if time <= fees[0]:
        return fees[1]
    return int(math.ceil((time - fees[0]) / fees[2])) * fees[3] + fees[1]

def convert_to_minute(time):
    hour, minute = map(int, time.split(":"))
    return hour * 60 + minute

def duration(in_time, out_time):
    return convert_to_minute(out_time) - convert_to_minute(in_time)


def solution(fees, records):
    car_log = []
    info = dict()
    for log in records:
        time, num, in_out = log.split()
        if in_out == "IN":
            if num not in car_log:
                car_log.append(num)
                info[num] = [1, time, 0]
            else:
                info[num][0], info[num][1] = 1, time
        else:
            info[num][0] = 0
            in_time = info[num][1]
            info[num][2] += duration(in_time, time)

    car_log.sort()
    answer = []
    for c in car_log:
        if info[c][0] == 1:
            info[c][2] += duration(info[c][1], "23:59")
        answer.append(charge(info[c][2], fees))

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

solution(fees, records)