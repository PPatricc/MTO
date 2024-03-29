#!/usr/bin/env python3

import sys
import re


def my_printf(format_string,param):
    if '#b' not in format_string:
         print(format_string)
         return
         
    
    to_print = bin(int(param))
    to_print = to_print.replace('0b','')
    to_print = to_print.replace('-0b','')
    
    temp_print = ''
    my_table = 'abcdefghij'
    
    for i, j in enumerate(to_print[::-1]):
    	if j == '0':
    	    temp_print = temp_print + '0'
    	else:
    	    temp_print = temp_print + my_table[i%10]
    	    
    temp_print = temp_print[::-1]
    
    print(format_string.replace('#b',str(temp_print)))



data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
