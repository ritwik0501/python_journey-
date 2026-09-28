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
# def add_name(name, names=[]):
#     names.append(name)
#     return names

# print(add_name("Rik"))
# print(add_name("Raktim"))
# print(add_name("Surya"))

# #in o/p I will get names at once ...
# # to fix that , I have to do like this 

# def add_name(name):
#     names=[]
#     names.append(name)
#     return names

# print(add_name("Rik"))
# print(add_name("Raktim"))
# print(add_name("Surya"))

# ## also u can do a better waay 

# #right way 
# def add_name(name, names=[]):
#     names.append(name)
#     return names

# print(add_name("Rik"))
# print(add_name("Raktim"))
# print(add_name("Surya"))

# #in o/p I will get names at once ...
# # to fix that , I have to do like this 

# def add_name(name,names=None):
#     if names==None:
#         names=[]
#     names.append(name)
#     return names

# print(add_name("Rik"))
# print(add_name("Raktim"))
# print(add_name("Surya"))


# **Function library:** write and test `celsius_to_f`, `is_prime`, 
# `reverse_string`, `count_vowels`, `factorial` (iterative), and `fibonacci(n)`.

def celsius_to_f(n):
    return (n*1.8)+32

def is_prime(n):
    flag =True
    for i in range(n):
        if n%i==0:
            flag=False
    
    if(flag):
        return True
    else:
        return False
    
def reverse_string(strring):
    return strring[::-1]


def count_vowels(sentence):
    vowel_list=['A','E','I','O','U','a','e','i','o','u']
    count=0
    for i in sentence:
        if i in vowel_list:
            count += 1
        else:
            continue
        
    return count
             



def factorial(num):
    facto=1
    for i in range(1,num+1):
        facto *= i
    
    return facto

# print(factorial(5))

#0,1,1,2,3,5,8
# def fibonacci(n):
#     start=0
#     second=1
#     sum=0
#     print(0)
#     for i in range(n-1):
#         sum =start+second
#         print(sum)
#         temp=start
#         start=sum  
#         second=temp
    
#     return sum 

#this things work done but a smaller better approach 

def fibonacci(n):
    start = 0
    second = 1

    print(start)

    for i in range(n - 1):
        total = start + second
        print(total)

        start = second
        second = total

    return total

fibonacci(10)
    

# rewrite your 1.5 adventure game so each scene is a function. Note the reduction in nesting.
## skip this one 


# - [ ] **Calculator v2:** each operation is a function; 
# a dictionary maps operator symbols to functions. 
# (First taste of functions as values.)


# def addition(*oeprator):
#     total=0
#     for i in oeprator:
#         total += i

#     return total

# # print(addition(2,4))
# #10,5,3,

# def subtraction(*oprator):
#     total=oprator[0]
#     for i in range(1,len(oprator)):
#         total -= oprator[i]
#     return total

# def multiplication(*oeprator):
#     total=1
#     for i in oeprator:
#         total *= i
#     return total

# def division(*oeprator1):
#     return oeprator1[0]/oeprator1[1]

# def calculate(*inputs):
#     return True 

# calculator_v2={
#     "+":addition,
#     "-":subtraction,
#     "*":multiplication,
#     "/":division,
#     "=":calculate
# }
# values=[]
# print('Enter how many values u want to enter ; for division only first 2 input will be valid')
# number_of_inpiut=int(input())
# print("Enter value one by one ")
# for i in range(number_of_inpiut):
#     values.append(float(input())) ## always remember if u do not specify the type it will automatically take string
# print('Enter the opearation')
# operation=input()

# if operation in calculator_v2:
#     result=calculator_v2[operation](*values)
#     print("Result:",result)
# else:
#     print("Invalid operator")


# **Command-Line To-Do Manager (250–300 lines):** 
# add, list, complete, delete, and filter tasks. 
# Every operation is its own well-named function under 20 lines.
# Data lives in a list in memory (persistence arrives in Phase 3). 
# Include a `main()` function and the `if __name__ == "__main__":` guard.
if __name__=="__main__":
    task=[]
    task_status=[]
    def add_task():
        print("Enter name of the task")
        task_name=str(input())
        task.append(task_name)
        task_status.append("pending")
        return True

    def list_task():
        for i in range(len(task)):
            print(f"{i+1} {task[i]}  {task_status[i]}")

    def complete_task():
        print("Enter task numeber to mark as completed ")
        task_number=int(input())
        task_status[task_number-1]="Completed"
        print("Done ! completed")
        return True
    
    def delete_task():
        print("Enter task numeber to delete ")
        task_number=int(input())
        task.remove(task_number-1)
        task_status.remove(task_number-1)
        print("Done ! Deleted Successfully")
        return True
    def filter_task():
        print("1.Show all task")
        print("2.Show pending task")
        print("3.Show completed task")
        print("Enter your choice")
        choose=int(input())
        
        if choose==1:
            list_task()
        elif choose==2:
            number=1
            for i in range(len(task)):
                # number=1
                if task_status[i]=="pending":
                    print(f"{number}. {task[i]} {task_status[i]}")
                    number += 1
        elif choose==3:
            number=1
            for i in range(len(task)):
                number=1
                if task_status[i]=="Completed":
                    print(f"{number}. {task[i]} {task_status[i]}")
                    number += 1
        else:
            print("Enter valid input")
            
            
add_task()
add_task()
add_task()
add_task()
list_task()
complete_task()
complete_task()
list_task()
filter_task()
filter_task()
filter_task()
list_task()
           
    ## my work till here after that I have used Ai to built rest of the part 
    
    
task = []
task_status = []


def add_task():
    task_name = input("Enter name of the task: ")

    task.append(task_name)
    task_status.append("pending")

    print("Task added successfully!")


def list_task():
    if len(task) == 0:
        print("No tasks available.")
        return

    print("\n--- All Tasks ---")

    for i in range(len(task)):
        print(f"{i + 1}. {task[i]} - {task_status[i]}")


def complete_task():
    if len(task) == 0:
        print("No tasks available.")
        return

    list_task()

    task_number = int(input("Enter task number to mark as completed: "))

    if task_number < 1 or task_number > len(task):
        print("Invalid task number.")
        return

    task_status[task_number - 1] = "Completed"

    print("Task completed successfully!")


def delete_task():
    if len(task) == 0:
        print("No tasks available.")
        return

    list_task()

    task_number = int(input("Enter task number to delete: "))

    if task_number < 1 or task_number > len(task):
        print("Invalid task number.")
        return

    task.pop(task_number - 1)
    task_status.pop(task_number - 1)

    print("Task deleted successfully!")


def filter_task():
    print("\n1. Show all tasks")
    print("2. Show pending tasks")
    print("3. Show completed tasks")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        list_task()

    elif choice == 2:
        print("\n--- Pending Tasks ---")

        number = 1

        for i in range(len(task)):
            if task_status[i] == "pending":
                print(f"{number}. {task[i]} - {task_status[i]}")
                number += 1

    elif choice == 3:
        print("\n--- Completed Tasks ---")

        number = 1

        for i in range(len(task)):
            if task_status[i] == "Completed":
                print(f"{number}. {task[i]} - {task_status[i]}")
                number += 1

    else:
        print("Invalid choice.")


def main():

    while True:

        print("\n========== TO-DO MANAGER ==========")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Filter Tasks")
        print("6. Exit")
        print("===================================")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_task()

        elif choice == 2:
            list_task()

        elif choice == 3:
            complete_task()

        elif choice == 4:
            delete_task()

        elif choice == 5:
            filter_task()

        elif choice == 6:
            print("Exiting To-Do Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
        
# main()