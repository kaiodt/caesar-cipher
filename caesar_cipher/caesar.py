from string import ascii_lowercase


def encrypt(text, rot=13):
    """Encrypts text."""
    encrypted = ''

    for char in text.lower():
        if char == ' ':
            encrypted += char
        elif char not in ascii_lowercase:
            ...
        else:
            pos = ascii_lowercase.find(char) + rot
            encrypted += ascii_lowercase[pos % 26]

    return encrypted


def decrypt(text, rot=13):
    """Decrypts text."""
    decrypted = ''

    for char in text.lower():
        if char == ' ':
            decrypted += char
        elif char not in ascii_lowercase:
            ...
        else:
            pos = ascii_lowercase.find(char) - rot
            decrypted += ascii_lowercase[pos % 26]

    return decrypted
