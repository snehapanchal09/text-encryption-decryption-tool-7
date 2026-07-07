import base64

print("===== Simple Text Encryption & Decryption Tool =====")

text = input("Enter your text: ")

print("\n1. Encrypt")
print("2. Decrypt")

choice = input("Enter your choice (1/2): ")

if choice == "1":
    encrypted = base64.b64encode(text.encode()).decode()
    print("\nEncrypted Text:")
    print(encrypted)

elif choice == "2":
    try:
        decrypted = base64.b64decode(text.encode()).decode()
        print("\nDecrypted Text:")
        print(decrypted)
    except:
        print("Invalid encrypted text!")

else:
    print("Invalid choice!")