def reciprocal_cipher(text):
    text=text.upper()
    result=""
    for char in text:
        if 'A'<=char<='Z':
            cipher_text=chr(155-ord(char))
            result+=cipher_text
        else:
            result+=char
    return result

original_text=input("Enter any string: ")
encrypted=reciprocal_cipher(original_text)
print("Encrypted text: ", encrypted)