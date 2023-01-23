#OPEN FILE
file = open("file_teks2.txt","r")
data = file.read()
#PROSES MENCARI INPUT
file.close()
posisi = data.split()
#MEMBUAT VARIABEL KOSONG PEMENANG
pemenang = None

#MEMBUAT FUNGSI MENAMPILKAN POSISI
def menampilkan_posisi(posisi):
    print(f"{posisi[0]}  {posisi[1]}  {posisi[2]} \n{posisi[3]}  {posisi[4]}  {posisi[5]} \n{posisi[6]}  {posisi[7]}  {posisi[8]}")
#MENCARI SIAPA MENANG DI KOLOM
def cek_menang_kolom(posisi):
    global pemenang
    if posisi[0] == posisi[1] == posisi[2] and posisi[0] != "_": #Mencari Pemenang dengan index [0,1,2]
        pemenang = posisi [0]
        return True
    elif posisi[3] == posisi[4] == posisi[5] and posisi[3] != "_": #Mencari Pemenang dengan index [3,4,5]
        pemenang = posisi[3]
        return True
    elif posisi[6] == posisi[7] == posisi[8] and posisi[6] != "_": #Mencari Pemenang dengan index [6,7,8]
        pemenang = posisi[6]
        return True
#MENCARI SIAPA MENANG DI ROW
def cek_menang_row(posisi):
    global pemenang
    if posisi[0] == posisi[3] == posisi[6] and posisi[0] != "_": #Mencari Pemenang dengan index [0,3,6]
        pemenang = posisi [0]
        return True
    elif posisi[1] == posisi[4] == posisi[7] and posisi[1] != "_": #Mencari Pemenang dengan index [1,4,7]
        pemenang = posisi[1]
        return True
    elif posisi[2] == posisi[5] == posisi[8] and posisi[2] != "_": #Mencari Pemenang dengan index [2,5,8]
        pemenang = posisi[2]
        return True
#MENCARI SIAPA MENANG DI MIRING
def cek_menang_miring(posisi):
    global pemenang
    if posisi[0] == posisi[4] == posisi[8] and posisi[0] != "_": #Mencari Pemenang dengan index [0,4,8]
        pemenang = posisi [0]
        return True
    elif posisi[2] == posisi[4] == posisi[6] and posisi[2] != "_": #Mencari Pemenang dengan index [2,4,6]
        pemenang = posisi[2]
        return True
#MENCARI PEMAIN MENANG
def siapa_menang():
    global pemenang
    if cek_menang_kolom(posisi) or cek_menang_row(posisi) or cek_menang_miring(posisi): #Menncari pemenang diantara kolom,row, dan miring
        return(f"Dimenangkan oleh {pemenang}")                       #Meretrun Fungsi untuk mendapatkan pemenang
    else:
        print("pemenang: none")
        print(mencari_posisi_hampir_memang(posisi_hampir="x"))
        print(mencari_posisi_hampir_memang(posisi_hampir="0"))

#MENCARI PEMAIN HAMPIR MENANG DENGAN FUNGSI
def mencari_posisi_hampir_memang(posisi_hampir):            #Membuat fungsi untuk mencari index posisi hampir kemaren
    global posisi
    if posisi[0] == posisi[1] == posisi_hampir:             #Mencari posisi hampir menang dengan index[0,1]
        return (f"Hampir menang oleh: {posisi_hampir}") 
    elif posisi[1] == posisi[2] == posisi_hampir:           #Mencari posisi hampir menang dengan index[1,2]
        return (f"Hampir menang oleh: {posisi_hampir}") 
    elif posisi[3] == posisi[4] == posisi_hampir:          
        return (f"Hampir menang oleh: {posisi_hampir}") 
    elif posisi[4] == posisi[5] == posisi_hampir:           
        return (f"Hampir menang oleh: {posisi_hampir}") 
    elif posisi[6] == posisi[7] == posisi_hampir:
        return (f"Hampir menang oleh: {posisi_hampir}") 
    elif posisi[7] == posisi[8] == posisi_hampir:
        return (f"Hampir menang oleh: {posisi_hampir}") 
        #ROW HAMPIR MENANG
    elif posisi[0] == posisi[3]  == posisi_hampir:
        return (f"Hampir menang oleh: {posisi_hampir}")
    elif posisi[3] == posisi[6] == posisi_hampir:
         return (f"Hampir menang oleh: {posisi_hampir}") 
    elif posisi[1] == posisi[4]  == posisi_hampir:
        return (f"Hampir menang oleh: {posisi_hampir}")
    elif posisi[4] == posisi[7]  == posisi_hampir:
        return (f"Hampir menang oleh: {posisi_hampir}") 
    elif posisi[2] == posisi[5] == posisi_hampir:
        return (f"Hampir menang oleh: {posisi_hampir}") 
    elif posisi[5] == posisi[8] == posisi_hampir:
        return (f"Hampir menang oleh: {posisi_hampir}") 
        #MIRING HAMPIR MENANG 
    elif posisi[0] == posisi[4]  ==  posisi_hampir:
        return (f"Hampir menang oleh: {posisi_hampir}") 
    elif posisi[4] == posisi[8] == posisi_hampir:
        return (f"Hampir menang oleh: {posisi_hampir}") 
    elif posisi[2] == posisi[4] == posisi_hampir:
        return (f"Hampir menang oleh: {posisi_hampir}") 
    elif posisi[4] == posisi[6] == posisi_hampir:
        return (f"Hampir menang oleh: {posisi_hampir}") 

#MENCARI SIAPA HAMPIR MENANG
def siapa_hampir_menang():                                          #Membuat fungsi hampir menag
    global pemenang                                                 #Memanggil varabel global pemenang
    if pemenang == "x":                                               #Menanggil fungsi posisi hampir menang jika pemenang "x"
        return mencari_posisi_hampir_memang(posisi_hampir="0")      
    elif pemenang == "0":                                            #Menanggil fungsi posisi hampir menang jika pemenang "0"
        return mencari_posisi_hampir_memang(posisi_hampir="x")
    elif pemenang == "None":                                         #Menanggil fungsi posisi hampir menang jika pemenang "None"
        return mencari_posisi_hampir_memang(posisi_hampir="0")
#MENAMPILKAN POSISI
menampilkan_posisi(posisi)
if str(siapa_menang()) != 'None':                                       
	print(siapa_menang())
	print(siapa_hampir_menang())
