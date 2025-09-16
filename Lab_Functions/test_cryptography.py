import cryptography
print(f"Cryptography library imported successfully!")
print(f"Version: {cryptography.__version__}")
from cryptography.fernet import Fernet

def main():
    # generate a key
    key = Fernet.generate_key()
    cipher = Fernet(key)
    
    # get input from user
    message_str = input("Enter a message to encrypt: ")
    
    # encode to bytes
    message_bytes = message_str.encode('utf-8')
    
    # encrypt
    token = cipher.encrypt(message_bytes)
    print("Encrypted token:", token)
    
    # decrypt
    decrypted_bytes = cipher.decrypt(token)
    
    # decode back to string
    decrypted_str = decrypted_bytes.decode('utf-8')
    print("Decrypted message:", decrypted_str)

if __name__ == "__main__":
    main()
