import random
import string

def generate_password(letters, numbers, symbols):
    # pick characters from each type
    chars = (
        random.choices(string.ascii_letters, k=letters) +
        random.choices(string.digits,        k=numbers) +
        random.choices(string.punctuation,   k=symbols)
    )

    # shuffle and join
    random.shuffle(chars)
    return ''.join(chars)


def check_strength(total, numbers, symbols):
    if total >= 12 and numbers > 0 and symbols > 0:
        return "💪 Strong"
    elif total >= 8:
        return "😒 Medium"
    else:
        return "😿 Weak"


def get_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            print("Enter a positive number.")
        except ValueError:
            print("Numbers only please.")


# ___________ Main program ______________
print("🔐 Password Generator")
print("─" * 30)

letters = get_input("How many letters? : ")
numbers = get_input("How many numbers? : ")
symbols = get_input("How many symbols? : ")

total = letters + numbers + symbols

if total == 0:
    print("❌ Please enter at least 1 character.")
else:
    password = generate_password(letters, numbers, symbols)
    strength = check_strength(total, numbers, symbols)

    print("─" * 30)
    print(f"Password : {password}")
    print(f"Length   : {total}")
    print(f"Strength : {strength}")
    print("─" * 30)