#!/usr/bin/env python3

##
## EPITECH PROJECT, 2021
## B-CNA-410-MAR-4-1-groundhog-iliam.amara
## File description:
## Groundhog
##

import os
import sys
import math

period = int(0)
r = float(0)
last_r = float(0)
switch = int(0)
switched_time = int(0)
weirdest_values_time = int(0)
weirdest_values_list = []

def helper(): 
    print("SYNOPSIS\n    ./groundhog period\n\nDESCRIPTION\n    period        the number of days defining a period")

def add_number(l, a):
    l.append(float(a))
    return l

def temperature_increase_average(li):
    if len(li) <= period:
        return "nan"
    g = 0
    l = len(li) - period
    while l < len(li):
        tmp = li[l] - li[l - 1]
        if tmp > 0:
            g += tmp
        l += 1
    g /= period
    g = round(g, 2)
    return g

def relative_temperature_evolution(li):
    global r
    global switch
    global last_r

    switch = 0
    if len(li) <= period:
        return "nan"
    le = len(li)
    last_r = r
    r1 = li[le - period - 1]
    r2 = li[le - 1]
    if r1 == 0:
        r = int(0)
    else:
        r = int((round((r2-r1)/r1*100, 0)))
    return r

def standard_deviation(li):
    if len(li) < period:
        return "nan"
    le = len(li)
    x = 0
    y = 0
    for i in range(le - period, le):
        x += li[i]
        y += pow(li[i], 2)
    return (round(math.sqrt(y / period - pow(x/period, 2)), 2))

def switch_occur():
    global switch
    global switched_time
    global r
    global last_r

    if last_r > 0 and r < 0:
        switch = 1
    if last_r < 0 and r > 0:
        switch = 1
    if switch == 1:
        switched_time += 1
        return ("      a switch occurs")
    return ""

def print_all(li):
    print("g={}      r={}%      s={}{}".format(temperature_increase_average(li), relative_temperature_evolution(li), standard_deviation(li), switch_occur()))

def index_to_list():
    with open('indexes.txt') as f:
        li = f.read().splitlines()
    return li

def isFloat(ipt):
    try:
        float(ipt)
        return True
    except ValueError:
        return False

def end_of_program():
    global switched_time
    global weirdest_values_list
    global weirdest_values_time

    print("Global tendency switched {} times".format(switched_time))
    print("5 weirdest values are {}".format(weirdest_values_list)) # sorted decreasing weirdness

def main():
    list_n = []
    #list_x = index_to_list() # pour tester
    i = 0
    while 1:
        try:
            jump = 0
            #ipt = list_x[i] # pour tester
            ipt = input() # à mettre en comm pour tester
            #print(ipt) # pour tester
            if ipt == "STOP":
                end_of_program()
                sys.exit(0)
            if isFloat(ipt) == False:
                jump = 1
        except:
            return os.EX_DATAERR
        if jump == 0:
            list_n = add_number(list_n, ipt)
            # print(list_n)
            print_all(list_n)
        i += 1
    sys.exit(0)

def error_handling():
    global period

    if len(sys.argv) != 2:
        print("./Groundhog: Bad input. -h or --help for help")
        sys.exit(84)
    if sys.argv[1] == "--help" or sys.argv[1] == "-h":
        helper()
        sys.exit(0)
    try:
        period = int(sys.argv[1])
    except:
        sys.exit(84)

def groundhog():
    error_handling()
    main()

if __name__ == '__main__':
    groundhog()