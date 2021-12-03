kata = input("Input: ")
kata1 = len(kata)
print('Output:')
for a in range(kata1):
    for b in range(kata1-a-1):
        print(' ',end='')
    for b in range(a+1):
       print(kata[b],end='')
    print()
for a in range(1,kata1):
    for c in range(a):
        print(' ', end='')
    for c in range(kata1-a):
        print(kata[c], end='')
    print()