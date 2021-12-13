print("Program Mencari bilangan prima dan total bilangan prima")
print("Silahkan masukan nilai awal dan akhir bilangan prima yang mau di cari")
# Logika mencari prima/ Rumus mencari bilangan prima
def rumus_mencari_prima (x):
  for i in range(2, x):
    if x % i == 0:
      return False
  return True

# program mencari bilangan prima 
def prima (awal, akhir):
  list_bilangan_prima = []
  for x in range(awal, akhir + 1):
    if rumus_mencari_prima(x):
      list_bilangan_prima.append(x)
  return list_bilangan_prima

# Memasukan nilai parameter dari  program nya
awal = int(input("Masukan angka pertama :"))
akhir = int(input("Masukan angka terakhir :"))

# Hasil akhir
hasil = prima(awal,akhir)
jumlah_prima = len(hasil)
print(f'bilangan prima antara {awal} dan {akhir} adalah :', hasil)
print("Total bilangan prima adalah :", jumlah_prima)
print("Hai saya sedang mencoba git")
print("hallo")
