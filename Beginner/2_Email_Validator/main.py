
# email = input("Enter your Email")
fnd = False
list_of_email_providers = ["@gmail.com","@yahoo.com","@hotmail.com","@icloud.com","@outlook.com","@pypro.com"]

email = input("Enter your Email")
if len(email) > 13:
	for suffix in list_of_email_providers:
		if suffix in email:
			print("You have a valid Email")
			print("You can Proceed")
			fnd = True
		
if not fnd:
	print("Your email is invalid")