from Database import assets

user_id = 0
loop = "n"
status_login = False
credit_card = "y"

def cek_login(p):
    for user in assets:
        if user['pin'] == p:
            return user
    return False
 
 
def cek_user(id):
    for i in range(len(assets)):
        if assets[i]['id'] == str(id):
            return int(i)
    return -1
 
 
def cek_rekening(no):
    for i in range(len(assets)):
        if str(assets[i]['no_rekening']) == str(no):
            return int(i)
    return -1
 
 
def transfer_uang(uang, no_rekening):
    index1 = cek_user(user_id)
    index2 = cek_rekening(no_rekening)
    if index1 >= 0:
        if assets[index1]['saldo'] >= int(uang):
            assets[index1]['saldo'] = assets[index1]['saldo'] - int(uang)
            assets[index2]['saldo'] = assets[index2]['saldo'] + int(uang)
            print("Anda berhasil mentransfer uang Rp." + str(uang) + " ke Rekening " + no_rekening)
            print("sisa saldo anda adalah Rp.", assets[index1]['saldo'])
        else:
            print(" maaf! saldo anda tidak cukup! ")
 
 
def ambil_uang(uang):
    index1 = cek_user(user_id)
    if index1 >= 0:
        if assets[index1]['saldo'] >= int(uang):
            assets[index1]['saldo'] = assets[index1]['saldo'] - int(uang)
            print("Anda berhasil menarik uang Rp." + str(uang))
            print("sisa saldo anda adalah Rp.", assets[index1]['saldo'])
        else:
            print(" maaf! saldo anda tidak cukup! ")

print(50*'=')
print("         SELAMAT DATANG DI ATM BANK 12.1A.15         ")
print(50*'=')

while credit_card == "y":
    while not status_login:
        print("Silahkan masukan pin anda!")
        pin = input("Masukan Kode PIN : ")
        login = cek_login(pin)
    
        if login:
            print()
            print("            Masuk sebagai "   + login['username']           )
            user_id = login['id']
            status_login = True
            loop = "y"
        else:
            print("")
            print("  PIN YANG ANDA MASUKAN SALAH! ")
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            print(" MASUKAN PIN ANDA DENGAN BENAR! ")
            print("")

    while loop == "y" and status_login:
        id = assets[cek_user(user_id)]
        print()
        print(50*"=")
        print("         PILIH TRANSAKSI YANG ANDA INGINKAN           ")
        print(50*"=")
        print("1.Cek Saldo")
        print("2.Transfer Uang")
        print("3.Ambil Uang")
        print("4.Logout")
        print("5.Keluar ATM")
        print(50*"=")
        print()
        opsi = int(input(" Pilih menu TRANSAKSI : "))
        if opsi == 1:
            print("")
            print(" Sisa Saldo anda Rp.", id['saldo'])
            print("")
            print("")
            loop = "n"
        elif opsi == 2:
            print("")
            print(50*"=")
            print("     SILAHKAN MASUKAN NO. REKENING TUJUAN ")
            print(50*"=")
            no_rek = input(" Masukan No Rekening Tujuan : ")
            print("")
            cnk = cek_rekening(no_rek)
            if cnk >= 0:
                print(50*"=")
                print("             SILAHKAN MASUKAN NOMINAL ")
                print(50*"=")
                print("")
                nominal = input(" Masukan Nominal : ")
                transfer_uang(nominal, no_rek,)
                print("")
                loop = "n"
            else:
                print("")
                print("     NOMOR REKENING YANG DI TUJU TIDAK DITEMUKAN ")
                print("")
                loop = "n"

        elif opsi == 3:
            print("     SILAHKAN MASUKAN NOMINAL YANG DI TARIK ")
            nominal = input("Masukan Nominal : ")
            ambil_uang(nominal)
            print("")
            loop = "n"
        elif opsi == 4:
            status_login = False

        elif opsi == 5:
            status_login = False
            loop = "n"
            pakai_atm = "n"
        else:
            print("pilihan tidak tersedia")

        if status_login == True:
            input("Kembali ke menu (TEKAN Enter) ")
            print("")
            loop = "y"