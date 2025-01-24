from string import ascii_lowercase
def encrypt(text,n=13):
    """encrypts text"""
    encrypted = ""
    for l in text:
        l = l.lower()
        if l == ' ':
            encrypted += l
        elif l not in ascii_lowercase: ...
        else:
            pos = ascii_lowercase.find(l) + n
            l = ascii_lowercase[pos % 26]
            encrypted += l
    return encrypted

def decrypt(text,n=13):
    "decrypts text"
    decrypted = ""
    for l in text:
        l = l.lower()
        if l == ' ':
            decrypted += l
        elif l not in ascii_lowercase: ...
        else:
            pos = ascii_lowercase.find(l) - n
            l = ascii_lowercase[pos % 26]
            decrypted += l
    return decrypted