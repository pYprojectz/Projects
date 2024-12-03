while True:
	user_age = input("Enter Your age : ")
	if user_age.isdigit():
		user_age = int(user_age)
		if 100 > user_age >= 18:
			print("User is an Adult")
			break
		elif 0 < user_age < 18:
			print("User is not an Adult")
			break
		else:
			print("Invalid Age\nRange is between 1-100\nTry Again")
	else:
		print(f"{user_age} is Invalid")