def ceaser_cipher(text,shift,mode="encrypt"):
    result = ""
    if mode == "decrypt": 
        shift = -shift
    for char in text:
        if char.isupper():
            result+=chr(ord(char)-65+shift%26+65)
        elif char.islower():
            result +=chr(ord(char)-97+shift%26+97)
        else:
            result+=char
    return result

text=input("enter message: ")
shift=int(input("enter shift value: "))
mode=input("enter mode (encrypt/decrypt): ")
output=ceaser_cipher(text,shift,mode)
print("Output: ", output)