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
bekert = int(input())
def ureshelyszuro(bekert):
    vanures2 = False
    vanures3 = False
    vanures4 = False
    vanures5 = False
    vanuresplusz = False
    for p in range(len(teljes)):
        ures = 0
        ezasor = 0
        josor = 0
        ezazoszlop = 0
        for resz in teljes:
            ezazoszlop += 1
            for sor in resz:
                    ezasor += 1
                    for szek in sor:
                        if szek == 0:
                            ures += 1
                        else:
                            ures = 0
                        if bekert == 2:
                            if ures == 2:
                                vanures2 = True
                                joszlop = ezazoszlop
                                tempi = sor
                                josor = ezasor
                        if bekert == 3:
                            if ures == 3:
                                vanures3 = True
                                joszlop = ezazoszlop
                                tempi = sor
                                josor = ezasor
                        if bekert == 4:
                            if ures == 4:
                                vanures4 = True
                                joszlop = ezazoszlop
                                tempi = sor
                                josor = ezasor
                        if bekert == 5:
                            if ures == 5:
                                vanures5 = True
                                joszlop = ezazoszlop
                                tempi = sor
                                josor = ezasor
                        if bekert > 1 and vanures2 == False and vanures3 == False and vanures4 == False and vanures5 == False and bekert < ures:
                            vanuresplusz = False
                            joszlop = ezazoszlop
                            tempi = sor
                            josor = ezasor
    return(vanures2, vanures3, vanures4, vanures5, vanuresplusz, josor, tempi)
print(ureshelyszuro(bekert))
