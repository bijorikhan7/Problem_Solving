#comparison operator chaining

marks=int(input("enter mark:"))
if 80 <= marks <= 100 :
    print ("A+")

elif 70 <= marks <= 79 :
    print ("A")

elif 60 <= marks <= 69 :
    print ("A-")

else:
    print("B")