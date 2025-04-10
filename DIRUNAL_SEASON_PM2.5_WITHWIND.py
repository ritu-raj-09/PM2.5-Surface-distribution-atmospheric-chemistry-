# estimation of PM2.5 mass concentration using the re-analysis data over the Indian subcontinent.

import netCDF4 as nc
import numpy as np
from os import listdir as l
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import warnings
warnings.filterwarnings('ignore')

k=0
j=0
MAH = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG','SEP','OCT','NOV','DEC']  # month list
content = ['time', 'lon', 'lat', 'BCSMASS', 'DUSMASS25', 'OCSMASS', 'SO4SMASS', 'SSSMASS25']   # ds.variables.keys()

#MAKING LIST FOR PER HOUR DATA FOR WIND AND ALL 
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

w0=[]
w01=[]
w02=[]
w03=[]
w04=[]
w5=[]
w6=[]
w6=[]
w7=[]
w8=[]
w9=[]
w10=[]
w11=[]
w12=[]
w13=[]
w14=[]
w15=[]
w16=[]
w17=[]
w18=[]
w19=[]
w20=[]
w21=[]
w22=[]
w23=[]

uw0=[]
uw1=[]
uw2=[]
uw3=[]
uw4=[]
uw5=[]
uw6=[]
uw6=[]
uw7=[]
uw8=[]
uw9=[]
uw10=[]
uw11=[]
uw12=[]
uw13=[]
uw14=[]
uw15=[]
uw16=[]
uw17=[]
uw18=[]
uw19=[]
uw20=[]
uw21=[]
uw22=[]
uw23=[]


winter = []
wwinter = []

spring = []
wspring = []

summer = []
wsummer = []

autumn = []
wautumn = []



for i in range(1,13):   
    if i<10 :
          month = "0"+str(i)
    else:
          month = str(i)
    

    # fn = f"data/MERRA2_400.tavg1_2d_aer_Nx.{year}{month}{date}.SUB.nc" formate of file
    for year in range(2011,2021):
        if i in(1,2,12):
            f1 = ["season/"+x for x in l("season/") if f"MERRA2_400.tavg1_2d_aer_Nx.{year}{month}" in x] # PM2.5 DATA FILES
            w1 = ["wind/"+x for x in l("wind/") if f"MERRA2_400.tavg1_2d_slv_Nx.{year}{month}" in x]# WIND DATA FILE
            winter=winter+f1
            wwinter=wwinter+w1
        elif i in (3,4,5):
            f2 = ["season/"+x for x in l("season/") if f"MERRA2_400.tavg1_2d_aer_Nx.{year}{month}" in x]# PM2.5 DATA FILES
            w2 = ["wind/"+x for x in l("wind/") if f"MERRA2_400.tavg1_2d_slv_Nx.{year}{month}" in x]# WIND DATA FILE
            spring=spring+f2
            wspring=wspring+w2
        elif i in (6,7,8):
            f3 = ["season/"+x for x in l("season/") if f"MERRA2_400.tavg1_2d_aer_Nx.{year}{month}" in x]# PM2.5 DATA FILES
            w3 = ["wind/"+x for x in l("wind/") if f"MERRA2_400.tavg1_2d_slv_Nx.{year}{month}" in x]# WIND DATA FILE
            summer=summer+f3
            wsummer=wsummer+w3
        else:
            f4 = ["season/"+x for x in l("season/") if f"MERRA2_400.tavg1_2d_aer_Nx.{year}{month}" in x]# PM2.5 DATA FILES
            w4 = ["wind/"+x for x in l("wind/") if f"MERRA2_400.tavg1_2d_slv_Nx.{year}{month}" in x]# WIND DATA FILE
            autumn=autumn+f4
            wautumn=wautumn+w4

    #PM2.5 CALCULATION
for file in winter:########important#NOTE FOR OTHER SEAON YOU NEED TO CHANGE 'winter' with there name ....example for summer you need to replace winter by summer 
    #EXTRACTING THE DATA
    ds = nc.Dataset(file)
    SO4 = np.array(ds["SO4SMASS"][:])
    OC = np.array(ds["OCSMASS"][:])
    BC = np.array(ds["BCSMASS"][:])
    Dust25 = np.array(ds["DUSMASS25"][:])
    SS25 = np.array(ds["SSSMASS25"][:])
    PM25 = 1.375*SO4 + 1.6*OC + BC + Dust25 + SS25#CALCULATION FOR PM2.5
    PM25 = PM25*(10**9)
    lats = ds.variables['lat'][:]
    lons = ds.variables['lon'][:]
    time = ds.variables['time'][:]
    #EXTRACTING THE PM2.5 FOR EACH HOUR AND APPENDING IN RESPECTIVLY LIST
    for i in PM25:
        j=j+1# J REPRESENT DUMMY HOUR 
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
#WIND DATA EXTRACTION SAME LIKE PM2.5
j=0
for file in wwinter:#########important####NOTE FOR OTHER SEAON YOU NEED TO CHANGE 'wwinter' with there name ....example for summer you need to replace winter by wsummer 
    dwws = nc.Dataset(file)
    U500 = np.array(dwws["U500"][:])
    for i in U500:
        k=k+1 #K REPRESENT DUMMY HOUR
        if k==1:
            w0.append(i)
        elif k==2:
            w01.append(i)
        elif k==3:
            w02.append(i)
        elif k==4:
            w03.append(i)
        elif k==5:
            w04.append(i)
        elif k==6:
            w5.append(i)
        elif k==7:
            w6.append(i)
        elif k==8:
            w7.append(i)
        elif k==9:
            w8.append(i)
        elif k==10:
            w9.append(i)
        elif k==11:
            w10.append(i)
        elif j==12:
            w11.append(i)
        elif k==13:
            w12.append(i)
        elif k==14:
            w13.append(i)
        elif k==15:
            w14.append(i)
        elif k==16:
            w15.append(i)
        elif k==17:
            w16.append(i)
        elif k==18:
            w17.append(i)
        elif k==19:
            w18.append(i)
        elif k==20:
            w19.append(i)
        elif k==21:
            w20.append(i)
        elif k==22:
            w21.append(i)
        elif k==23:
            w22.append(i)
        else:
            w23.append(i)
    k=0

