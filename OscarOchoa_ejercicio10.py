import urllib
from io import StringIO
from io import BytesIO
import csv
import numpy as np
from datetime import datetime
import matplotlib.pylab as plt
import pandas as pd
import scipy.signal as signal

Inicio = '20080201'
Final   = '20080201'
datos9=pd.read_csv('https://hub.mybinder.org/user/computociencias-fisi2029-201910-cwhww83w/edit/Seccion_1/Fourier/Datos/transacciones2009.txt',sep="\t")
datos["date [AST]"]=pd.to_datetime(datos["date [AST]"],format='%Y%m%d %H:%M:%S')
datos.set_index(["date [AST]"],inplace=True)

datos8=pd.read_csv('https://hub.mybinder.org/user/computociencias-fisi2029-201910-cwhww83w/edit/Seccion_1/Fourier/Datos/transacciones2008.txt',sep="\t")
datos["date [AST]"]=pd.to_datetime(datos["date [AST]"],format='%Y%m%d %H:%M:%S')
datos.set_index(["date [AST]"],inplace=True)

datos10=pd.read_csv('https://hub.mybinder.org/user/computociencias-fisi2029-201910-cwhww83w/edit/Seccion_1/Fourier/Datos/transacciones2010.txt',sep="\t")
datos["date [AST]"]=pd.to_datetime(datos["date [AST]"],format='%Y%m%d %H:%M:%S')
datos.set_index(["date [AST]"],inplace=True)
