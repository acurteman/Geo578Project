# Functions for final project go here.

# Import needed modules
from arcpy import Clip_management, Exists

# The first return value for each function should be a boolean value representing if the
# function was successfull or not.

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
    
# If landcover raster is present, have user input values for each landcover type
# def getLandcoverValues( rastLandcover)    This function should return a list of values
#                                                                               for each unique value in the landcover raster.

# If hydrology was not passed, but desired, generate from DEM
# def genHydro( rastHydro):     This function should return a raster/shapefile conaining hydrology

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

# NICK - Perform raster calculations on given rasters
# def calcModel( rastDEM, rastHydro, rastLandcover, numHydroBands, hydroBandDist,
#                               numSlopeBands, slopeCutoff):    This function should return
#                                                                                           a raster that is the result of
#                                                                                           the model calculations
