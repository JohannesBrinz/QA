''' Versuch QA
 Johannes Brinz & Caterina Vanelli
 Datum: 17.12.2020
 Ort: Rec C301'''

import numpy as np
import matplotlib.pyplot as plt
import random
import pandas as pd
from scipy import optimize
import math
import matplotlib.font_manager as fm
import matplotlib.mlab as mlab
from scipy.stats import norm
from scipy.signal import find_peaks

#Datenimport
D4611_400 = pd.read_csv("Daten Cate Jo/4611_400.dat", sep = " ", header = 0, \
    names = ["f[Hz]", "Sig[-]"])
D4611_600 = pd.read_csv("Daten Cate Jo/4611_600.dat", sep = " ", header = 0, \
    names = ["f[Hz]", "Sig[-]"])
D4612 = pd.read_csv("Daten Cate Jo/4612.dat", sep = " ", header = 0, \
    names = ["f[Hz]", "Sig[-]"])
D4613_10 = pd.read_csv("Daten Cate Jo/4613_10mm.dat", sep = " ", header = 0, \
    names = ["f[Hz]", "Sig[-]"])
D4613_13 = pd.read_csv("Daten Cate Jo/4613_13mm.dat", sep = " ", header = 0, \
    names = ["f[Hz]", "Sig[-]"])
D4614 = pd.read_csv("Daten Cate Jo/4614.dat", sep = " ", header = 0, \
    names = ["f[Hz]", "Sig[-]"])

#Definition von Funktionen
L = 400e-3
def k(n):
    return n*np.pi/L

def f(k):
    return k * 347.6 /  (2*np.pi)


#4.6.1 Plot der Resonanzen für L=400 und L=600 mit und ohne Irisblende
#L=400
plt.plot(D4611_400["f[Hz]"]*2*np.pi/347.6, D4611_400["Sig[-]"], linewidth = 2)
plt.errorbar(k(np.linspace(0, 28, 28)), np.linspace(5, 5, 28),  fmt='x', color = "green")
plt.title('Resonanzfrequenzen für L = 400 mm', fontsize = 15)
plt.xlabel('Wellenzahl  [$m^{-1}$]' , fontsize = 13)
plt.ylabel('Signalhöhe [au]', fontsize = 13)
plt.grid(True)
plt.legend(['gemessene Resonanzen', "erwartete Werte für k durch $k = n\pi/L$ "], fontsize = 13)
plt.savefig('Plots/P4611_400.png', dpi=300)
plt.clf()

#L=400 mit
L = 421e-3
plt.plot(D4614["f[Hz]"]*2*np.pi/347.6, D4614["Sig[-]"], linewidth = 2)
#plt.errorbar(k(np.linspace(0, 10, 10)), np.linspace(5, 5, 10),  fmt='x', color = "green")
plt.title('Resonanzfrequenzen für L = 421 mm mit Irisblende', fontsize = 15)
plt.xlabel('Wellenzahl  [$m^{-1}$]', fontsize = 13)
plt.ylabel('Signalhöhe [au]', fontsize = 13)
plt.grid(True)
plt.legend(['gemessene Resonanzen', "k durch $k = n\pi/L$ "], fontsize = 13)
plt.savefig('Plots/P4614.png', dpi=300)
plt.clf()


#L=600 ohne
L = 600e-3
plt.plot(D4611_600["f[Hz]"]*2*np.pi/347.6, D4611_600["Sig[-]"], linewidth = 2)
#plt.errorbar(k(np.linspace(0, 28, 28)), np.linspace(5, 5, 28),  fmt='x', color = "green")
plt.title('Resonanzfrequenzen für L = 633 mm ohne Irisblende', fontsize = 15)
plt.xlabel('Wellenzahl  [$m^{-1}$]' , fontsize = 13)
plt.ylabel('Signalhöhe [au]', fontsize = 13)
plt.grid(True)
plt.legend(['gemessene Resonanzen', "erwartete Werte für k durch $k = n\pi/L$ "], fontsize = 13)
plt.savefig('Plots/P4611_600.png', dpi=300)
plt.clf()

