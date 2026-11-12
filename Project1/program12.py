
#inner if / nested if statement
'''
if 7>5 :
    if 7>9 :
        print ("done")

    else :
        print("not done")

'''

#.......................................

#largest number

'''
num1= input("enter the num1 :")
num2= input("enter the num2 :")
num3= input("enter the num3 :")

if num1>num2 :
    if num1>num3 :
        print("num1 is large",num1)
    else :
        print ("num3 is large", num3)

#if num2>num1:
else :
    if num2>num3:
        print("num2 is large",num2)
    else :
        print ("num3 is large", num3)

'''
#four number among largest

num1= input("enter the num1 :")
num2= input("enter the num2 :")
num3= input("enter the num3 :")
num4= input("enter the num4 :")

if num1>num2 :
    if num1>num3 :
        if num1>num4 :
           print("num1 is large",num1)
        else :
           print("num4 is large", num4)

#if num2 > num1:
if num2 > num3:
     if num2 > num4:
         print("num2 is large", num2)
     else :
         print("num4 is large", num4)

#if num3 > num1:
        #if num3 > num2:
if num3 > num4 :
     print("num3 is large", num3)
else :
     print("num4 id large", num4)




