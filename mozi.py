import random

def feltolto():
    sor = []
    sor2 = []
    nezoterbal = []
    nezoterjobb = []
    teljes = []
    while len(nezoterbal) != 15:
        for i in range(10):
            randi = random.randint(0,3)
            sor.append(randi)
        nezoterbal.append(sor)
        sor = []

    while len(nezoterjobb) != 15:
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
    print("           v        á        s       z       o      n")
    for i in range(len(nezoter[0])):
            print(nezoter[0][i], str(i+1).zfill(2), nezoter[1][i])
kiiir(teljes)

def bekero():
    print("Hány jegy kell (max. 5)")
    bekert = int(input())

    while bekert > 5 or bekert < 2:
        print("Ez így nem jó mert ötnél tőbb nem lehet ÉS 2-nél kisebb sem. Próbálja meg most normálisan!!")
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
        talalt = False
        for resz in teljes:
            if not talalt:
                ezazoszlop += 1
                ezasor = 0
                for sor in resz:
                    if not talalt:
                        ezasor += 1
                        ures = 0
                        for szek in sor:
                            if not talalt:
                                if szek == 0:
                                    ures += 1
                                else:
                                    ures = 0

                                if bekert == 2:
                                    if ures == 2:
                                        vanures2 = True
                                        joszlop = ezazoszlop
                                        josor = ezasor
                                        talalt = True
                                if bekert == 3:
                                    if ures == 3:
                                        vanures3 = True
                                        joszlop = ezazoszlop
                                        josor = ezasor
                                        talalt = True
                                if bekert == 4:
                                    if ures == 4:
                                        vanures4 = True
                                        joszlop = ezazoszlop
                                        josor = ezasor
                                        talalt = True
                                if bekert == 5:
                                    if ures == 5:
                                        vanures5 = True
                                        joszlop = ezazoszlop
                                        josor = ezasor
                                        talalt = True
                                if bekert > 1 and vanures2 == False and vanures3 == False and vanures4 == False and vanures5 == False and bekert < ures:
                                    vanuresplusz = True
                                    joszlop = ezazoszlop
                                    josor = ezasor
                                    talalt = True
    if not talalt:                    
        joszlop = 0
    return(vanures2, vanures3, vanures4, vanures5, vanuresplusz, joszlop, josor)

vanures2, vanures3, vanures4, vanures5, vanuresplusz, oszlop, sor = ureshelyszuro(bekert)

def szamolos(teljes):
    felnotbev = 0
    diakbev = 0
    gyerekbev = 0
    teljesardb = 0
    dikadb = 0
    gyerekdb = 0

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