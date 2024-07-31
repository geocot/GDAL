from osgeo import ogr,osr,gdal
gdal.UseExceptions()

wfsdr = ogr.GetDriverByName('WFS')
#Service
url = "https://data.geopf.fr/wfs/ows?SERVICE=WFS&VERSION=2.0.0"
wfs_ds = wfsdr.Open('WFS:' + url)

"""
print(wfs_ds.GetLayerCount())
for i in range(wfs_ds.GetLayerCount()):
    couche = wfs_ds.GetLayerByIndex(i)
    print(couche.GetName())
"""
couchePylone = wfs_ds.GetLayerByName('BDTOPO_V3:pylone')

feature = couchePylone.GetNextFeature()
while feature:
    print(feature)
    feature = couchePylone.GetNextFeature()