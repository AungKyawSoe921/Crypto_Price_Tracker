import os
from cryptography.fernet import Fernet

# Path to store the key
key_path = 'secret.key'

def generate_key():
    """Generate and save a key if it does not exist."""
    if not os.path.exists(key_path):
        key = Fernet.generate_key()
        with open(key_path, 'wb') as key_file:
            key_file.write(key)
        print("Key generated and saved.")
    else:
        print("Key already exists.")

def load_key():
    """Load the saved key."""
    if os.path.exists(key_path):
        with open(key_path, 'rb') as key_file:
            key = key_file.read()
        return key
    else:
        raise FileNotFoundError("Encryption key not found. Generate it first.")

def encrypt_password(password):
    """Encrypt the provided password."""
    key = load_key()
    cipher_suite = Fernet(key)
    encrypted_password = cipher_suite.encrypt(password.encode())
    return encrypted_password

def decrypt_password(encrypted_password):
    """Decrypt the provided encrypted password."""
    key = load_key()
    cipher_suite = Fernet(key)
    decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
    return decrypted_password

def main():
    generate_key()  # Generate the key if it doesn't exist

    choice = input("Do you want to (E)ncrypt or (D)ecrypt a password? ").strip().upper()

    if choice == 'E':
        password = input("Enter your Gmail password to encrypt: ").strip()
        encrypted_password = encrypt_password(password)
        print("Encrypted password:", encrypted_password.decode())
    elif choice == 'D':
        encrypted_password = input("Enter the encrypted password to decrypt: ").strip()
        try:
            encrypted_password = encrypted_password.encode()  # Convert input to bytes
            decrypted_password = decrypt_password(encrypted_password)
            print("Decrypted password:", decrypted_password)
        except Exception as e:
            print("Error decrypting password:", e)
    else:
        print("Invalid choice. Please choose (E) or (D).")

if __name__ == "__main__":
    main()
