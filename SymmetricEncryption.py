"""
The objective of this script is to implement encryption for a message using block cipher (AES and DES).
- Generating the same key for both methods.
- Carry out a code analysis to come up with the weaknesses and strengths.
- Measure each algorithm's encryption speed.
- Measure each algorithm's RAM memory usage.
"""

import time
import psutil
from Crypto.Cipher import AES, DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

message = input("Enter your message: ")

# Function to convert message to bytes
def message_bytes():
    byte_input = message.encode('utf-8')
    return byte_input

base_key = get_random_bytes(32) # generates the shared key

# AES Cipher Setup
aes_key = base_key[:16]  # AES needs a key that is 128 bits long (16 bytes).
start_time = time.time()  # Start timer for AES encryption
aes_cipher = AES.new(aes_key, AES.MODE_CBC) # Creates AES cipher object using CBC mode.
aes_cipher_text = aes_cipher.encrypt(pad(message_bytes(), AES.block_size)) # Encrypts the cipher object
aes_encrypt_time = time.time() - start_time  # Measure time taken for AES encryption
aes_init_vec = aes_cipher.iv # Saves the cipher's Initialization Vector

# DES Cipher Setup
des_key = base_key[:8]  # DES uses a 56-bit key (8 bytes).
start_time = time.time()  # Start timer for DES encryption
des_cipher = DES.new(des_key, DES.MODE_CBC) # Creates DES cipher object using CBC mode.
des_cipher_text = des_cipher.encrypt(pad(message_bytes(), DES.block_size)) # Encrypts the cipher object.
des_encrypt_time = time.time() - start_time  # Measure time taken for DES encryption
des_init_vec = des_cipher.iv # Saves IV.

# Outputting encrypted results
print("AES Encrypted:", aes_cipher_text.hex())
print("DES Encrypted:", des_cipher_text.hex())

# AES Decipher Function
aes_decipher = AES.new(aes_key, AES.MODE_CBC, iv=aes_init_vec)
start_time = time.time()  # Start timer for decryption
aes_plain_text = unpad(aes_decipher.decrypt(aes_cipher_text), AES.block_size)
aes_decrypt_time = time.time() - start_time  # Measure time taken for decryption

# DES Decipher Function
des_decipher = DES.new(des_key, DES.MODE_CBC, iv=des_init_vec)
start_time = time.time()
des_plain_text = unpad(des_decipher.decrypt(des_cipher_text), DES.block_size)
des_decrypt_time = time.time() - start_time

# Outputting decrypted results
print("AES Decrypted:", aes_plain_text.decode('utf-8'))
print("DES Decrypted:", des_plain_text.decode('utf-8'))

# Measure the RAM used by the process
process = psutil.Process()
memory_usage = process.memory_info().rss / (1024 * 1024) # Convert to MB
print(f"RAM Used: {memory_usage:.2f} MB")

# Output encryption times
print(f"AES Encryption Time: {aes_encrypt_time:.6f} seconds")
print(f"DES Encryption Time: {des_encrypt_time:.6f} seconds")