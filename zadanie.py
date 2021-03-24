"""Dla danych z zadania 5 ( telefony.txt ) matura próbna CKE 2021 napisz program który da odpowiedzi na następujące pytania:
1Podaj liczbę połączeń w rozbiciu na stacjonarne , komórkowe, zagraniczne
2Podaj trzy numery telefonów, pod które wykonano najwięcej połączeń, i liczby tych połączeń.
3Utwórz zestawienie liczby połączeń – oddzielnie do telefonów stacjonarnych i komórkowych – wykonanych w poszczególnych dniach
Odpowiedzi wyświetl na konsoli
Uwaga pierwsza linia w pliku jest linią nagłówkową ( należy ją pominąć w trakcie odczytu )"""

#telefony stacjonarne 7 cyfr
# tel kom 8 cyfr
# zagraniczne 10 lub więcej
stacjonarne = [];komorkowe = [];zagraniczne = [];slownik = {};i = 1
data2 = "3-07-2017";
stacj = 0;
kom = 0
plik = open("telefony.txt","r")

next(plik)
for linia in plik:

    linia = linia.split()
    numer = linia[0]
    numer2 = numer
    numer3 = numer
    data = linia[1]


    if len(numer) == 7:
        stacjonarne.append(numer)
    elif len(numer) == 8:
        komorkowe.append(numer)
    else:
        zagraniczne.append(numer)

    if numer2 not in slownik.keys():
        slownik[numer2]=1
    else:
        slownik[numer2]+=1

    print(data2,data)

    while i > 0:
        if data2 == data:
            if numer3 == 7:
                stacj += 1
            elif numer3 == 8:
                kom += 1a
        else:
            print("stacjonarne = ",stacj)
            print("komorkowe = ",kom)
            stacj = 0;
            kom = 0
    data2 = data

slownik = sorted(slownik.items(), key=lambda X:X[1])

oddzielacz = "-------------------"
print(oddzielacz)
print("zad1")
print("Stacjonarne = ",len(stacjonarne))
print("Komorkowe = ",len(komorkowe))
print("Zagraniczne = ",len(zagraniczne))
print(oddzielacz)
print("zad2")
print("Top1",slownik[-1])
print("Top1",slownik[-2])
print("Top1",slownik[-3])
print(oddzielacz)
print("zad3")





