import geopandas as gpd
import matplotlib.pyplot as plt

# Importing an ESRI Shapefile and plotting it using GeoPandas
districts = gpd.read_file(r'.\Shapefiles\districts.shp')
districts.plot(cmap = 'hsv', edgecolor = 'black', column = 'district')
plt.title('Districts Plot')
plt.show()

area_of_interest = gpd.read_file(r'.\Shapefiles\area_of_interest.shp')
area_of_interest.plot()
plt.title('Area of Interest Plot')
plt.show()

atms = gpd.read_file(r'.\Shapefiles\atms.shp')
# Plot the figures side by side
fig, (ax1, ax2) = plt.subplots(nrows = 2, figsize = (10,8))
districts.plot(ax = ax1, cmap = 'hsv', edgecolor = 'black', column = 'district')
area_of_interest.plot(ax = ax2, color = 'green')
plt.suptitle('Districts and Area of Interest Plot')
plt.show()

# Plotting multiple layers
fig, ax = plt.subplots(figsize = (10,8))
districts.plot(ax = ax, cmap = 'hsv', edgecolor = 'black', column = 'district')
area_of_interest.plot(ax = ax, color = 'none', edgecolor = 'black')
atms.plot(ax = ax, color = 'black', markersize = 14)
plt.suptitle('Multiple Layers Plot')
plt.show()

# Reprojecting GeoPandas GeoDataFrames
fig, ax = plt.subplots(figsize = (8,6))
districts = districts.to_crs(epsg = 32629)
districts.plot(ax = ax, cmap = 'hsv', edgecolor = 'black', column = 'district')
area_of_interest = area_of_interest.to_crs(epsg = 32629)
area_of_interest.plot(ax = ax, color = 'none', edgecolor = 'black')
plt.title('Reprojected GeoDataFrames Plot')
plt.show()

# Intersecting Layers
districts_in_aoi = gpd.overlay(districts, area_of_interest, how = 'intersection')
districts_in_aoi.plot(edgecolor = 'red')
plt.title('Intersected Layers Plot')
plt.show()