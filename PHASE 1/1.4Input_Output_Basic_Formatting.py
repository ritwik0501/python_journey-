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
    
# items=[]
# price=[]
# subtotal=0
# for i in range(3):
#     print(f"Enter the name of the item{i+1}")
#     items.append(str(input()))
#     print(f"Enter the price of item {i+1}")
#     price.append(float(input()))

# for i in price:
#     subtotal =i+subtotal

# subtotal_after_tax=(subtotal*(8/100))

# print("========================")
# print("         RECEIPT        ")
# print("=========================")
# print("Item                price")

# for i in range(3):
#     print(f"{items[i]:<10}{price[i]:>15}")
    
# print("=========================")
# print(f"subtotal      {subtotal:>10}")
# print(f"after tax(8%) {subtotal_after_tax:10}")
# print("=========================")
# print(f"total         {subtotal+subtotal_after_tax:10}")

# **Interactive Quiz Game (120–180 lines):** 10 hardcoded questions, 
# tracks score, shows a progress indicator ("Question 4 of 10"), 
# gives immediate feedback, and prints a final grade with a percentage breakdown.

questions = [
    {
        "question": "What is the output of len([10, 20, 30, 40])?",
        "options": ["3", "4", "5", "Error"],
        "answer": "4"
    },

    {
        "question": "Which data structure follows the FIFO principle?",
        "options": ["Stack", "Queue", "Tree", "Graph"],
        "answer": "Queue"
    },

    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["function", "define", "def", "func"],
        "answer": "def"
    },

    {
        "question": "What does CPU stand for?",
        "options": [
            "Central Processing Unit",
            "Computer Processing Utility",
            "Central Program Unit",
            "Core Processing Utility"
        ],
        "answer": "Central Processing Unit"
    },

    {
        "question": "Which of these is mutable in Python?",
        "options": ["Tuple", "String", "List", "Integer"],
        "answer": "List"
    },

    {
        "question": "What is the average time complexity of binary search?",
        "options": ["O(1)", "O(n)", "O(log n)", "O(n²)"],
        "answer": "O(log n)"
    },

    {
        "question": "What does == do in Python?",
        "options": [
            "Assigns a value",
            "Compares two values",
            "Checks the data type only",
            "Creates a variable"
        ],
        "answer": "Compares two values"
    },

    {
        "question": "Which SQL command is used to retrieve data?",
        "options": ["GET", "FETCH", "SELECT", "READ"],
        "answer": "SELECT"
    },

    {
        "question": "Which OOP concept allows a child class to acquire properties from a parent class?",
        "options": [
            "Encapsulation",
            "Abstraction",
            "Inheritance",
            "Polymorphism"
        ],
        "answer": "Inheritance"
    },

    {
        "question": "What will 10 // 3 return in Python?",
        "options": ["3.33", "3", "4", "1"],
        "answer": "3"
    }
]
import time
import os
len_questions=len(questions)
correct =0
incorrect=0
score=0
for i in range(len_questions):
    # print(f"Question {i+1} out of 10")
    print(f"Question {i+1} out of 10\n-------------------\n{questions[i]["question"]}")
    print("Options")
    for j in questions[i]["options"]:
        print(f"->{j}")
    print("Enter your anser here")
    ans=input()
    if(ans ==questions[i]["answer"]):
        correct += 1
        print("Answer is right✅")
    else:
        incorrect += 1
        print("Answer is wrong ❌")
        print("correct answer is ", questions[i]["answer"])
    print(f"Score : {correct}/{i+1}")
    input("Press Enter to continue...")
    os.system("cls")

print("=======================")
print("     QUIZ RESULT        ")       
print("========================")
print(f"correct Answers: {correct}")
print(f"Incorrect Answer: {incorrect}")
print(f"Score:{correct}/10")
print(f"Percentage: {(correct/10)*100}")

print("===========================")
    
    

    
    


