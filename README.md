# PM2.5-Surface-distribution-atmospheric-chemistry-
This repository contains code to analyze and visualize the surface-level PM2.5 concentration using NASA MERRA-2 reanalysis data. Users can specify the latitude and longitude range to extract and study the spatial distribution of PM2.5 over a specific region of the Earth. The script not only processes the data but also generates a clear plot of PM2.5 distribution for easy interpretation.

🌍 Overview
📌 Objective: To compute and visualize the distribution of surface PM2.5 concentrations for a selected geographical region.

🌐 Data Source: NASA's MERRA-2 (Modern-Era Retrospective analysis for Research and Applications, Version 2) reanalysis dataset.

🔧 Inputs: Latitude and longitude boundaries, MERRA-2 NetCDF file.

📊 Outputs:

Extracted PM2.5 data over the region of interest

Surface distribution plot of PM2.5 concentrations

🧠 How It Works
User provides:

Latitude and longitude range

MERRA-2 NetCDF file (e.g., MERRA2_400.tavg1_2d_aer_Nx.YYYYMMDD.nc4)

The script:

Extracts relevant PM2.5 concentration data for the specified region

Plots and saves the PM2.5 surface distribution using matplotlib and BaseMap
