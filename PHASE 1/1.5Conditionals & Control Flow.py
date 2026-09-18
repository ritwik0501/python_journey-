# - [ ] Write a grade calculator (A–F)  deliberately reverse the condition order to see the bug it causes.

print("Enter your score")
score=float(input())

if 90<=score  <=100:
    print("Grade A")
elif 80<=score   <=89:
    print("Grade B")
elif 70<=score   <=79:
    print("Grade c")
elif 60<=score    <=69:
    print("Grade D")
elif 50<=score   <=59:
    print("Grade E")
else:
    print("Grade F")
    
