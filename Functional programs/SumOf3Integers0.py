'''
date = '06/04/2021'
modified_date = '07/04/2021'
author = 'Vijay Kshirasagar'
description = 'A program with cubic running time. Read in N integers and counts the   number of triples that sum to exactly 0.'
'''

def findTriplets(arr, n):
    try:
        found = False
        for i in range(0, n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
             
                    if (arr[i] + arr[j] + arr[k] == 0):
                        print(arr[i], arr[j], arr[k])
                        found = True
    except Exception as e:
        print(e)                    
                    
    # If no triplet with 0 sum
    # found in array
    if (found == False):
        print(" not exist ")
 
# main function
arr = [0, -1, 2, -3, 1]
n = len(arr)
findTriplets(arr, n)