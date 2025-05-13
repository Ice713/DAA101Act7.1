# 📌 Code 1: Prime Number Checker
# Prime Number Checker - Educational Tool
# This code is free to use, modify, and distribute.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
print("Prime" if is_prime(num) else "Not Prime")

# 📌 Code 2: Encrypted Note Storage
# Encrypted Note Storage - Secure Note Taking Tool
# Must be kept open-source under the same terms as the original code.

from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

def save_note():
    note = input("Enter your note: ")
    encrypted_note = cipher.encrypt(note.encode())
    with open("encrypted_note.txt", "wb") as file:
        file.write(encrypted_note)

save_note()

# 📌 Code 3: REST API Requester
# REST API Requester - Flexible Network Tool
# Can be used in both open-source and commercial projects with some conditions.

import requests

def fetch_data(api_url):
    response = requests.get(api_url)
    return response.text

print("REST API Requester")
url = input("Enter API URL: ")
print(fetch_data(url))