#L=600 mit
L = 633e-3
plt.plot(D4612["f[Hz]"]*2*np.pi/347.6, D4612["Sig[-]"], linewidth = 2)
plt.title('Resonanzfrequenzen für L = 600 mm mit Irisblende', fontsize = 15)
plt.xlabel('Wellenzahl  [$m^{-1}$]', fontsize = 13)
plt.ylabel('Signalhöhe [au]', fontsize = 13)
plt.grid(True)
plt.legend(['gemessene Resonanzen', "erwartete Werte für k durch $k = n\pi/L$ "], fontsize = 13)
plt.savefig('Plots/P4612.png', dpi=300)
plt.clf()

#Vergleich der Dispersionen L=600
L = 633e-3
plt.plot(D4612["f[Hz]"]*2*np.pi/347.6, D4612["Sig[-]"], linewidth = 1, ls = "--")
plt.plot(D4613_13["f[Hz]"]*2*np.pi/347.6, D4613_13["Sig[-]"], linewidth = 1, linestyle = "-")
plt.plot(D4613_10["f[Hz]"]*2*np.pi/347.6, D4613_10["Sig[-]"], linewidth = 1, ls = "-")
plt.title('Dispersion für verschiedene Irisblenden', fontsize = 15)
plt.xlabel('Wellenzahl  [$m^{-1}$]', fontsize = 13)
plt.ylabel('Signalhöhe [au]', fontsize = 13)
plt.grid(True)
plt.legend(['d = 16mm', "d = 13mm", "d = 10mm"], fontsize = 13)
plt.savefig('Plots/P4613.png', dpi=300)
plt.clf()

#find peaks
peaks_400 = find_peaks(D4611_400["Sig[-]"])
peaks_600_ohne = find_peaks(D4611_600["Sig[-]"])
peaks_600_mit = find_peaks(D4612["Sig[-]"])


f400_file = pd.DataFrame()
f400_mit_file = pd.DataFrame()
f600_file = pd.DataFrame()
f600_mit_file = pd.DataFrame()
f8x75_file = pd.DataFrame()
f8x75_file_minus = pd.DataFrame()
f400_file_minus = pd.DataFrame()
f400_mit_file_minus = pd.DataFrame()
f600_file_minus = pd.DataFrame()
f600_mit_file_minus = pd.DataFrame()

f400_file["Frequenz"]  = [500, 900, 1300, 1750, 2150, 2600, 3050, 3450, 3900, 4350, 4750, 5150, 5600, 6050, 6450, \
6900, 7300, 7750, 8150, 8600, 9000, 9450, 9900, 10300, 10750, 11600]

f400_mit_file["Frequenz"] = [450, 750, 1100, 1450, 1800, 2100, 2400, 3350, 3750, 4050, 4400, 4650, 4950, 5100, \
6750, 6900, 7150, 7400, 7700, 7900, 9950, 10150, 10350, 10600]

f600_file["Frequenz"] = [450, 750, 1050, 1400, 1750, 2100, 2400, 2800, 3100, 3450, 3800, 4150, 4500, 4850, 5150, \
5500, 5850, 6200, 6550, 6900, 7250, 7550, 7900, 8250, 8600, 8950, 9300, 9650, 10000, 10300, 10650, 11000, 11350, 11700]

f600_mit_file["Frequenz"] = [600, 850, 1150, 1450, 1700, 2000, 2250, 2400, 3350, 3600, 3800, 4100, 4350, 4600, 4800, 5000,\
6550, 6750, 6900, 7150, 7350, 7550, 7800, 7950, 9900, 10050, 10250, 10450, 10650, 10850, 11000]

