# estimation of PM2.5 mass concentration using the re-analysis data over the Indian subcontinent.

import netCDF4 as nc
import numpy as np
from os import listdir as l
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import warnings
warnings.filterwarnings('ignore')


j=0
MAH = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG','SEP','OCT','NOV','DEC']  # month list
content = ['time', 'lon', 'lat', 'BCSMASS', 'DUSMASS25', 'OCSMASS', 'SO4SMASS', 'SSSMASS25']   # ds.variables.keys()

h0=[]
h1=[]
h2=[]
h3=[]
h4=[]
h5=[]
h6=[]
h7=[]
h8=[]
h9=[]
h10=[]
h11=[]
h12=[]
h13=[]
h14=[]
h15=[]
h16=[]
h17=[]
h18=[]
h19=[]
h20=[]
h21=[]
h22=[]
h23=[]



for i in range(1,13):   
    year = "2020"
    if i<10 :
          month = "0"+str(i)
    else:
          month = str(i)
    

    # fn = f"data/MERRA2_400.tavg1_2d_aer_Nx.{year}{month}{date}.SUB.nc" formate of file
    
    if i in (6,7,8,9):
          files = ["NOV/"+x for x in l("NOV/") if f"MERRA2_401.tavg1_2d_aer_Nx.{year}{month}" in x] # PM2.5 DATA FILES
    else:
          files = ["NOV/"+x for x in l("NOV/") if f"MERRA2_400.tavg1_2d_aer_Nx.{year}{month}" in x]  # PM2.5 DATA FILES

          

    #PM2.5 CALCULATION
    for file in files:
        #EXTRACTING  DATA
        ds = nc.Dataset(file)
        SO4 = np.array(ds["SO4SMASS"][:])
        OC = np.array(ds["OCSMASS"][:])
        BC = np.array(ds["BCSMASS"][:])
        Dust25 = np.array(ds["DUSMASS25"][:])
        SS25 = np.array(ds["SSSMASS25"][:])
        lats = ds.variables['lat'][:]
        lons = ds.variables['lon'][:]

        PM25 = 1.375*SO4 + 1.6*OC + BC + Dust25 + SS25#CALCULATION FOR PM2.5
        #PM25 = np.mean(PM25, axis=0)
        PM25 = PM25*(10**9)
        lats = ds.variables['lat'][:]
        lons = ds.variables['lon'][:]
        time = ds.variables['time'][:]
        #EXTRACTING EACH HOUR DATA THERE IS TOTAL 24 HOUR AND APPENDING ALL DATA TO THE THERE RESPECTIVLY LIST 
        for i in PM25:
              j=j+1
              if j==1:
                    h0.append(i)
              elif j==2:
                    h1.append(i)
              elif j==3:
                    h2.append(i)
              elif j==4:
                    h3.append(i)
              elif j==5:
                    h4.append(i)
              elif j==6:
                    h5.append(i)
              elif j==7:
                    h6.append(i)
              elif j==8:
                    h7.append(i)
              elif j==9:
                    h8.append(i)
              elif j==10:
                    h9.append(i)
              elif j==11:
                    h10.append(i)
              elif j==12:
                    h11.append(i)
              elif j==13:
                    h12.append(i)
              elif j==14:
                    h13.append(i)
              elif j==15:
                    h14.append(i)
              elif j==16:
                    h15.append(i)
              elif j==17:
                    h16.append(i)
              elif j==18:
                    h17.append(i)
              elif j==19:
                    h18.append(i)
              elif j==20:
                    h19.append(i)
              elif j==21:
                    h20.append(i)
              elif j==22:
                    h21.append(i)
              elif j==23:
                    h22.append(i)
              else:
                    h23.append(i)
        j=0

h=[h0,h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13,h14,h15,h16,h17,h18,h19,h20,h21,h22,h23]

o=1
for i in h:
      m=np.array(i)
      m=np.mean(m, axis=0)
      mp = Basemap(projection = 'merc',llcrnrlon = 60,llcrnrlat = 0,urcrnrlon = 100,urcrnrlat = 40,resolution = 'i')

      lon, lat = np.meshgrid(lons, lats)#MAKING LAT LON INTO 2D
      x,y = mp(lon, lat)

          
      cmap = mpl.cm.rainbow
      norm = mpl.colors.Normalize(vmin=0, vmax=100)#COLOR PLOTTING
      c_scheme = mp.contourf(x, y, np.squeeze(m),extend='max',cmap= cmap,norm=norm,levels=np.arange(0,100))#PLOTTING DATA
      mp.drawcoastlines()
      mp.drawstates()
      mp.drawcountries()
      mp.drawparallels (np.arange(0,50,10), labels=[True, False, False, False],linewidth=0.0)
      mp.drawmeridians (np.arange(60,110,10), labels=[0,0,0,1],linewidth=0.0)



      #COLORBAR AND TITLE
      cbar = mp.colorbar(c_scheme, location = 'right', pad = '10%')
      cbar.set_label('PM2.5(\u03BCg per meter cube)',loc='center',rotation = 90)
      plt.title('DIURNAL AVERAGE PM2.5: MONTH ' +str(o)+ '-hour ---NOV2020' )
      plt.show()
      o=o+1
      #plt.savefig(r'C:\Users\tryri\Desktop\cook'+'\\'+ 'R'+str(i)+'.png')
             
