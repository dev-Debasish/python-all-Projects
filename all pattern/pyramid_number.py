'''

#!  v.v.i

    1
   121
  12321
 1234321

'''

print(":::PYRAMID NUMBER PATTERN:::")

def pyramid_number_pattern(rows):
    for i in range(rows):
        # spaces
        print(' ' * (rows - i - 1), end = '')
        
        # printing increasing number
        for  j  in range(i + 1):
            print(j+1, end = '')
        
        # printing decreasing number
        for j in range(i,0,-1):
            print(j, end = '')
        
        # move to the next line
        print()
        

n = int(input("Enter the no. of rows:: "))
pyramid_number_pattern(n)





#! printing the decresing number
# row = 4
# for i in range(row):
#     for j in range(i,0,-1):
#         print(j, end = '')
#     print()