f8x75_file["Frequenz"] = [150, 300, 550, 750, 1050, 1250, 1500, 1750, 2350, 2600, 2800, 3050, 3300, 3500, 3650, 4550, 4750, 4900, 5150, 5350, \
5500, 6800, 6900, 7100, 7250, 7450, 7600, 9100, 9250, 9400, 9600, 9700, 11300, 11450, 11600, 11850, 11750]

f8x75_file["Wellenvektor"] = f8x75_file["Frequenz"] * 2*np.pi/347.6
f400_file["Wellenvektor"] = f400_file["Frequenz"] * 2*np.pi/347.6
f400_mit_file["Wellenvektor"] = f400_mit_file["Frequenz"] * 2*np.pi/347.6
f600_file["Wellenvektor"] = f600_file["Frequenz"] * 2*np.pi/347.6
f600_mit_file["Wellenvektor"] = f600_mit_file["Frequenz"] * 2*np.pi/347.6

'''
f8x75_file_minus["Wellenvektor"] = -f8x75_file["Wellenvektor"]
f400_file_minus["Wellenvektor"] = -f400_file["Wellenvektor"]
f400_mit_file_minus["Wellenvektor"] = -f400_mit_file["Wellenvektor"]
f600_file_minus["Wellenvektor"] = -f600_file["Wellenvektor"]
f600_mit_file_minus["Wellenvektor"] = -f600_mit_file["Wellenvektor"]

#adding
f8x75_file["Wellenvektor"] = f8x75_file["Wellenvektor"].append(f8x75_file_minus["Wellenvektor"])
f400_file["Wellenvektor"] = f400_file_minus["Wellenvektor"].append(f400_file["Wellenvektor"])
f400_mit_file["Wellenvektor"] = f400_mit_file_minus["Wellenvektor"].append(f400_mit_file["Wellenvektor"])
f600_file["Wellenvektor"] = f600_file_minus["Wellenvektor"].append(f600_file["Wellenvektor"])
f600_mit_file["Wellenvektor"] = f600_mit_file_minus["Wellenvektor"].append(f600_mit_file["Wellenvektor"])
'''

#Reziproken Gittervektor abziehen
for i in range(0, 25):
    if f400_file["Wellenvektor"][i] > np.pi/0.053:            #pi/a = 8pi/L
        f400_file["Wellenvektor"][i] -= 2*np.pi/0.053
    if f400_file["Wellenvektor"][i] > np.pi/0.053:
        f400_file["Wellenvektor"][i] -= 2*np.pi/0.053
    if f400_file["Wellenvektor"][i] > np.pi/0.053:
        f400_file["Wellenvektor"][i] -= 2*np.pi/0.053

for i in range(0, 24):
    if f400_mit_file["Wellenvektor"][i] > np.pi/0.053:            #pi/a = 8pi/L
        f400_mit_file["Wellenvektor"][i] -= 2*np.pi/0.053
    if f400_mit_file["Wellenvektor"][i] > np.pi/0.053:
        f400_mit_file["Wellenvektor"][i] -= 2*np.pi/0.053
    if f400_mit_file["Wellenvektor"][i] > np.pi/0.053:
        f400_mit_file["Wellenvektor"][i] -= 2*np.pi/0.053

for i in range(0, 34):
    if f600_file["Wellenvektor"][i] > np.pi/0.053:            #pi/a = 8pi/L
        f600_file["Wellenvektor"][i] -= 2*np.pi/0.053
    if f600_file["Wellenvektor"][i] > np.pi/0.053:
        f600_file["Wellenvektor"][i] -= 2*np.pi/0.053
    if f600_file["Wellenvektor"][i] > np.pi/0.053:
        f600_file["Wellenvektor"][i] -= 2*np.pi/0.053
    if f600_file["Wellenvektor"][i] > np.pi/0.053:
        f600_file["Wellenvektor"][i] -= 2*np.pi/0.053

