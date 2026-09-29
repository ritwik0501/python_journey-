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

def show_finally(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return None
    finally:
        print("Done")
        
print(show_finally(10,0))