
def printMenu():
    print('''======== Daftar Penjualan Barang Toko ========
    1.Tampilkan Daftar Penjualan
    2.Menambah Barang/Menghapus Barang
    3.Mengubah Barang
    4.Membeli Barang
    5.Keluar Program''')

def printDaftarPenjualan():
    while True:
        print('''\n1.Tampilkan Seluruh Daftar Penjualan
2.Tampilkan Daftar Penjualan Satu Barang
3.Tampilkan Daftar Penjualan Kategori Barang
4.Kembali ke Menu Sebelumnya''')
        option1=input('Masukkan Pilihan :')
        if(option1=='1'):
            print('====== Daftar Barang =====')
            for key in DaftarPenjualan[0].keys():
                print(f"{key:<10}",end='|')
            print('')
            for i in DaftarPenjualan:
                for val in i.values():
                    print(f"{val:<10}",end='|')
                print('')
        if(option1=='2'):
            while True:
                option2=input('Masukan ID/Nama Barang(Input "cancel" untuk kembali) :')
                if option2.lower()=='cancel':
                    break
                elif not any (i['Nama']==option2.lower() or i['ID']==option2.lower() for i in DaftarPenjualan):
                    print("Nama/ID barang tidak ada")
                else:
                    for i in DaftarPenjualan:
                        if(i['Nama']==option2.lower()):
                            for key in i.keys():
                                print(f"{key:<10}",end='|')
                            print('')
                            for val in i.values():              
                                print(f"{val:<10}",end='|')
                            print('\n')                           
                            break
                        elif(i['ID']==option2.lower()):
                            for key in i.keys():
                                print(f"{key:<10}",end='|')
                            print('')
                            for val in i.values():              
                                print(f"{val:<10}",end='|')
                            print('\n')                           
                            break
        if(option1=='3'):
            while True:
                option2=input('Masukan Kategori Barang(Input "cancel" untuk kembali) :')
                if option2.lower()=='cancel':
                    break
                elif not any (i['Kategori']==option2.capitalize() for i in DaftarPenjualan):
                    print("Kategori barang tidak ada")
                else:
                    j=DaftarPenjualan[0]
                    for key in j.keys():
                        print(f"{key:<10}",end='|')
                    print('')
                    for i in DaftarPenjualan:
                        if(i['Kategori']==option2.capitalize()):
                            for val in i.values():              
                                print(f"{val:<10}",end='|')
                            print('')
                    print('')                      
        if(option1=='4'):
            break

def addOrDeleteData():
    while True:
        option=input('''    1.Menambah Barang
    2.Menghapus Barang
    3.Kembali ke Menu Sebelumnya
Masukkan Pilihan Menu :''')
        if(option=='1'):
            addData()
        if(option=='2'):
            deleteData()
        if(option=='3'):
            break

def addData():
    while True:
        idBarang=input('Masukkan ID Barang :')
        if any(i['ID']==idBarang.lower() for i in DaftarPenjualan):
            print("ID barang sudah ada")
        else:
            namaBarang=input('Masukkan Nama Barang :')
            stockBarang=int(input('Masukkan Stock Barang '))
            hargaBarang=int(input('Masukkan Harga Barang '))
            penjualan=int(input('Masukkan Penjualan Barang :'))
            kategoriBarang=input('Masukkan Kategori Barang :')
            DaftarPenjualan.append({'ID':idBarang,'Nama':namaBarang,'Stock':stockBarang,'Penjualan':penjualan,'Harga':hargaBarang,'Kategori':kategoriBarang})
            print('Barang berhasil ditambahkan')
            break

def deleteData():
    while True:
        idBarang=input('Masukkan ID Barang (Input "cancel" untuk kembali):')
        if idBarang.lower()=='cancel':
            break
        if not any (i['ID']==idBarang.lower() for i in DaftarPenjualan):
            print("ID barang tidak ada")
        else:
            for i in range (len(DaftarPenjualan)):
                if(DaftarPenjualan[i]['ID']==idBarang.lower()):
                    del DaftarPenjualan[i]
                    print('Barang berhasil dihapus')
                    break

def changeData():
    while True:
        input1=input('Masukkan ID Barang (Input "cancel" untuk kembali) :')
        if input1.lower()=='cancel':
            break
        indexBarang=0
        for i in range(len(DaftarPenjualan)):
            if(DaftarPenjualan[i]['ID']==input1):
                indexBarang=i
        if not any (i['ID']==input1.lower() for i in DaftarPenjualan):
            print("ID barang tidak ada")
        else:
            while True:
                input2=input('''1.Ubah ID Barang
2.Ubah Nama Barang
3.Ubah Harga Barang
4.Ubah Stock Barang
5.Ubah Kategori Barang
6.Ubah Penjualan Barang
7.Kembali ke Menu Sebelumnya
Masukkan Pilihan Menu :''')
                if(input2=='1'):
                    input3=input('Masukkan ID Barang Baru :')
                    DaftarPenjualan[indexBarang]['ID']=input3
                elif(input2=='2'):
                    input3=input('Masukkan Nama Barang Baru :')
                    DaftarPenjualan[indexBarang]['Nama']=input3
                elif(input2=='3'):
                    input3=input('Masukkan Harga Barang Baru :')
                    DaftarPenjualan[indexBarang]['Harga']=input3
                elif(input2=='4'):
                    input3=input('Masukkan Stock Barang Baru :')
                    DaftarPenjualan[indexBarang]['Stock']=input3
                elif(input2=='5'):
                    input3=input('Masukkan Kategori Barang Baru :')
                    DaftarPenjualan[indexBarang]['Harga']=input3
                elif(input2=='6'):
                    input3=input('Masukkan Kategori Barang Baru :')
                    DaftarPenjualan[indexBarang]['Penjualan']=input3
                elif(input2=='7'):
                    break

