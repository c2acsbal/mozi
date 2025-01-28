import random

def feltolto():
    sor = []
    sor2 = []
    nezoterbal = []
    nezoterjobb = []
    teljes = []
    while len(nezoterbal) != 16:
        for i in range(10):
            randi = random.randint(0,4)
            sor.append(randi)
        nezoterbal.append(sor)
        sor = []

    while len(nezoterjobb) != 16:
        for t in range(10):
            randi2 = random.randint(0,4)
            sor2.append(randi2)
        nezoterjobb.append(sor2)
        sor2 = []
    
    teljes.append(nezoterbal)
    teljes.append(nezoterjobb)
    return teljes

teljes = feltolto()

def kiir(nezoter):
    for i in range(len(nezoter[0])-1):
            print(nezoter[0][i], str(i+1).zfill(2), nezoter[1][i])

kiir(teljes)