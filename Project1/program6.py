#triangle area calc
base=   float(input("Enter base Value: "))
height= float(input("Enter height Value: "))

Result= 0.5 * base * height

print("the area of the t is: ",Result)
print("convert the result :",int(Result))

#..................................................

print("_______")
print(" ")
#circle area calc
radius= float(input("enter radius value:"))
result_c= 3.1416 * radius * radius

print("the area of the c is: ", result_c)

#..................................................

print("_______")
print(" ")
#trapezoid area calc

a=float(input("Enter the value of a :"))
b=float(input("Enter the value of b : "))
h=float(input("Enter the value of h :"))

Area_T= (0.5 * (a+b)) * h
print("The area of the T is: ", Area_T)

#..................................................

print("_______")
print(" ")
#ellipse area calc

A=float(input("Enter the value of A :"))
B=float(input("Enter the value of B : "))

Area_e= 3.1416 * A * B
print("The area of the E is: ", Area_e)




