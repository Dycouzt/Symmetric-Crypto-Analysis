# AES & DES Encryption Performance Comparison in Python

This project implements two classical block cipher algorithms—AES and DES—to encrypt and decrypt messages using a shared key. It compares their performance based on encryption speed, memory usage, and diffusion rate, offering a hands-on perspective on symmetric encryption and cryptographic evaluation.

---

## Goal

The goal of this project is to gain practical experience with symmetric key encryption and to understand the performance and security differences between the AES and DES algorithms. It provides foundational insight into cryptography and secure communication.

---

## Features

- Encrypts and decrypts plaintext using AES and DES in CBC mode
- Uses a common key for both algorithms
- Measures:
- Encryption and decryption speed
- Memory (RAM) usage
- Diffusion rate (bit changes from minor message differences)
- Outputs ciphered and deciphered messages in readable format
- Performs a basic security comparison between the two algorithms

---

## Requirements

This project uses the following Python libraries:
- pycryptodome (for AES and DES implementations)
- psutil (to measure RAM usage)
- time (for speed benchmarking)

Install the required libraries with:

```bash
pip install pycryptodome psutil
```

---

## Project Structure

```plaintext
  Cryptography/
├── main.py
├── aes_algth.py
├── des_algth.py
├── aes_diffusion.py
├── des_diffusion.py
└── README.md 
```      

---

## How It Works

1. User Input:
    - The user is prompted to enter a message for encryption.
2. Encryption:
    - The same random key is used for both AES and DES.
    - Each algorithm:
    - Encrypts the message
    - Decrypts it to verify correctness
    - Measures and prints the time taken and memory used
3. Diffusion Analysis:
    - Uses two similar inputs (e.g., “Hello” and “Jello”)
    - Encrypts both and compares how many bits differ in the ciphertext
    - Calculates and prints the diffusion rate as a percentage

---

## Code Highlights

- Crypto.Cipher.AES.new(key, AES.MODE_CBC): Creates AES cipher in CBC mode.
- Crypto.Cipher.DES.new(key, DES.MODE_CBC): Creates DES cipher in CBC mode.
- pad() and unpad(): Ensures messages fit block size requirements.
- time.time(): Used to benchmark encryption and decryption times.
- psutil.Process().memory_info().rss: Measures memory used by the process in MB.
- XOR bitwise comparison used for diffusion rate analysis.

---

## Sample Output

```plaintext
Enter your message: hello world

AES Encrypted: 6b5f6f7d9342...
AES Decrypted: hello world
RAM Used: 17.32 MB
AES Encryption Time: 0.000172 seconds
AES Decryption Time: 0.000103 seconds

DES Encrypted: 82afc56e3a9f...
DES Decrypted: hello world
RAM Used: 17.35 MB
DES Encryption Time: 0.000288 seconds
DES Decryption Time: 0.000214 seconds

Press 'y' to continue to the diffusion analysis: y

=== AES Diffusion ===
Diffusion Rate: 46.88% (60 bits differ out of 128)
Original Ciphertext: 2be0e7d5...
Modified Ciphertext: af59c3bd...

=== DES Diffusion ===
Diffusion Rate: 39.06% (50 bits changed out of 128)
Ciphertext 1: 5a3cd2...
Ciphertext 2: 712bc7...
```  

---

## To run the script:

```bash
python3 main.py
```

Then follow the prompts to enter:
- A plaintext message to encrypt
- Whether you want to run the diffusion rate analysis

---

## Conclusion

This project demonstrates how AES and DES work in practice, providing a simple but powerful environment to compare their efficiency and behavior. It highlights why modern cryptography has largely replaced DES with AES and offers a starting point for further exploration into cryptographic engineering, penetration testing, and secure application design.

---

## Author

Diego Acosta – Dycouzt