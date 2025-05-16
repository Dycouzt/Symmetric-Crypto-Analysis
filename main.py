"""
The objective of this script is to implement encryption for a message using block cipher (AES and DES).
- Generating the same key for both methods.
- Carry out a code analysis to come up with the weaknesses and strengths.
- Measure each algorithm's encryption speed.
- Measure each algorithm's RAM memory usage.
"""

from aes_algth import aes_encryption
from des_algth import des_encryption
from aes_diffusion import calculate_diffusion_rate
from des_diffusion import calculate_des_diffusion_rate


message = input("Enter your message: ")

# Function to convert message to bytes. Encryption algorithms only work with bytes.
def message_bytes():
    byte_input = message.encode('utf-8')
    return byte_input

aes_encryption(message_bytes())
des_encryption(message_bytes())

choice = str(input("Press 'y' to continue to the diffusion analysis: "))

if choice == "y":
    calculate_diffusion_rate("Hello", "Jello")
    calculate_des_diffusion_rate("Hello", "Jello")
else:
    print("Wrong input. Try again! ")

