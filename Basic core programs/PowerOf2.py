N=int(input('enter number from 1 to 31: '))
if N>31 and N>=0:
    print('please enter number from 1 to 31')
else:
    for i in range(N):
        result= pow(2,i)
        print (result)
