def main():
  # Daftar harga tiket
  harga_tiket = {
    "Cirebon - Semarang PP": 200000,
    "Semarang - Tegal PP": 150000,
    "Semarang - Pekalongan PP": 100000,
    "Pekalongan - Brebes PP": 50000,
    "Tegal - Brebes PP": 50000,
    "Cirebon - Kroya PP": 300000,
    "Kroya - Purwokerto PP": 100000,
    "Purwokerto - Yogyakarta PP": 150000,
    "Yogyakarta - Solo PP": 100000,
    "Solo - Semarang PP": 150000,
    "Semarang - Jakarta PP": 400000,
    "Bandung - Kroya PP": 350000,
    "Kroya - Yogyakarta PP": 200000,
    "Yogyakarta - Solo PP": 100000,
    "Solo - Madiun PP": 150000,
    "Madiun - Jember PP": 250000,
    "Jember - Surabaya PP": 200000
  }

  # Menampilkan daftar tujuan perjalanan
  print("Daftar tujuan perjalanan:")
  print("-" * 20)
  for tujuan in harga_tiket:
    print(f"{tujuan}: Rp {harga_tiket[tujuan]}")

  # Mendapatkan tujuan perjalanan
  tujuan = input("Masukkan tujuan perjalanan Anda: ")

  # Mengecek apakah tujuan tersedia
  if tujuan not in harga_tiket:
    print("Mohon maaf jurusan yang Anda pilih tidak tersedia")
    return

  # Mendapatkan nama dan jumlah penumpang
  nama = input("Masukkan nama Anda: ")
  jumlah_penumpang = int(input("Masukkan jumlah penumpang: "))

  # Meminta pengguna memasukkan angka sesuai jumlah penumpang jika jumlah penumpang lebih dari 1
  if jumlah_penumpang > 1:
    nama_penumpang = []
    for i in range(jumlah_penumpang):
      nama_penumpang.append(input(f"Masukkan nama penumpang ke-{i + 1}: "))

  # Menghitung harga total
  harga_total = harga_tiket[tujuan] * jumlah_penumpang

  # Menampilkan informasi pemesanan
  print("Informasi pemesanan:")
  print("-" * 20)
  print("Tujuan:", tujuan)
  print("Nama:", nama)
  print("Jumlah penumpang:", jumlah_penumpang)
  print("Harga total:", harga_total)

  # Konfirmasi pemesanan
  konfirmasi = input("Silakan konfirmasi pemesanan Anda (Y/T): ")

  # Menampilkan pesan konfirmasi
  if konfirmasi.lower() == "y":
    print("Terima kasih atas pemesanan Anda!")
    print("Detail pemesanan telah dikirim ke email Anda.")
  else:
    print("Pemesanan dibatalkan.")

if __name__ == "__main__":
  main()
