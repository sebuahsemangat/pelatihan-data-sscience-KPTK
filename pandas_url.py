



import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population_density' #ini alamat webnya
data = pd.read_html(url) # perintah untuk membaca alamat web
data_table = data[0] # pilih tabel pertama karena di web ada dua tabel
# data_table.to_csv('data_kepadatan_penduduk.csv') # convert jadi csv
# data_table.to_json('test_json.json')
# print(data_table)
data_table.to_excel('test_exel.xlsx')