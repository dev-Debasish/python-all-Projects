'''
#! v.v.i

****
*  *
*  *
****

'''

print("Print a hollow square: ")

def hollow_square(row):
    # row = int(input("Enter the value of row: "))
    for i in range(row):
        if (i == 0 or i == row - 1):
            print('*' * row)
        else:
            print('*' + ' ' * (row - 2) + '*')
                

n = int(input("Enter the no. of rows: "))
# print(hollow_square(n))
hollow_square(n)



#?  -------------------------------------------------------------


'''
****
*  *
****
'''


# hollow square print with different rows and cols value 

print("::hollow rectangle::")

def hollow_rectangle(rows, cols):
    for i in range(rows):
        if i == 0 or i == (rows - 1):
            print('*' * cols)
        else:
            print('*' + ' ' * (cols - 2) + '*')
        

hollow_rectangle(3, 4)
# hollow_rectangle(4,3)
# hollow_rectangle(4,4)
# hollow_rectangle(5,3)


