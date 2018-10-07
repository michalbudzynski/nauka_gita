
#import time

#marka = "POLONEZ"
#ilosc_drzwi = 5
#print("twoja ulubiona marka to: " + marka.lower() + " .Ilosc drzwi samochodu to: " + str(ilosc_drzwi) + ''+ "...A poza tym jest godzina... " + time.strftime("%H:%M:%S"))

#imie_kota = "Tadeusz"
#imie_psa = "Brajan"
#waga_kota = 6
#waga_psa = 34
#waga_suma = waga_kota + waga_psa
#    print("Moj pies nazywa sie: " + imie_psa)
#    print ("Moj kot nazywa sie: " + imie_kota)
#    print ("kot wazy: " + str(waga_kota))
#    print ("Waga psa: " + str(waga_psa))
#    print ("Razem waza: " + str(waga_suma))


#samochody = ['polonez', 'syrenka','trabant']
#for s in samochody:
#    print(s)

#rok_prod = [1989,1976,1988]
#for n in rok_prod:
#    print(n)

#print (len(rok_prod))

#for idx in range(len(samochody)):
#    print("idx: " + str(idx) + ": " + samochody[idx])
#    print(samochody[idx] + ", rok produkcji: " + str(rok_prod[idx]))

#samolot = ("name:" 'boeing', 'przebieg:' '1000', "rok produkcji" '1988')
#    print(samolot['name'])
#for key, value in samolot.iteritems():
#    print("{0}:{1}".format(key,value))

#for key in samoloty:
#    print("{0}:{1},key, samoloty[key]")


def print_dict(d):
    for key, value in d.iteritems():
        print("{0}:{1}".format(key,value))

if __name__ == "__main__":
    samolot = {'name' : 'boeing', 'przebieg' : 1000, 'rok produkcji' : 1988}

    print_dict(samolot)
    print_dict(samolot)
