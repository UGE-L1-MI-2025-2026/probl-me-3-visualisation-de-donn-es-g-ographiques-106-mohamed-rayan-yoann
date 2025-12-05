import math
from fltk import *
import shapefile

LARGEUR = 700
HAUTEUR = 600
cree_fenetre(LARGEUR, HAUTEUR)

codes_outre_mer = ["971", "972", "973", "974", "976"]

sf = shapefile.Reader("departements/departements-20180101")

def wgs_mercator(coord = tuple):
    lon, lat = coord
    R = 2300
    x = R * math.radians(lon)
    y = R * math.log(math.tan(math.pi/4 + math.radians(lat)/2))
    y_max = R * math.log(math.tan(math.pi/4 + 44))
    x = x - sf.bbox[0]
    y = y_max - y
    return x, y

#departement = [sf.shape(i) for i in range(len(sf.records()))]

#liste_wgs_mercator = list(map(wgs_mercator_point, departement))
essonne = sf.shape(8)
liste_mercator_essonne = list(map(wgs_mercator, (coord for coord in essonne.points)))

"""for i in range(len(sf.records())):
    record = sf.record(i)
    code_dept = record[0]

    if code_dept not in codes_outre_mer:
        print(code_dept)
        departement = sf.shape(i)
        liste_mercator_dept = list(map(wgs_mercator, (coord for coord in departement.points)))
        polygone(liste_mercator_dept, tag = "departement"+str(i))
        deplace("departement" + str(i),300, 2325)"""

for i in range(len(sf.records())):
    record = sf.record(i)
    code_dept = record[0]

    if code_dept not in codes_outre_mer:
        departement = sf.shape(i)
        liste_mercator_dept = list(map(wgs_mercator, (coord for coord in departement.points)))
        liste_parts = departement.parts

        #declaration liste modifie
        liste_modifie = []
        for e in liste_parts:
            liste_modifie.append(e)
        liste_modifie.append(len(liste_mercator_dept))


        for k in range(len(liste_modifie)-1):
            debut = liste_modifie[k]
            print("debut : ", debut)
            fin = liste_modifie[k+1]
            print("fin : ", fin)
            print("longueur liste :", len(liste_modifie))
            #polygone(liste_mercator_dept[debut:fin], tag = "departement"+str(i))
            #deplace("departement" + str(i),300, 2325)
            polygone(liste_mercator_dept[debut:fin], tag = "departement{}_{}".format(i, k))
            deplace("departement{}_{}".format(i, k), 200, 2325)

    
                



attend_ev()


ferme_fenetre()