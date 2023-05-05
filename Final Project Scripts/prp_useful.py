# Useful blocks of code
# Sources: GSP 318, SpaPy

##########

# Function header and documentation

""" 
*  Converts a Latitude/Longitude pair into a  UTM coordinate in a specified UTM Zone.
*  The UTMZone and South  must be provided and can be obtained by calling the  functions
*  below with the  Latitude and Longitude. This allows UTM values to get determined
*  for zones outside the  default zone.
* 
* Args:
* 	Longitude - Coordinate in the East-West  direction from -180 (Greenwich England) back to 180
* 		at the same location
* 	Latitude - Coordinate in the North-South  direction from -90  (south pole) to 90 (north pole)
* 	Datum - One of the constants from the  properties above
* 	UTMZone - Zone for the desired  coordinates. Can be found with GetUTMZoneFromLonLat() below
*  	South - True if in the southern hemisphere, false otherwise.  Can be found with GetSouthFromLat() below
* 
* Returns:
* 	Easting - Horizontal UTM coordinate within  the specified zone
* 	Northing - Vertical UTM position given the  specified value of  South
*
*  Raises:          
* 	IOError: An error when the lat/lon is not valid 
"""
##########

# Error messages with try/except blocks

# Simple message
try:
    x="hi"+1
except Exception  as TheException:
    print("Sorry, an error has occurred: "+format(TheException))
    
# With additional information
import sys
import traceback

try:
    x="hi"+1
except Exception  as TheException:
    print("Sorry, an error has occurred: "+format(TheException))
    exc_type, exc_value, exc_traceback =sys.exc_info()
    print(exc_type)
    print(exc_value)
    traceback.print_tb(exc_traceback, limit=10)

##########

# Print coordinate values into useful format
Latitude=40.12345
Longitude=-105.12345
print("Coordinate: "+format(Latitude,"0.7")+"\xB0 N, "+format(Longitude,"0.7")+"\xB0 W")

##########

# Automatically close file in excel
import os
os.system('taskkill /IM excel.exe')

##########

# Write a synthetic ASCII grid file
TheFile=open("gradient.asc","w")
TheFile.write("ncols 10\n")
TheFile.write("nrows 10\n")
TheFile.write("xllcorner     0.0\n")
TheFile.write("yllcorner     0.0\n")
TheFile.write("cellsize      1.0\n")
TheFile.write("NODATA_value  -9999\n")
  
# use the code from 3.4 to write out 10 rows and 10 columns of data here

##########

# Split date and time from USGS earthquake file

TheFile=open("earthquakes_all_day.csv","r") # open the file for reading (thus the "r")

NumLines=0
TheHeader=TheFile.readline() # read the header line from the file

TheLine=TheFile.readline() # read the next line in the file
while ((TheLine!="") and (NumLines<100)): # while the line is not blank, go through this loop

    TheElements=TheLine.split(",") # split up the columns of the line

    TheDateTimeString=TheElements[0] # get the datetime string
    print(TheDateTimeString) # print the string for debugging
    
    TheDateTimeElements=TheDateTimeString.split("T") # split the date and time into separate strings
    
    TheDateString=TheDateTimeElements[0] # get the date string
    TheTimeString=TheDateTimeElements[1] # get the time string
    
    TheDateElements=TheDateString.split("-") # break up the date elements
    
    TheYearString=TheDateElements[0]
    TheMonthString=TheDateElements[1]
    TheDayString=TheDateElements[2]
    
    print(TheMonthString + "/" + TheMonthString + "/" + TheYearString)    

    TheLine=TheFile.readline() # read the next line in the file
    NumLines+=1 # add one to count the number of lines read
    

TheFile.close()

print("Read "+format(NumLines)+" lines from the file")

##########

# Function to convert Celsius to Fahrenheit

def CelsiusFahrenheit(TheCelsiusValue):
    TheFahrenheitValue=(9.0/5.0)*TheCelsiusValue+32.0
    return(TheFahrenheitValue)
           
DegreesFahrenheit=CelsiusFahrenheit(0)
print(DegreesFahrenheit)



