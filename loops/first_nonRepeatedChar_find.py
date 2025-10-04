str = "abcdcbardmnyy"

for char in str:
    print(char)
    if (str.count(char) == 1):
        print("result = ",char)
        break