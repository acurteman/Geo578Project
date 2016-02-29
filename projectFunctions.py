# Functions for final project go here.

# Import needed modules
from arcpy import Clip_management, Exists
import os

# The first return value for each function should be a boolean value representing if the
# function was successfull or not.

#######################################
# Alex:
# Load all parameters from param file
def ReadParamFileGeneric(paramfile):
    
    # test if the file exists
    if not(os.path.isfile(paramfile)):
        print("This file not found: "+paramfile)
        return False, None     
    
    #set up a blank dictionary value
    params={}
    
    try:
        with open(paramfile) as f:
            
            for line in f:
                check=line.split(": ")
                #if the result has exactly two values, we know we've found one
                #match.  Add this to the dictionary           
                
                if len(check) == 2:
                    #by assignment, the dictionary grows
                    #We also need to make sure that any leading spaces are cleanedup 
                    params[check[0]]=check[1].strip()
                    
    except:   # we get here if it couldn't open the file
        
        print("Problem reading the paramfile: "+paramfile)
        return False, None
   
    #return the dictionary value, along with a success flag
    return True, params
#######################################

#######################################
# Nick:
# Convert hydrology shapefile to raster, then calculate distance.
# This can probably be done easily by creating a cost distance
# raster. First convert the hydrology to a raster, then do
# a cost distance analysis. 
def genHydroRast( vectHydro):
    # Code stuffs goes here
#######################################

#######################################
# Alex:
# If rasters are not uniform cell size, convert all to same cell size
# def createUniformCells( DEM, hydro, landcover)
#######################################

#######################################
# Clip all rasters by the given boundaries
def clipRaster(inRaster, bounds):
    
    # Create file name for output raster
    outRaster = inRaster + '_CLIP'
    outLen = len(outRaster)
    clipCount = 1

    # Check if output filename exists already, and correct if so
    validName = False
    while not validName:

        # If it does not exist, name is valid
        if Exists(outRaster) ==0:
            #print('Output filename: {0}'.format(outRaster))
            validName = True

        # Else add number to end of output name and check again
        else:
            print('File <{0}> already exists, incrementing file name.'.format(outRaster))
            outRaster = outRaster[:outLen] + str(clipCount)
            clipCount += 1

    # Print out parameters to be used in Clip_management
    #print('Attempting Clip with following parameters: \n    ' +
          #'in_raster: {0}\n    rectange: {1}\n    out_raster: {2}'.format(
              #inRaster, bounds, outRaster))

    # Attempt to execute Clip_management
    try:
        Clip_management(inRaster, bounds, outRaster)
        return True, outRaster

    # If Clip_management failed:
    except:
        #print('Error with Clip_management tool')
        #print('File probably exists, but was previously created incorrectly.')
        #print('Check directory for <{0}> and consider removing.'.format(outRaster))
        return False, None
########################################

########################################
# Nick:
# Convert DEM to slope
def genSlope( DEM):
    # Inster code stuffs here
########################################

########################################
# Alex:
# Convert rasters to weights
def convertSlope( rastSlope, numSlopeBands, SlopeCutoff):

def convertHydro( rastHydro):

def convertLandcover( rastLandcover, landcoverValues):
########################################

########################################
# If output file name not provided, generate output file name
def genOutputName():       #This function should return a name for the output file

    # Create file name for output raster
    outRaster = 'archPredictiveModel'
    outLen = len(outRaster)
    clipCount = 1

    # Check if output filename exists already, and correct if so
    validName = False
    while not validName:

        # If it does not exist, name is valid
        if Exists(outRaster) ==0:
            #print('Output filename: {0}'.format(outRaster))
            validName = True

        # Else add number to end of output name and check again
        else:
            print('File <{0}> already exists, incrementing file name.'.format(outRaster))
            outRaster = outRaster[:outLen] + str(clipCount)
            clipCount += 1

    return outRaster
#######################################

#######################################
# NICK - Perform raster calculations on given rasters
def calcModel( rastDEM, rastHydro, rastLandcover):
    # Insert code stuffs here
#######################################
