#!/usr/bin/env python3

import sys
import re

def change_num(x):
    if x == '0':
        return 'a'
    if x == '1':
        return 'b'
    if x == '2':
        return 'c'
    if x == '3':
        return 'd'
    if x == '4':
        return 'e'
    if x == '5':
        return 'f'
    if x == '6':
        return 'g'
    if x == '7':
        return 'h'
    if x == '8':
        return 'i'
    if x == '9':
        return 'j'
    return x
    
def my_printf(format_string,param):

    #for index, char in enumerate(param):
    #    if not(param[index]=='.'):
    #        param[index]=change_num(param[index])
    #    else:
    #        break
            
    x = re.search("#\.\d+h", format_string)
    if x:    
        format = x.group()
        num = format[2:-1]
        x = round(float(param),int(num))
        print(x)
        return
    print(format_string)



data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
