#!/usr/bin/env python3

import sys
import re
    
def my_printf(format_string,param):
    if int(param) != 0:
        param = hex(int(param))
        param = str(param).lstrip("0x")     
    
    param = param.replace("a","g")
    param = param.replace("b","h")
    param = param.replace("c","i")
    param = param.replace("d","j")
    param = param.replace("e","k")
    param = param.replace("f","l")
    param = param.replace("0","o")
    
    x = re.search("#\.\d+j", format_string)
    if x:    
        format = x.group()
        num = format[2:-1]
        
        s = param.rjust(int(num), '0')
        z = s.replace("0","o")
        x = re.sub("#\.\d+j", z, format_string)
        print(x)
        return
    print(format_string)



data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
