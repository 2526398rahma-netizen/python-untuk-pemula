class Siswa:
    def __init__(self, nama, sekolah, jumlah_apel):
        self.nama = nama
        self.sekolah = sekolah
        self.jumlah_apel = jumlah_apel

    def perkenalan(self):
        return "Nama saya " + self.nama + " dari " + self.sekolah

    def tambah_apel(self, jumlah):
        self.jumlah_apel += jumlah

siswa1 = Siswa("Rahma", "SMKN 2 Subang", 9)
print(siswa1.perkenalan())
print("Jumlah apel:", siswa1.jumlah_apel)
siswa1.tambah_apel(3)
print("Jumlah apel sekarang:", siswa1.jumlah_apel)
