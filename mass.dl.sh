#!/bin/bash

read -p "Enter the book URL: " book_url

python3 archive-org-downloader.py -e youremail@mail.com -p "your.pass" --file books_to_download.txt
