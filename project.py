import random
import string
import sys
import pyfiglet

def print_usage_and_exit():
    """Print usage instructions and exit."""
    print("Usage: python figlet.py [-f | --font <font_name>]")
    sys.exit(1)

def display_name_in_ascii():
    """Display a stylized ASCII art of 'AGHILES' using pyfiglet."""
    ascii_art = pyfiglet.figlet_format("AGHILES", font="slant")
    print(ascii_art)

def menu():
    """Display the main menu and prompt user for choice."""
    display_name_in_ascii()
    print("\nMenu:")
    print("1. Generate a random password")
    print("2. Choose a password starting with a specified word")
    print("3. Choose a password ending with a specified word")
    choice = input("Choose an option (1/2/3): ")
    return choice

def main():
    """Main function to manage the password generator."""
    choice = menu()

    if choice == '1':
        length = int(input("Enter the length of the password: "))
        password = generate_password(length)
        print("Generated password:", password)
    elif choice == '2':
        start_word = input("Enter the word to start the password with: ")
        length = int(input("Enter the length of the password: "))
        try:
            password = password_starting_with(start_word, length)
            print("Generated password starting with '{}': {}".format(start_word, password))
        except ValueError as ve:
            print(ve)
    elif choice == '3':
        end_word = input("Enter the word to end the password with: ")
        length = int(input("Enter the length of the password: "))
        try:
            password = password_ending_with(end_word, length)
            print("Generated password ending with '{}': {}".format(end_word, password))
        except ValueError as ve:
            print(ve)
    else:
        print("Invalid option.")

def generate_password(length):
    """Generate a random password of specified length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_starting_with(word, length):
    """Generate a password starting with a specified word."""
    characters = string.ascii_letters + string.digits + string.punctuation
    if len(word) >= length:
        raise ValueError("The specified word is longer than the requested password length.")
    start_password = word + ''.join(random.choice(characters) for _ in range(length - len(word)))
    return start_password

def password_ending_with(word, length):
    """Generate a password ending with a specified word."""
    characters = string.ascii_letters + string.digits + string.punctuation
    if len(word) >= length:
        raise ValueError("The specified word is longer than the requested password length.")
    end_password = ''.join(random.choice(characters) for _ in range(length - len(word))) + word
    return end_password

if __name__ == "__main__":
    main()
