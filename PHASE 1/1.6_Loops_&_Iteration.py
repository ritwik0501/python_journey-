# Print a right triangle, then a pyramid, 
# then a diamond of asterisks using nested loops
# triangle


# for i in range(6):
#     for j in range(i):
#         print("*",end="")
#     print()

# pyramid
#     *
#    ***
#   *****
#  *******
# *********
# *******In Python, end="" tells print() 
# not to move to the next line after printing.****


# for i in range(1,5):
#     for j in range(5-i):
#         print(" ",end="") 
#     for j in range(2*i-1):
#         print("*",end="")
#     print()


# diamond
 
# for i in range(1,5):
#     for j in range(5-i):
#         print(" ",end="")
#     for j in range(2*i-1):
#         print("*",end="")
#     print()

# for j in range(5,0,-1):
#     for i in range(5-j):
#         print(" ",end="")
#     for i in range(2*j-1):
#         print("*",end="")
#     print()
 
# - [ ] Sum every number from 1 to 100 divisible by 3 or 5.

# sum=0
# for i in range(1,101):
#     if i%3==0 or i%5==0:
#         sum=sum+i
        
# print("Sum of every number from 1 to 100 divisible by 3 or 5",sum)


# - [ ] Use `enumerate` to print a numbered list, and `zip` to pair names with scores.

# lists=["a","b","c","d","e","f"]
# for index,item in enumerate(lists):
#     print(index,item)

# list2=["A","B","C","D","E","F"]

# for item1,item2 in zip(lists,list2):
#     print(item1,item2)


# - [ ] **FizzBuzz:** the classic 1–100 interview screen. Then do it in one line with a comprehension.


# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         print("FizzBuzz")
#     elif i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")
#     else:
#         print(i)


# - [ ] **Multiplication table:** print a formatted, aligned 12×12 grid with header row and column.


# for i in range(1, 13):

#     print(i, end="\t")

#     for j in range(1, 13):
#         print(i * j, end="\t")

#     print()

# print("     ", end="")

# for j in range(1, 13):
#     print(f"{j:4}", end="")

# print()
# print("-" * 55)

# for i in range(1, 13):
#     print(f"{i:2} |", end="")

#     for j in range(1, 13):
#         print(f"{i * j:4}", end="")

#     print()
    
    
# - [ ] **Number guessing game:** computer picks 1–100, gives higher/lower hints, limits attempts,
# and offers a replay loop.

# import random

# random_num=random.randint(1,100)
# # print(random_num)
# guess=0
# attempt=7
# check=True
# while True:
#     print(random_num)
#     print(f"Attempt left{attempt}/7")
#     if attempt==0:
#         print("You have exusated all the attempts,,,wanna reply(YES/NO) ?")
#         take_decesion=str(input())
#         if take_decesion.lower()=="yes":
#             random_num=random.randint(1,100)
#             attempt=7
#             continue
#         elif take_decesion.lower()=="no":
#             break
#         else:
#             print("rong input...terminatig")
#             break
    
#     print("Guess the number from 1 to 100!")
#     guess=int(input())
#     if random_num==guess:
#         print("Yahooo!got the num")
#         break
#     elif guess>random_num:
#         print("lower")
#         attempt -= 1
#     else:
#         print("Go upper")
#         attempt -= 1

#  print all primes below 100, then optimise the inner loop to stop at `√n` 
# and explain why that's valid.

# for i in range(2,101):
#     is_prime=True
#     for j in range(2,i):
#         if i%j==0:
#             is_prime=False
#             break
#     if is_prime:
#         print(i)

# ptimise the inner loop to stop at `√n` 
# # and explain why that's valid.

# for i in range(2,101):
#     is_prime=True
#     for j in range(2,int(i**0.5)+1):
#         # print(f"J, {j}, {i}")
#         if i%j==0:
#             is_prime=False
#             break
#     if is_prime:
#         print(i)



# [ ] **ATM Simulator (200–250 lines):** menu loop with balance check, 
# deposit, withdraw, and transaction history. 
# Enforce PIN entry with 3 attempts, prevent overdrafts, 
# validate all amounts, 
# and exit cleanly. Use only what you've learned so far.
balance=100
pin=1234
transaction=[]
while True:
    print("==========")
    print("    Menu  ")
    print("==========")
    print("1.Check your balance")
    print("2.Add Balance")
    print("3.Withdraw Balance")
    print("4.Transaction History")
    print("5.Chnage your pin")
    print("6.Exit")
    print('Enter your choice')
    choice=int(input())
   
    pin_attempts=3

    match choice:
        case 1:
            # pin_attempts=3
            while(pin_attempts>0):
                print("Enter your PIN")
                input_given=int(input())
                # print(pin,input_given)
                if pin==input_given:
                    print("CORRECT PIN")
                    print("Your account balance is :",balance)
                    break
                else:
                    print(f"WRONG PIN! {pin_attempts-1} ATTEMPT LEFT!")
                    pin_attempts -=1
                    break
            # print("3 ATTEMPT DONE ")
            # break
        case 2:
            print("Enter how much money you want to add")
            enter_balance=int(input())
            if enter_balance>0:
                balance+=enter_balance
                print("Your money has been added to your bank account")
                transaction.append({
                    "type":"deposite",
                    "amount":enter_balance
                })
                print("Your bank balance is ",balance)
                
            else:
                print("Enter valid amount")
                # break
        case 3:
            print("Enter amount to to withdraw balance")
            balance_withdraw=int(input())
            if balance_withdraw>0 and balance_withdraw<=balance:
                while(pin_attempts>0):
                    print("Enter your PIN")
                    input_given=int(input())
                    if input_given==pin:
                        print("CORRECT PIN")
                        print("You have successfully withdraw money",balance_withdraw)
                        balance-= balance_withdraw
                        transaction.append({
                            "type":"Withdraw",
                            "amount":balance_withdraw
                        })
                        print("Your account balance is :",balance)
                        break
                    else:
                        print(f"WRONG PIN! {pin_attempts-1} ATTEMPT LEFT!")
                        pin_attempts -=1
                        break
                # print("3 attempt done")
            else:
                print("Enter valid amount")
        case 4:
            while(pin_attempts>0):
                print("Enter your PIN")
                input_given=int(input())
                            # print(pin,input_given)
                if pin==input_given:
                    print("CORRECT PIN")
                    print("=======Transaction History========")
                    loop=1
                    for i in transaction:
                        print(f"{loop} {i['type']} { i['amount']}")
                        loop +=1
                    break   
                else:
                    print(f"WRONG PIN! {pin_attempts-1} ATTEMPT LEFT!")
                    pin_attempts -=1
                    break
        case 5:
            print("Enter old pin")
            oldpin=int(input())
            if oldpin==pin:
                print("Enter new pin")
                pin=int(input())
                print("Your pin is successfully updated")
            else:
                print("Enter right pin!Try again")
        case 6:
            exit()