def add_task(task,all_task=[]):
    all_task.append(task)
    return all_task

def delete_task(task_no,all_task=[]):
    """##key lesson:- pop will remove the item as FIFO but .remove()  need particular item name to delete""" 
    all_task.pop(task_no)
    return all_task

print(delete_task.__doc__)
if __name__=="__main__":
    list1=[]
    print(add_task("helo",list1))
    print(add_task("helo1",list1))
    print(add_task("helo2",list1))
    print(delete_task(0,list1))
    help(delete_task)