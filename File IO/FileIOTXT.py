'''
date = '08/04/2021'
modified_date = '08/04/2021'
author = 'Vijay Kshirasagar'
description = 'File IO operations for txt file.'
'''

file1 = open("myfile.txt","w")
L = ["This is Delhi \n","This is Paris \n","This is London \n"]
file1.write("Hello \n")
file1.writelines(L)
file1.close()

file1 = open("myfile.txt","r+") 
  
print ("Output of Read function is ")
print (file1.read())
print()