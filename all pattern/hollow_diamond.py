'''
for [row = 3]
    *
   * *
  *   *
   * *
    *
''' 


def hollow_diamond(row):
    # 🔹 Top half of the diamond
    for i in range(row):
        print(' ' * (row - i - 1) + '*', end='')  # Left spaces + first star
        if i > 0:  # To avoid extra '*' in the first row
            print(' ' * (2 * i - 1) + '*', end='')  # Inner spaces + second star
        print()  # Move to the next line

    # 🔹 Bottom half of the diamond
    for i in range(row - 2, -1, -1):  # Reverse loop for symmetry
        print(' ' * (row - i - 1) + '*', end='')  # Left spaces + first star
        if i > 0:
            print(' ' * (2 * i - 1) + '*', end='')  # Inner spaces + second star
        print()  # Move to the next line

# Input from user
n = int(input("Enter the value of n: "))
hollow_diamond(n)

