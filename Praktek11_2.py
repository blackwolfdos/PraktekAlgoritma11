class mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai
        
    def getNama(self):
        return self.nama
    
    def setNama(self):
        self.nama = input("Nama: ")
        
    def getNilai(self):
        return self.nilai
    
    def setNilai(self):
        self.nilai = input("Nilai: ")
        
    def hapus(self):
        self.nama = None
        self.nilai = None
        
mhs = mahasiswa(None, None)

def Deklarasi():
    mhs.setNama()
    mhs.setNilai()
    
def Menampilakn():
    print(mhs.getNama())
    print(mhs.getNilai())

def Mengubah():
    while True:
        ubah = input('Apa yang ingin di ubah ? (Nama/Nilai)')
        
        if ubah == "Nama":
            mhs.setNama()
            print("Nama berhasil di ubah")
            break
        elif ubah == "Nilai":
            mhs.setNilai()
            print("Nilai berhasil di ubah")
            break
        else:
            print("Masukkan pilihan dengan benar")
            
def Hapus():
    mhs.hapus()
    print("Data berhasil di hapus")

while True:
    print("\n")
    print("=========Program OOP=========")
    print("1. Deklarasi Data")
    print("2. Menampilkan Data")
    print("3. Mengubah Data")
    print("4. Menghapus Data")
    print("5+. Keluar Aplikasi")

    pilih = int(input("Masukkan pilihan (1/2/3/4/5): "))
    
    if pilih == 1:
        Deklarasi()
    elif pilih == 2:
        Menampilakn()
    elif pilih == 3:
        Mengubah()
    elif pilih == 4:
        Hapus()
    else:
        break