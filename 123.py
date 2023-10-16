def encrypt(text,s):
    result=" "
    for i in range (len(text)):
        char=text[i]
        if (char.isupper()):
            result+= char((ord(char)+s-65)%26+ 65)
        else:
            result += char((ord(char) + s-97)% 26 + 97)
            return result
text="ATTACKATONCE"
s=4
print("Text:"+text)
print("Shift:"+str(s))
print("Cipher:"+encrypt(text,s))
        
            