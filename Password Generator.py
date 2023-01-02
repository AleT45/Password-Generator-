import random

def passwordGenerator(length):
    chars = "abcdefghinjklmonprstuvwxyzABCDEFGHIJKLMONPQRSTUVWXYZ123456789!@#$%^&*"
    password =""
    for _ in range(length):
        password += chars[random.randint(0, len(chars) - 1)]
    return password

length = int(input("Enter the desired password length with the 12 - 16 range: "))
if length < 12:
    print("Password is too short")
elif length > 16:
    print("Password is too long")
else:    
    password = passwordGenerator(length)
    print(password)
