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
    
def change_let(y):
    try:
        x = int(y)
        return str((x+5)%10)
    except:
        return y    

def my_printf(format_string,param):
  
    x = re.search("#\.\d+h", format_string)
    if x:    
        format = x.group()
        num = format[2:-1]
        x = round(float(param),int(num))
        z = str(x)
        s = list(z)
        flag=0
        for index, char in enumerate(s):
                if s[index]=='.':
                    flag = 1
                if flag==0:
                    s[index] = change_num(s[index])
                else:
                    s[index] = change_let(s[index])
                
        
        m = ''.join(s)
        print(m)
        return
    print(format_string)



data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
