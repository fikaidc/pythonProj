N = 7
spisok = [2, 3, 2, 8, 7, 0, 1]
print(len(spisok))
for C in range(N-1):
    for i in range(N-1):
        if spisok[i] > spisok[i+1]:
            tmp = spisok[i]
            spisok[i] = spisok[i+1]
            spisok[i+1] = tmp


print("Hello", spisok)
