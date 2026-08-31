print("Bill Split Calculator")

print()

while True:
	bill_amount = float(input("bill_amount: "))
	if bill_amount <= 0:
		print("Bill amount can't be zero or negative. Try again!")
	else:
		break
		
		
		
while True:
	tip_percentage = float(input("tip_percentage: "))
	if tip_percentage < 0:
		print("Tip percentage can't be negative. Try again!")
	else:
		break
		
		

tip_amount = tip_percentage / 100 * bill_amount
total = bill_amount + tip_amount
print(f"Total: ${total:.2f}")


print()
while True:
	number_of_person = int(input('No. of person: '))
	if number_of_person <= 0:
		print("Number of person can't be 0 Or negative. Try again!")
	else:
		split_amount = total / number_of_person
		print(f"each will pay: ${split_amount:.2f}")
		break

print()		
print("Thank You! Have a nice day!")
