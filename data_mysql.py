import mysql.connector

# Koneksi ke database public (remote)
remote_db = mysql.connector.connect(
    host="mysql-rfam-public.ebi.ac.uk",
    user="rfamro",
    password="",
    port = "4497",
    database="Rfam"
)

# Koneksi ke database lokal
local_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port ="3306",
    database="pelatihan_data_science"
)

remote_cursor = remote_db.cursor(dictionary=True)
local_cursor = local_db.cursor()

# Ambil data dari tabel remote
remote_cursor.execute("SELECT * FROM clan")
rows = remote_cursor.fetchall()

# Masukkan data ke database lokal
for row in rows:
    
    local_cursor.execute("""
        INSERT INTO clan (clan_acc, id, previous_id, description, author, comment) VALUES (%s, %s, %s, %s, %s, %s)
    """, (row['clan_acc'], row['id'], row['previous_id'], row['description'], row['author'], row['comment']))

local_db.commit()

# Tutup koneksi
remote_cursor.close()
local_cursor.close()
remote_db.close()
local_db.close()
