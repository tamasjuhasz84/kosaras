# hazai          idegen              hazai_pont   idegen_pont     helyszín                                időpont
# 7up Joventut    Adecco Estudiantes     81           73               Palacio Mun. De Deportes De Badalona   2005.04.03

import streamlit as st
import numpy as np
import pandas as pd
import time

st.header('Ez az ACB Kosárlabdaliga 2004-2005 OKJ feladat BUI változata!')
st.text('')

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
st.write("3.feladat:  Real Madrid mérkőzések száma:")

st.write('Hazai')
my_bar = st.progress(0)

for percent_complete in range(hazai):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1)
st.write(hazai)

st.write('Idegen')
my_bar = st.progress(0)

for percent_complete in range(idegen):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1)
st.write(idegen)


#4. feladat
dontetlen ='nem'
for sor in eredmeny:
    if sor[2] == sor[3]:
        dontetlen = 'igen'
st.write("4.feladat:  Volt döntetlen?")
if dontetlen == 'nem':
    st.error(dontetlen)
else:
    st.success(dontetlen)
#5. feladat
csapat ='Nincs Barcelonai csapat a listában!'
for sor in eredmeny:
    if sor[0].find("Barcelona"):
        csapat = sor[0]
st.write("5.feladat:  barcelonai csapat neve:")
if csapat == 'Nincs Barcelonai csapat a listában!':
    st.error(csapat)
else:
    st.success(csapat)

#6. feladat
st.write("6.feladat:")
st.title('2004. November 21-én ezeket a mérkőzéseket rendezték!')
tabla=list()
for sor in eredmeny:
    if sor[5] == "2004-11-21":
        tabla.append((sor[0],sor[1],sor[2],sor[3]))

st.write(pd.DataFrame(tabla, columns=['Hazai', 'Vendég', 'Hazai pontok', 'Vendég pontok' ], index=['','','','','','']))
#        st.write(sor[0], " - ", sor[1], " ", sor[2], ":", sor[3])
#        st.write(pd.DataFrame({
#            sor[0]: [sor[2]],
#            sor[1]: [sor[3]],
#        }))            

#7. feladat
st.write('7.feladat:')
st.header('Stadionok, ahol 20-nál több mérkőzést játszottak az idényben:')
hely = [] 
for sor in eredmeny:
    hely.append(sor[4])
szamlalo = 1
rendezett = sorted(hely)
kezdoertek = rendezett[1]
d= list()
for sor in rendezett:
    if sor == kezdoertek:
        szamlalo += 1
    else:
        if szamlalo > 20:
            d.append((kezdoertek,szamlalo))
            szamlalo = 1
            kezdoertek = sor
        else:
            szamlalo = 1
            kezdoertek = sor

st.table(pd.DataFrame(d, columns=['Helyszín', 'Mérkőzések száma'], index=['','','']))

st.balloons()


