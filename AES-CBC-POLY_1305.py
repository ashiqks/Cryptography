
# coding: utf-8

# In[1]:


import secrets
import scrypt

password = 'to be passed or guessed'
salt = secrets.token_bytes(32)
key = scrypt.hash(password, salt, N=2048, r=8, p=1, buflen=32)
print(key)


# In[3]:


#Encryption and MAC generation

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Hash import Poly1305

def generate_Poly1305_mac(data, key):
    mac = Poly1305.new(key=key, cipher=AES, data=data)
    return (mac.hexdigest(), mac.nonce)

def verify_Poly1305_mac(data, key, nonce, mac_digest):
    mac_verify = Poly1305.new(data=data, key=key, nonce=nonce,                         
                         cipher=AES)
    try:
        mac_verify.hexverify(mac_digest)
        print('Message Authentication Success')
    except:
        print('Message Authentication Failed')
        
        
aes_enc = AES.new(key, AES.MODE_CBC)
data = b'message to be parsed using the AES symmetric cipher mode with a key derived from scrypt key derivation function'
cipher_text = aes_enc.encrypt(pad(data, AES.block_size))
iv = aes_enc.iv
hexdigest, poly_nonce = generate_Poly1305_mac(data=data, key=key)

print('hexdigest: ', hexdigest)
print('poly_nonce: ', poly_nonce)


# In[6]:


#Decryption and MAC verification

aes_dec = AES.new(key, AES.MODE_CBC, iv)
message = unpad(aes_dec.decrypt(cipher_text), AES.block_size)
verify_Poly1305_mac(data=message, key=key, nonce=poly_nonce, mac_digest=hexdigest)
print(message.decode('utf-8')) 

