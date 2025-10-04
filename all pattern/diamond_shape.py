'''
#!  v.v.i

    *
   ***
  *****
   ***
    *
    
'''

def diamond_shape(row):
    # for first pyramid pattern
    for i in range(row):
        # print first level of space
        print(' ' * (row - i - 1), end = '')
        # print pyramid pattern
        for j in range(2*i + 1):
            print('*', end = '')
        print()
    # for 2nd inverted pyramid
    for i in range(row-2,-1,-1):
        # space print
        print(' ' * (row - i - 1), end = '')
        # invertedpyramid print
        for j in range(2*i +1):
            print('*', end = '')
        print()

n = int(input("Enter the no. of rows: "))
diamond_shape(n)