def celsius_to_fahrenheit(c):
	return round((c * 9/5) + 32, 2)


def fahrenheit_to_celsius(f):
	return round((f - 32) * (5/9),2)

while True:
	print("Quick Tip \n'c' - Celsius and 'f' - Fahrenheit")
	from_temp = input("Enter the Temperature you're Converting From 'c' , 'f' >>").lower()
	while True:
		try:
			value = float(input("Enter your Value : "))
			break
		except Exception as e:
			print(f"{e}\nInvalid Value")
			
	if from_temp == 'c':
		print(f"{value}°C is --> {celsius_to_fahrenheit(value)}℉")
	elif from_temp == 'f':
		print(f"{value}℉ is --> {fahrenheit_to_celsius(value)}°C")
	else:
		print("Invalid Option")
