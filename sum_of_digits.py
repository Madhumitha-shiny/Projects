# Accept an integer and print the sum of its digits

num = int(input("Enter the number : "))
num2 = num
sum = 0

while num != 0 :
    dig = num%10
    sum = sum + dig
    num = num//10

print("The sum of the digits of the number",num2,"is",sum)
