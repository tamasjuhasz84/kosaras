# hazai          idegen              hazai_pont   idegen_pont     helyszín                                időpont
# 7up Joventut    Adecco Estudiantes     81           73               Palacio Mun. De Deportes De Badalona   2005.04.03

with open('eredmenyek.csv') as f:
    fejlec = f.readline().strip().split(';')
    eredmeny = [sor.strip().split(';') for sor in f]

#3. feladat
hazai  = 0
idegen = 0
for sor in eredmeny:
    if sor[0] == 'Real Madrid':
        hazai += 1
    if sor[1] == 'Real Madrid':
        idegen += 1
print(f'3.feladat:  Real Madrid:  Hazai: {hazai}, Igeden: {idegen}')

#4. feladat
dontetlen ='nem'
for sor in eredmeny:
    if sor[2] == sor[3]:
        dontetlen = 'igen'
print(f'4.feladat:  Volt döntetlen? {dontetlen}')

#5. feladat
csapat ='Nincs Barcelonai csapat a listában!'
for sor in eredmeny:
    if sor[0].find("Barcelona"):
        csapat = sor[0]
print(f'5.feladat:  barcelonai csapat neve: {csapat}')

#6. feladat
print(f'6.feladat:')
for sor in eredmeny:
    if sor[5] == "2004-11-21":
        print(f'       {sor[0]}-{sor[1]} ({sor[2]}:{sor[3]})')


#7. feladat
print(f'7.feladat:')
hely = [] 
for sor in eredmeny:
    hely.append(sor[4])
szamlalo = 1
rendezett = sorted(hely)
kezdoertek = rendezett[1]
for sor in rendezett:
    if sor == kezdoertek:
        szamlalo += 1
    else:
        if szamlalo > 20:
            print(f'       {kezdoertek} {szamlalo}')
            szamlalo = 1
            kezdoertek = sor
        else:
            szamlalo = 1
            kezdoertek = sor



    
