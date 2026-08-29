print("Bill Split Calculator")

bill_amount = float(input("bill_amount: "))
tip_percentage = float(input("tip_percentage: "))

tip_amount = tip_percentage / 100 * bill_amount
total = bill_amount + tip_amount
print(f"Total: ${total:.2f}")

number_of_person = int(input('No. of person: '))

split_amount = total / number_of_person
print(f"each will pay: ${split_amount:.2f}")

print("Thank You!") 