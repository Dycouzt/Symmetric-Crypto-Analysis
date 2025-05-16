"""
This is the DES encryption algorithm module. Includes its function, where the goal is to create a cipher object,
encrypt it and decrypt it, measuring the algorithm's speed and RAM usage.
"""

import time
import psutil
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

base_key = get_random_bytes(32) # generates the shared key

def des_encryption(message_bytes):

    des_key = base_key[:8]  # DES uses a 56-bit key (8 bytes).
    start_time = time.time()  # Start timer for DES encryption
    des_cipher = DES.new(des_key, DES.MODE_CBC)  # Creates DES cipher object using CBC mode.
    des_cipher_text = des_cipher.encrypt(pad(message_bytes, DES.block_size))  # Encrypts the cipher object
    des_encrypt_time = time.time() - start_time  # Measure time taken for DES encryption
    des_init_vec = des_cipher.iv  # Saves the cipher's Initialization Vector

    print("DES Encrypted:", des_cipher_text.hex())

  # AES Decipher Function
    aes_decipher = DES.new(des_key, DES.MODE_CBC, iv=des_init_vec)
    start_time = time.time()  # Start timer for decryption
    des_plain_text = unpad(aes_decipher.decrypt(des_cipher_text), DES.block_size)
    des_decrypt_time = time.time() - start_time  # Measure time taken for decryption

    print("DES Decrypted:", des_plain_text.decode('utf-8'))

    # Measure the RAM used by the process
    process = psutil.Process()
    memory_usage = process.memory_info().rss / (1024 * 1024)  # Convert to MB
    print(f"RAM Used: {memory_usage:.2f} MB")
    print(f"DES Encryption Time: {des_encrypt_time:.6f} seconds")
    print(f"DES Decryption Time: {des_decrypt_time:.6f} seconds")
