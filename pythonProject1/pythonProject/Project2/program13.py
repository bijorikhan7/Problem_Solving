#nested if

num1=float(input("enter num1:"))
num2=float(input("enter num2:"))
num3=float(input("enter num3:"))

if(num1>num2) :
    if(num1>num3):
        print("num1 is large")
    else:
        print("num3 is large")

else :
    if(num2>num3):
        print("num2 is large")