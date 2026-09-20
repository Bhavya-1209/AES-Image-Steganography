import cv2
import string
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import hashlib

# AES encrypt/decrypt helpers
def derive_key(key_str):
  return hashlib.sha256(key_str.encode()).digest()[:16] # AES-128

def encrypt_message(msg, key_str):
  key = derive_key(key_str)
  cipher = AES.new(key, AES.MODE_CBC)
  ct = cipher.encrypt(pad(msg.encode(), AES.block_size))
  return cipher.iv + ct

def decrypt_message(cipher_bytes, key_str):
  key = derive_key(key_str)
  iv = cipher_bytes[:16]
  ct = cipher_bytes[16:]
  Cipher = AES.new(key, AES.MODE_CBC, iv)
  return unpad(Cipher.decrypt(ct), AES.block_size).decode()

#char/Byte Mapping
d={}
c={}
for i in range(256):
  d[chr(i)]=i
  c[i]=chr(i)

#Load Image
x=cv2.imread('/content/stego.jpg')
i,j=x.shape[0],x.shape[1]
print("Image size:",i,j)

#Get user input
key=input("Enter Key to encrypt & hide:")
text=input("Enter Text to hide:")

#Encrypt message with AES
encrypted_bytes=encrypt_message(text,key)
l=len(encrypted_bytes)
print(f"Encrypted message length (in bytes): {l}")

#Hide encrypted data
kl = 0
n=0
m=0
z=0

for i in range(l):
  x[n, m, z]=encrypted_bytes[i]^d[key[kl]]
  n +=1
  m +=1
  z = (z+1) % 3
  m = (m+1) % 3
  kl = (kl+1) % len(key)

#save stegonography image
cv2.imwrite('encrypted_img.jpg', x)
print("success")

# Extraction
kl=0
n=0
m=0
z=0

ch=int(input("\nEnter 1 to extract data from Image:"))
if ch==1:
  key1=input("enter key to extract text:")
  if key == key1:
    encrypted_back=bytearray()
    for i in range(l):
      encrypted_back.append(x[n,m,z]^d[key[kl]])
      n+=1
      m+=1
      m=(m+1)%3
      z=(z+1)%3
      kl=(kl+1)%len(key)

    try:
      decrypted=decrypt_message(bytes(encrypted_back),key)
      print("Decrypted meassage:",decrypted)
    except:
      print("Invalid key or message is corrupted")
  else:
    print("key mismatch")
else:
  print("Thank you. Existing.")