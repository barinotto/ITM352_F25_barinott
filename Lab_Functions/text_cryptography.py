# test_cryptography.py

#try:
    #from cryptography.fernet import Fernet

    # Generate a key
   # key = Fernet.generate_key()
   #fernet = Fernet(key)

    # Encrypt and decrypt a message
   # message = b"Hello, cryptography!"
  #  encrypted = fernet.encrypt(message)
   # decrypted = fernet.decrypt(encrypted)

   # print("Encryption successful!")
   # print("Original message:", message)
   # print("Encrypted message:", encrypted)
   # print("Decrypted message:", decrypted)

#except ImportError:
   # print("cryptography library is NOT installed.")
#except Exception as e:
   # print("Something went wrong:", e)

from cryptography.fernet import Fernet

def encrypt_message(key: bytes, message: str) -> bytes:
    """Encrypt a plaintext message using the given key."""
    f = Fernet(key)
    # encode the message (string → bytes), then encrypt
    encrypted = f.encrypt(message.encode('utf-8'))
    return encrypted

def decrypt_message(key: bytes, encrypted_message: bytes) -> str:
    """Decrypt an encrypted message (bytes) using the given key."""
    f = Fernet(key)
    # decrypt returns bytes; decode to string
    decrypted_bytes = f.decrypt(encrypted_message)
    return decrypted_bytes.decode('utf-8')

def main():
    # Generate or load a key; here we generate a new one
    key = Fernet.generate_key()
    print("Encryption key (keep this secret!):", key)

    user_input = input("Enter a message to encrypt: ")

    encrypted = encrypt_message(key, user_input)
    print("Encrypted message:", encrypted)

    # Now decrypt it
    decrypted = decrypt_message(key, encrypted)
    print("Decrypted message:", decrypted)

if __name__ == "__main__":
    main()

