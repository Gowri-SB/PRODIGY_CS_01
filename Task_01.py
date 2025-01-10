def caesar_cipher():
    def encrypt(text, shift):
        result = ""
        for char in text:
            if char.isalpha():  # Check if character is a letter
                shift_base = ord('A') if char.isupper() else ord('a')
                # Shift character and wrap around
                shifted = (ord(char) - shift_base + shift) % 26 + shift_base
                result += chr(shifted)
            else:
                result += char  # Non-alphabetic characters remain unchanged
        return result

    def decrypt(text, shift):
        return encrypt(text, -shift)  # Decryption is reverse of encryption

    print("Welcome to the Caesar Cipher!")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    choice = input("Choose an option (1 or 2): ")

    if choice not in ['1', '2']:
        print("Invalid choice. Please choose 1 or 2.")
        return

    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (integer): "))

    if choice == '1':
        encrypted_message = encrypt(message, shift)
        print("Encrypted Message:", encrypted_message)
    elif choice == '2':
        decrypted_message = decrypt(message, shift)
        print("Decrypted Message:", decrypted_message)

# Run the program
caesar_cipher()