for i in range(0, 31):
    if f600_mit_file["Wellenvektor"][i] > np.pi/0.053:            #pi/a = 8pi/L
        f600_mit_file["Wellenvektor"][i] -= 2*np.pi/0.053
    if f600_mit_file["Wellenvektor"][i] > np.pi/0.053:
        f600_mit_file["Wellenvektor"][i] -= 2*np.pi/0.053
    if f600_mit_file["Wellenvektor"][i] > np.pi/0.053:
        f600_mit_file["Wellenvektor"][i] -= 2*np.pi/0.053
    if f600_mit_file["Wellenvektor"][i] > np.pi/0.053:
        f600_mit_file["Wellenvektor"][i] -= 2*np.pi/0.053

for i in range(0, 37):
    if f8x75_file["Wellenvektor"][i] > np.pi/0.078:            #pi/a = 8pi/L
        f8x75_file["Wellenvektor"][i] -= 2*np.pi/0.078
    if f8x75_file["Wellenvektor"][i] > np.pi/0.078:
        f8x75_file["Wellenvektor"][i] -= 2*np.pi/0.078
    if f8x75_file["Wellenvektor"][i] > np.pi/0.078:
        f8x75_file["Wellenvektor"][i] -= 2*np.pi/0.078



#4.6.1 Plot der Dispersion für L=400 und L=600 mit und ohne Irisblende
#L=400 ohne
plt.errorbar(f400_file["Wellenvektor"][0:25], f400_file["Frequenz"][0:25], linewidth = 2, fmt='x', color = "green")
plt.errorbar(-f400_file["Wellenvektor"][0:25], f400_file["Frequenz"][0:25], linewidth = 2, fmt='x', color = "green")
plt.title('Dispersionsrelation für L = 421 mm ohne Irisblende', fontsize = 15)
plt.xlabel('Wellenzahl  [$m^{-1}$]' , fontsize = 13)
plt.ylabel('Frequenz [Hz]', fontsize = 13)
plt.grid(True)
plt.xlim(-80, 80)
#plt.legend(['gemessene Resonanzen', "erwartete Werte für k durch $k = n\pi/L$ "], fontsize = 13)
plt.savefig('Plots/Dispersion_400_ohne.png', dpi=300)
plt.clf()

#L=400 mit
plt.errorbar(f400_mit_file["Wellenvektor"], f400_mit_file["Frequenz"], linewidth = 2, fmt='x', color = "green")
plt.errorbar(-f400_mit_file["Wellenvektor"], f400_mit_file["Frequenz"], linewidth = 2, fmt='x', color = "green")
plt.title('Dispersionsrelation  für L = 400 mm mit Irisblende', fontsize = 15)
plt.xlabel('Wellenzahl  [$m^{-1}$]' , fontsize = 13)
plt.ylabel('Frequenz [Hz]', fontsize = 13)
plt.grid(True)
plt.xlim(-80, 80)
#plt.legend(['gemessene Resonanzen', "erwartete Werte für k durch $k = n\pi/L$ "], fontsize = 13)
plt.savefig('Plots/Dispersion_400_mit.png', dpi=300)
plt.clf()

#L=600 ohne
plt.errorbar(f600_file["Wellenvektor"], f600_file["Frequenz"], linewidth = 2, fmt='x', color = "green")
plt.errorbar(-f600_file["Wellenvektor"], f600_file["Frequenz"], linewidth = 2, fmt='x', color = "green")
plt.title('Dispersionsrelation  für L = 600 mm ohne Irisblende', fontsize = 15)
plt.xlabel('Wellenzahl  [$m^{-1}$]' , fontsize = 13)
plt.ylabel('Frequenz [Hz]', fontsize = 13)
plt.grid(True)
plt.xlim(-80, 80)
#plt.legend(['gemessene Resonanzen', "erwartete Werte für k durch $k = n\pi/L$ "], fontsize = 13)
plt.savefig('Plots/Dispersion_600_ohne.png', dpi=300)
plt.clf()


