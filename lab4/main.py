#!/usr/bin/env python3

import sys
import re

def my_printf(format_string,param):
    shouldDo=True
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx+1] == 'g':
            	flag =0
            	for x in param:
            		if x.isdigit() or x== '+' or x== '-' or x=='*' or x=='/':
            			flag=1
            	if flag == 1:
            		param = str(eval(param))
            	if param.isnumeric():
            		param = param[::-1]
            		param = param.lstrip("0")
            		print(param,end="")
            		shouldDo=False
            		
            else:
                print(format_string[idx].lstrip("#g"),end="")
        else:
            shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())

