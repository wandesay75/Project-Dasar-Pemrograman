from Database import assets

user_id = 0
loop = "n"
status = False
out_program = "y"

def cek_login(kode_pin):
    for user in assets:
        if user['pin'] == kode_pin:
            return user
    return False
 
 
def cek_user(id):
    for i in range(len(assets)):
        if assets[i]['id'] == str(id):
            return int(i)
    return -1
 
 
def cek_rekening(rek_dituju):
    for i in range(len(assets)):
        if str(assets[i]['no_rekening']) == str(rek_dituju):
            return int(i)
    return -1
 
 
def transfer_uang(uang, no_rekening):
    rek_pribadi = cek_user(user_id)
    rek_dituju = cek_rekening(no_rekening)
    if rek_pribadi >= 0:
        if assets[rek_pribadi]['saldo'] >= int(uang):
            assets[rek_pribadi]['saldo'] = assets[rek_pribadi]['saldo'] - int(uang)
            assets[rek_dituju]['saldo'] = assets[rek_dituju]['saldo'] + int(uang)
            print("Anda Berhasil Mentransfer Uang Rp." + str(uang) + " ke Rekening " + no_rekening)
            print("Sisa Saldo Anda Adalah Rp.", assets[rek_pribadi]['saldo'])
        else:
            print(" Maaf! Saldo Anda Tidak Cukup! ")
 
 
def ambil_uang(uang):
    rek_pribadi = cek_user(user_id)
    if rek_pribadi >= 0:
        if assets[rek_pribadi]['saldo'] >= int(uang):
            assets[rek_pribadi]['saldo'] = assets[rek_pribadi]['saldo'] - int(uang)
            print("Anda Berhasil Menarik Uang Rp." + str(uang))
            print("Sisa Saldo Anda Adalah Rp.", assets[rek_pribadi]['saldo'])
        else:
            print(" Maaf! Saldo Anda Tidak Cukup! ")

print(50*'=')
print("         SELAMAT DATANG DI ATM BANK RUT         ")
print("            (Ruang Untuk Transaksi)             ")
print(50*'=')

while out_program == "y":
    while not status:
        print("Silahkan Masukan PIN ATM Anda!")
        kode_pin = input("Masukan Kode PIN : ")
        login = cek_login(kode_pin)
    
        if login:
            print()
            print("            Masuk Sebagai "   + login['nama_pengguna']           )
            user_id = login['id']
            status = True
            loop = "y"
        else:
            print("")
            print("  PIN YANG ANDA MASUKAN SALAH! ")
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            print(" MASUKAN PIN ANDA DENGAN BENAR! ")
            print("")

    while loop == "y" and status:
        id = assets[cek_user(user_id)]
        print(50*"=")
        print("         PILIH TRANSAKSI YANG ANDA INGINKAN           ")
        print(50*"=")
        print("1.Cek Saldo")
        print("2.Transfer Uang")
        print("3.Penarikan Tunai")
        print("4.Logout")
        print("5.Keluar Program")
        print(50*"=")
        print()
        opsi = int(input(" Pilih Menu TRANSAKSI : "))
        if opsi == 1:
            print("")
            print(" Sisa Saldo Anda Rp.", id['saldo'])
            print("")
            print("")
            loop = "n"
        elif opsi == 2:
            print("")
            print(50*"=")
            print("         SILAHKAN MASUKAN NO. REKENING TUJUAN ")
            print(50*"=")
            rek_dituju = input(" Masukan No Rekening Tujuan : ")
            print("")
            cnk = cek_rekening(rek_dituju)
            if cnk >= 0:
                print(50*"=")
                print("             SILAHKAN MASUKAN NOMINAL ")
                print(50*"=")
                print("")
                uang = input(" Masukan Nominal : ")
                transfer_uang(uang, rek_dituju,)
                print("")
                loop = "n"
            else:
                print("")
                print("     NOMOR REKENING YANG DI TUJU TIDAK DITEMUKAN ")
                print("")
                loop = "n"

        elif opsi == 3:
            print("     SILAHKAN MASUKAN NOMINAL YANG DI TARIK ")
            uang = input("Masukan Nominal : ")
            ambil_uang(uang)
            print("")
            loop = "n"
        elif opsi == 4:
            status = False
            print("**************************************************")
            print("                 ", login['nama_pengguna'])
            print("ANDA TELAH LOGOUT DARI ATM SILAHKAN LOGIN KEMBALI")
            print("***************************************************")

        elif opsi == 5:
            status = False
            loop = "n"
            out_program = "n"
        else:
            print("PILIHAN TIDAK TERSEDIA")

        if status == True:
            input("Kembali Ke Menu (TEKAN Enter) ")
            print("")
            loop = "y"
