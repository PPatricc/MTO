#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    leng = len(format_string)
    i=0
    while(i<leng):
        if(format_string[i] == '#' and format_string[i+1]=='.' and format_string[i+2].isdigit and format_string[i+3]=='k'):
            print(param[0:int(format_string[i+2])].swapcase(), end="")
            i=i+4
        elif(format_string[i] == '#' and format_string[i+1]=='k'):
            print(param.swapcase(),end="")
            i=i+2
        else:
            print(format_string[i], end="")
            i=i+1
    print("")
    
    
data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())

