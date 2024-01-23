import random
print("^-^-" *30)
print("                                             PT.SINAR ABADI                      ")
print("\n")
print("                     Selamat Datang di Aplikasi Pemesanan Tiket Kereta Api PT. SINAR ABADI       ")
print("^-^-" *30)

print("\n")
list_menu = ["Pemesanan Tiket" , "Pengajuan Refund Tiket" , "Customer Service"]
print("1" , list_menu[0])
print("2" , list_menu[1])
print("3" , list_menu[2])

while(True):
    
    #jika mmeimilih opsi 1 (memesan) maka lengkapi data diri
    menu =  input("Masukan Pilihan Anda   :     ")
    if menu == "1":
        print("\n")
        print("="*50)
        print("              Formulir Data Diri               ")
        print("="*50)
        print("\n")
        nama   = input("Masukan Nama Lengkap  :     ")
        no_ktp = input("Masukan Nomor KTP     :     ")
        alamat = input("Masukan Alamat Anda   :     ")
        
        print("\n")

        #Masukan  kereta pilihan
        print("="*50)
        print("              DAFTAR KERETA               ")
        print("="*50)
        list_kereta = ["Kereta Tawang Jaya", "Kaligung"]
        print("1" , list_kereta[0])
        print("2" , list_kereta[1])
        print("="*36)
        kereta = input("Pilih Kereta Anda : ")
        print("\n")

