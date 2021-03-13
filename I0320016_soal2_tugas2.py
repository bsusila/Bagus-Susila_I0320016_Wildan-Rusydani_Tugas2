#Identitas Mahasiswa
Nama_lengkap = "Bagus Susila"
Nama_panggilan = "Bagus"
Pekerjaan = "Mahasiswa"
Jurusan = "Teknik Industri"
Universitas = "Universitas Sebelas Maret"
Angkatan = "2020"
NIM = "I0320016"
Tempat_lahir = "Surakarta"
Tanggal_lahir = "5 Agustus 2002"
Alamat = "Jalan Kalimas Mertodranan, Pasarkliwon, Surakarta"
SMA = "SMAN 3 Surakarta"
Hobi = "Olahraga"
Tinggi_badan = 168
Berat_badan = 53
Ukuran_sepatu = 42
Minuman_favorit = "Es Teh"
Makanan_favorit = "Nasi Goreng"
Warna_favorit = "Hitam"
Motto_hidup = "Tetaplah Merasa Bodoh"

#Penghitungan Usia
Tglskrg = 12
Blnskrg = 3
Thnskrg = 2021
Tgllhr = 5
Blnlhr = 8
Thnlhr = 2002
Usia_Hari = (Thnskrg*365 + Blnskrg*30 + Tglskrg) - (Thnlhr*365 + Blnlhr*30 + Tglskrg)
Usia_T = int(Usia_Hari/365)
Usia_B = int((Usia_Hari % 365)/30)
Usia_H = int((Usia_Hari % 365) % 30)

#Hasil
print("Hai nama saya", Nama_lengkap, "biasa dipanggil", Nama_panggilan)
print("Saya sekarang merupakan", Pekerjaan, "pada jurusan", Jurusan, "di", Universitas, "dengan", NIM)
print("Saya lahir di", Tempat_lahir, "pada tanggal", Tanggal_lahir)
print("Usia saya yaitu", Usia_T, "tahun", Usia_B, "bulan", Usia_H, "hari")
print("Alamat rumah saya di", Alamat)
print("Sebelum masuk di Teknik Industri saya merupakan siswa", SMA)
print("Hobi saya yaitu", Hobi)
print("Tinggi badan saya adalah", Tinggi_badan, "cm")
print("Berat badan saya adalah", Berat_badan, "kg")
print("Ukuran sepatu saya adalah", Ukuran_sepatu)
print("Makanan favorit saya adalah", Makanan_favorit, "dan minuman favorit saya adalah", Minuman_favorit)
print("Warna favorit saya adalah", Warna_favorit)
print("Motto hidup saya yaitu", Motto_hidup)
