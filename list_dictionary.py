warna = ["merah", "hijau", "kuning"]
warna.append("biru")
print("Daftar warna:", warna)
print("Warna pertama:", warna[0])
print("Jumlah warna:", len(warna))

siswa = {"nama": "Rahma", "sekolah": "SMKN 2 Subang", "jumlah_apel": 9}
siswa["warna_favorit"] = "hijau"
print("Data siswa:", siswa)
print("Nama:", siswa["nama"])
for kunci, isi in siswa.items():
    print(kunci, "=", isi)
