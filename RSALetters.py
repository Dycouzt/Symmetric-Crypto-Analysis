# Python Program for implementation of RSA Algorithm for letter version
# Using Unicode convertion ord() we change string to int values for encryption.
import hashlib


def power(base, expo, m):
    res = 1
    base = base % m
    while expo > 0:
        if expo & 1:
            res = (res * base) % m
        base = (base * base) % m
        expo = expo // 2
    return res


def modInverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d
    return -1


def generateKeys():
    p = 61 # p = 5
    q = 53 # q = 11
    # using smaller primes doesn;t allow larger number greater than 55 to be encrypted

    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e, where 1 < e < phi(n) and gcd(e, phi(n)) == 1
    for e in range(2, phi):
        if gcd(e, phi) == 1:
            break

    # Compute d such that e * d ≡ 1 (mod phi(n))
    d = modInverse(e, phi)

    return e, d, n


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def encrypt_string(msg, e, n):
    return [power(ord(char), e, n) for char in msg]


def decrypt_string(ciphertext, d, n):
    return ''.join([chr(power(char_code, d, n)) for char_code in ciphertext])


if __name__ == "__main__":
    e, d, n = generateKeys()

    print(f"Public Key (e, n): ({e}, {n})")
    print(f"Private Key (d, n): ({d}, {n})")

    msg = input("msg: ")
    print(f"Original Message: {msg}")

    encrypted = encrypt_string(msg, e, n)
    print(f"Encrypted Message: {encrypted}")

    decrypted = decrypt_string(encrypted, d, n)
    print(f"Decrypted Message: {decrypted}")
