#Welcome prompt for customer 
message = "Welcome to Chico's restaurant"
print(message.upper())
print("-" * len(message))

#prompt for user's input
name = input("Customer name: ")
amount = float(input("Amount of bill(before tax): $"))
partySize = int(input("Number of people in your party: "))

#calulating tax
def addedTax():
	valueTax = 0.16
	tax = valueTax * amount
	return tax

#calculating total amount
def totalBill():
	total = amount + addedTax()
	return total

#calculating total per person
def splitTotals():
	perPerson = totalBill() / partySize
	return perPerson

#calculating takeAway price
def takeAway():
	question = input("Do you have any take aways?")
	if question == "yes":
		dishes = int(input("How many plates would you like to take away?"))
		toGO = dishes * 100
	else:
		toGO = 0

	return toGO

#calculating delivery
def deliveryCharge():
	message = (input("Would you like you meal to be delivered?"))
	if message == "yes":
		delivery = 500
	
	return delivery

#display results
print()
print("Total bill for", name.upper())
print("Tax: ", addedTax())
print("TakeAway: Ksh.")
print("Delivery charge: Ksh.")
print("Total: ", totalBill() + takeAway() + deliveryCharge())
print("Amount per person: Ksh.", splitTotals())
print("Thank you for your business, please come back again!!!")
