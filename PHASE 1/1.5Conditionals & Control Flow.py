# - [ ] Write a grade calculator (A–F)  deliberately reverse the condition order to see the bug it causes.

# print("Enter your score")
# score=float(input())

# if 90<=score  <=100:
#     print("Grade A")
# elif 80<=score   <=89:
#     print("Grade B")
# elif 70<=score   <=79:
#     print("Grade c")
# elif 60<=score    <=69:
#     print("Grade D")
# elif 50<=score   <=59:
#     print("Grade E")
# else:
#     print("Grade F")



# - [ ] Rewrite a 3-level nested `if` as a flat chain of guard clauses.

#control flow 
#   Is user logged in?
# │
# ├── NO → Reject
# │
# └── YES
#      │
#      └── Is user verified?
#           │
#           ├── NO → Reject
#           │
#           └── YES
#                │
#                └── Does user have permission?
#                     │
#                     ├── NO → Reject
#                     │
#                     └── YES → Allow  


user_loggin=True
user_verified=True
user_have_permission=True

if(user_loggin):
    if(user_verified):
        if(user_have_permission):
            print("User have permission")
        else:
            print("user restricted")
    else:
        print("User is only verified")
else:
    print("User is only logged in ")

