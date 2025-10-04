'''

A
AB
ABC
ABCD

'''

def incremental_letters(row):
    letter = 65
    for i in range(row):
        for j in range(i+1):
            print(chr(letter), end = '')
        letter +=1
        print()
        
        
n = int(input("Enter the value of n: "))
incremental_letters(n)