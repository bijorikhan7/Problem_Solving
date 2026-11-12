#logical operator

num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
num3=int(input("enter num3:"))

if num1>num2 and num1>num3 :
    print("large is:",num1)

elif num2>num1 and num2>num3 :
    print("large is:",num2)

else:
    print("large is:",num3)

print("...................................")


#vowel ,consonant (or)

ch=str (input("enter character:"))

if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
    print("vowel")
else:
    print("consonant")

print("...................................")

#not

x=11
print(not(x>6 and x<10))