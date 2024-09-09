import os

# Define the credentials file
credentials_file = 'iadownload_credentials.txt'

# Function to get credentials
def get_credentials():
    if os.path.exists(credentials_file):
        with open(credentials_file, 'r') as file:
            book_id = file.read().strip()
            return book_id
    else:
        book_id = input("Enter the item ID of the book (e.g., kybalionstudyofh00init): ")
        with open(credentials_file, 'w') as file:
            file.write(book_id)
        return book_id

# Get user input for book ID
book_id = get_credentials()
output_directory = input("Enter the output directory (leave blank for current directory): ")

# Set output directory if provided
if output_directory:
    command = f"./iadownload.py --item={book_id} --outdir={output_directory}"
else:
    command = f"./iadownload.py --item={book_id}"

# Execute the command
os.system(command)
