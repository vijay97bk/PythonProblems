'''
date = '08/04/2021'
modified_date = '10/04/2021'
author = 'Vijay Kshirasagar'
description = 'Given N distinct Coupon Numbers, how many random numbers do you need to generate distinct 
                coupon number? This program simulates this random process.'
'''
import random

def AddCouponNumber():
    try:
        couponSet=set()
        condition=True

        while condition==True:
            userCoupon=int(input('enter distenct numbers: '))

            #for i in couponSet:
            #    if i==userCoupon:
            #        print('number already exists, enter different number')
            #    else:

            couponSet.add(userCoupon)
            print('Number added: ')
            print(userCoupon)
            anotherNumber=input('to add another number enter y, or enter any other key to stop: ')
            if anotherNumber == 'y' or anotherNumber == 'Y':
                condition=True
            #elif anotherNumber == 'n' or anotherNumber == 'N': 
             #   condition=False   
            else:
                #print('enter correct option')
                condition=False

        sortedUserCoupon=sorted(couponSet)
        firstElement=sortedUserCoupon[0]
        lastElement=sortedUserCoupon[len(sortedUserCoupon)-1]
        Coupons=set()
        condition2=True
        while condition2==True:
            randomCoupan= random.randint(firstElement,lastElement)
            print('generated coupon: ')
            print(randomCoupan)
            Coupons.add(randomCoupan)
            print('Coupon set is:')
            generateAnotherCoupon=input('enter y to generate another coupon, or press any other key to see all generated coupons: ')
            if generateAnotherCoupon=='y' or generateAnotherCoupon=='Y':
                condition2=True
            else:
                condition2=False
        
        print(Coupons)
    except Exception as e:
        print(e)       

AddCouponNumber()