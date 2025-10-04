str = input("Enter the string: ")
reversed_string = ""  #Empty string 
for char in str:
    reversed_string = char + reversed_string
    
print("The reversed_string is::  ",reversed_string)