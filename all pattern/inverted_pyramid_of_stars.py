'''

*******
 *****
  ***
   *

'''

def inverted_pyramid_of_stars(row):
    for i in range(row):
        print(' ' * i, end = '')
        
        for j in range(2*(row-i-1)+1):
            print('*', end = '')
        print()
        
        
n = int(input("Enter the value of n:: "))
inverted_pyramid_of_stars(n)