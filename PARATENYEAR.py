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

jan = []
wjan = []

feb = []
wfeb = []

mar = []
wmar = []

apr = []
wapr = []

may = []
wmay = []

jun = []
wjun = []

jul = []
wjul = []

aug = []
waug = []

sep = []
wsep = []

octo = []
wocto = []

nov = []
wnov = []

dec = []
wdec = []


for i in range(1,13):
    if i<10 :
          month = "0"+str(i)
    else:
          month = str(i)
    

    # fn = f"data/MERRA2_400.tavg1_2d_aer_Nx.{year}{month}{date}.SUB.nc" formate of file
    
    for year in range(2011,2021):
        if i == 1:
              f1 = ["season/"+x for x in l("season/") if f"MERRA2_400.tavg1_2d_aer_Nx.{year}{month}" in x] # PM2.5 DATA FILES
              w1 = ["wind/"+x for x in l("wind/") if f"MERRA2_400.tavg1_2d_slv_Nx.{year}{month}" in x]#WIND DATA FILE FOR RESPECTIVELY MONTH
              jan=jan+f1
              wjan=wjan+w1
        elif i == 2:
              f2 = ["season/"+x for x in l("season/") if f"MERRA2_400.tavg1_2d_aer_Nx.{year}{month}" in x]
              w2 = ["wind/"+x for x in l("wind/") if f"MERRA2_400.tavg1_2d_slv_Nx.{year}{month}" in x]
              feb=feb+f2
              wfeb=wfeb+w2
        elif i == 3:
              f3 = ["season/"+x for x in l("season/") if f"MERRA2_400.tavg1_2d_aer_Nx.{year}{month}" in x]
              w3 = ["wind/"+x for x in l("wind/") if f"MERRA2_400.tavg1_2d_slv_Nx.{year}{month}" in x]
              mar=mar+f3
              wmar=wmar+w3
        elif i == 4:
              f4 = ["season/"+x for x in l("season/") if f"MERRA2_400.tavg1_2d_aer_Nx.{year}{month}" in x]
              w4 = ["wind/"+x for x in l("wind/") if f"MERRA2_400.tavg1_2d_slv_Nx.{year}{month}" in x]
              apr=apr+f4
              wapr=wapr+w4
        elif i == 5:
              f5 = ["season/"+x for x in l("season/") if f"MERRA2_400.tavg1_2d_aer_Nx.{year}{month}" in x]
              w5 = ["wind/"+x for x in l("wind/") if f"MERRA2_400.tavg1_2d_slv_Nx.{year}{month}" in x]
              may=may+f5
              wmay=wmay+w5
        elif i == 6:
              f6 = ["season/"+x for x in l("season/") if f"MERRA2_400.tavg1_2d_aer_Nx.{year}{month}" in x]
              w6 = ["wind/"+x for x in l("wind/") if f"MERRA2_400.tavg1_2d_slv_Nx.{year}{month}" in x]
              jun=jun+f6
              wjun=wjun+w6

        elif i == 7:
              f7 = ["season/"+x for x in l("season/") if f"MERRA2_400.tavg1_2d_aer_Nx.{year}{month}" in x]
              w7 = ["wind/"+x for x in l("wind/") if f"MERRA2_400.tavg1_2d_slv_Nx.{year}{month}" in x]
              jul=jul+f7
              wjul=wjul+w7
        elif i == 8:
              f8 = ["season/"+x for x in l("season/") if f"MERRA2_400.tavg1_2d_aer_Nx.{year}{month}" in x]
              w8 = ["wind/"+x for x in l("wind/") if f"MERRA2_400.tavg1_2d_slv_Nx.{year}{month}" in x]
              aug=aug+f8
              waug=waug+w8

        elif i == 9:
              f9 = ["season/"+x for x in l("season/") if f"MERRA2_400.tavg1_2d_aer_Nx.{year}{month}" in x]
              w9 = ["wind/"+x for x in l("wind/") if f"MERRA2_400.tavg1_2d_slv_Nx.{year}{month}" in x]
              sep=sep+f9
              wsep=wsep+w9

        elif i == 10:
              f10 = ["season/"+x for x in l("season/") if f"MERRA2_400.tavg1_2d_aer_Nx.{year}{month}" in x]
              w10 = ["wind/"+x for x in l("wind/") if f"MERRA2_400.tavg1_2d_slv_Nx.{year}{month}" in x]
              octo=octo+f10
              wocto=wocto+w10

        elif i == 11:
              f11 = ["season/"+x for x in l("season/") if f"MERRA2_400.tavg1_2d_aer_Nx.{year}{month}" in x]
              w11 = ["wind/"+x for x in l("wind/") if f"MERRA2_400.tavg1_2d_slv_Nx.{year}{month}" in x]
              nov=nov+f11
              wnov=wnov+w11
        else:
              f12 = ["season/"+x for x in l("season/") if f"MERRA2_400.tavg1_2d_aer_Nx.{year}{month}" in x]
              w12 = ["wind/"+x for x in l("wind/") if f"MERRA2_400.tavg1_2d_slv_Nx.{year}{month}" in x]
              dec=dec+f12
              wdec=wdec+w12




