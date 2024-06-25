import random
import string

def main():
    password = generate_password(12)
    print("Generated password:", password)

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_strength(password):
    strength = "Weak"  # À compléter avec la logique pour évaluer la force du mot de passe
    return strength

def additional_function():
    # Exemple d'une autre fonction personnalisée
    pass

if __name__ == "__main__":
    main()
