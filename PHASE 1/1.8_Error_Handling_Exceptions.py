# # Drill1
# # Deliberately trigger each of the seven common exceptions listed above and 
# # read each traceback.


# # types of errors:-
# ValueError,
# KeyError
# ZeroDivisionError,
# AttributeError,
# ArithmeticError,
# IndexError,
# SyntaxError

# - [ ] Write a `safe_divide(a, b)` that returns `None` instead of raising on division by zero.

# def safe_divide(a, b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         return None
    
# - [ ] Show a case where `finally` runs even though the function returned early.

# def show_finally(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         return None
#     finally:
#         print("Done")
        
# print(show_finally(10,0))
#  [ ] **Bulletproof input:** write `get_int(prompt, min_val, max_val)` that loops until it gets a valid integer in range, 
# handling both `ValueError` and out-of-range separately.

def get_int(prompt,min_val,max_val):
    while True:
        try:
            print(f"{prompt}")
            value_given=int(input())
        except ValueError:
            print("Enter valid integer value")
        else:
            if value_given < min_val or value_given > max_val:
                print("Pls enter the value within range")
            else:
                return value_given

age=get_int("Enter your age",1,120)
print("Your age is ", age )