def printCart(cart):
    if(len(cart)==0):
        print("Daftar belanja masih kosong")
    else:
        print("==== Daftar Belanja ====")
        print(f"{'No':<2}|{'Nama':<10}|{'Jumlah':<10}|{'Harga':<10}|{'Total Harga':<10}|")
        for i in range(len(cart)):
            print(f"{i+1:<2}|{cart[i][0]:<10}|{cart[i][1]:<10}|{cart[i][2]:<10}|{cart[i][3]:<10}")
    print('')


def addCart():
    cart=[]
    while True:
        option=input('''    1.Tambahkan Barang
    2.Tampilkan Daftar Barang
    3.Tampilkan Belanjaan
    4.Bayar
    5.Kembali
Masukkan pilihan menu :''')
        if(option=='1'):
            while True:
                index=0
                id=input('Masukkan ID Barang (Input "cancel" untuk kembali):')
                if(id.lower()=='cancel'):
                    break
                elif not any(DaftarPenjualan[i]['ID']==id for i in range(len(DaftarPenjualan))):
                    print("ID Barang tidak ada")
                    continue
                qty=int(input('Masukkan Jumlah Beli :'))
                for i in range(len(DaftarPenjualan)):
                    if DaftarPenjualan[i]['ID']==id:
                        index=i
                        break
                if(qty>DaftarPenjualan[index]['Stock']):
                    print(f"Stock tidak cukup, stock {DaftarPenjualan[index]['Nama']} tinggal {DaftarPenjualan[index]['Stock']}")
                elif(DaftarPenjualan[index]['Stock']>=qty>0):
                    if any(i[4]==index for i in cart):
                        for i in cart:
                            if i[4]==index:
                                i[1]+=qty
                                i[3]+=(qty*i[2])
                                break
                    else:
                        cart.append([DaftarPenjualan[index]['Nama'], qty, DaftarPenjualan[index]['Harga'], (qty*DaftarPenjualan[index]['Harga']), index])
                    break
                elif(qty<=0):
                    for i in range(len(cart)):
                        if(cart[i][4]==index):
                            cart[i][1]+=qty
                            if(cart[i][1]<=0):
                                del cart[i]
                            else:
                                cart[i][3]+=(qty*cart[i][2])
                    break

        elif(option=='2'):
            printDaftarPenjualan()
        elif(option=='3'):
            printCart(cart)
        elif(option=='4'):
            printCart(cart)
            totalHarga=0
            for i in range(len(cart)):
                totalHarga+=cart[i][3]
            while True:
                print(f'Total harga :{totalHarga}')
                uangBayar=int(input('Masukkan jumlah uang :'))           
                if(uangBayar<totalHarga):
                    uangKurang=totalHarga-uangBayar
                    print('Uang anda kurang {}'.format(uangKurang))
                elif(uangBayar==totalHarga):
                    print('Uang anda pas. Terima kasih telah berbelanja\n')
                    for item in cart:
                        DaftarPenjualan[item[4]]['Stock']-=item[1]
                        DaftarPenjualan[item[4]]['Penjualan']+=item[1]
                    break
                    
                elif(uangBayar>totalHarga):
                    kembalian=uangBayar-totalHarga
                    print('Terima kasih telah berbelanja. Kembalian anda {}\n'.format(kembalian))
                    for item in cart:
                        DaftarPenjualan[item[4]]['Stock']-=item[1]
                        DaftarPenjualan[item[4]]['Penjualan']+=item[1]                    
                    break
            cart.clear()
            break
        elif(option=='5'):
            break


DaftarPenjualan=[
    {'ID':'213','Nama':'spion','Stock':23,'Penjualan':2,'Harga':130000,'Kategori':'Aksesoris'},
    {'ID':'214','Nama':'wiper','Stock':15,'Penjualan':10,'Harga':70000,'Kategori':'Aksesoris'},
    {'ID':'238','Nama':'kaca','Stock':18,'Penjualan':4,'Harga':250000,'Kategori':'Panel'}

]



while True:
    printMenu()
    option=input("Pilih menu yang diinginkan :")
    if(option=='1'):
        printDaftarPenjualan()
    if(option=='2'):
        addOrDeleteData()
    if(option=='3'):
        changeData()
    if(option=='4'):
        addCart()
    if(option=='5'):
        break