for file in wwinter:#########important####NOTE FOR OTHER SEAON YOU NEED TO CHANGE 'winter' with there name ....example for summer you need to replace winter by wsummer 
    dwws = nc.Dataset(file)
    V500 = np.array(dwws["V500"][:])    
    for i in V500:
        j=j+1
        if j==1:
            uw0.append(i)
        elif j==2:
            uw1.append(i)
        elif j==3:
            uw2.append(i)
        elif j==4:
            uw3.append(i)
        elif j==5:
            uw4.append(i)
        elif j==6:
            uw5.append(i)
        elif j==7:
            uw6.append(i)
        elif j==8:
            uw7.append(i)
        elif j==9:
            uw8.append(i)
        elif j==10:
            uw9.append(i)
        elif j==11:
            uw10.append(i)
        elif j==12:
            uw11.append(i)
        elif j==13:
            uw12.append(i)
        elif j==14:
            uw13.append(i)
        elif j==15:
            uw14.append(i)
        elif j==16:
            uw15.append(i)
        elif j==17:
            uw16.append(i)
        elif j==18:
            uw17.append(i)
        elif j==19:
            uw18.append(i)
        elif j==20:
            uw19.append(i)
        elif j==21:
            uw20.append(i)
        elif j==22:
            uw21.append(i)
        elif j==23:
            uw22.append(i)
        else:
            uw23.append(i)
    j=0    


#h IS LIST FOR ALL PM2.5 DATA WITH EACH HOUR SIMILAR voi and uw IS EAST AND WEST WIND RESPECTIVELY

h=[h0,h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13,h14,h15,h16,h17,h18,h19,h20,h21,h22,h23]
voi=[w0,w01,w02,w03,w04,w5,w6,w7,w8,w9,w10,w10,w12,w13,w14,w15,w16,w17,w18,w19,w20,w21,w22,w23]
uw=[uw0,uw1,uw2,uw3,uw4,uw5,uw6,uw7,uw8,uw9,uw10,uw11,uw12,uw13,uw14,uw15,uw16,uw17,uw18,uw19,uw20,uw21,uw22,uw23]





for o in range(0,24):
      #TAKING DIURNAL MEAN OF PM2.5 AND EAST AND WEST WIND  
      uv=np.array(uw[o])
      uv=np.mean(uv, axis=0)

      vv=np.array(voi[o])
      vv=np.mean(vv,axis=0)
      
      m=np.array(h[o])
      m=np.mean(m, axis=0)
      #print(m)

      #MAP FORMATION
            
      mp = Basemap(projection = 'merc',llcrnrlon = 61,llcrnrlat = 0,urcrnrlon = 100,urcrnrlat = 40,resolution = 'i')

      lon, lat = np.meshgrid(lons, lats)#CONVERTING LAT LON IN 2D
      x,y = mp(lon, lat)

                
      cmap = mpl.cm.rainbow
      norm = mpl.colors.Normalize(vmin=0, vmax=120)
      c_scheme = mp.contourf(x, y, np.squeeze(m),extend='max',cmap= cmap,norm=norm,levels=np.arange(0,110))#PLOTTING DATA
      mp.drawcoastlines()
      mp.drawstates()
      mp.drawcountries()
      mp.drawparallels (np.arange(0,50,10), labels=[True, False, False, False],linewidth=0.0)
      mp.drawmeridians (np.arange(60,110,10), labels=[0,0,0,1],linewidth=0.0)


      #PLOTTING WIND DATA
      yy = np.arange(0, y.shape[0],2)
      xx = np.arange(0, x.shape[1],2)
      points = np.meshgrid(yy, xx)
                        
      q = plt.quiver(x[points], y[points], vv[points], uv[points])
      plt.quiverkey(q, X=0.3, Y=1.1, U=10,label='10m/s', labelpos='E')

                  
   

      #COLORBAR AND TITLE
      bounds=np.arange(0,110,20)
      cbar = mp.colorbar(c_scheme, location = 'right', pad = '10%',ticks=bounds)
      cbar.set_label('PM2.5 (\u03BCg/m\u00b3)',loc='center',rotation = 90)
      plt.title('DIURNAL AVERAGE PM2.5: Winter ' +str(o)+ '-hour (2011-2020)' )##########important#for each season you need to change name   
      plt.show()
      #plt.savefig(r'C:\Users\tryri\Desktop\DIURNALTEN\\'+ str(o)+'.png')
             


             