#Jika Memilih Kereta Opsi 1
        if kereta == "1":
            kereta = "KA Tawang Jaya"
            print("-"*50)
            print("     SELAMAT DATANG DI KERETA TAWANG JAYA        ")
            print("-"*50)
        #daftar waktu keberangkatan 
            print("         Daftar waktu Keberangkatan          ")
            print("\n")
            tanggal = input("Masukan Tanggal (hh/bb/tt): ")
            print("\n")
            print("jam keberangkatan")
            list_jam = ["06.00" , "12.00" , "18.00"]
            print("1" , list_jam[0])
            print("2" , list_jam[1])
            print("3" , list_jam[2])
            print("=" * 36)
            jam = input("Masukan Jam Keberangkatan Anda :   ")
            print("\n")
            if jam == "1":
                jam = "06.00"
            if jam == "2":
                jam = "12.00"
            if jam == "3":
                jam = "18.00"


        #daftar kota tujuan
            print("="*50)
            print("              DAFTAR TUJUAN               ")
            print("="*50)
            print("\n")
            list_tujuan  = ["Stasiun Gambir" , "Stasiun Semarang Poncol"]
            print("1" , list_tujuan[0])
            print("2" , list_tujuan[1]) 
            print("="*36)
            tujuan = input("Masukan  Tujuan Anda :   ")

        #jika memilih tujuan 1
            if tujuan == "1":
                tujuan = "Stasiun Gambir"
                print()
                print("="*50)
                print("              DAFTAR KELAS               ")
                print("="*50)
        #pilih kelas
                print("")
                print("Kelas: ")
                Kelas=["Bisnis" , "Ekonomi"]
                for x in range (2):
                    print(x+1, Kelas[x])
                
        #jika memilih kelas bisnis 
                print("="*36)
                kelas   = input("Pilihlah Kelas Anda : ")
                if kelas=="1":
                    kelas = "bisnis"

                    print("\n")
                    pesan=input("Jumlah tiket yang dipesan (max 3 tiket):")
                    if pesan=="1":
                        D = 1*120000
                        print("Total harga tiket anda sebesar Rp.", D)
                        pesan = "1 tiket"
                    elif pesan=="2":
                        D = 2*120000
                        print("Total harga tiket anda sebesar Rp.", D)
                        pesan = "2 tiket"
                    elif pesan=="3":
                        D = 3*120000
                        print("Total harga tiket anda sebesar Rp.", D)
                        pesan = "3 tiket"
                    else: 
                        print("Maksimal pemesanan adalah 3 tiket!")
                    jml_uang = int(input("Masukan Jumlah Uang : "))
                    print('='*36)
                              
                
        #jika memilih kelas ekonomi
                elif kelas=="2":
                    kelas="ekonomi"

                    print("\n")
                    pesan=input("Jumlah tiket yang dipesan (max 3 tiket):")
                    
                    if pesan=="1":
                        D = 1*70000
                        print("Total harga tiket anda sebesar Rp.", D)
                        pesan = "1 tiket"
                    elif pesan=="2":
                        D = 2*70000
                        print("Total harga tiket anda sebesar Rp.", D)
                        pesan = "2 tiket"
                    elif pesan=="3":
                        D = 3*70000
                        print("Total harga tiket anda sebesar Rp.", D)
                        pesan = "3 tiket"
                    else:
                        print("Maksimal pemesanan adalah 3 tiket!")
                        break
                    jml_uang = int(input("Masukan Jumlah Uang : "))
                    print('='*36)
                else:
                    print("Kelas tidak valid, mohon input kelas 1/2!")

        #Jika memilih tujuan 2
            if tujuan == "2":
                tujuan = "Kaligung"
        #pilih kelas
                print("\n")
                print("="*50)
                print("              DAFTAR KELAS               ")
                print("="*50)
                print("")
                print("Kelas: ")
                Kelas=["Bisnis" , "Ekonomi"]
                for x in range (2):
                    print(x+1, Kelas[x])
                
        #jika memilih kelas bisnis 
                print('='*36)
                kelas   = input("Pilihlah Kelas Anda : ")
                if kelas=="1":
                    kelas = "Bisnis"
                    pesan=input("Jumlah tiket yang dipesan (max 3 tiket):")

                    print('='*36)
                    if pesan=="1":
                        D = 1*125000
                        print("Total harga tiket anda sebesar Rp.", D)
                        pesan = "1 tiket"
                    elif pesan=="2":
                        D = 2*125000
                        print("Total harga tiket anda sebesar Rp.", D)
                        pesan = "2 tiket"
                    elif pesan=="3":
                        D = 3*125000
                        print("Total harga tiket anda sebesar Rp.", D )
                        pesan = "3 tiket"
                    
                    else: 
                        print("Maksimal pemesanan adalah 3 tiket!")
                        break      
                    jml_uang = int(input("Masukan Jumlah Uang : "))
                    print('='*36)
        #jika memilih kelas ekonomi
                elif kelas=="2":
                    kelas = "ekonomi"
                    pesan=input("Jumlah tiket yang dipesan (max 3 tiket):")
                   
                    if pesan=="1":
                        D = 1*75000
                        print("Total harga tiket anda sebesar Rp.", D)
                        pesan = "1 tiket"
                    elif pesan=="2":
                        D = 2*75000
                        print("Total harga tiket anda sebesar Rp.", D)
                        pesan = "2 tiket"
                    elif pesan=="3":
                        
                        D = 3*75000
                        print("Total harga tiket anda sebesar Rp.", D)
                        pesan = "2 tiket"
                       
                    else:
                        print("Maksimal pemesanan adalah 3 tiket!")
                        break
                    jml_uang = int(input("Masukan Jumlah Uang : "))
                    print('='*36)
                else:
                    print("Kelas tidak valid, mohon input kelas 1/2!")


            print("\n")








