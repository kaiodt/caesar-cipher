from caesar_cipher.caesar import encrypt

def test_encrypt_kaio_should_return_xnvb():
    assert encrypt('Kaio') == 'xnvb'

def test_encrypt_xnvb_should_return_xnvb():
    assert encrypt('xnvb') == 'kaio'

def test_encrypt_should_return_lowercase():
    assert encrypt('A').islower()

def test_encrypt_should_preserve_spaces():
    assert encrypt('A B')[1] == ' '
