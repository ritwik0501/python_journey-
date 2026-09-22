# Print a right triangle, then a pyramid, 
# then a diamond of asterisks using nested loops
# triangle


# for i in range(6):
#     for j in range(i):
#         print("*",end="")
#     print()

# pyramid
#     *
#    ***
#   *****
#  *******
# *********
# *******In Python, end="" tells print() 
# not to move to the next line after printing.****


# for i in range(1,5):
#     for j in range(5-i):
#         print(" ",end="") 
#     for j in range(2*i-1):
#         print("*",end="")
#     print()


# diamond
 
# for i in range(1,5):
#     for j in range(5-i):
#         print(" ",end="")
#     for j in range(2*i-1):
#         print("*",end="")
#     print()

# for j in range(5,0,-1):
#     for i in range(5-j):
#         print(" ",end="")
#     for i in range(2*j-1):
#         print("*",end="")
#     print()
 
# - [ ] Sum every number from 1 to 100 divisible by 3 or 5.

# sum=0
# for i in range(1,101):
#     if i%3==0 or i%5==0:
#         sum=sum+i
        
# print("Sum of every number from 1 to 100 divisible by 3 or 5",sum)


# - [ ] Use `enumerate` to print a numbered list, and `zip` to pair names with scores.

# lists=["a","b","c","d","e","f"]
# for index,item in enumerate(lists):
#     print(index,item)

# list2=["A","B","C","D","E","F"]

# for item1,item2 in zip(lists,list2):
#     print(item1,item2)


# - [ ] **FizzBuzz:** the classic 1–100 interview screen. Then do it in one line with a comprehension.


# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         print("FizzBuzz")
#     elif i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")
#     else:
#         print(i)


# - [ ] **Multiplication table:** print a formatted, aligned 12×12 grid with header row and column.


# for i in range(1, 13):

#     print(i, end="\t")

#     for j in range(1, 13):
#         print(i * j, end="\t")

#     print()

# print("     ", end="")

# for j in range(1, 13):
#     print(f"{j:4}", end="")

# print()
# print("-" * 55)

# for i in range(1, 13):
#     print(f"{i:2} |", end="")

#     for j in range(1, 13):
#         print(f"{i * j:4}", end="")

#     print()
    
    
# - [ ] **Number guessing game:** computer picks 1–100, gives higher/lower hints, limits attempts,
# and offers a replay loop.

import random

random_num=random.randint(1,100)
# print(random_num)
guess=0
attempt=7
check=True
while True:
    print(random_num)
    print(f"Attempt left{attempt}/7")
    if attempt==0:
        print("You have exusated all the attempts,,,wanna reply(YES/NO) ?")
        take_decesion=str(input())
        if take_decesion.lower()=="yes":
            random_num=random.randint(1,100)
            attempt=7
            continue
        elif take_decesion.lower()=="no":
            break
        else:
            print("rong input...terminatig")
            break
    
    print("Guess the number from 1 to 100!")
    guess=int(input())
    if random_num==guess:
        print("Yahooo!got the num")
        break
    elif guess>random_num:
        print("lower")
        attempt -= 1
    else:
        print("Go upper")
        attempt -= 1

    