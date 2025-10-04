num = int(input("Enter the number: "))
factorial = 1
while (num > 0):
    factorial = factorial * num
    num = num - 1
    
print("FACTORIAL = ",factorial)