def reciprocal_cipher(text):
    text = text.upper()
    cipher = ""
    for char in text:
        if 'A'<= char <='Z':
            cipher += chr(155-ord(char))
        else:
            cipher += char

    return cipher

# 
plain_text=input("Enter your message: ")
encrypted=reciprocal_cipher(plain_text)
print("Encrypted text: ", encrypted)    