#L=600 mit
plt.errorbar(f600_mit_file["Wellenvektor"], f600_mit_file["Frequenz"], linewidth = 2, fmt='x', color = "green")
plt.errorbar(-f600_mit_file["Wellenvektor"], f600_mit_file["Frequenz"], linewidth = 2, fmt='x', color = "green")
plt.title('Dispersionsrelation  für L = 600 mm mit Irisblende', fontsize = 15)
plt.xlabel('Wellenzahl  [$m^{-1}$]' , fontsize = 13)
plt.ylabel('Frequenz [Hz]', fontsize = 13)
plt.grid(True)
plt.xlim(-80, 80)
#plt.legend(['gemessene Resonanzen', "erwartete Werte für k durch $k = n\pi/L$ "], fontsize = 13)
plt.savefig('Plots/Dispersion_600_mit.png', dpi=300)
plt.clf()

#L=8x75 mit
plt.errorbar(f8x75_file["Wellenvektor"], f8x75_file["Frequenz"], linewidth = 2, fmt='x', color = "green")
plt.errorbar(-f8x75_file["Wellenvektor"], f8x75_file["Frequenz"], linewidth = 2, fmt='x', color = "green")
plt.title('Dispersionsrelation  für L = 8x75 mm mit Irisblende', fontsize = 15)
plt.xlabel('Wellenzahl  [$m^{-1}$]' , fontsize = 13)
plt.ylabel('Frequenz [Hz]', fontsize = 13)
plt.grid(True)
plt.xlim(-55, 55)
#plt.legend(['gemessene Resonanzen', "erwartete Werte für k durch $k = n\pi/L$ "], fontsize = 13)
plt.savefig('Plots/Dispersion_8x75_mit.png', dpi=300)
plt.clf()

#Bestimmung der Zustandsdichte 4.6.1
rho_file = pd.DataFrame()
rho_file["Delta Frequenz"] = f400_mit_file["Frequenz"]
for i in range(0, 23):
    rho_file["Delta Frequenz"][i] = f400_mit_file["Frequenz"][i + 1] - f400_mit_file["Frequenz"][i]

rho_file["Rho"] = 1/rho_file["Delta Frequenz"]


plt.errorbar(f400_mit_file["Frequenz"][0:23]*((2*np.pi)/343.421), rho_file["Rho"][0:23], linewidth = 2, fmt='x', color = "green")
plt.title('Zustandsdichte für L = 8x50mm mit Irisblende', fontsize = 15)
plt.xlabel('Wellenvektor [$m^{-1}$]' , fontsize = 13)
plt.ylabel("Zustandsdichte [-]", fontsize = 13)
plt.grid(True)
#plt.legend(['gemessene Resonanzen', "erwartete Werte für k durch $k = n\pi/L$ "], fontsize = 13)
plt.savefig('Plots/Zustandsdichte.png', dpi=300)
plt.clf()


#Aufgabe 4.6.3
#Aufgabe 4.6.3.1
f4631_ohne = pd.DataFrame()
f4631_stör = pd.DataFrame()
f4631_ohne["Frequenz"] = [250, 450, 675, 900, 1100, 1300, 1500, 1700, 1875, 2025, 2125, 3400, 3500, 3650, 3800, 3975, 4125, 4300, 4550, 4675, 6725, 6775, 6875, \
6975, 7100, 7225, 7350, 7475, 7575, 10075, 10150, 10225, 10325, 10450, 10550, 10650, 10750]
f4631_stör["Frequenz"] = [250, 475, 700, 925, 1150, 1300, 1600, 1800, 2000, 2175, 2300, 3400, 3525, 3675, 3850, 4025, 4100, 4475, 4625, \
4750, 4875, 6700, 6775, 6875, 7025, 7150, 7525, 7625, 7750, 7825, 10025, 10125, 10225, 10375, 10675, 10775, 10875]
f4631_ohne["Wellenvektor"] = f4631_ohne["Frequenz"] * 2*np.pi/343.421
f4631_stör["Wellenvektor"] = f4631_stör["Frequenz"] * 2*np.pi/343.421

