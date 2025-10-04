'''

    *
   ***
  *****
 *******

'''

def pyramid_of_stars(row):
    for i in range(row):
        print(' ' * (row - i - 1), end = '')
        
        for j in range(i + 1):
            print('*', end = '')
        
        for j in range(i, 0, -1):
            print('*', end = '')
        
        print()


n = int(input("Enter the value of n:: "))
pyramid_of_stars(n)