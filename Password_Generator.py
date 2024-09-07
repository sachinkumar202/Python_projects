import random
import string

def generate_password(length, use_uppercase, use_digits, use_special):
    # Define possible characters based on user preferences
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    special = string.punctuation if use_special else ''

    # Combine all possible characters
    all_characters = lower + upper + digits + special
    
    # Ensure at least some characters are selected
    if len(all_characters) == 0:
        raise ValueError("No character types selected. Please enable at least one option.")

    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    print("Password Generator")

    # Get user preferences
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            raise ValueError("Length must be a positive number.")
        
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_special = input("Include special characters? (y/n): ").lower() == 'y'

        # Generate and display the password
        password = generate_password(length, use_uppercase, use_digits, use_special)
        print(f"Generated Password: {password}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
