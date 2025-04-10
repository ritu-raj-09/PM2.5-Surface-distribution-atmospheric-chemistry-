# estimation of PM2.5 mass concentration using the re-analysis data over the Indian subcontinent.
# WITH WIND VECTOR


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
          files = ["newdata/"+x for x in l("newdata/") if f"MERRA2_401.tavg1_2d_aer_Nx.{year}{month}" in x] # PM2.5 DATA FILES
          dws = ["metadata/"+x for x in l("metadata/") if f"MERRA2_401.tavg1_2d_slv_Nx.{year}{month}" in x] # WIND DATA FILES
    else:
          files = ["newdata/"+x for x in l("newdata/") if f"MERRA2_400.tavg1_2d_aer_Nx.{year}{month}" in x]  # PM2.5 DATA FILES
          dws = ["metadata/"+x for x in l("metadata/") if f"MERRA2_400.tavg1_2d_slv_Nx.{year}{month}" in x]  # WIND DATA FILES
          

    #PM2.5 CALCULATION
          
    dayAvgs = []
    for file in files:
        ds = nc.Dataset(file)
        SO4 = np.array(ds["SO4SMASS"][:])
        OC = np.array(ds["OCSMASS"][:])
        BC = np.array(ds["BCSMASS"][:])
        Dust25 = np.array(ds["DUSMASS25"][:])
        SS25 = np.array(ds["SSSMASS25"][:])
        PM25 = 1.375*SO4 + 1.6*OC + BC + Dust25 + SS25#CALCULATION FOR PM2.5
        dayAvgs.append(np.mean(PM25, axis=0))#DAYAVERAGE

    dayAvgs = np.array(dayAvgs)
    moAvgs = np.mean(dayAvgs,axis=0)#MONTHLY AVERGAGE
    moAvgs = moAvgs*(10**9)


    #EXTRACTING WIND DATA
    
    wU500 = []
    wV500 = []
    for file in dws:
        dwws = nc.Dataset(file)
 
        U500 = np.array(dwws["U500"][:])
        V500 = np.array(dwws["V500"][:]) #U850 = np.array(dwws["U850"][:])#V850 = np.array(dwws["V850"][:])#U250 = np.array(dwws["U250"][:])#V250 = np.array(dwws["V250"][:])

        wU500.append(np.mean(U500, axis=0))
        wV500.append(np.mean(V500, axis=0))#wU850.append(np.mean(U850, axis=0))#wV850.append(np.mean(V850, axis=0))#wU250.append(np.mean(U250, axis=0))#wV250.append(np.mean(V250, axis=0))



    wU500 = np.array(wU500)
    wV500 = np.array(wV500)#wU850 = np.array(wU850)#wV850 = np.array(wV850)#wU250 = np.array(wU250)#wV250 = np.array(wV250)
    

    mwU500 = np.mean(wU500, axis=0)
    mwV500 = np.mean(wV500, axis=0)#mwU850 = np.mean(wU850, axis=0)#mwV850 = np.mean(wV850, axis=0)#mwU250 = np.mean(wU250, axis=0)#mwV250 = np.mean(wV250, axis=0)



    #MAP FORMATION AND PLOTING
    
    lats = ds.variables['lat'][:]
    lons = ds.variables['lon'][:]
    time = ds.variables['time'][:]

    mp = Basemap(projection = 'merc',
                 llcrnrlon = 61,
                 llcrnrlat = 0,
                 urcrnrlon = 100,
                 urcrnrlat = 40,
                 resolution = 'i')

    lon, lat = np.meshgrid(lons, lats)
    x,y = mp(lon, lat)
    
    
    cmap = mpl.cm.rainbow
    norm = mpl.colors.Normalize(vmin=0, vmax=150)
    c_scheme = mp.contourf(x, y, np.squeeze(moAvgs),extend='max',cmap= cmap,norm=norm,levels=np.arange(0,150))#PLOTTING DATA
    mp.drawcoastlines()
    mp.drawstates()
    mp.drawcountries()
    mp.drawparallels (np.arange(0,40,5), labels=[True, False, False, False],linewidth=0.0)
    mp.drawmeridians (np.arange(60,100,5), labels=[0,0,0,1],linewidth=0.0)

    #WIND DATA PLOTTING
    yy = np.arange(0, y.shape[0],2)
    xx = np.arange(0, x.shape[1],2)
    points = np.meshgrid(yy, xx)
    q = plt.quiver(x[points], y[points], mwU500[points], mwV500[points])
    plt.quiverkey(q, X=0.3, Y=1.1, U=10,label='10m/s', labelpos='E')


    #COLORBAR AND TITLE
    bounds = np.arange(0, 160,20)
    cbar = mp.colorbar(c_scheme,location = 'right', pad = '10%',ticks=bounds)
    cbar.set_label('PM2.5 (\u03BCg/m\u00b3)',loc='center',rotation = 90)
    plt.title('AVERAGE PM2.5: ' + MAH[i-1]+ '-2021')
    #plt.show()
    plt.savefig(r'C:\Users\tryri\Desktop\surfacpm2.5_2021\\'+ str(i)+'.png')
