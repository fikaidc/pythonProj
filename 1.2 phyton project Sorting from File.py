file = open("python data.py") #открываем файл
line_list = file.readlines() #в списсок закид
for line in line_list:      #print(line)
    str_list = line.split() #поделмть посив
    print("str_list = ", str_list)

for i in range (0, len(str_list)):
    box = int(str_list[i])
    str_list[i] = box #преобразовали в целоч
print('str_list with nums =', str_list)

#Сортировка
L = str_list
for i in range(0, len(L)):
    for j in range(0, len(L)-i-1):
        if L[j+1] < L[j]:
            a = L[j]
            L[j] = L[j+1]
            L[j+1] = a
    print("str_list with sorting = ", str_list)