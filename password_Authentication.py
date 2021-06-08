class Authentication():
    
    #constructor method
    def __init__(self, username):
        self.uname = username

    #username should include lowercase characters
    def lower(self):
        lower = any(char.islower() for char in self.uname)
        return lower

    #username should include uppercase characters
    def upper(self):
        upper = any(char.isupper() for char in self.uname)
        return upper

    #username should include number characters
    def digit(self):
        digit = any(char.isdigit() for char in self.uname)
        return digit

    def validate(self):
        lower_one = self.lower()
        upper_one = self.upper()
        digit_one = self.digit()
        length = len(self.uname) #length of the username
                                                            #length has to be greater or equals 8
        all_def = lower_one and upper_one and digit_one and length >= 8

        #executes if all_def = True
        if all_def: # or if lower_one and upper_one and digit_one and length >= 8
            print("Username checked out")
            return True

        #executes if lower_one = false
        elif not lower_one:
            print("You didn't use lowercase")
            return False

        #executes if upper_one = false
        elif not upper_one:
            print("You didn't use uppercase")
            return False

        #executes if digit_one = false
        elif not digit_one:
            print("You didn't use number")
            return False
            
        #executes if if length of username is less than 8
        elif length < 8:
            print("Username should at least have 8 characters")


C = Authentication(input())
d = C.validate()
print(d)