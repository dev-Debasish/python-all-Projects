'''
1
12
123
1234

'''


print(":::INCREMENTAL NUMBERS PATTERN:::")

def incremental_numbers(rows):
    for i in range(rows):
        for j in range(i + 1):
            print(j + 1, end = " ")
        print()    

row = int(input("Enter the no. of rows:: "))
incremental_numbers(row)