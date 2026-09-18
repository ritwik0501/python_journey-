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


# user_loggin=True
# user_verified=True
# user_have_permission=True

# if(user_loggin):
#     if(user_verified):
#         if(user_have_permission):
#             print("User have permission")
#         else:
#             print("user restricted")
#     else:
#         print("User is only verified")
# else:
#     print("User is only logged in ")


# - [ ] **Rock-paper-scissors:** one round versus a random computer choice (`import random`), 
# declaring winner or tie.
import random
print("Enter your choice: rock, paper, or scissors")
print("Enter 'exit' to quit the game")
user_choice=input().lower()
computer_choice= random.choice(['rock', 'paper', 'scissors'])
if user_choice=="exit":
    exit()
elif user_choice=="rock" and computer_choice=="scissors":
    print("You win! Rock beats scissors.")
elif user_choice=="rock" and computer_choice=="paper":
    print("computer win! paper beats rock.")
elif user_choice=="paper" and computer_choice=="scissors":
    print("computer  win! scissors beats paper.") 
elif user_choice=="paper" and computer_choice=="rock":
    print("You win ! paper beats rock.")
elif user_choice=="scissors" and computer_choice=="rock":
    print("computer win! scissors beats rock.")
elif user_choice=="scissors" and computer_choice=="paper":
    print("You win! scissors beats paper.")
elif user_choice=="scissors" and computer_choice=="scissors":
    print("Draw! both chose scissors.")
elif user_choice=="paper" and computer_choice=="paper":
    print("Draw! both choose paper.")
elif user_choice=="rock" and computer_choice=="rock":
    print("Draw!both choose rock.")
    
else:
    print("Enter valid choice")
 
                     