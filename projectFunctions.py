# Functions for final project go here.

# Import needed modules
from arcpy import Reclassify_3d, CheckOutExtension, CheckInExtension, Clip_management, Exists, sa, Slope_3d, FeatureToRaster_conversion, Raster, Describe
import os

CheckOutExtension('3D')
CheckOutExtension('Spatial')

# The first return value for each function should be a boolean value representing if the
# function was successfull or not.

#######################################
def getBounds(feature_or_raster):
    # check existence, as always
    if Exists(feature_or_raster) ==0:
        print "File does not exist to get bounds"
        print feature_or_raster
        return False, None
    
    # Use the describe function to pull out the pieces we want
    
    try:
        d=Describe(feature_or_raster)
        xmin=str(d.Extent.XMin)
        xmax=str(d.Extent.XMax)
        ymin=str(d.Extent.YMin)
        ymax=str(d.Extent.YMax)
    except:
        print "Problem obtaining spatial information from file"
        return False, None
    
    
    #  bring it back
    return True, xmin+" "+ymin+" "+xmax+" "+ymax
#######################################

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
def genHydroRast(vectHydro, rastSlope, rastHydro, cellSize, rastHydroCost):

    # test if the file exists
    if not(os.path.isfile(vectHydro)):
        print("This file not found: "+vectHydro)
        return False, None
    
    if not Exists(rastHydro):
        try:
            FeatureToRaster_conversion(vectHydro, "FID", rastHydro, cellSize)
            print('rastHydro_Created')
    
        except:   # we get here if it couldn't open the file
    
            print("Problem with FeatureToRaster_conversion")
            return False, None
    
    else:
        print('rastHydro already exists, skipping')
    
    if not Exists(rastHydroCost):
        try:
            costDist = sa.CostDistance(rastHydro, rastSlope)
            costDist.save(rastHydroCost)
        except:
            print("Problem running cost distance.")
            return False, None
    
    else:
        print('rastHydroCost already exists, skipping.')
    
    #return the dictionary value, along with a success flag
    return True, rastHydroCost

#######################################

#######################################
# Alex:
# If rasters are not uniform cell size, convert all to same cell size
# def createUniformCells( DEM, hydro, landcover)
#######################################

#######################################
# Clip all rasters by the given boundaries
def clipRaster(inRaster, bounds, outRaster):

    if not Exists(outRaster):
    # Attempt to execute Clip_management
        try:
            print(outRaster)
            Clip_management(inRaster, bounds, outRaster)
            return True, outRaster
    
        # If Clip_management failed:
        except:
            #print('Error with Clip_management tool')
            #print('File probably exists, but was previously created incorrectly.')
            #print('Check directory for <{0}> and consider removing.'.format(outRaster))
            return False, None
    
    else:
        print('Raster already exists, skipping')
        return True, outRaster
########################################

########################################
# Nick:
# Convert DEM to slope
def genSlope( rastDEM, rastSlope):

    # test if the file exists
    if not(os.path.isfile(rastDEM)):
        print("This file not found: "+rastDEM)
        return False, None
    elif Exists(rastSlope):
        print('Output already exists, skipping slope function')
        return True, rastSlope

    try:
        Slope_3d(rastDEM, rastSlope, 'DEGREE')
        print('rastSlope_Created')

    except:   # we get here if it couldn't open the file
        print("Problem with Slope_3D")
        return False, None

    #return the dictionary value, along with a success flag
    return True, rastSlope

########################################

########################################
# Alex:
# Convert rasters to weights
def rastReclassify( inRaster, field, remap, outRast):
    if not Exists(outRast):
        #try:
        print(inRaster)
        print(field)
        print(remap)
        print(outRast)
        output = Reclassify_3d(inRaster, field, remap, outRast, "NODATA")
        #except:
            #print('Error with Reclassify')
            #return False, None
    else:
        print('{0} already exists, skipping reclassify'.format(outRast))
        return True, outRast

    return True, output
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
def calcModel( rastSlope, rastHydroCost, rastLandcover, outputRast):
    # test if the file exists
    if not(Exists(rastHydroCost)):
        print("This file not found: "+rastHydroCost)
        return False, None
    elif not(Exists(rastSlope)):
        print("This file not found: "+rastSlope)
        return False, None
        
    elif not(Exists(rastLandcover)):
        print("This file not found: "+rastLandcover)
        return False, None

    if not Exists(outputRast):
        try:
            r1 = sa.Raster(rastHydroCost)
            r2 = sa.Raster(rastSlope)
            r3 = sa.Raster(rastLandcover)
            results = r1 * r2 * r3
            results.save(outputRast)
        
        except:   # we get here if it couldn't open the file

            print("Problem doing maths.")
            return False, None

    else:
        print('Output model already exists.')
        return True, outputRast

    #return the output filename, along with a success flag
    return True, outputRast
#######################################
