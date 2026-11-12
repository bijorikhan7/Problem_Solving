#break & continue

#break:

i=1

while i <= 30:
    print(i)
    i=i+1
    if i == 20:
        break
print("End")

print(".........................")
#continue

i=1
while i <= 30:
    if i == 20:
        continue
    print(i)
    i=i+1
print("End")