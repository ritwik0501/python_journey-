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

def safe_divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return None
    