#jika memilih kereta 2
        if kereta == "2":
            kereta = "KA Kaligung"
            print("-"*50)
            print("     SELAMAT DATANG DI KERETA KALIGUNG        ")
            print("-"*50)

        #daftar waktu keberangkatan 
            print("         Daftar waktu Keberangkatan          ")
            print("\n")
            tanggal = input("Masukan Tanggal (hh/bb/tt):        ")
            print("\n")
            print("jam keberangkatan")
            list_jam = ["08.00" , "15.00" , "21.00"]
            print("1" , list_jam[0])
            print("2" , list_jam[1])
            print("3" , list_jam[2])
            print("=" * 36)
            jam = input("Masukan Jam Keberangkatan Anda :       ")
            print("\n")

        #daftar kota tujuan
            print("         Daftar Tujuan Keberangkatan         ")
            print("\n")
            list_tujuan  = ["Stasiun Jatibarang" , "Stasiun Tegal Sari"]
            print("1" , list_tujuan[0])
            print("2" , list_tujuan[1]) 
            print("="*36)
            tujuan = input("Masukan  Tujuan Anda :   ")

        #jika memilih tujuan 1
            if tujuan == "1":
                tujuan = "Stasiun Jatibarang"
            
        #pilih kelas
                print("")
                print("Kelas: ")
                Kelas=["Bisnis" , "Ekonomi"]
                for x in range (2):
                    print(x+1, Kelas[x])
                
        #jika memilih kelas bisnis 
                kelas   = input("Pilihlah Kelas Anda : ")
                if kelas=="1":
                    kelas = "bisnis"

                    print("\n")
                    pesan=input("Jumlah tiket yang dipesan (max 3 tiket):")
                    if pesan=="1":
                        D = 1*125000
                        print("Total harga tiket anda sebesar Rp.", D)
                    elif pesan=="2":
                        D = 2*125000
                        print("Total harga tiket anda sebesar Rp.", D)
                    elif pesan=="3":
                        D = 3*125000
                        print("Total harga tiket anda sebesar Rp.", D)
                    else: 
                        print("Maksimal pemesanan adalah 3 tiket!")
                        break 
                    jml_uang = int(input("Masukan Jumlah Uang : "))
                    print('='*36)     
                
        #jika memilih kelas ekonomi
                elif kelas=="2":
                    kelas="ekonomi"

                    print("\n")
                    pesan=input("Jumlah tiket yang dipesan (max 3 tiket):")
                    
                    if pesan=="1":
                        D = 1*75000
                        print("Total harga tiket anda sebesar Rp.", D)
                    elif pesan=="2":
                        D = 2*75000
                        print("Total harga tiket anda sebesar Rp.", D)
                    elif pesan=="3":
                        D = 3*75000
                        print("Total harga tiket anda sebesar Rp.", D)
                    else:
                        print("Maksimal pemesanan adalah 3 tiket!")
                        break
                    jml_uang = int(input("Masukan Jumlah Uang : "))
                    print('='*36)
                else:
                    print("Kelas tidak valid, mohon input kelas 1/2!")

        #Jika memilih tujuan 2
            if tujuan == "2":
                tujuan = "Tegal Sari"
        #pilih kelas
                print("")
                print("Kelas: ")
                Kelas=["Bisnis" , "Ekonomi"]
                for x in range (2):
                    print(x+1, Kelas[x])
                
        #jika memilih kelas bisnis 
                print('='*36)
                kelas   = input("Pilihlah Kelas Anda : ")
                if kelas=="1":
                    kelas = "Bisnis"
                    pesan=input("Jumlah tiket yang dipesan (max 3 tiket):")


                    if pesan=="1":
                        D = 1*125000
                        print("Total harga tiket anda sebesar Rp.", D)
                        pesan = "1 tiket"
                    elif pesan=="2":
                        D = 2*125000
                        print("Total harga tiket anda sebesar Rp.", D)
                        pesan = "2 tiket"
                    elif pesan=="3":
                        D = 3*125000
                        print("Total harga tiket anda sebesar Rp.", D)
                        pesan = "1 tiket"
                    else: 
                        print("Maksimal pemesanan adalah 3 tiket!")
                        break      
                    jml_uang = int(input("Masukan Jumlah Uang : "))
                    print('='*36)
        #jika memilih kelas ekonomi
                elif kelas=="2":
                    kelas = "ekonomi"
                    pesan=input("Jumlah tiket yang dipesan (max 3 tiket):")


                    if pesan=="1":
                        D = 1*75000
                        print("Total harga tiket anda sebesar Rp.", D)
                    elif pesan=="2":
                        D = 2*75000
                        print("Total harga tiket anda sebesar Rp.", D)
                    elif pesan=="3":
                        D = 3*75000
                        
                        print("Total harga tiket anda sebesar Rp.", D)
                    else:
                        print("Maksimal pemesanan adalah 3 tiket!")
                        break
                    jml_uang = int(input("Masukan Jumlah Uang : "))
                    print('='*36)
                else:
                    print("Kelas tidak valid, mohon input kelas 1/2!")


            print("\n")
                      
        kembali = jml_uang - D


        #tab
        print("\n")
        print("-"*60)   
        print("                         STRUK PEMBELIAN                          ")
        print("-"*60)
        print("No Tiket       :             ", random.randint(1000 , 999999))
        print("Nama anda      :             ", nama)
        print("Nomor KTP      :             ", no_ktp)
        print("Kereta         :             ", kereta)
        print("Tujuan         :             ", tujuan)
        print("kelas          :             ", kelas)
        print("Tanggal        :             ", tanggal)
        print("waktu          :             ", jam)
        print("Jumlah Tiket   :             ", pesan)
        print("Total Bayar    :             ", D)
        print("Jumlah Uang    :             ", jml_uang)
        print("Uang kembali   :             ", kembali)
        print("\n")
        print("-"*60)
        continue


    if menu == "2":
        print("\n")
        print("                                      ***SELAMAT DATANG DI MENU REFUND TIKET***           ")

        print("\n")
        print("="*60)
        print("                 ISI FORMULIR DATA DIRI ANDA             ")
        print("="*60)
        print("*lengkapi data diri sesuai dengan data pemesanan tiket")
        print("\n")
        tiket  = input("Masukan Nomor Tiket (max1):     ")
        nama   = input("Masukan Nama Lengkap Anda :     ")
        no_ktp = input("Masukan Nomor KTP         :     ")
        
        alasan = input("Masukan Alasan Pembatalan :     ")
        
        print("\n")
        print("-"*60)   
        print("                     STRUK PEMBATALAN                         ")
        print("-"*60)
        print("No Tiket           :         ", tiket)
        print("Nama anda          :         ", nama)
        print("Nomor KTP          :         ", no_ktp)
        print("alasan pembatalan  :         ", alasan)
        print("\n")
        print("="*60)

        print("*Cetak formulir dan berikan pada petugas di gardu tiket")
        continue


    if menu == "3":
        print("\n")
        print("                                      ***SELAMAT DATANG DI MENU CUSTUMER SERVICE***           ")
       
        print("\n")
        
        print("+=" * 18)
        print("    JADWAL KERETA  TAWANG JAYA       :")
        print("+=" * 18)
            
        print("=" * 36)
        print("         Jam Keberangkatan \n \n 06.00 \n 12.00  \n 18.00 ")
        print("=" * 36)
        print("       Tujuan Keberangkatan  \n \n 1. Stasiun Gambir \n 2. Stasiun Semarang Poncol")
        print("=" * 36)

        print('\n')
        print('\n')
        print("+=" * 18)
        print("    JADWAL KERETA  KALIGUNG       :")
        print("+=" * 18)
            
        print("=" * 36)
        print("         Jam Keberangkatan \n \n 08.00 \n 15.00  \n 21.00 ")
        print("=" * 36)
        print("       Tujuan Keberangkatan  \n \n 1. Stasiun Jatibarang \n 2. Stasiun Tegal Sari")
        print("=" * 36)
            
        print("\n")
        print("\n")

        print("=" * 36)
        print("    DAFTAR KONTAK PERSON       :")
        print("=" * 36)
        print("\n")
        print(" No Wa       : [082134931073] \n Instagram   : KASinarAbadi_123 \n gmail       : sinarAbadi23@gmail.com \n Telegram    : 08219389102 \n No Fax      ; 0928 1903 2132  ")

        print("=" * 36)