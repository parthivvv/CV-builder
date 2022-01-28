from cryptography import fernet

# key generation
key = fernet.generate_key()

# string the key in a file
with open('filekey.key', 'wb') as filekey:
    filekey.write(key)
