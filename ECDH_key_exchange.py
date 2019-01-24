
# coding: utf-8

# In[ ]:


#Importing necessary modules
from tinyec import registry
import secrets

#Getting the 'brainpoolP256r1' curve from the registry 
curve = registry.get_curve('brainpoolP256r1')
#Generating Alice's private 
alice_privatekey = secrets.randbelow(curve.field.n)
print("Alice's private key: ", alice_privatekey)
#Generating Bob's private key
bob_privatekey = secrets.randbelow(curve.field.n)
print("Bob's private key: ", bob_privatekey)

#Generating Alice's public key from her private key using the Generator point
alice_publickey = alice_privatekey * curve.g
print("Alice's public key: ", alice_publickey)
#Generating Bob's public key from his private key using the Generator point
bob_publickey = bob_privatekey * curve.g
print("Bob's public key: ", bob_publickey)
#The shared key with Alice
alice_sharedkey = alice_privatekey*bob_publickey
print("Alice's shared secret key: ", alice_sharedkey)
#The shared key with Bob
bob_sharedkey = bob_privatekey*alice_publickey
print("Bob's shared secret key: ", bob_sharedkey)

try:
    alice_sharedkey == bob_sharedkey
    print("Shared secret keys match each other")
except:
    print("Shared secret keys don't match each other")

