def valid_age(age):
    if age < 18 or age > 60:
        print("You are not old enough.")
        return False
    return True

def confirmpasswd(passwd, confirm_passwd):
    if passwd != confirm_passwd:
        print("Invalid password! Please try again.")
        return False
    return True
