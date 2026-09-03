# print("Enter a number")

# num=input()

# print("But it is a string",type(num))

#we can do int(input()) but in this case if user give 
#twelve like this instade of 12 it will surely crash the code 
#then to tackle this we use try expect block 

try:
    print("Enter number")
    num1=int(input())
except Exception as e:
    print("Error",e)