#!/usr/bin/env python3

import sys
import re

def change_num(x):
    new_num = int((x*2)/len(str(abs(x))))
    return new_num
 

def my_printf(format_string,param):
  



data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
