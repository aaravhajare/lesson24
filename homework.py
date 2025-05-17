import random
import string

def generate_password(length):
    if length < 6:
        return "Password length should be at least 6 characters."

    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits

    # Combine all characters
    all_chars = lower + upper + digits

    # Ensure password has at least one lowercase, one uppercase, and one digit
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits)
    ]

    # Fill the remaining characters
    for _ in range(length - 3):
        password.append(random.choice(all_chars))

    # Shuffle the list to make it random
    random.shuffle(password)

    # Join list into string
    return ''.join(password)

# Example usage
password_length = int(input("Enter password length: "))
print("Generated Password:", generate_password(password_length))
