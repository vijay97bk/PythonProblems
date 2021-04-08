'''
date = '06/04/2021'
modified_date = '07/04/2021'
author = 'Vijay Kshirasagar'
description = ' A library for reading in 2D arrays of integers, doubles, or booleans from standard input and printing them out to standard output.'
'''

def PrintArray(R,C):
   
    array = []
    print("Enter the entries rowwise:")
  
    # For user input
    for i in range(R):          # A for loop for row entries
        a =[]
        for j in range(C):      # A for loop for column entries
            a.append(input())
        array.append(a)
     
  
    # For printing the array
    for i in range(R):
        for j in range(C):
            print(array[i][j], end = " ")
        print()
         
try:
    PrintArray(4,4)
except Exception as e:
    print(e)