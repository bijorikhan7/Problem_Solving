import random

num= random.random()
print(num)

num= random.randint(20,40)
print(num)

num= random.randrange(30,50,2)
print(num)

num=random.uniform(40,90)
print(num)

num_list = random.sample(range(40,70),10)
print(num_list)

num_list = [2, 7, 9, 8, 0, 4]
random.shuffle(num_list)
print(num_list)

print(random.choice(num_list))

print("........................................................")

# guessing game
for x in range(1,11) :
    guess_num=int(input("enter guess num between 1 to 30:"))
    random_num= random.randint(1,30)

    if guess_num == random_num :
        print("you win! guessing num is :", guess_num)

    else:
        print("you fail! random num is :", random_num)
