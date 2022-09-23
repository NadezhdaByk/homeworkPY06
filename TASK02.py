# программа считаев в словах строки кол-во гласных букв и если оно равно выводит "Парам пам-пам",
# если не равно выводит "Пам парам"

from itertools import count


rifma='аотовт рплотвмен бпщегупрвт'
rifma1=rifma.split()
n=[]
glasnye=['а','е', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
for i in range(len(rifma1)):
    count=0
    for letter in rifma1[i]:
        if letter in glasnye:
            count+=1
    n.append(count)
  
# if (n[i]!=n[i+1] for i in range(len(n)-1)):
#     print("Пам парам")
# else:
#     print("Парам пам-пам")
count=0
for i in range(len(n)-1):
    if n[i]==n[i+1]:
        count+=1

if count==(len(n)-1):
    print("Парам пам-пам")
else:
    print("Пам парам")
        

    




