num = input("Enter a number you'd like to get the multiplication table for >> ")
rang = input("Enter the range from 1 - ")

if not num.isdigit():
	print("Invalid number Try 'Digits' instead")
else:
	num = int(num)
	if not rang.isdigit():
		pass
	else:
		rang = int(rang)
		for i in range(1,(rang+1),1):
			print(f"| --- {num} ❌ {i}  =  {num * i} ---- | ")
