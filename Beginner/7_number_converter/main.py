target_vals = {
	'h':'Hexadecimal',
	'o':'Octal',
	'b': 'Binary'
}
value = int(input("Decimal Value they will like to convert"))
target = input("Enter Target value h - hex , b - bin, o - oct").lower()

if target == 'h':
	print(f"The {target_vals[target]} Equivalent of {value} = {str(hex(value))[2:]}")
elif target == 'o':
	print(f"The {target_vals[target]} Equivalent of {value} = {str(oct(value))[2:]}")
elif target == 'b':
	print(f"The {target_vals[target]} Equivalent of {value} = {str(bin(value))[2:]}")
else:
	print("Invalid input")