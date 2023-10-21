'''Заданы M строк символов, которые вводятся с клавиатуры. Найти
количество символов в самой длинной строке. Выровнять строки по самой
длинной строке, поставив перед каждой строкой соответствующее
количество звёздочек.'''
print('Введите количество строк')
m = int(input())
simvol='*'
max_dlina=0
spisok=[]
nev_spisok=[]
for i in range(m):
   print('Введите строки')
   stroka=input() 
   spisok.append(stroka)
for i in spisok:
   dlina=len(i)
   if dlina>max_dlina:
      max_dlina=dlina
for i in spisok:
   if len(i)==max_dlina:
      nev_spisok.append(i)
   else:
       i=simvol*(max_dlina -len(i))+i
       nev_spisok.append (i)
for i in nev_spisok:
    print (i)
