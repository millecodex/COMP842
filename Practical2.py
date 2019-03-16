# full documentation of the cryptography library available at:
# https://pypi.org/project/cryptography/
import hashlib
from cryptography.fernet import Fernet
# Fernet.decrypt|encrypt|extract_timestamp|generate_key
# Standard fernet is a 128 bit key, more specifically it is AES in CBC mode
# every time a key is generated, fernet access the system os.random funtion
key = Fernet.generate_key()
print(key)
key2 = Fernet.generate_key()
print(key2)

# show listing of available methods
print(dir(Fernet))
#
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(b'we attack at dawn')
cipher_text_2 = cipher_suite.encrypt(b'We attack at dawn')
plain_text = cipher_suite.decrypt(cipher_text)
plain_text = plain_text.decode()

# backend provides access to a variety of helper methods
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
# 'ec' is elliptic curve cryptography library
# warning for all 'hazmat' stuffs: 
# beware the application you're coding!
from cryptography.hazmat.primitives.asymmetric import ec
# needs two parameters, curve and backend
curve = ec.SECP256K1()
private_key = ec.generate_private_key(curve,default_backend())
public_key = private_key.public_key()
print(public_key)

# view the private key (human readable) we must invoke serialization of the key object
from cryptography.hazmat.primitives import serialization
private_ks = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption())
# this is a byte object decoded into base64
print(private_ks.decode())

public_ks =public_key.public_bytes(
    serialization.Encoding.PEM,
    serialization.PublicFormat.SubjectPublicKeyInfo)
print(public_ks.decode())

# there is a method to output the curve coordinates in decimal
# outputs coordinates: the (x,y) point on the curve
print(public_key.public_numbers()) 
x_coord = public_key.public_numbers()._x
# convert to hex
pub_key_hex = hex(x_coord)
# strip the first two characters signifying python hex number
pub_key_hex = pub_key_hex[2:]
# append the prefix 03 indicating that the y-value was odd
# with this code, half the address should not validate
pub_key_hex = '03'+pub_key_hex

import hashlib
# double-hashed first as sha256, then as ripemd160 
temp = hashlib.sha256(pub_key_hex.encode())
pub_key_hash = hashlib.new('ripemd160',temp.digest()).digest()

# prefix a zero byte for a bitcoin address
pub_key_hash = bytes.fromhex('00')+pub_key_hash

# double sha256 hash and take the first 4 bytes as a checksum
dubhash = hashlib.sha256(hashlib.sha256(pub_key_hash).digest()).digest()
checksum = dubhash[:4]
pub_key_hash = pub_key_hash + checksum

# now convert to base58 encoding
# may have to >>> pip install base58
import base58
b58 = base58.b58encode(pub_key_hash)
btc_address = b58.decode()
print(btc_address)