from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

def calculate_des_diffusion_rate(message1, message2):
    key = get_random_bytes(8)  # DES key is 56 bits (8 bytes)
    iv = get_random_bytes(8)   # DES block size is 64 bits (8 bytes)

    cipher1 = DES.new(key, DES.MODE_CBC, iv)
    cipher2 = DES.new(key, DES.MODE_CBC, iv)

    ct1 = cipher1.encrypt(pad(message1.encode(), DES.block_size))
    ct2 = cipher2.encrypt(pad(message2.encode(), DES.block_size))

    # Compare bit-by-bit
    differences = 0
    total_bits = len(ct1) * 8  # Each byte is 8 bits

    for b1, b2 in zip(ct1, ct2):
        xor = b1 ^ b2
        differences += bin(xor).count("1")

    diffusion_percent = (differences / total_bits) * 100

    print("=== DES Diffusion Analysis ===")
    print(f"Original Message: {message1}")
    print(f"Modified Message: {message2}")
    print(f"Ciphertext 1: {ct1.hex()}")
    print(f"Ciphertext 2: {ct2.hex()}")
    print(f"Diffusion Rate: {diffusion_percent:.2f}% ({differences} bits changed out of {total_bits})")

calculate_des_diffusion_rate("Hello", "Jello")