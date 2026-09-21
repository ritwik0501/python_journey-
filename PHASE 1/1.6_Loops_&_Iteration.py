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

sum=0
for i in range(1,101):
    if i%3==0 or i%5==0:
        sum=sum+i
        
print("Sum of every number from 1 to 100 divisible by 3 or 5",sum)