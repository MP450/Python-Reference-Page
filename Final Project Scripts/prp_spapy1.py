# SpaPy Module

# Import libraries
import sys

# Open source spatial libraries
import shapely
import numpy
from osgeo import gdal
import math
import random

# SpaPy libraries
from SpaPy import SpaBase
from SpaPy import SpaPlot
from SpaPy import SpaVectors
from SpaPy import SpaView
from SpaPy import SpaReferencing
from SpaPy import SpaDensify
from SpaPy import SpaView
from SpaPy import SpaRasters
from SpaPy import SpaTopo
from SpaPy import SpaRasterVectors

# Set File Paths

CountriesFilePath="SpaPyTests/Data/NaturalEarth/ne_110m_admin_0_countries.shp"

OverlayFile="SpaPyTests/Data/Overlay/Box.shp"

HumbRiverPath="SpaPyTests/Data/HumboldtCounty/hydrography/nhd24kst_l_ca023.shp"

HumbZoningPath="SpaPyTests/Data/HumboldtCounty/Humboldt_Zoning_ClippedToEelRiver2.shp"

Zoning_Bay="SpaPyTests/Data/HumboldtCounty/Zoning_Bay.shp"

OutputFolderPath="" # Set folder path to same folder as scripts

# Show Zoning_Bay in SpaView
SpaView.Show(Zoning_Bay)

# Set data to view at 600x600 px
SpaView.Show(Zoning_Bay,600,600)

###########################################

###########################################

# Get information from shapefile

TheDataset=SpaVectors.SpaDatasetVector() #create a new layer

TheDataset.Load(HumbZoningPath) # load the contents of the layer


print("Type: "+format(TheDataset.GetType())) # get the type of data in the dataset

print("CRS: "+format(TheDataset.GetCRS())) # return the coordinate reference system

print("NumFeatures: "+format(TheDataset.GetNumFeatures())) # get the number of features in the dataset

print("Bounds: "+format(TheDataset.GetBounds())) # get the spatial bounds of the features

NumAttributes=TheDataset.GetNumAttributes()  # retrieve the number of attributes within a dataset

print("NumAttributes: "+format(NumAttributes)) # return with number of attributes

print("Show the dataset")

SpaView.Show(TheDataset)

print("Done showing the dataset")

###########################################

###########################################

# Buffer

SpaView.Show(CountriesFilePath) # display the dataset in a view

BufferedDataset=SpaVectors.Buffer(CountriesFilePath,10)  # create 10 unit buffer (represents 10 degrees in this instance)
BufferedDataset.Save(OutputFolderPath+"Buffered_10.shp") # save buffered shapefile

SpaView.Show(BufferedDataset) # display the dataset in a view

###########################################

# Union

UnionBuffer=SpaVectors.Union(BufferedDataset) # perform a union on the dataset

UnionBuffer.Save(OutputFolderPath+"UnionBuffer.shp")  # save union results

SpaView.Show(UnionBuffer) # view the results

###########################################

# Centroids

CentroidDataset=SpaVectors.Centroid(CountriesFilePath) # create centroid

CentroidDataset.Save(OutputFolderPath+"Centroid.shp")  # save centroid results

SpaView.Show(CentroidDataset)

###########################################

# Convex Hull

ConvexHullDataset=SpaVectors.ConvexHull(CountriesFilePath) # find convex hull

ConvexHullDataset.Save(OutputFolderPath+"ConvexHull.shp")  # save convex hull 

SpaView.Show(ConvexHullDataset) # view created convex hull dataset

###########################################

# Simplify

SimplifiedDataset=SpaVectors.Simplify(CountriesFilePath,2) # simpify shapefile
SimplifiedDataset.Save(OutputFolderPath+"Simplify.shp") # save simplified shapefile

SpaView.Show(SimplifiedDataset)

###########################################

# Clip

ClippedDataset=SpaVectors.Clip(CountriesFilePath,-50,-50,50,50) # clip dataset (XMin,YMin,XMax,YMax)
ClippedDataset.Save(OutputFolderPath+"Clip.shp") # save clipped shapefile

SpaView.Show(ClippedDataset) # show dataset

###########################################

###########################################

# Overlay Transformations

SpaView.Show(CountriesFilePath)          # Show the countries file
SpaView.Show(OverlayFile)          # Show the overlay file

###########################################

# Union

# Union between the two shapefiles
Union=SpaVectors.Union(CountriesFilePath,OverlayFile) # perform a union on a geometry to get the new layer
Union.Save(OutputFolderPath+"Union.shp") # save the output

SpaView.Show(Union)          # Show the Union file

###########################################

# Intersection

# Intersection between the two shapefiles
Intersection=SpaVectors.Intersection(CountriesFilePath,OverlayFile) # perform a union on a geometry to get the new layer
Intersection.Save(OutputFolderPath+"Intersection.shp") # save the output

# Difference

# Find the difference between the shapefiles and the polygon (erase the area of the smaller polygon)
Difference=SpaVectors.Difference(CountriesFilePath,OverlayFile) 
Difference.Save(OutputFolderPath+"Difference.shp") # save the output

SpaView.Show(Intersection)        # Show the Intersection file

SpaView.Show(Difference)          # Show the Difference file

###########################################

# Overlay Operations

# Intersection
Intersection=SpaVectors.Intersects(CountriesFilePath,OverlayFile)
print("Intersect:"+format(Intersection)) # should be true

# Touches
Touch=SpaVectors.Touches(CountriesFilePath,OverlayFile) # have at least one point in common but interiors do not intersect
print("Touch:"+format(Touch)) # should be False

# Disjoint
Disjoint=SpaVectors.Disjoint(CountriesFilePath,OverlayFile)
print("Disjoint:"+format(Disjoint)) # should be False

# Overlap
Overlap=SpaVectors.Overlaps(CountriesFilePath,OverlayFile)
print("Overlap:"+format(Overlap)) # should be true

# Cross
Cross=SpaVectors.Crosses(CountriesFilePath,OverlayFile)
print("Cross:"+format(Cross)) # should be False

# Contain
Contain=SpaVectors.Contains(CountriesFilePath,OverlayFile)
print("Touch:"+format(Touch)) # should be False