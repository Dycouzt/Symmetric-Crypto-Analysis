from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

def calculate_diffusion_rate(message1, message2):
    key = get_random_bytes(16)
    iv = get_random_bytes(16)

    cipher1 = AES.new(key, AES.MODE_CBC, iv)
    cipher2 = AES.new(key, AES.MODE_CBC, iv)

    ct1 = cipher1.encrypt(pad(message1.encode(), AES.block_size))
    ct2 = cipher2.encrypt(pad(message2.encode(), AES.block_size))

    # Compare byte-by-byte
    differences = 0
    total_bits = len(ct1) * 8  # 8 bits per byte

    for b1, b2 in zip(ct1, ct2):
        # XOR the bytes and count how many bits differ
        xor = b1 ^ b2
        differences += bin(xor).count("1")

    diffusion_percent = (differences / total_bits) * 100
    print(f"Diffusion Rate: {diffusion_percent:.2f}% ({differences} bits differ out of {total_bits})")
    print(f"Original Ciphertext: {ct1.hex()}")
    print(f"Modified Ciphertext: {ct2.hex()}")

calculate_diffusion_rate("Hello", "Jello")

