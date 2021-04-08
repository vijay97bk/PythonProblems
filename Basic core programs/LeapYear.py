year=int(input('Enter year: '))
if year<1000:
    print('invalid year, please enter 4 digit year value')
else:
    if year % 4 == 0 and year % 100 != 0:
        print(year, "is a Leap Year")
    elif year % 100 == 0:
        print(year, "is not a Leap Year")
    elif year % 400 ==0:
        print(year, "is a Leap Year")
    else:
        print(year, "is not a Leap Year")