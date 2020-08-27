# program to verify whether a given number is positive, negative, and zero

num = int(input("Enter the number : ")) # Accepting the input

# using if, elif and else conditional operators 
if num>0 :
    print("The number",num,"is a positive number")
elif num<0 :
    print("The number",num,"is a negative number")
else:
    print("the number is zero")
