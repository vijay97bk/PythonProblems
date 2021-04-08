'''
date = '06/04/2021'
modified_date = '07/04/2021'
author = 'Vijay Kshirasagar'
description = 'A program with cubic running time. Read in N integers and counts the   number of triples that sum to exactly 0.'
'''

def WindCalculation(t,v):
    try:
        # calculation part
        w=35.74+(0.6215*t)+((0.4275*t)-35.75)*pow(v,0.16)

        print('wind chill: ')
        print(w)
    except Exception as e:
        print(e)    

# input values
t= int(input('enter the value of temperature in Fahrenheit less then 50: '))
if t>50:
    print('Please enter value less then 50')
v= int(input('enter wind speed in miles per hour from 3 to 120: '))
if v<3 or v>120:
    print('enter value from 3 to 120')
WindCalculation(t,v)