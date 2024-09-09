import os
import subprocess

# Define the credentials file
credentials_file = 'archive_credentials.txt'

# Function to get credentials
def get_credentials():
    if os.path.exists(credentials_file):
        with open(credentials_file, 'r') as file:
            email, password = file.read().strip().split(',')
            return email, password
    else:
        email = input("Enter your Archive.org email: ")
        password = input("Enter your Archive.org password: ")
        with open(credentials_file, 'w') as file:
            file.write(f"{email},{password}")
        return email, password

# Get user credentials
email, password = get_credentials()

# Prompt for book URL
book_url = input("Paste the URL of the book you want to download: ")

# Construct the command
command = f"python3 archive-org-downloader.py -e {email} -p {password} -u {book_url}"

# Execute the command
os.system(command)
