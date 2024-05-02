import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not any([use_letters, use_numbers, use_symbols]):
        print("Please select at least one type of characters.")
        return None
    
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    length = int(input("Enter the length of the password: "))
    use_letters = input("Use letters? (y/n): ").lower() == 'y'
    use_numbers = input("Use numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Use symbols? (y/n): ").lower() == 'y'
    
    password = generate_password(length, use_letters, use_numbers, use_symbols)
    if password:
        print("Generated password:", password)

if __name__ == "__main__":
    main()
