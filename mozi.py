import random
teljes = []
nezoterbal = []
nezoterjobb = []
sor = []
sor2 = []
def feltolto():
    while len(nezoterbal) != 15:
        for i in range(10):
            randi = random.randint(0,4)
            sor.append(randi)

        nezoterbal.append(sor)
    while len(nezoterjobb) != 15:
        for t in range(10):
            randi2 = random.randint(0,4)
            sor2.append(randi2)
        
        nezoterjobb.append(sor2)
    
    teljes.append(nezoterbal)
    teljes.append(nezoterjobb)
    return teljes

teljes = feltolto()

def kiir(nezoter):
    for oldal in nezoter:
        for sor in oldal:
            print(sor)
        print("kövi")

kiir(teljes)