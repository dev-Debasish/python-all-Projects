'''
    *
   **
  ***
 ****
 
'''


# def left_aligned_tringle(rows):
#     for i in range(rows):
#         s = ''
#         # space
#         for j in range(rows - i - 1):
#             s = s + ' '
#         # print(s)    
#         # star
#         for j in range(i + 1):
#             s = s + '*'
#         print(s)
            
            
def left_aligned_tringle(rows):
    for i in range(rows):
        print(' ' * (rows - i - 1) + '*' * (i + 1))            


n = int(input("Enter the no. of rows: "))
left_aligned_tringle(n)