def c_to_f(c=None, f=None):
	ans = 0
	if c is not None:
		ans = ((c * 9 / 5) + 32)
	elif f is not None:
		ans = (f - 32) / (9 / 5)
	return round(ans, 1)


def c_to_k(c=None, k=None):
	ans = 0
	if k is None:
		ans = c + 273.15
	elif c is None:
		ans = k - 273.15
	return round(ans, 1)


def k_to_f(k=None, f=None):
	ans = 0
	if k is not None:
		ans = ((k - 273.15) * 9 / 5) + 32
	elif f is not None:
		ans = ((f - 32) * 5 / 9) + 273.15
	return round(ans, 1)


lst = ['c', 'k', 'f']

while True:
	print("Welcome to Temp Converter")
	print("Quick Tip : 'c' --> celsius , 'f' --> fahrenheit , 'k --> Kelvin' \n")
	fro = input("You are Converting From ? c , f, k --> ").lower()
	to = input("You are Converting To    ? c , f, k --> ").lower()
	
	if fro in lst and to in lst:
		while True:
			try:
				value_fro = float(input("Enter the Value >> "))
				break
			except Exception as e:
				print(f"{e}\nEnter a Valid number")
				
		if fro == 'c' and to == 'f':
			result = c_to_f(c=value_fro)
			print(f"{value_fro}℃ --> {result}℉")
		
		elif fro == 'c' and to == 'k':
			result = c_to_k(c=value_fro)
			print(f"{value_fro}℃ --> {result}°K")
		
		elif fro == 'f' and to == 'c':
			result = c_to_f(f=value_fro)
			print(f"{value_fro}℉ --> {result}℃")
		
		elif fro == 'f' and to == 'k':
			result = k_to_f(f=value_fro)
			print(f"{value_fro}℉ --> {result}°K")
		
		elif fro == 'k' and to == 'f':
			result = k_to_f(k=value_fro)
			print(f"{value_fro}°K --> {result}℉")
		
		elif fro == 'k' and to == 'c':
			result = c_to_k(k=value_fro)
			print(f"{value_fro}°K --> {result}℃")
		
		elif fro == to:
			print("From and To cannot be the same Values")
		
		else:
			print("Invalid Option")
			
			
# # Implemented the if and else using the match Case method if you'd like to check it out as well
# 		match (fro, to):
# 			case ('c', 'f'):
# 				result = c_to_f(c=value_fro)
# 				print(f"{value_fro}℃ --> {result}℉")
#
# 			case ('c', 'k'):
# 				result = c_to_k(c=value_fro)
# 				print(f"{value_fro}℃ --> {result}°K")
#
# 			case ('f', 'c'):
# 				result = c_to_f(f=value_fro)
# 				print(f"{value_fro}℉ --> {result}℃")
#
# 			case ('f', 'k'):
# 				result = k_to_f(f=value_fro)
# 				print(f"{value_fro}℉ --> {result}°K")
#
# 			case ('k', 'f'):
# 				result = k_to_f(k=value_fro)
# 				print(f"{value_fro}°K --> {result}℉")
#
# 			case ('k', 'c'):
# 				result = c_to_k(k=value_fro)
# 				print(f"{value_fro}°K --> {result}℃")
#
# 			case _ if fro == to:
# 				print("From and To cannot be the same Values")
#
# 			case _:
# 				print("Invalid Option")
#
	
	else:
		print("Invalid Option")
		
		
