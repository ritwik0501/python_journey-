def is_even(num):
    if num%2==0:
        return True
    else:
        return False

print("Enter  a number to check odd or even")
num=int(input())

if(is_even(num)):
    print("The number is divisible by two so that is why it is even")
else:
    print("The number is not divisible by two so that is why it is odd")


#above one is my answer ,next one is AI's answer. 
# Version 1: returns a bool
def is_even(n):
    return n % 2 == 0


# Version 2: prints the result
def print_even(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")


# Using the returning version
result = is_even(10)

if result:
    print("The number is even")


# Using the printing version
result = print_even(10)

print("Value returned by print_even:", result)