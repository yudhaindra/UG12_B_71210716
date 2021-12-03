bil = int(input("Masukkan banyak bilangan : "))
jumlah = 1

print("Total = ",end =" ")
for i in range(1,bil+1):
    if(i % 7 == 0):
        jumlah = jumlah + 0
        print("+ 0",end =" ")

    elif(i % 3 == 0):
        jumlah = jumlah + (i * -1)
        print("- " + str(i),end =" ")

    elif(i==1):
        print(str(i),end =" ")

    else:
        jumlah = jumlah + i
        print("+ " + str(i),end =" ")

print("\nHasil perhitungan diatas ialah " + str(jumlah))