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