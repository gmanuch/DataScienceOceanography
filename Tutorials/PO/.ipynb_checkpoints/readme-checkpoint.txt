Data for this project is downloaded using the Copernicus API: https://cds.climate.copernicus.eu/api-how-to follow these quick instructions first. 

The download_era.py script gets this data:  https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels-monthly-means-preliminary-back-extension?tab=form   

You will need to agree to terms and conditions following the link that you will recieve when trying to run the download script for the first time;

Once you download the data, there will be an .nc file that is loded and analysed in ENSO.ipynb

The notebook showcases how to work with data using xarray and some basic time series analysis of ENSO events.



#This is how we coarsened the dataset from 1/4 degree to a 1 degree grid to speed up the analysis;

ERA5="/dat1/gmanuch/ERA5/winds_sst_pres_prec.nc" # specify the data file to load
era = xr.open_dataset(ERA5); #xarray can open different format data, netcdf is one of them#era_coarse=era.coarsen(longitude=4, latitude=4, boundary="trim").mean(); # coarsen the data to a 1x1 degree from a 0.25x0.25 degree; could do it to begin with to save computing!
era_coarse.to_netcdf('/dat1/gmanuch/DataScienceOceanography/ERA5_Coarse.nc'); # save to a netcdf file



