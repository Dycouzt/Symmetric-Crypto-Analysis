"""
This is the AES encryption algorithm module. Includes its function, where the goal is to create a cipher object,
encrypt it and decrypt it, measuring the algorithm's speed and RAM usage.
"""

import time
import psutil
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

base_key = get_random_bytes(32) # generates the shared key

def aes_encryption(message_bytes):

    aes_key = base_key[:16]  # AES needs a key that is 128 bits long (16 bytes).
    start_time = time.time()  # Start timer for AES encryption
    aes_cipher = AES.new(aes_key, AES.MODE_CBC)  # Creates AES cipher object using CBC mode.
    aes_cipher_text = aes_cipher.encrypt(pad(message_bytes, AES.block_size))  # Encrypts the cipher object
    aes_encrypt_time = time.time() - start_time  # Measure time taken for AES encryption
    aes_init_vec = aes_cipher.iv  # Saves the cipher's Initialization Vector

    print("AES Encrypted:", aes_cipher_text.hex())

  # AES Decipher Function
    aes_decipher = AES.new(aes_key, AES.MODE_CBC, iv=aes_init_vec)
    start_time = time.time()  # Start timer for decryption
    aes_plain_text = unpad(aes_decipher.decrypt(aes_cipher_text), AES.block_size)
    aes_decrypt_time = time.time() - start_time  # Measure time taken for decryption

    print("AES Decrypted:", aes_plain_text.decode('utf-8'))

    # Measure the RAM used by the process
    process = psutil.Process()
    memory_usage = process.memory_info().rss / (1024 * 1024)  # Convert to MB
    print(f"RAM Used: {memory_usage:.2f} MB")
    print(f"AES Encryption Time: {aes_encrypt_time:.6f} seconds")
    print(f"AES Decryption Time: {aes_decrypt_time:.6f} seconds")
