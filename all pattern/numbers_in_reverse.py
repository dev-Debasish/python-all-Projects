'''
1234
123
12
1

'''


def number_in_reverse(row):
    for i in range(1, row+1):
        for j in range(row - i + 1):
            print(j+1, end = '')
        print()
    
n = int(input("Enter the value of n:: "))
number_in_reverse(n)