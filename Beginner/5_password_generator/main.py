import random
import string


letters = [i for i in string.ascii_letters]
digits = [digit for digit in string.digits]
sys = [punc for punc in string.punctuation]
all_chars = letters + digits + sys

print("Welcome to Command-Line Password Generator")
print("To generate your Password")
length = int(input("     Enter the length of your password 10 - 45 : >>"))
password = ""

for i in range(length):
	a = random.choice(all_chars)
	password += a

print(f"Your Generated password is -->  '{password}'")
print(len(password))