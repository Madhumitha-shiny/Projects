# Accept an integer value and verify whether the given number is sivisible by 9 

num = int(input("Enter the number : ")) # Accepting the input

if num%9 == 0 :
    print("The numer",num,"is divisible by 9")
else:
    print("The number",num,"is not divisble by 9")
