##---------------------------------------------------------------------
## ImportARGOS.py
##
## Description: Read in ARGOS formatted tracking data and create a point
##    feature class from the [filtered] tracking points
##
## Usage: ImportArgos <ARGOS folder> <Output feature class> 
##
## Created: Fall 2018
## Author: matthew.brantley@duke.edu (for ENV859)
##---------------------------------------------------------------------

#Import modules
import sys, os, arcpy

# Set input variables (Hard-wired)
inputFile = 'V:/ARGOSTracking/data/ARGOSData/1997dg.txt'
outputFC = "V:/ARGOSTracking/scratch/ARGOStrack.shp"

# open the ARGOS data file for reading
inputFileObj = open(inputFile, 'r')

# Get the first line of data so we can loop
lineString = inputFileObj.readline()
while lineString:
    #run code only if line contains Date :
    if("Date :" in lineString):

    #split line into a list
        lineList = lineString.split()

        tagID = lineData[0]

        #Get the next line
        line2String = inputFileObj.readline()
        line2Data = line2String.split()

        #get attributes from second line
        obsLat = line2Data[2]
        obsLon = line2Data[5]

        # Print results to see how we're doing
        print (tagID,"Lat:"+obsLat,"Long:"+obsLon)

    
    #get the next line
    lineString = inputFileObj.readline()

#Close the file object
inputFileObj.close()

    