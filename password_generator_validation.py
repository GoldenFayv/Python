############### PASSWORD VALIDATION ##########################


# Should have at least one number.
# Should have at least one uppercase and one lowercase character.
# Should have at least one special symbol.
# Should be between 8 to 32 characters long.

specialSymbol = "^[];',./!@#\"\$%^&*()_+:<>?"

while True: #The loop will run indefinitely until something within it breaks it
	def password_validation(password):
		validate = True

		if len(password) < 8 or len(password) > 32:
			print("length of password should be in the range of 8 and 32")
			validate = False

		elif not any(char.isdigit() for char in password):
			print("Add at least one numerical value")
			validate = False

		elif not any(char.isupper() for char in password):
			print("Add at least one uppercase")
			validate = False

		elif not any(char.islower() for char in password):
			print("Add at least one lowercase")
			validate = False

		elif not any(char in specialSymbol for char in password):
			print("Add at least one specialSymbol")
			validate = False

		if validate:
			return validate


	if(password_validation(input())):
		print("valid password")
		break
	
	else:
		print("Invalid password")

# import random

# def password_generator():
# 	password_size = int(input())

# 	password_list = "qwertyuiopasdfgjklzxcvbnm1234567890"#[];',./!@#$%^&*()_+:<>?"

# 	# password = "".join(random.sample(password_list, password_size))
# 	print(random.sample(password_list, password_size))
# 	# print(password)
# password_generator()