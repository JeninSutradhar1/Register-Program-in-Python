from helpers import confirmpasswd
from helpers import valid_age

# Take username
name = input("What is your name?: ")
print("Hello!", name)
print("Let's make a 2-step sign in!")

# Ask a valid age (18-60)
age = int(input("What is your age?: "))

if not valid_age(age):
    exit()

# Set a password for user
passwd = input("Set a password: ")
confirm_passwd = input("Confirm password: ")
# Confirm password
if not confirmpasswd(passwd, confirm_passwd):
    exit()

# Greet!
print("Congratulations! Your name has been successfully registered.")