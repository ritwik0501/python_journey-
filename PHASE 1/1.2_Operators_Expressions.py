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

cents= int(input())

quarters= cents//25
remaining_quarter=cents%25

dimes= remaining_quarter//10
remaining_dimes=remaining_quarter%10

nickels= remaining_dimes//5
pennies= remaining_dimes%5

print(f"Quartes of {cents} cents is {quarters}")
print(f"dimes of {cents} cents is {dimes}")
print(f"nickels of {cents} cents is {nickels}")
