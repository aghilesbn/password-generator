import random
import string

def main():
    # Main function that utilizes other functions to generate a password
    password = generate_password(12)  # Example: generate a 12-character password
    print("Generated password:", password)

def generate_password(length):
    # Function to generate a random password
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_strength(password):
    # Optional function to evaluate password strength (bonus)
    strength = "Weak"  # Logic to evaluate password strength
    return strength

if __name__ == "__main__":
    main()
