#https://www.sanfoundry.com/python-problems-solutions/#python-programs-list

#series using range and for loop

#1+2+3+.....+n

n=int(input("Enter the value of n:"))
sum=0

for x in range(1,n+1,1):
    sum=sum+x
print(sum)

print("................................................")

#2+4+6+8+..........+n

n=int(input("Enter the value of n:"))
sum=0

for x in range(2,n+1,2):
    sum=sum+x
print(sum)

print("................................................")

#1^2+2^2+3^2........n

n=int(input("Enter the value of n:"))
sum=0

for x in range(1,n+1,1):
    sum=sum+(x*x)
print(sum)

print("................................................")

#1+1/2+2/3+..........1/n

n=int(input("Enter the value of n:"))
sum=0

for x in range(1,n+1,1):
    sum=sum+(1/x)
print(sum)


