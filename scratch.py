import datetime

dzien = input("Wybierz dzien: ")
miesiac = input("Wybierz miesiac: ")
actualDate = '2019-',str(miesiac),'-',str(dzien)
date = datetime.datetime.striptime(str(actualDate), "%Y-%m%d")
print("Dzisiaj jest ", date.timetuple().tm_yday," ", x.date().year, " roku")


