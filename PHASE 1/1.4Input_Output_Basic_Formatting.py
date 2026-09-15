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

# import time 

# for i in range(101):
#     bar= "#" * (i//5)
#     spaces=" "*(20-len(bar))
    
#     print(f"Downloading...[{bar}{spaces}]",end="\r")
#     # time.sleep(0.1)
    
# print("Successfully Download!`              ")

# - Task 2 Print a formatted table of 5 products and prices, with columns aligned using f-string padding.
# you have to put proper and normal value to look the table good 
# print("Enter 5 product name ")
# products=[]
# for i in range(5):
#     products.append(str(input()))

# price=[]
# for j in range(5):
#     print(f"Enter the price of product {products[j]}")
#     price.append(str(input()))
    
# # Table header
# print("+----------------------+------------+")
# print(f"| {'Product':<20} | {'Price':>10} |")
# print("+----------------------+------------+")

# # Table rows
# for j in range(5):
#     print(f"| {products[j]:<20} | {price[j]:>10} |")

# print("+----------------------+------------+")

### Exercises
# **Robust number reader:** 
# keep asking for a number until the user supplies a valid one 
# (use a loop and `.isdigit()` for now; 
# you'll do it properly with `try/except` in 1.8).
 
# while(1):
#     print('Enter valid number')
#     num=input()
#     if(num.isdigit()):
#         exit()

# suggestion:- u can use break instade of exit() ..exit will end whole programme fourcefully 
# but break will only break the loop 

# **Receipt generator:** ask for 3 items and prices,
# print a receipt with aligned columns, subtotal, 8% tax, and total.
    
items=[]
price=[]
subtotal=0
for i in range(3):
    print(f"Enter the name of the item{i+1}")
    items.append(str(input()))
    print(f"Enter the price of item {i+1}")
    price.append(float(input()))

for i in price:
    subtotal =i+subtotal

subtotal_after_tax=(subtotal*(8/100))

print("========================")
print("         RECEIPT        ")
print("=========================")
print("Item                price")

for i in range(3):
    print(f"{items[i]:<10}{price[i]:>15}")
    
print("=========================")
print(f"subtotal      {subtotal:>10}")
print(f"after tax(8%) {subtotal_after_tax:10}")
print("=========================")
print(f"total         {subtotal+subtotal_after_tax:10}")

   

