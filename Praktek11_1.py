class mahasiswa:
    mhsCount = 0
    
    def __init__(self, nama, nim, angkatan):
        self.nama = nama
        self.nim = nim
        self.angkatan = angkatan
        
        mahasiswa.mhsCount += 1
        
    def printNama(self):
        print("Nama: ", self.nama)
        print("NIM: ", self.nim)
        print("Angkatan: ", self.angkatan)
        print("\n")
        print("Total Mahasiswa: ", mahasiswa.mhsCount)
        
    def getterNama(self):
        return self.nama
            

nama = input("Nama Anda: ")
nim = int(input("Nim Anda: "))
angkatan = int(input("Angkatan Anda: "))     
print("\n")       

mhs1 = mahasiswa(nama, nim, angkatan)
mhs1.printNama()