# 📌 Code 1: Simple Timer Utility
# Timer Utility - Basic Time Management Tool
# This code is free to use, modify, and distribute.

import time

def countdown(seconds):
    while seconds:
        print(f"Time left: {seconds} seconds")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

count = int(input("Enter countdown time in seconds: "))
countdown(count)

# 📌 Code 2: Secure Password Generator
# Secure Password Generator - High-Security Tool
# Any modifications must also remain open-source.

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

print("Secure Password Generator")
length = int(input("Enter password length: "))
print("Generated Password:", generate_password(length))

# 📌 Code 3: Data Converter - JSON to CSV
# Data Converter - JSON to CSV
# Suitable for both commercial and non-commercial use with attribution.

import json
import csv

def json_to_csv(json_file, csv_file):
    with open(json_file) as json_data:
        data = json.load(json_data)

    with open(csv_file, 'w', newline='') as csv_data:
        writer = csv.writer(csv_data)
        writer.writerow(data[0].keys())
        for entry in data:
            writer.writerow(entry.values())

print("JSON to CSV Converter")
json_file = input("Enter JSON file name: ")
csv_file = input("Enter CSV file name: ")
json_to_csv(json_file, csv_file)

