#  Use `%` to determine if a number is even, 
# and `//` plus `%` to split 3725 seconds into hours, minutes, seconds.

# print("Enter a number to check a number is even or odd")
# number= int(input())

# if (number%2==0):
#     print("Number is even")
# else:
#     print("Number is odd")
# number = 3725

# hours = number // 3600
# number = number % 3600

# minutes = number // 60
# number = number % 60

# seconds = number

# print(hours, minutes, seconds)

    
##2
# print(2 + 3 * 4 ** 2 // 5)
# ans 11-- to understand learn operator precedency 


# num=int(input())

# if(num>=10 and num<=20):
#     print("True")
# else:
#     print("False")


### Exercises
# - [ ] **Change maker:** given 
# an amount in cents, print how many quarters, dimes, nickels, and pennies make it up, using only `//` and `%`.

# cents= int(input())

# quarters= cents//25
# remaining_quarter=cents%25

# dimes= remaining_quarter//10
# remaining_dimes=remaining_quarter%10

# nickels= remaining_dimes//5
# pennies= remaining_dimes%5

# print(f"Quartes of {cents} cents is {quarters}")
# print(f"dimes of {cents} cents is {dimes}")
# print(f"nickels of {cents} cents is {nickels}")

# ##exercise 
# **Leap year checker:** implement the real rule (divisible by 4, except centuries, unless divisible by 400) 
# as a single boolean expression.

# print("Enter year to check leapyear")
# year=int(input())

# if ((year % 4 == 0 and year % 100 !=0 )or year %400 ==0):
#         print("leapYear ")
        
# else:
#     print("Not leap year")    

# Mini-project
# - [] **Simple Calculator (80–120 lines):** menu-driven, supports the six arithmetic operators, 
# keeps a running "last result" the user can reuse, and refuses to divide by zero. 
# No functions yet — that's deliberate, so you'll *feel* why you need them in 1.6.
    
print("=== Calculator ===")

last_result = 0

while True:

    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Floor Division (//)")
    print("6. Modulo (%)")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "7":
        print("Calculator closed.")
        break

    # Get first number
    first = input("Enter first number (or 'last' to reuse result): ")

    if first == "last":
        num1 = last_result
    else:
        num1 = float(first)

    # Get second number
    num2 = float(input("Enter second number: "))

    if choice == "1":
        result = num1 + num2

    elif choice == "2":
        result = num1 - num2

    elif choice == "3":
        result = num1 * num2

    elif choice == "4":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            continue

        result = num1 / num2

    elif choice == "5":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            continue

        result = num1 // num2

    elif choice == "6":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            continue

        result = num1 % num2

    else:
        print("Invalid choice.")
        continue

    last_result = result

    print("Result:", result)

