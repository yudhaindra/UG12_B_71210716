linam = [] 
likur = [] 
lihat = 0
count = 0
henti = " "


while(henti.upper!= "STOP"):
    nama = str(input("Masukkan nama : "))
    if(nama == "STOP"):
        henti = "STOP"
        break

    else:
        n = int(input("Masukkan nomor kursi "+ nama + " : "))
        
        if(len(likur)==0):
            linam.insert(count,nama)
            likur.insert(count,n)
            count = count + 1

        else:
            for i in range(len(likur)):
                if(likur[i] == n):
                    lihat = 0
                    break
                else:
                    lihat = 1
            
            if(lihat==1):
                linam.insert(count,nama)
                likur.insert(count,n)
                count = count + 1
            else:
                print("Mohon maaf kursi tersebut telah terisi!")

print()
print("List kursi yang telah terisi: ")

for i in range (count):
    print("Kursi nomor " + str(likur[i]) + " telah diisi oleh " + str(linam[i]))