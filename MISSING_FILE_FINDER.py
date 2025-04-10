import netCDF4 as nc
import numpy as np
from os import listdir as l
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import warnings
warnings.filterwarnings('ignore')



MAH = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG','SEP','OCT','NOV','DEC']  # month list
content = ['time', 'lon', 'lat', 'BCSMASS', 'DUSMASS25', 'OCSMASS', 'SO4SMASS', 'SSSMASS25']   # ds.variables.keys()

winter=[]
spring=[]
summer=[]
autumn=[]
for i in range(10,13):
      autumn=[]
      winter=[]

      if i<10 :
            month = "0"+str(i)
      else:
            month = str(i)

      if i in (1,3,5,7,8,10,12):
            b = 32
      elif i == 2:
            b = 30
      else:
            b = 31
      
      for h in range(1,b):
            autumn.append(h)

      f1 = ["wind/"+x for x in l("wind/") if f"MERRA2_400.tavg1_2d_slv_Nx.2020{month}" in x] # PM2.5 DATA FILES
      winter=winter+f1
      for p in winter:
            k = int(p[-9:-7])
            autumn.remove(k)
      print(MAH[i-1],autumn)
