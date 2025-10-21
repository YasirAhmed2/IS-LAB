import string
alphabet = string.ascii_uppercase
key = "QWERTYUIOPASDFGHJKLZXCVBNM"
encryption_dict={alphabet[i]:key[i] for i in range(26)}
decryption_dict={key[i]:alphabet[i] for i in range(26)}

def encrypt(text):
    result = ""
    
    for char in text.upper():
        if char in encryption_dict:
            result+=encryption_dict[char]
        else:
            resut+=char
    return result

def decrypt(text):
    result=""
 
    for char in text.upper():
        if char in decryption_dict:
            result+=decryption_dict[char]
        else:
            result+=char    
    return result

plain_text=input("Enter your message: ")
mode=input("Enter mode (encrypt/decrypt): ")
if mode=="encrypt":
    output=encrypt(plain_text)
else:
    output=decrypt(plain_text)

print("Output: ", output)