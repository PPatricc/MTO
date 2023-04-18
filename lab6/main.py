#!/usr/bin/env python3

import sys
import re


def replace(number):
    new_number = 0
    position = 1
    while number > 0:
        digit = number % 10
        new_digit = (digit * 9 + 1) % 10
        new_number += new_digit * position
        position *= 10
        number //= 10
    return new_number
    
def my_printf(format_string,param):
    pattern = r'^[0-9+\-*/()]+$'
    if str(param).isdigit() or re.match(pattern,str(param)):
    	param = int(eval(str(param)))
    	param = str(replace(int(param)))
    list1 = list(param)
    for i in range(len(list1)):
        if list1[i].isdigit():
            if list1[i] == '0':
                list1[i] ='1'
            list1[i] = str(int(list1[i]))
        else:
            list1[i]=""
    param = ''.join(list1)

    x = re.search("#\.\d+g", format_string)
    if x:    
        format = x.group()
        num = format[2:-1]
        
        s = param.rjust(int(num), '0')
        x = re.sub("#\.\d+g", s, format_string)
        print(x)
        return
    print(re.sub("#g", param, format_string))

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
