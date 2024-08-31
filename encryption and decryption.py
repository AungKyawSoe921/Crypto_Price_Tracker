import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from cryptography.fernet import Fernet

# Function to generate a key and write it to a file
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Function to load the key from a file
def load_key():
    return open("secret.key", "rb").read()

# Function to encrypt a message
def encrypt_message(message):
    key = load_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

# Function to decrypt a message
def decrypt_message(encrypted_message):
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message

# Function to handle encryption button click
def encrypt():
    message = entry.get()
    if not message:
        messagebox.showwarning("Input Error", "Please enter a message to encrypt.")
        return
    encrypted_message = encrypt_message(message)
    result_var.set(f"Encrypted message: {encrypted_message.decode()}")
    copy_button.config(state=tk.NORMAL)
    # Save the encrypted message to a variable for copying
    root.clipboard_clear()
    root.clipboard_append(encrypted_message.decode())

# Function to handle decryption button click
def decrypt():
    encrypted_message = entry.get()
    if not encrypted_message:
        messagebox.showwarning("Input Error", "Please enter a message to decrypt.")
        return
    try:
        decrypted_message = decrypt_message(encrypted_message.encode())
        result_var.set(f"Decrypted message: {decrypted_message}")
    except Exception as e:
        messagebox.showerror("Decryption Error", f"Failed to decrypt message: {str(e)}")

# Function to copy the encrypted message to the clipboard
def copy_to_clipboard():
    encrypted_message = result_var.get().split(": ")[1]
    root.clipboard_clear()
    root.clipboard_append(encrypted_message)
    messagebox.showinfo("Copied", "Encrypted message copied to clipboard.")

# Generate and write a new key (only need to do this once)
generate_key()

# Set up the GUI
root = tk.Tk()
root.title("Encrypt and Decrypt")
root.geometry("600x400")  # Set the window size

# Main frame
main_frame = ttk.Frame(root, padding="20 20 20 20")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Entry frame
entry_frame = ttk.Frame(main_frame, padding="10 10 10 10")
entry_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

ttk.Label(entry_frame, text="Enter your message:", font=("Helvetica", 14)).grid(row=0, column=0, pady=10, sticky=tk.W)
entry = ttk.Entry(entry_frame, width=70, font=("Helvetica", 14))
entry.grid(row=1, column=0, pady=10, sticky=(tk.W, tk.E))

# Button frame
button_frame = ttk.Frame(main_frame, padding="10 10 10 10")
button_frame.grid(row=1, column=0, pady=20, sticky=(tk.W, tk.E))

encrypt_button = ttk.Button(button_frame, text="Encrypt", command=encrypt, width=20)
encrypt_button.grid(row=0, column=0, padx=10)

decrypt_button = ttk.Button(button_frame, text="Decrypt", command=decrypt, width=20)
decrypt_button.grid(row=0, column=1, padx=10)

copy_button = ttk.Button(button_frame, text="Copy to Clipboard", state=tk.DISABLED, command=copy_to_clipboard, width=20)
copy_button.grid(row=0, column=2, padx=10)

# Result label
result_var = tk.StringVar()
result_label = ttk.Label(main_frame, textvariable=result_var, wraplength=550, font=("Helvetica", 14))
result_label.grid(row=2, column=0, pady=20, sticky=(tk.W, tk.E))

# Configure resizing
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
main_frame.columnconfigure(0, weight=1)

root.mainloop()
