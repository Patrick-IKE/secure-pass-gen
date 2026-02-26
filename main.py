import random
import string

def password_gen():
    while True:
        print("-"*45)
        name = input("what is your name? ").title()
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        punctuation = ["!","@","$","#","%","^","&","*","(",")","_","-","+","="]
        amount = int(input(f"Hello {name}. welcome to the password generator. Choose between 8 - 12 for the length of your password: "))
        while amount < 8 or amount > 12:
            print("Invalid input!")
            amount = int(input("Choose between 8 - 12 for the length of your password: "))

        keg = random.sample(numbers + punctuation + random.sample(string.ascii_letters, 52), amount)
        pass_key = "".join(keg)
        print(pass_key)
        print("-"*45)
        retry = input("Press 1 to continue or 0 to exit the program: ")
        while retry not in ["1", "0"]:
            print("Invalid input!")
            retry = input("Press 1 to continue or 0 to exit the program: ")
        if retry == "0":
            print("End of the program, bye!")
            break

password_gen()
