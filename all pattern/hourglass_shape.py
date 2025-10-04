'''

*********
 *******
  *****
   ***
    *
   ***
  *****
 *******
*********

'''


def hourglass_shape(row):
# first pyramid in reverse
    for i in range(row):
        print(' ' * i, end = '')
        print('*' * (2*(row - i)-1), end = '')
        print()
    # 2nd pyramid in original except the 1st one
    for i in range(row-2, -1, -1):
        print(' ' * i, end = '')
        print('*' * (2*(row - i)-1), end = '')
        print()
    
    
    
    
    
n = int(input("Enter the value of n: "))
hourglass_shape(n)