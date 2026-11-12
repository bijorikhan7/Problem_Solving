#logical and & or operation

#logical AND operation


num1= input("enter the first number:  ")
num2= input("enter the second number: ")
num3= input("enter the third number:  ")

if num1>num2 and num1>num3 :
     print("num1 is largest:", num1)
elif num2>num1 and num2>num3 :
     print("num2 is largest:", num2)
else :
     print("num3 is largest:",num3)



#.........................................

#logical OR operation

#find vowel/consonant
#vowel=a,e,i,o,u

ch= input("enter the character: ")

if ch=='a' or ch=='e' or ch=='i' or ch=='o'  or ch=='u' :
    print("vowel")
else :
    print("consonant")

