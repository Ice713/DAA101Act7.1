# 📌 Code 1: Basic Text File Writer
# Text File Writer - Simple Utility Tool
# This code is free to use, modify, and distribute.

def write_to_file(filename, text):
    with open(filename, 'w') as file:
        file.write(text)

print("Text File Writer")
filename = input("Enter filename: ")
text = input("Enter text to write: ")
write_to_file(filename, text)


# 📌 Code 2: Encrypted Message Sender
# Encrypted Message Sender - Secure Communication Tool
# Users can modify and share this code, but must keep it open-source under the same terms.

from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_message(message):
    return cipher.encrypt(message.encode())

print("Secure Message Sender")
message = input("Enter message to encrypt: ")
print("Encrypted:", encrypt_message(message))

# 📌 Code 3: Web Data Scraper
# Web Data Scraper - Flexible Usage Tool
# Can be used in commercial and non-commercial projects with some conditions.

import requests
from bs4 import BeautifulSoup

def scrape_title(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.title.string if soup.title else "No Title"

print("Web Data Scraper")
url = input("Enter website URL: ")
print("Title:", scrape_title(url))

