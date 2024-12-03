
value = input("Welcome which year would you like to check ? ")

if not value.isdigit():
	print("Invalid year")
else:
	value = int(value)
	if value % 4 == 0:
		print(f"The year {value} is a leap year")
	else:
		print(f"The year {value} is not a leap year")
