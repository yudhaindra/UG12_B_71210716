angka = int(input("Input : "))
print("Output : ")
for i in range(angka):
    for j in range(angka-i-1):
        print(" ",end="  ")
    for j in range(angka):
        if j == 0 or i == (angka-1) or i == j:
            print("*", end= "  ")
        else:
            print(end="   ")
    print()