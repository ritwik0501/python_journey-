# print("Enter a number")

# num=input()

# print("But it is a string",type(num))

#we can do int(input()) but in this case if user give 
#twelve like this instade of 12 it will surely crash the code 
#then to tackle this we use try expect block 

# try:
#     print("Enter number")
#     num1=int(input())
# except Exception as e:
#     print("Error",e)

#this code is use to show loading but not progress bar 
# import time

# for i in range(1,100,2):
#     print(f"Loading in {i}...",end="\r")
#     time.sleep(1)

# print("Done!")

# task 1 Build a progress bar that prints on one line using `end="\r"`.

import time 

for i in range(101):
    bar= "#" * (i//5)
    spaces=" "*(20-len(bar))
    
    print(f"Downloading...[{bar}{spaces}]",end="\r")
    # time.sleep(0.1)
    
print("Successfully Download!`              ")
    