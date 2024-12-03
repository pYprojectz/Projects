def lower_case(string):
	lower_txt = ""
	lst = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	for i in string:
		if i in lst:
			j = ord(i) + 32
			lower_txt += chr(j)
		else:
			lower_txt += i
	return lower_txt


def upper_case(string):
	upper_txt = ""
	lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	for i in string:
		if i in lst:
			j = ord(i) - 32
			upper_txt += chr(j)
		else:
			upper_txt += i
	return upper_txt


while True:
	user = input("Enter text to Convert :- ")
	print(f"The Lowercase Version :- {lower_case(user)} \n")
	print(f"The Uppercase Version :- {upper_case(user)}")

