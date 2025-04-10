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


for i in range(1,13):
    year = "2021"
    if i<10 :
          month = "0"+str(i)
    else:
          month = str(i)
    

    # fn = f"data/MERRA2_400.tavg1_2d_aer_Nx.{year}{month}{date}.SUB.nc" formate of file
    
    if i in (6,7,8,9):
          files = ["data/"+x for x in l("data/") if f"MERRA2_401.tavg1_2d_aer_Nx.{year}{month}" in x] # PM2.5 DATA FILES
    else:
          files = ["data/"+x for x in l("data/") if f"MERRA2_400.tavg1_2d_aer_Nx.{year}{month}" in x]  # PM2.5 DATA FILES

          

    #parameter plotting
          
    day = []
    
    for file in files:
        ds = nc.Dataset(file)
        SO4 = np.array(ds["SO4SMASS"][:])
        OC = np.array(ds["OCSMASS"][:])
        BC = np.array(ds["BCSMASS"][:])
        Dust25 = np.array(ds["DUSMASS25"][:])
        SS25 = np.array(ds["SSSMASS25"][:])
        day.append(np.mean(SO4, axis=0))

    day = np.array(day)
    S = np.mean(day,axis=0)
    S = S*(10**9)


    #MAP FORMATION AND PLOTING
    
    lats = ds.variables['lat'][:]
    lons = ds.variables['lon'][:]
    time = ds.variables['time'][:]

    mp = Basemap(projection = 'merc',
                 llcrnrlon = 60,
                 llcrnrlat = 0,
                 urcrnrlon = 100,
                 urcrnrlat = 40,
                 resolution = 'i')

    lon, lat = np.meshgrid(lons, lats)
    x,y = mp(lon, lat)
    
    
    cmap = mpl.cm.rainbow
    norm = mpl.colors.Normalize(vmin=0, vmax=20)
    c_scheme = mp.contourf(x, y, np.squeeze(S),extend='max',cmap= cmap,norm=norm,levels=np.arange(0,20))#PLOTTING DATA
    mp.drawcoastlines()
    mp.drawstates()
    mp.drawcountries()
    mp.drawparallels (np.arange(0,40,5), labels=[True, False, False, False],linewidth=0.0)
    mp.drawmeridians (np.arange(60,100,5), labels=[0,0,0,1],linewidth=0.0)



    #COLORBAR AND TITLE
    cbar = mp.colorbar(c_scheme, location = 'right', pad = '10%')
    cbar.set_label('PM2.5(\u03BCg per meter cube)',loc='center',rotation = 90)
    plt.title('AVERAGE sulphate: MONTH ' + MAH[i-1]+ '-2021' )
    plt.show()
    #plt.savefig(r'C:\Users\tryri\Desktop\cook'+'\\'+ 'R'+str(i)+'.png')
