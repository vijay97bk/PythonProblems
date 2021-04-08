N=int(input('Enter the value of N: '))
if N<=0:
    print('Please enter value greater then 0')
else:
    Result=0
    for i in range(1,N+1):
        s=1/i
        Result+=s
print(Result)