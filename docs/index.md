# Caesar's Cipher

The goal of this project is to implement an app that is capable of executing **Caesar's Cipher** (aka **ROT13**).

## Use Cases

### Encrypt

```python
from caesar import encrypt

encrypt('Kaio')  # xnvb
```

### Decrypt

```python
from caesar import decrypt

decrypt('xnvb')  # kaio
```

### Choosing a Rotation other than 13

```python
from caesar import decrypt, encrypt

encrypt('Kaio', 14)  # yowc
decrypt('yowc', 14)  # kaio
```
