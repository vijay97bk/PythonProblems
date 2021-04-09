'''
date = '08/04/2021'
modified_date = '08/04/2021'
author = 'Vijay Kshirasagar'
description = 'Write a Stopwatch Program for measuring the time that elapses between the start and end clicks'
'''

import os    
import time    
second = 0    
minute = 0    
hours = 0    
while(True):        
    print('-------------')    
    print(' %d : %d : %d '%(hours,minute,second))    
    print('-------------')    
    time.sleep(1)    
    second+=1    
    if(second == 60):    
        second = 0    
        minute+=1    
    if(minute == 60):    
        minute = 0    
        hours+=1    