while (True) :
    Nama = str(input("Masukkan nama: "))
    NIM = int(input("Masukkan NIM:(Harus sesuai)"))
    if (NIM == 116) :
        
        while(True):
            print("")
            print("Pilihan:")
            print("1. Menghitung harga")
            print("2. Keluar")
            print("")
            Pilihan = int(input("Masukkan pilihan: "))
            if (Pilihan == 1) :
                Harga = int(input("Masukkan harga barang: "))
                Jumlah = int(input("Masukkan jumlah barang: "))
                Total = Harga * Jumlah
                Pengali = 0.25
                if (Total > 250000):
                    Harga_diskon = Total * Pengali
                    Harga_setelah_diskon = Total - Harga_diskon
                    print("")
                    print("Hore anda telah mendapatkan diskon!")
                    print("Total harga sebelumnya: Rp.", Total)
                    print("Total harga setelah di diskon: Rp.", Harga_setelah_diskon)
                    print("")
                    print("Ketik 1 jika ingin mengulang atau 2 untuk keluar")
                    print("")
                else :
                    print("")
                    print("Maaf anda tidak bisa mendapatkan diskon karena total harga kurang dari ketentuan.")
                    print("Total harga: Rp.", Total,)
                    print("")
                    print("Ketik 1 jika ingin mengulang atau 2 untuk keluar")
                    print("")
            elif (Pilihan == 2) :
                print("Program Selesai.")
                break   
            else :
                print("")
                print("Pilihan tidak tersedia, coba dengan mengetik 1 atau 2")
                print("")
    else:
        print("Maaf anda tidak bisa masuk")
        break