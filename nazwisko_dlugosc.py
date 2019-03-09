name = input("Podaj imie i nazwisko: ")
tablica_slow = name.split(" ")
print(tablica_slow)
imie = tablica_slow[0]
nazwisko = tablica_slow[1]
print('Dlugosc imienia: ', len(imie))
print('Nazwisko malymi literami: ', nazwisko.lower())