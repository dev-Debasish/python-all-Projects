'''
****
***
**
*
'''

print("inverted right angle tringle pattern: ")
n = int(input("Enter the value of n: "))

for i in range(n):
    s = ''
    for j in range(n - i):
        s = s + '*'
    print(s)
    
    
