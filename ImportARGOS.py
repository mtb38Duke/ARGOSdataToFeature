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