
# Setup library imports and file paths.
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

# File Paths

CountriesFilePath="SpaPyTests/Data/NaturalEarth/ne_110m_admin_0_countries.shp"

OverlayFile="SpaPyTests/Data/Overlay/Box.shp"

HumbRiverPath="SpaPyTests/Data/HumboldtCounty/hydrography/nhd24kst_l_ca023.shp"

HumbZoningPath="SpaPyTests/Data/HumboldtCounty/Humboldt_Zoning_ClippedToEelRiver2.shp"

Zoning_Bay="SpaPyTests/Data/HumboldtCounty/Zoning_Bay.shp"

OutputFolderPath=""

####################################

####################################

ZoningDataset=SpaVectors.SpaDatasetVector() #create a new layer
ZoningDataset.Load(HumbZoningPath) # load the contents of the layer

NumAttributes=ZoningDataset.GetNumAttributes()  # returns with the number of attributes found within the vector file
print("Num Attributes: "+format(NumAttributes)) #print out number of attributes

####################################

####################################

AttributeIndex=0 # we set Index to zero to begin with the first attribute
# We set up the while loop to run as long as our index is less than the number of attributes
while (AttributeIndex<NumAttributes): 
    # the following will format and return the name, type and width of each attribute
    AttributeName=ZoningDataset.GetAttributeName(AttributeIndex)
    AttributeType=ZoningDataset.GetAttributeType(AttributeIndex)
    print("Attribute: "+format(AttributeName)+", Type: "+format(AttributeType)) 
    AttributeIndex+=1 # we will add one to the index to run through the next attribute in line

####################################
    
####################################
    
print("******* Finding Attribute values for ZONING********")

NumFeatures=ZoningDataset.GetNumFeatures()  # returns with the number of features found within the vector file

# The following lines of code runs through all of the values in the Zoning field and returns with each one
FeatureIndex=0
while (FeatureIndex<NumFeatures):
    AttributeValue=ZoningDataset.GetAttributeValue("ZONING",FeatureIndex)
    print(format(AttributeValue))
    FeatureIndex+=1

####################################
    
####################################
    
print("******** Finding Attribute values for ACRES ************")
# The following lines of code runs through all of the values in the AREA field and returns with each one
    
FeatureIndex=0         
while (FeatureIndex<NumFeatures):  
    AttributeValue=ZoningDataset.GetAttributeValue("ACRES",FeatureIndex) 
    print(AttributeValue)
    FeatureIndex+=1

####################################
    
####################################
    
print("******** Finding The Total Number of Acres ************")
FeatureIndex=0
Sum=0
while (FeatureIndex<NumFeatures):
    Sum+=ZoningDataset.GetAttributeValue("ACRES",FeatureIndex)
    FeatureIndex+=1
     
print("Sum of acres (total area): "+format(Sum))
print("Mean of area in acres: "+format(Sum/NumFeatures))


####################################

####################################

print("******** Deleting the attribute ABRREV ************")
ZoningDataset.DeleteAttribute("ABRREV")
ZoningDataset.Save(OutputFolderPath+"Zoning_AttributeRemoved.shp")

####################################

####################################

print("******** Deleting the first 10 features in a shapefile ************")

ZoningDataset=SpaVectors.SpaDatasetVector() #create a new layer
ZoningDataset.Load(HumbZoningPath) # load the contents of the layer

# delete the first 10 features
Index=0
while (Index<10):
 ZoningDataset.DeleteFeature(0)
 Index+=1

# Save the result
ZoningDataset.Save(OutputFolderPath+"Zoning_First_10_gone.shp")