from caesar import encrypt, decrypt
from argparse import ArgumentParser

parser = ArgumentParser(description="Caesar's Cipher")
parser.add_argument('text', help='Text to encrypt/decrypt', type=str)
parser.add_argument('-n', help='Shift value', default=13, type=int, required=False)
parser.add_argument('-d', help='Decrypt text', required=False, action='store_true')

def cli():
    args = parser.parse_args()
    if args.d:
        result = decrypt(args.text, args.n)
    else:
        result = encrypt(args.text, args.n)
    
    print(f'Input: {args.text}')
    print(f'Output: {result}')

cli()