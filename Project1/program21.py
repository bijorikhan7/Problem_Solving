'''
#using list :

1|list length
2|creating new list
3|insert new item at any position
4|remove items from list
5|sort the list items
6|sort the list items in reverse
7|pop out the last item from list
8|copy list
9|position/location of any items
10|count any list item from list
11|clear the list

'''

subject = ["bangla","english","math","physics","chemistry","biology","ict"]

print(len(subject))

subject.append("higher math")  #add new item will always appear on the last of a list
print(subject)

subject.insert(3,"Accounting")
print(subject)

subject.remove("higher math")
print(subject)

subject.sort()
print(subject)

subject.reverse()
print(subject)

subject.pop()
subject.pop()
print(subject)

sub2 = subject.copy()
print(sub2)

pos = subject.index("chemistry")
print(pos)

pos_c=subject.count("biology")
print(pos_c)

subject.clear()
print(subject)