#Abzug Reziproker Wellenvektor
for i in range(0, 37):
    if f4631_ohne["Wellenvektor"][i] > np.pi/0.053:            #pi/a
        f4631_ohne["Wellenvektor"][i] -= 2*np.pi/0.053
    if f4631_ohne["Wellenvektor"][i] > np.pi/0.053:
        f4631_ohne["Wellenvektor"][i] -= 2*np.pi/0.053
    if f4631_ohne["Wellenvektor"][i] > np.pi/0.053:
        f4631_ohne["Wellenvektor"][i] -= 2*np.pi/0.053
    if f4631_ohne["Wellenvektor"][i] > np.pi/0.053:
        f4631_ohne["Wellenvektor"][i] -= 2*np.pi/0.053
    if f4631_ohne["Wellenvektor"][i] > np.pi/0.053:
        f4631_ohne["Wellenvektor"][i] -= 2*np.pi/0.053


for i in range(0, 37):
    if f4631_stör["Wellenvektor"][i] > np.pi/0.053:
        f4631_stör["Wellenvektor"][i] -= 2*np.pi/0.053
    if f4631_stör["Wellenvektor"][i] > np.pi/0.053:
        f4631_stör["Wellenvektor"][i] -= 2*np.pi/0.053
    if f4631_stör["Wellenvektor"][i] > np.pi/0.053:
        f4631_stör["Wellenvektor"][i] -= 2*np.pi/0.053
    if f4631_stör["Wellenvektor"][i] > np.pi/0.053:
        f4631_stör["Wellenvektor"][i] -= 2*np.pi/0.053


#Plots Reudziertes Zonenschema
#Ohne Störung
plt.errorbar(f4631_ohne["Wellenvektor"], f4631_ohne["Frequenz"], linewidth = 2, fmt='x', color = "green")
plt.errorbar(-f4631_ohne["Wellenvektor"], f4631_ohne["Frequenz"], linewidth = 2, fmt='x', color = "green")
plt.title('Dispersionsrelation ohne Störung', fontsize = 15)
plt.xlabel('Wellenzahl  [$m^{-1}$]' , fontsize = 13)
plt.ylabel('Frequenz [Hz]', fontsize = 13)
plt.grid(True)
plt.xlim(-80, 80)
#plt.legend(['gemessene Resonanzen', "erwartete Werte für k durch $k = n\pi/L$ "], fontsize = 13)
plt.savefig('Plots/RZ_4631_ohne.png', dpi=300)
plt.clf()

#Mit Störung
plt.errorbar(f4631_stör["Wellenvektor"], f4631_stör["Frequenz"], linewidth = 2, fmt='x', color = "green")
plt.errorbar(-f4631_stör["Wellenvektor"], f4631_stör["Frequenz"], linewidth = 2, fmt='x', color = "green")
plt.title('Dispersionsrelation mit Störung', fontsize = 15)
plt.xlabel('Wellenzahl  [$m^{-1}$]' , fontsize = 13)
plt.ylabel('Frequenz [Hz]', fontsize = 13)
plt.grid(True)
plt.xlim(-80, 80)
#plt.legend(['gemessene Resonanzen', "erwartete Werte für k durch $k = n\pi/L$ "], fontsize = 13)
plt.savefig('Plots/RZ_4631_stör.png', dpi=300)
plt.clf()

#Aufgabe 4.6.3.1
#Hier fehlen die Daten

#Aufgabe 4.6.4 Defekte
#Aufgabe 4.6.4.1
f4641_ohne = pd.DataFrame()
f4641_stör = pd.DataFrame() #Störung an 6. Stelle
f4641_ohne["Frequenz"] = [275, 500, 725, 975, 1200, 1425,1675, 1900, 2100, 2300, 2450, 3400, 3550, 3725, 3950, 4150, 4350,\
4575, 4750, 4925, 5075, 6675, 6775, 6900, 7075, 7250, 7425, 7600, 7750, 7900, 9925, 10000, 10125, 10250, 10425, 10575,\
10725, 10875, 11000]
f4641_stör["Frequenz"] = [275, 475, 700, 925, 1175, 1375, 1600, 1825, 2025, 2275, 2375, 3425, 3675, 3800, 4050, 4225,\
4425, 4650, 4800, 5000, 6775, 6900, 7050, 7225, 7400, 7575, 7750, 7850, 8025, 9925, 10100, 10150, 10350, 10475, 10650,\
10800, 10900]
f4641_ohne["Wellenvektor"] = f4641_ohne["Frequenz"] * 2*np.pi/343.421
f4641_stör["Wellenvektor"] = f4641_stör["Frequenz"] * 2*np.pi/343.421

