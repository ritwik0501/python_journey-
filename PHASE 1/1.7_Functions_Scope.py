# def is_even(num):
#     if num%2==0:
#         return True
#     else:
#         return False

# print("Enter  a number to check odd or even")
# num=int(input())

# if(is_even(num)):
#     print("The number is divisible by two so that is why it is even")
# else:
#     print("The number is not divisible by two so that is why it is odd")


# #above one is my answer ,next one is AI's answer. 
# # Version 1: returns a bool
# def is_even(n):
#     return n % 2 == 0


# # Version 2: prints the result
# def print_even(n):
#     if n % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")


# # Using the returning version
# result = is_even(10)

# if result:
#     print("The number is even")


# # Using the printing version
# result = print_even(10)

# print("Value returned by print_even:", result)

#second
# - [ ] Write a function with two required, one default, and `*args` parameters.
# Call it five different ways.


def two_required(first_one="Hellow",*args):
    for i in args:
        print(f"{first_one}, {i}")
    
two_required("Hi","Rik")
two_required("Hi","Rik","Raktim","Surya","Pritam")


#this one is importent 
def two_required1(*names,greeting="Hellow"):
    for i in names:
        print(f"{greeting}, {i}")

two_required1("Rik")
two_required1("Rik1","Rik2","RIk3",greeting="HIii")

def two_requried2(first_name,second_name):
    print(f"{first_name},{second_name}")
    
two_requried2("Hi","RIk")



def reu4(name,greeting="Hellow"):
    for i in name:
        print(f"{greeting},{name}")
        
reu4("Hiiiiiiiiii","Rik")

#here hii rik is printing many times because HIIi have 10 char so it goes into name and name to loop .



# - [ ] Demonstrate the mutable-default bug, then fix it.
def default_bug_fix(name,gretting="Hlw"):
    print(f"{gretting}, {name}")
    
default_bug_fix("Rikkkkkk")  
print("To fix that :")
default_bug_fix("jodu",gretting="Ki re")

## this is wrong 🔴

#right way 
def add_name(name, names=[]):
    names.append(name)
    return names

print(add_name("Rik"))
print(add_name("Raktim"))
print(add_name("Surya"))

#in o/p I will get names at once ...
# to fix that , I have to do like this 

def add_name(name):
    names=[]
    names.append(name)
    return names

print(add_name("Rik"))
print(add_name("Raktim"))
print(add_name("Surya"))

## also u can do a better waay 

#right way 
def add_name(name, names=[]):
    names.append(name)
    return names

print(add_name("Rik"))
print(add_name("Raktim"))
print(add_name("Surya"))

#in o/p I will get names at once ...
# to fix that , I have to do like this 

def add_name(name,names=None):
    if names==None:
        names=[]
    names.append(name)
    return names

print(add_name("Rik"))
print(add_name("Raktim"))
print(add_name("Surya"))