m = [jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec]
a = [wjan, wfeb, wmar, wapr, wmay, wjun, wjul, waug, wsep, wocto, wnov, wdec]


#FOR DIFFERENT PARAMETER...JUST CHANGE PARAMETER

for i in range(0,12):
      dayAvgs = []
      for file in m[i]:
          ds = nc.Dataset(file)
          #SO4 = np.array(ds["SO4SMASS"][:])
          #OC = np.array(ds["OCSMASS"][:])
          #BC = np.array(ds["BCSMASS"][:])
          #Dust25 = np.array(ds["DUSMASS25"][:])
          SS25 = np.array(ds["SSSMASS25"][:])
          dayAvgs.append(np.mean(SS25, axis=0))#NEED TO CHANGE EVERY TIME FOR DIFFRENT PARAMETER( WHEN PLOT DIFFRENT PARAMETER)

      dayAvgs = np.array(dayAvgs)
      moAvgs = np.mean(dayAvgs,axis=0)
      moAvgs = moAvgs*(10**9)
      #print(moAvgs)

#WIND EXTRACTION
      wU500 = []
      wV500 = []
      for file in a[i]:
            dwws = nc.Dataset(file)
            U500 = np.array(dwws["U500"][:])
            V500 = np.array(dwws["V500"][:])
            wU500.append(np.mean(U500, axis=0))
            wV500.append(np.mean(V500, axis=0))

      wU500 = np.array(wU500)
      wV500 = np.array(wV500)

      mwU500 = np.mean(wU500, axis=0)
      mwV500 = np.mean(wV500, axis=0)





      #MAP FORMATION AND PLOTING
          
      lats = ds.variables['lat'][:]
      lons = ds.variables['lon'][:]
      time = ds.variables['time'][:]

      mp = Basemap(projection = 'merc',llcrnrlon = 61,llcrnrlat = 0,urcrnrlon = 100,urcrnrlat = 40,resolution = 'i')

      lon, lat = np.meshgrid(lons, lats)#1D TO 2D CONVERSION OF LON AND LAT
      x,y = mp(lon, lat)

          
          
      cmap = mpl.cm.rainbow
      norm = mpl.colors.Normalize(vmin=0, vmax=20)
      c_scheme = mp.contourf(x, y, np.squeeze(moAvgs),extend='max',cmap= cmap,norm=norm,levels=np.arange(0,20))#PLOTTING DATA
      mp.drawcoastlines()
      mp.drawstates()
      mp.drawcountries()
      mp.drawparallels (np.arange(0,40,5), labels=[True, False, False, False],linewidth=0.0)
      mp.drawmeridians (np.arange(60,100,5), labels=[0,0,0,1],linewidth=0.0)

#wind plotting
      yy = np.arange(0, y.shape[0],2)
      xx = np.arange(0, x.shape[1],2)
      points = np.meshgrid(yy, xx)
      q = plt.quiver(x[points], y[points], mwU500[points], mwV500[points])
      plt.quiverkey(q, X=0.3, Y=1.1, U=10,label='10m/s', labelpos='E')



      #COLORBAR AND TITLE

      bounds = np.arange(0, 20,5)
      cbar = mp.colorbar(c_scheme, location = 'right', pad = '10%',ticks=bounds)
      cbar.set_label('SeaSalt2.5 (\u03BCg/m\u00b3)',loc='center',rotation = 90)
      plt.title('SeaSalt2.5 AVERAGE: '+ MAH[i] +' (2011-2020)' )
      #plt.show()
      plt.savefig(r'C:\Users\tryri\Desktop\climaticmean\\'+str(i)+'.png')


            

        
