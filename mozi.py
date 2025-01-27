import random
teljes = []
nezoterbal = []
nezoterjobb = []
sor = []
sor2 = []
def feltolto():
    while len(nezoterbal) != 10:
        for i in range(10):
            randi = random.randint(0,4)
            sor.append(randi)

        nezoterbal.append(sor)
    while len(nezoterjobb) != 10:
        for t in range(10):
            randi2 = random.randint(0,4)
            sor2.append(randi)
        
        nezoterjobb.append(sor2)
    
    teljes.append(nezoterbal)
    teljes.append(nezoterjobb)
    return teljes

feltolto()
print("egymasmelle?")
egymasmelle = input()
egymasmelleakar = False
if egymasmelle == "i":
    egymasmelleakar = True
    print("egymásmellé mennyit?")
    egymasmelleennyit = int(input())
else:
    egymasmelleakar == False
    print("ok akkor mennyit")
    mennyitakarsz = int(input())

print("Milyen fajta jegyet szeretnél? (d - diák/nyugdíjas, f - felnőtt, gy - gyerek)")
milyen = input()

szamolos = 0
if egymasmelleakar == False:
    for t in teljes:
        for l in t:
             for q in l:
                if q == 0 and szamolos != mennyitakarsz:
                     print("Van szabadhely")
                     szamolos += 1 

elif egymasmelleakar == True:
    for t in teljes:
        for l in t:
            for q in l:
                if szamolos != egymasmelleennyit:
                    if q == 0:
                        szamolos += 1
                    else:
                        szamolos == 0
    if szamolos == egymasmelleennyit:
        print('asd')