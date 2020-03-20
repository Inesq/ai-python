# Zaimportuj bazę danych przedstawiająca płatki owsiane pod linkiem
# https://www.kaggle.com/crawford/80-cereals
# Dodaj plik CSV do repl.it.
# Załaduj bazę danych do Pythona nastepnie zademonstruj takie akcje:
# • Wyświetlenie danych z wybranej kolumny.
# • Wyświetlenie typu danych z wybranej kolumny.
# pomocne linki:
# • https://repl.it/@27942/CSV
# • https://repl.it/@jgranato/Data-AnalysisApply


import csv
import pandas as pd

dane=pd.read_csv('cereal.csv')
print(dane)#wyswietlanie csv po wczytaniu przez "pande"
print(dane.dtypes)#wyswietlanie typow danych
print(dane.iloc[[1]])#wyswietla wiersz (tutaj o nuemrze jeden)
print(dane['protein'])#wyswietla kolumne o podanej nazwie
