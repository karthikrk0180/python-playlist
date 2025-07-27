def encrypt(message, key):
    result = ""
    
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + key) % 26
            result += chr(base+shifted)
        else:
            result += char  
            
    return result

def decrypt(message, key):
    return encrypt(message, -key)

def main():
    print("======Ceaser Cipher=====")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt: ").strip().upper()
    
    if choice not in ['E','D']:
        print("Invalid choice. Please select E or D\n")
        return
    
    message = input("Enter the message: ")
    try:
        key = int(input("Enter the Key (Integer): "))
    except ValueError:
        print("Invalid key! \n")
        return
    
    if choice == 'E':
        result = encrypt(message, key)
        print(f"Encrypted Message: {result}")
    else:
        result = decrypt(message,key)
        print(f"Decrypted Message: {result}")
        
    
    
if __name__ == "__main__":
    main()