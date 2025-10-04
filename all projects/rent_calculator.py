# inputs 
rent = int(input("Enter the total rent: "))
food = int(input("Total food ordered for snaking: "))
total_electricity = int(input("Enter the total amount of electricity you spend: "))
charge_per_unit = int(input("Enter the total per unit charge: "))
people = int(input("Enter the no. of people living in: "))
# logics
total_bill = total_electricity * charge_per_unit;
output = (rent + food + total_bill) // people;
# output
print("Each people will pay = ", output)



