'''
1
22
333
4444

'''


print(":::REPEATED NUMBER PATTERN:::")

def repeated_numbers(rows):
    for i in range(rows):
        for j in range(i + 1):
            print(i + 1, end = " ")
        print()
        

n = int(input("Enter the no. of rows:: "))
repeated_numbers(n)
