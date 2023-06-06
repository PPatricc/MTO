#!/usr/bin/env python3

import sys
import re

def change_num(x):
    new_num = int((x*2)/len(str(abs(x))))
    return new_num
 
 
 
def change_odd(x):
    if x % 2 != 0:
        p = hex(x)
        rep = str(p).lstrip("0x") 
        return rep
    return x   


def my_printf(format_string,param):
    if '#a' not in format_string:
         print(format_string)
         return
    
    new_N = change_num(int(param))
    to_print = change_odd(new_N)
    
    print(format_string.replace('#a',str(to_print)))



data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
