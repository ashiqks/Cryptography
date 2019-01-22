
# coding: utf-8

# In[1]:


import secrets
import scrypt

password = 'to be passed or guessed'
salt = secrets.token_bytes(32)
key = scrypt.hash(password, salt, N=2048, r=8, p=1, buflen=32)
print(key)


# In[2]:


#Encryption
from Crypto.Cipher import ChaCha20_Poly1305 as cha

data = b'Cipher with authentication enabled'
chacha20 = cha.new(key=key)
cipher_text, mac = chacha20.encrypt_and_digest(data)
nonce = chacha20.nonce

print('cipher_text: ', cipher_text)
print('mac: ', mac)


# In[3]:


#Decryption

try:
    chacha_poly = cha.new(key=key, nonce=nonce)
    data = chacha_poly.decrypt_and_verify(cipher_text, mac)
    print('The message is: ', data)
    print('Message is verified')
except:
    print("The message couldn't be verified")

