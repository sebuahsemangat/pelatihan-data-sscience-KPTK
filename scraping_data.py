import pandas as pd
import requests
from bs4 import BeautifulSoup

# URL target
url = 'https://www.w3schools.com/html/html_tables.asp'

# Kirim request
response = requests.get(url)

# Cek status
if response.status_code != 200:
    print(f"Gagal mengakses halaman: {response.status_code}")
    exit()

# Parsing HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Cari semua tabel
h3 = soup.find_all('h3')


for tag in h3:
    print(tag.get_text(strip=True))