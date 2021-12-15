#Kmd=[] #tühi järjend
#Km=10 #esimene päev
#print("1. päeval pikkus oli",Km)
#Kmd.append(Km)
#for p in range(2,8):
#    Km*=1.1# >10%
#    Kmd.append(round(Km,2))
#print(Kmd)
#print(Kmd[2])
#print(Kmd.index(16.11)+1)
#Kmd.remove(10) 
#print(Kmd,"Listis on kokku elemendid on",Kmd.count(16.11))
#print(len(Kmd),"on jänud listis")

#Maakond=["Tallinn","Narva, Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa, Lääne-Virumaa, Jõgevamaa","Tartu linn","Tartumaa, Põlvamaa, Võrumaa, Valgamaa","Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa"," Läänemaa, Hiiumaa, Saaremaa"]
#while 1:
#    try:
#        Index=int(input("Index=> "))
#        if len(str(Index))==5:
#            break
#    except ValueError:
#        print("Valesti sisestatud index!")
#i_list=list(str(Index))
##print(str(Index))
##print(i_list)
#s1=int(i_list[0])
#print(Maakond[s1-1])
#if s1 in [1,2,3]:
#    print("Jätke kodus!")
#else:
#    print("Kanna maski!")

                                                                            #2

#from random import*
#spisok=[]
##N=int(input("N"))
#while 1:
#    try:
#        N=int(input("N=>"))
#        if N>=2:
#            break
#    except ValueError:
#        print("Valesti sisestatud index!")
#for i in range(N):
#    spisok.append(randint(1,100))
#print(spisok)
#for s in spisok:
#    print(s)
#first=spisok[0]
#last=spisok[-1]
#spisok.pop(0)
#spisok.insert(0,last)
#spisok.pop(-1)
#spisok.insert(N-1,first)
#print(spisok)

#spisok.remove(last)
#spisok.append(first)

#spisok2=spisok.copy()
#spisok2.reverse
#print(spisok2)

                                                                            #3
#from random import*
#spisok=[]
#while 1:
#    try:
#        N=int(input("N=>"))
#        if N>=2:
#            break
#    except ValueError:
#        print()
#for i in range(N):
#    spisok.append(randint(1,100))
#print(spisok)
#print(max(spisok))
#print(len(spisok))
#a=max(spisok)/len(spisok)
#print(round(a,2))
#max_=max(spisok)
#ind=spisok.index(max_)
#spisok.pop(ind)
#spisok.insert(ind,round(a,2))
#print(spisok)

                                                                            #4
#from random import*
#spisok=[]
#while 1:
#    try:
#        N=int(input("N=>"))
#        if N>=2:
#            break
#    except ValueError:
#        print()
#for i in range(N):
#    spisok.append(randint(-100,100))
#print(spisok)
#spisok1_=[]
#for n in spisok:
#    spisok1_.append(abs(n))
#spisok1_.sort()
#print("по возрастанию=>",spisok1_)
#spisok1_.sort(reverse=True)
#print("по убыванию=>",spisok1_)


                                                                  #5
#spisok1=['крот', 'белка', 'выхухоль']
#spisok2=['a', 'aa', 'aaa', 'aaaa', 'aaaaa']
#spisok3=['qweasdqweas', 'q', 'rteww', 'ewqqqqq']
#spisok1.sort(key=len)
##print(spisok1)
#spisok2.sort(key=len)
##print(spisok2)
##print(spisok3)
#ss=[spisok1,spisok2,spisok3]
#N=0
#while N<len(ss):
#    pikkem=0
#    sN_=[]
#    for s in ss[N]:
#        pikkus=len(s)
#        if pikkus>pikkem: pikkem=pikkus
#    for s in ss[N]:
#        sN_.append(s.ljust(pikkem,"_"))
#    print(sN_)
#    N+=1


#for s in spisok1:
#    width1=len(s)
#    if width1>width: width=width1
#for s in spisok1:
#    sp.append(s.ljust(width,"_"))
#print(sp)
#for s2 in spisok2:
#    width2=len(s2)
#    if width2>wid: wid=width2
#for s2 in spisok2:
#    sp2.append(s2.ljust(wid,"_"))
#print(sp2)
#for s3 in spisok3:
#    width3=len(s3)
#    if width3>widt: widt=width3
#for s3 in spisok3:
#    sp3.append(s3.ljust(widt,"_"))
#print(sp3)
                                                  # Домашнее задание по видео

honor=["1","2","3","Я улетел","ÖÖ","lilled","Я роняю Zapad,У!","Põhjala","Tinker","DOTA","3","1000-7","Papich","What the dog doing?","3", "Admiral Z"]
print("РАБота со списками")

while 1:
    try:
        vibor=int(input("Будем работать? 1-да; 2-нет; =>"))
        if  vibor==1 or vibor==2:
            break
    except ValueError:
        print()
print(honor)
while 1:
    print("Используйте 1 из 10 функций для списка, указанные ниже")
    print("1 - Добавим элемент в конец списка ")
    print("2 - Расширяет список, добавляя в конец всех, символы введеные пользователем (ввод нного кол-ва символов привидет к добавлению нного кол-ва элементов )")
    print("3 - присоединить строку к списку ")#изначально была функция инсерт для списка
    print("4 - Удаляет элемент в списке")
    print("5 - Меняет регистр на противоположный в введенной строке  ")#изначально была функция Поп для списков 
    print("6 - Вести значения в строку и проверить, Начинаются ли слова в строке с заглавной буквы")#изначально была сортировка 
    print("7 - Ввести строку, а затем перевести в верхний регистр первую букву каждого слова") # изначально была функуция реверс для списка 
    print("8 - Копия списка  ")
    print("9 - Очищает список")
    print("10 - Кол-во повтарений 3-го элемента ")
    nomer=""
    while nomer!=int and nomer not in [1,2,3,4,5,6,7,8,9,10]:
        try:
            nomer=int(input("выберите номер: => "))
        except ValueError:
            print()
    if nomer==1:
        honor.append(input("Добавьте элемент:  "))
        print(honor)
    elif nomer==2:       
        honor.extend(input("Добавьте значение: "))
        print(honor)
    elif nomer==3:       
        newx2 =str(input("Введите текст: => "))
        newx2 =newx2.join(honor)
        print(newx2)
    elif nomer==4:
        honor.remove(input("Введите значение: "))
        print(honor)
    elif nomer==5:
        newx3 =str(input("Введите текст: => "))
        newx3=newx3.swapcase()
        print(newx3)
    elif nomer==6:
        a = str(input("Введите текст: => "))
        b = str(input("Введите текст: => "))
        c = str(input("Введите текст: => "))
        d = str(input("Введите текст: => "))
        print(a.istitle())
        print(b.istitle())
        print(c.istitle())
        print(d.istitle())
    elif nomer==7:
        newx=str(input("Введите текст: => "))
        newx=newx.title()
        print(newx)
    elif nomer==8:
        honor.copy()
        print(honor)
        new_honor=honor.copy()
        print(new_honor)
    elif nomer==9:
        honor.clear()
        print(honor)
    elif nomer==10:
        count=honor.count("3")
        print("Кол-во повторений элемента:", count)
        print(honor)    
