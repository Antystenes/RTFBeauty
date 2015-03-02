#!/usr/bin/python
#coding: latin-1

from random import randint

imionam = ["Andrzej", "Zdzisław", "Mściwój", "Gerwazy", "Zbyszko", "Jurand",  "Alojzy", "Eustachy"]

imionaf = ["Zdzisława", "Mirosława", "Zenobia", "Stefania", "Barbara"] 

nazwiska = ["Komorowicz","Kononowicz", "Korwin-Mikke", "Tusk", "Golonko", "Namib", "N'mir", "Yolo", "Słegmaster", "Nołskołp", "Blejz it" ]

sex = ["Mężczyzna", "Kobieta"]

plik = open('listaludzi', 'w')

for w in range( 50 ):
    losujplec = randint(0,1)
    if losujplec == 0:
        plik.write(imionam[randint(0,len(imionam)-1)]+'\n')
    else:
        plik.write(imionaf[randint(0,len(imionaf)-1)]+'\n')
    plik.write(nazwiska[randint(0,len(nazwiska)-1)]+'\n')
    plik.write(sex[losujplec]+'\n')
    plik.write(str(randint(1,28))+'.'+str(randint(1,12))+'.'+str(randint(1492,2015))+'r.\n')
    plik.write(str(randint(100000000,999999999))+2*'\n')

