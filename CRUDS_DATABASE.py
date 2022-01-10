import mysql.connector
import os
db = {
    'host' : 'localhost',
    'user' :'root',
    'password' : '',
    'database' : 'CRUDS1'
}

koneksi = mysql.connector.connect(**db)
# crs = koneksi.cursor()

# buat_table = """ Create table pelanggan(
#     kode int not null auto_increment,
#     nama varchar(100),
#     alamat varchar(100),
#     primary key(kode)
# ) engine = innodb
# """

# crs.execute(buat_table)
# print("Table berhasil di buat")


# Fungsi insert data
def insert_data(koneksi):
    crs = koneksi.cursor()
    
    # Bikin input
    nama = input("Masukan nama : ")
    alamat = input("Masukan alamat : ")
    isi_data =  (nama,alamat)

    # insert database nya
    data = "insert into pelanggan(nama, alamat) values( %s, %s)"
    crs.execute(data, isi_data)
    koneksi.commit() #nama "koneksi" tergantung dari nama variable untuk koneksi ke local host
    print("Berhasil memasukan data")

def show_data(koneksi):
    crs = koneksi.cursor()
    crs.execute("Select * from  pelanggan")
    for i in crs:
        print(i)


def update_data(koneksi):
    crs = koneksi.cursor()
    # Menampilkan isi database
    show_data(koneksi)
    
    # input nya
    nomor = int(input("Masukan id pelanggan : "))
    nama = input("Masukan nama baru : ")
    alamat = input("Masukan alamat baru : ")

    # Update
    update_data = "update pelanggan set nama =%s, alamat=%s where kode =%s "
    isi_data = (nama, alamat, nomor)
    crs.execute(update_data, isi_data)
    koneksi.commit() #nama "koneksi" tergantung dari nama variable untuk koneksi ke local host
    print("Data berhasil di update")

def delete_data(koneksi):
    crs = koneksi.cursor()
    
    # Tampilkan isi database
    show_data(koneksi)

    # Input
    kode = int(input("Masukan Kode Pelanggan : "))

    # Delete data
    delete_data = "delete from pelanggan where kode = %s"
    data = (kode, )
    crs.execute(delete_data, data)
    koneksi.commit()
    print("Data berhasil di hapus")

def cari_data(koneksi):
    crs = koneksi.cursor()
    kode = input("Masukan Kata kunci : ")

    isi_data = "Select * from pelanggan where nama like %s or alamat like %s"
    cari  = ("%{}%".format(kode), "%{}%".format(kode))
    crs.execute(isi_data, cari)
    hasil = crs.fetchall()

    if crs.rowcount < 0:
        print("Data tidak ada")
    else:
        for i in hasil:
            print(i)


# fungsi menu
def menu(koneksi):
    print("=============CRUDS Sederhana 1=================")
    print("1. insert data")
    print("2. Show data")
    print("3. Update data")
    print("4. Delete Data")
    print("5. Cari data")
    print("6. exit")
    menu = int(input("Pilih memu : "))

    # Clear screen, digunakan ketika selesai pilih menu terminal akan di bersihkan otomatis
    os.system("cls")

    if menu == 1:
        insert_data(koneksi)
    elif menu == 2:
        show_data(koneksi)
    elif menu == 3:
        update_data(koneksi)
    elif menu == 4:
        delete_data(koneksi)
    elif menu == 5: 
        cari_data(koneksi)
    elif menu == 6:
        exit()
    else:
        print("Tidak ada Pilihan menu")


while True:
    menu(koneksi)
