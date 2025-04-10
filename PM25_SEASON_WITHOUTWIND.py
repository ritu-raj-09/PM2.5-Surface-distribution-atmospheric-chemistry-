# estimation of PM2.5 mass concentration using the re-analysis data over the Indian subcontinent.

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
for i in range(1,13):
    if i<10 :
          month = "0"+str(i)
    else:
          month = str(i)
    

    # fn = f"data/MERRA2_400.tavg1_2d_aer_Nx.{year}{month}{date}.SUB.nc" formate of file
    
    for year in range(2011,2020):
        if i in(1,2,12):
            f1 = ["season/"+x for x in l("season/") if f"MERRA2_400.tavg1_2d_aer_Nx.{year}{month}" in x] # PM2.5 DATA FILES
            winter=winter+f1
        elif i in (3,4,5):
            f2 = ["season/"+x for x in l("season/") if f"MERRA2_400.tavg1_2d_aer_Nx.{year}{month}" in x]
            spring=spring+f2
        elif i in (6,7,8):
            f3 = ["season/"+x for x in l("season/") if f"MERRA2_400.tavg1_2d_aer_Nx.{year}{month}" in x]
            summer=summer+f3
        else:
            f4 = ["season/"+x for x in l("season/") if f"MERRA2_400.tavg1_2d_aer_Nx.{year}{month}" in x]
            autumn=autumn+f4

dayAvgs = []
for file in autumn:
    ds = nc.Dataset(file)
    SO4 = np.array(ds["SO4SMASS"][:])
    OC = np.array(ds["OCSMASS"][:])
    BC = np.array(ds["BCSMASS"][:])
    Dust25 = np.array(ds["DUSMASS25"][:])
    SS25 = np.array(ds["SSSMASS25"][:])
    PM25 = 1.375*SO4 + 1.6*OC + BC + Dust25 + SS25#CALCULATION FOR PM2.5
    dayAvgs.append(np.mean(PM25, axis=0))

dayAvgs = np.array(dayAvgs)
moAvgs = np.mean(dayAvgs,axis=0)
moAvgs = moAvgs*(10**9)
#print(moAvgs)


#MAP FORMATION AND PLOTING
    
lats = ds.variables['lat'][:]
lons = ds.variables['lon'][:]
time = ds.variables['time'][:]

mp = Basemap(projection = 'merc',llcrnrlon = 61,llcrnrlat = 0,urcrnrlon = 100,urcrnrlat = 40,resolution = 'i')

lon, lat = np.meshgrid(lons, lats)
x,y = mp(lon, lat)
    
    
cmap = mpl.cm.rainbow
norm = mpl.colors.Normalize(vmin=0, vmax=100)
c_scheme = mp.contourf(x, y, np.squeeze(moAvgs),extend='max',cmap= cmap,norm=norm,levels=np.arange(0,100))#PLOTTING DATA
mp.drawcoastlines()
mp.drawstates()
mp.drawcountries()
mp.drawparallels (np.arange(0,40,5), labels=[True, False, False, False],linewidth=0.0)
mp.drawmeridians (np.arange(60,100,5), labels=[0,0,0,1],linewidth=0.0)



#COLORBAR AND TITLE
cbar = mp.colorbar(c_scheme, location = 'right', pad = '10%')
cbar.set_label('PM2.5(\u03BCg per meter cube)',loc='center',rotation = 90)
plt.title('PM2.5 AVERAGE Autumn(2011-2020)' )
plt.show()
    #plt.savefig(r'C:\Users\tryri\Desktop\cook'+'\\'+ 'R'+str(i)+'.png')


            

        
