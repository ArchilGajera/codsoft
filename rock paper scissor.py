import random
import string

def generate_password(length):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    length = max(length, 8)

    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

def main():
    try:
        password_length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Please enter a valid integer for the password length.")
        return

    password = generate_password(password_length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
