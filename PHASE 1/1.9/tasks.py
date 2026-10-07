# def add_task(task,all_task=[]):
#     all_task.append(task)
#     return all_task

# def delete_task(task_no,all_task=[]):
#     """##key lesson:- pop will remove the item as FIFO but .remove()  need particular item name to delete""" 
#     all_task.pop(task_no)
#     return all_task

# print(delete_task.__doc__)
# if __name__=="__main__":
#     list1=[]
#     print(add_task("helo",list1))
#     print(add_task("helo1",list1))
#     print(add_task("helo2",list1))
#     print(delete_task(0,list1))
#     help(delete_task)


# - [ ] Use `random.sample`, `random.shuffle`, and `random.choices` and articulate the difference.
import random

# random.sample is using for pick sample data randomly , u can put how many random data u want to pick 
#random.shuffle is used when u want to suffle a list 
# random.choice is used when u want to choice one from list.


list_one=['a','b','c','d','e']

list_2=list_one
# print(random.sample(list_one,3))
# print(random.shuffle(list_one))
# it will return none but it suffle main list 
# print(list_2)
# print(random.choice(list_one))