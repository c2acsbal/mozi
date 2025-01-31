import random

def feltolto():
    sor = []
    sor2 = []
    nezoterbal = []
    nezoterjobb = []
    teljes = []
    while len(nezoterbal) != 16:
        for i in range(10):
            randi = random.randint(0,3)
            sor.append(randi)
        nezoterbal.append(sor)
        sor = []

    while len(nezoterjobb) != 16:
        for t in range(10):
            randi2 = random.randint(0,3)
            sor2.append(randi2)
        nezoterjobb.append(sor2)
        sor2 = []
    
    teljes.append(nezoterbal)
    teljes.append(nezoterjobb)
    return teljes

teljes = feltolto()

def kiiir(nezoter):
    for i in range(len(nezoter[0])-1):
            print(nezoter[0][i], str(i+1).zfill(2), nezoter[1][i])
    print("")
    print("           v        á        s       z       o      n")
kiiir(teljes)

def bekero():
    print("Hány jegy kell (max. 5)")
    bekert = int(input())

    while bekert > 5 and bekert < 2:
        print("Ez így nem jó mert ötnél tőbb nem lehet")
        bekert = int(input())
    return bekert

bekert = bekero()

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
        joszlop = 0
        for resz in teljes:
            ezazoszlop += 1
            ezasor = 0
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
                                josor = ezasor
                        if bekert == 3:
                            if ures == 3:
                                vanures3 = True
                                joszlop = ezazoszlop
                                josor = ezasor
                        if bekert == 4:
                            if ures == 4:
                                vanures4 = True
                                joszlop = ezazoszlop
                                josor = ezasor
                        if bekert == 5:
                            if ures == 5:
                                vanures5 = True
                                joszlop = ezazoszlop
                                josor = ezasor
                        if bekert > 1 and vanures2 == False and vanures3 == False and vanures4 == False and vanures5 == False and bekert < ures:
                            vanuresplusz = False
                            joszlop = ezazoszlop
                            josor = ezasor
    return(vanures2, vanures3, vanures4, vanures5, vanuresplusz, joszlop, josor)

vanures2, vanures3, vanures4, vanures5, vanuresplusz, oszlop, sor = ureshelyszuro(bekert)

def szamolos(teljes):
    felnotbev = 0
    diakbev = 0
    gyerekbev = 0
    teljesardb = 0
    dikadb = 0
    gyerekdb = 0
    #0 - üres, 1 felnőtt, 2 - diák, 3 - gyerek

    for sor in teljes:
        for sorr in sor:
            for szek in sorr:
                if szek == 1:
                    felnotbev += 2500
                    teljesardb += 1
                elif szek == 2:
                    diakbev += 2100
                    dikadb += 1
                elif szek == 3:
                    gyerekbev += 1300
                    gyerekdb += 1
    osszdb = gyerekdb + dikadb + teljesardb
    osszbev = gyerekbev + diakbev + felnotbev
    return osszbev, teljesardb, osszdb
osszbev, teljesdb, osszdb = szamolos(teljes)

def kihasznallak(osszdb):
    kihaszn = osszdb / (15*20)
    return kihaszn

kihasznaltsag = kihasznallak(osszdb)

def kiir(vanures2, vanures3, vanures4, vanures5, vanuresplusz, oszlop, sor, kihasznaltsag, osszbev, teljesdb, osszdb, bekert):
    if vanures2 == True:
        print("Persze, hogy van egymás melett 2 üres hely! Itt van:")
        if oszlop == 1:
            print("Bal oszlop","", sor, ". sor")
        elif oszlop == 2:
            print("Jobb oszlop","", sor, ". sor")
    elif vanures3 == True:
        print("Persze, hogy van egymás melett 3 üres hely! Itt van:")
        if oszlop == 1:
            print("Bal oszlop","", sor, ". sor")
        elif oszlop == 2:
            print("Jobb oszlop","", sor, ". sor")
    elif vanures4 == True:
        print("Persze, hogy van egymás melett 4 üres hely! Itt van:")
        if oszlop == 1:
            print("Bal oszlop","", sor, ". sor")
        elif oszlop == 2:
            print("Jobb oszlop","", sor, ". sor")
    elif vanures5 == True:
        print("Persze, hogy van egymás melett 5 üres hely! Itt van:")
        if oszlop == 1:
            print("Bal oszlop","", sor, ". sor")
        elif oszlop == 2:
            print("Jobb oszlop","", sor, ". sor")
    elif vanuresplusz == True:
        print("Persze, hogy van egymás melett", bekert, "üres hely! Itt van:")
        if oszlop == 1:
            print("Bal oszlop","", sor, ". sor")
        elif oszlop == 2:
            print("Jobb oszlop","", sor, ". sor")
    elif bekert == 0 or bekert > 5 or bekert == 1:
        print("Kérlek normális értéket adjál már")
    else:
        print("Sajnos nem tudok ennyi  üres hellyel szolgálni :(")
    print("")
    print("Itt a mozi kihasználtsága százalélkban", round(kihasznaltsag*100, 2), "%")
    print("")
    print("Össszesen", osszdb, "jegyet értékesítettek")
    print("")
    print("A mozi összbevétele", osszbev, "Ft volt")
    print("")
    print(teljesdb, "db teljes árú jegyet értékesítettek")

kiir(vanures2, vanures3, vanures4, vanures5, vanuresplusz, oszlop, sor, kihasznaltsag, osszbev, teljesdb, osszdb, bekert)