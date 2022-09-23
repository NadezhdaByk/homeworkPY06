# Вам уже приходилось писать таблицу умножения. Но в этот раз вас попросили сделать в плюс
#  к таблице и умножения еще таблицу сложения, а также таблицу возведения в степень.
# Что не копировать один и тот же код и обобщить все три функции до единой рисования таблиц 
# (бинарных) арифметических операций, напишите функцию print_operation_table
# (operation, num_rouws=9, num_colums=9), которая принимает в качестве аргумента функцию, 
# вычисляющую элемент по номеру строки и столбца.

line=int(input('Введите кол-во строчек '))
row=int(input('Введите кол-во столбцов '))
choose=input("какую операцию выполнтить: 1- сумма, 2 - умножение, 3- возведение в степень? ")

comp=[0]*row
def f_comp(x, y):
    for i in range(1, x+1):
        for j in range(y):
            comp[j]=(j+1)*i
        print(*comp)

sum=[0]*(row+1)
def f_sum(x, y):
    for i in range(0, x+1):
        for j in range(y+1):
            sum[j]=i+j
        print(*sum)
 
deg=[0]*(row+1)
def f_deg(x, y): 
    print(*[i for i in range(line+1)])   
    for i in range(1, x+1):
        for j in range(y+1):
            if j==0:
                deg[j]=i
            else:    
                deg[j]=i**j
        print(*deg)
if choose==3:
    f_deg(line, row)
elif choose==1:
    f_sum(line, row)
else:
    f_comp(line, row) 