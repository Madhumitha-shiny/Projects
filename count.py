# Accept a number and print the count of digits in it without using for loop

num = input("Enter the number : ") # Accepting the input
num2 = num
try :
    num = int(num)
    count = len(num2)
    print("The count of digits in",num,"is",count)
except:
    print("Entered number is not an integer")
