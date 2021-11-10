def menu():
    print("==========MENU==========")
    print("[1] Login Admin")
    print("[2] Discount Chance")
    print("[3] Keluar")

while True:
    menu()
    pilih = int(input("pilih menu: "))

    def admin():
        print ("----------- MENU ----------")
        print ("[1] Show Data")
        print ("[2] Insert Data")
        print ("[3] Edit Data")
        print ("[4] Delete Data")
        print ("[5] Exit")

    def garis1():
        print("=" * 30)
    
    def garis2():
        print("=" * 40)

    if pilih == 1 :
        garis1()
        username= input("Username: ")
        password= input("Password: ")
        garis1()
        if username == "Dinda" or username == "dinda" and password == "061":
            print("Anda berhasil login")
            print("Selamat Datang di Menu Admin!")
            garis1()
            admin()

        else:
            print("Username atau password yang anda masukan salah!")
            garis1()
            menu()
            break

    elif pilih == 2 :
        garis2()
        kode = input("Masukan Kode yang Anda Miliki!: ")
        garis2()
        if kode == "Happyuse":
            print("Kode yang Anda Masukan benar!")
            print("Selamat Anda Telah Mendapat Diskon Sebesar 30%")
            garis2()
            menu()
            break
        else:
            print("Kode yang Anda Masukan Salah!")
            garis2()
            menu()
            break

    elif pilih == 3 :
        garis1()
        print("Terimakasih telah berkunjung!")
        garis1()
        menu()
        break

    else :
        garis2()
        print("Pilihan yang Anda Masukan Tidak Tersedia")
        print("Periksa Ulang Pilihan Anda!")
        print("dan Silahkan Coba Lagi")
        print("(Menu yang tersedia hanya menu 1,2,3. menu", pilih, "Tidak Tersedia)")
        garis2()
        break

    def admin():
        print ("----------- MENU ----------")
        print ("[1] Show Data")
        print ("[2] Insert Data")
        print ("[3] Edit Data")
        print ("[4] Delete Data")
        print ("[5] Exit")

    while True:
        admin()
        pilih1 = int(input("pilih menu="))

        if pilih1 == 1 :
            dict = {"Inilah Menu yang Kami Mliki": "!",
                    "Bunga Mawar Merah/Putih": 10000,
                    "Bunga Mawar Pelangi"    : 20000,
                    "Bunga Matahari"         : 16000,
                    "Bunga Kapas"            : 18000}
            garis2()
            for i,j in dict.items():
                print("{} = {}".format(i, j))
            garis2()
    
        elif pilih1 == 2 :
            dict = {"Inilah Menu yang Kami Miliki": "!",
                    "Bunga Mawar Merah/Putih": 10000,
                    "Bunga Mawar Pelangi"    : 20000,
                    "Bunga Matahari"         : 16000,
                    "Bunga Kapas"            : 18000}
            garis2()
            bunga_baru = input("Masukan Nama Bunga: ")
            harga_baru = input("Masukan harga: ")
            garis2()
            dict.update({bunga_baru            : harga_baru})
            for i,j in dict.items():
                print("{} = {}".format(i, j))
            garis2()

        elif pilih1 == 3 :
            dict = {"Inilah Menu yang Kami Miliki": "!",
                    "Bunga Mawar Merah/Putih": 10000,
                    "Bunga Mawar Pelangi"    : 20000,
                    "Bunga Matahari"         : 16000,
                    "Bunga Kapas"            : 18000}
            garis2()
            for i,j in dict.items():
                print("{} = {}".format(i, j))
            garis2()
            a = input("Bunga Mana? ")
            b = input("Jadi Bunga? ")
            dict[b] = dict.pop(a)
            garis2()
            for i,j in dict.items():
                print("{} = {}".format(i, j))
            garis2()

        elif pilih1 == 4 :
            dict = {"Inilah Menu yang Kami Miliki": "!",
                    "Bunga Mawar Merah/Putih": 10000,
                    "Bunga Mawar Pelangi"    : 20000,
                    "Bunga Matahari"         : 16000,
                    "Bunga Kapas"            : 18000}
            garis2()
            for i,j in dict.items():
                print("{} = {}".format(i, j))
            garis2()
            c = input("Bunga Mana yang Akan di Hapus? ")
            dict.pop(c)
            for i,j in dict.items():
                print("{} = {}".format(i, j))
            garis2()

        elif pilih1 == 5 :
            garis1()
            print("Keluar Program")
            print("Terimakasih Sudah Berkunjung")
            garis1()
            break

        else:
            garis2()
            print("Pilihan yang Anda Masukan Tidak Tersedia")
            print("Periksa Ulang Pilihan Anda!")
            print("dan Silahkan Coba Lagi")
            print("(Menu yang tersedia hanya menu 1,2,3. menu", pilih1, "Tidak Tersedia)")
            garis2()
