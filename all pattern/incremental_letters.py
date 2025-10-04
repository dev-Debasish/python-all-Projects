'''

A
AB
ABC
ABCD

'''

def incremental_letters(row):
    for i in range(row):
        letter = 65
        for j in range(i+1):
            print(chr(letter), end = '')
            letter +=1
        print()
        
        
n = int(input("Enter the value of n: "))
incremental_letters(n)