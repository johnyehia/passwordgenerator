import random
import string

def generate_password(length, uppercase=True, lowercase=True, digits=True, symbols=True):
    chars = ''
    if uppercase:
        chars += string.ascii_uppercase
    if lowercase:
        chars += string.ascii_lowercase
    if digits:
        chars += string.digits
    if symbols:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password


def save_password(password, filename):
    with open(filename, 'a') as f:
        f.write(password + '\n')


length = int(input("Enter password length: "))
uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
digits = input("Include digits? (y/n): ").lower() == 'y'
symbols = input("Include symbols? (y/n): ").lower() == 'y'

password = generate_password(length, uppercase, lowercase, digits, symbols)
print("Your password is:", password)

save = input("Save password to file? (y/n): ").lower() == 'y'
if save:
    filename = input("Enter filename: ")
    save_password(password, filename)
    print("Password saved to file!")
