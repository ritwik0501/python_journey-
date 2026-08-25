# y=10
# x=y
# print(x) 
# y=20
# x=y
# print("neww assignment",x)

# x="ritwik"
# y="10"
# print(x+y)

#assignmemt -1
# x=10
# y="ritwik"
# z=3.14
# a=True
# b= None
# print(type(x))
# print(type(y))
# print(type(z))
# print(type(a))
# print(type(b))

# assignment- 2

# print(0.1 + 0.2 == 0.3)
# it will be false because of float value works different in puthon 

#assignment- 3
# 0- false
# ""-
# []- empty object
# False- False
# None - none data type 
# 1 - true 

# values = [0, "", [], "False", None, -1]

# for value in values:
#     print(repr(value), "=>", bool(value))

#----EXERCSISE-------#
# 1.ask for a temperature in Celsius, print Fahrenheit and Kelvin to 2 decimal places.
# print("Enter  temp in celsius");
# a=float(input())
# print("In Fahrenheit",round((a*1.8)+32,2));
# print("In kelvin",round((a+273.15),2))


# 2.take 5 hardcoded values of mixed types, print each with its type and whether it's truthy.

# values=[1,"2",3.14,None,-1,True,0]
# for value in values:
#     print(repr(value),"=>",type(value)," ",bool(value))

# # Mini-project
# # collect name, age, height, city, and favourite number from the user, validate 
# # that age and number convert to `int` cleanly, then print 
# # a formatted "profile card" with a text border. Handle the case where someone types "twenty" for age.

# print("Enter your name ")
# name=str(input())
# print("Enter your age")
# age=int(input())
# print("Enter your height")
# height= float(input())
# print("Enter your city name")
# city=str(input())
# print("Enter your Favourite number")
# fav_num=int(input())
 
# if(type(age) and type(fav_num) == int):
#     print(name,age,height,city,fav_num)
# else:
#     print("Enter proper data")
# print("Enter your name:")
# name = input()

# print("Enter your age:")
# try:
#     age = int(input())
# except ValueError:
#     print("Invalid age. Please enter a whole number.")
#     exit()

# print("Enter your height:")
# height = float(input())

# print("Enter your city:")
# city = input()

# print("Enter your favourite number:")
# try:
#     fav_num = int(input())
# except ValueError:
#     print("Invalid favourite number. Please enter a whole number.")
#     exit()

# print()
# print("+--------------------------+")
# print("|       PROFILE CARD       |")
# print("+--------------------------+")
# print(f"| Name:       {name:<12} |")
# print(f"| Age:        {age:<12} |")
# print(f"| Height:     {height:<12} |")
# print(f"| City:       {city:<12} |")
# print(f"| Favourite:  {fav_num:<12} |")
# print("+--------------------------+")