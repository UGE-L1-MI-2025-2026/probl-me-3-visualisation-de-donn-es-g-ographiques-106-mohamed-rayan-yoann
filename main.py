import math
from fltk import *
import shapefile

LARGEUR = 800
HAUTEUR = 700

sf = shapefile.Reader("departements/departements-20180101")
print((len(sf.records())))

def 

