
# coding: utf-8

# In[ ]:


import hashlib
from binascii import hexlify

#Convert the x & y components to bytes of length 32
x_component = int.to_bytes(alice_sharedkey.x, 32, 'big')
y_component = int.to_bytes(alice_sharedkey.y, 32, 'big')

#Create a SHA3_256 class
sha3_key = hashlib.sha3_256()

#Update the hash object with x_component
sha3_key.update(x_component)

#Concatenate the y_component with x_component in the hash object
sha3_key.update(y_component)

#Derive the key
secret_key = hexlify(sha3_key.digest())

print(secret_key)