#Abzug Reziproker Wellenvektor
for i in range(0, 39):
    if f4641_ohne["Wellenvektor"][i] > np.pi/0.053:            #pi/a
        f4641_ohne["Wellenvektor"][i] -= 2*np.pi/0.053
    if f4641_ohne["Wellenvektor"][i] > np.pi/0.053:
        f4641_ohne["Wellenvektor"][i] -= 2*np.pi/0.053
    if f4641_ohne["Wellenvektor"][i] > np.pi/0.053:
        f4641_ohne["Wellenvektor"][i] -= 2*np.pi/0.053
    if f4641_ohne["Wellenvektor"][i] > np.pi/0.053:
        f4641_ohne["Wellenvektor"][i] -= 2*np.pi/0.053
    if f4641_ohne["Wellenvektor"][i] > np.pi/0.053:
        f4641_ohne["Wellenvektor"][i] -= 2*np.pi/0.053



for i in range(0, 37):
    if f4641_stör["Wellenvektor"][i] > np.pi/0.053:
        f4641_stör["Wellenvektor"][i] -= 2*np.pi/0.053
    if f4641_stör["Wellenvektor"][i] > np.pi/0.053:
        f4641_stör["Wellenvektor"][i] -= 2*np.pi/0.053
    if f4641_stör["Wellenvektor"][i] > np.pi/0.053:
        f4641_stör["Wellenvektor"][i] -= 2*np.pi/0.053
    if f4641_stör["Wellenvektor"][i] > np.pi/0.053:
        f4641_stör["Wellenvektor"][i] -= 2*np.pi/0.053


#Plots Reudziertes Zonenschema
#Ohne Störung
plt.errorbar(f4641_ohne["Wellenvektor"], f4641_ohne["Frequenz"], linewidth = 2, fmt='x', color = "green")
plt.errorbar(-f4641_ohne["Wellenvektor"], f4641_ohne["Frequenz"], linewidth = 2, fmt='x', color = "green")
plt.title('Dispersionsrelation ohne Störung', fontsize = 15)
plt.xlabel('Wellenzahl  [$m^{-1}$]' , fontsize = 13)
plt.ylabel('Frequenz [Hz]', fontsize = 13)
plt.grid(True)
plt.xlim(-80, 80)
#plt.legend(['gemessene Resonanzen', "erwartete Werte für k durch $k = n\pi/L$ "], fontsize = 13)
plt.savefig('Plots/RZ_4641_ohne.png', dpi=300)
plt.clf()

#Mit Störung
plt.errorbar(f4641_stör["Wellenvektor"], f4641_stör["Frequenz"], linewidth = 2, fmt='x', color = "green")
plt.errorbar(-f4641_stör["Wellenvektor"], f4641_stör["Frequenz"], linewidth = 2, fmt='x', color = "green")
plt.title('Dispersionsrelation mit Störung', fontsize = 15)
plt.xlabel('Wellenzahl  [$m^{-1}$]' , fontsize = 13)
plt.ylabel('Frequenz [Hz]', fontsize = 13)
plt.grid(True)
plt.xlim(-80, 80)
#plt.legend(['gemessene Resonanzen', "erwartete Werte für k durch $k = n\pi/L$ "], fontsize = 13)
plt.savefig('Plots/RZ_4641_stör.png', dpi=300)
plt.clf()
