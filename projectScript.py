# Main script for project goes in this file.

# Import needed modules:
from projectFuctions import *

# Define function name and arguments. Possible inputs: DEM, hydrology file, Landcover file,
# bounding box to clip all rasters, number of hydrology bands, distance of hydrology bands,
# number of slope bands, cut off points for slope bands, boolean value to include hydrology,
# output file name,  dict of landcover values.
def createArchModel( paramFile):
    
    ######################################
    # Load variables from param file
    ok, paramDict = ReadParamFileGeneric(paramFile)

    # Assign variables
    if ok:
        rastDEM = paramDict['rastDEM']
        vectHydro = paramDict['vectHydro']
        rastHydro = paramDict['rastHydro']
        rastHydroCost = paramDict['rastHydroCost']
        rastLandcover = paramDict['rastLandcover']
        rastSlope = paramDict['rastSlope']
        boundary = paramDict[boundary]
        slopeCutoff = paramDict['slopeCutoff']
        hydroCutoff = paramDict['hydroCutoff']
        outputRast = paramDict['outputRast']
        landcoverValues = paramDict['landcoverValues']
        cellSize = paramDict['landcoverValues']

    else:
        print('Error loading parameters')
        return False, None
    ######################################

    ########################################
    # Convert DEM to slope here:
    ok, rastSlope = genSlope(rastDEM)
    ########################################

    ######################################
    # Genereate hydrology raster here
    rastHydroCost = genHydroRast(vectHydro, rastSlope)
    ######################################

    ######################################
    # Clip all rasters by the given boundaries
    # Clipping the DEM
    print('Attempting DEM clip.')
    ok, clipDEM = clipRaster( rastDEM, boundary):

    #Check for errors, exit if needed
    if not ok:
        print('Error with DEM clip.')
        return False, None

    # Clip Hydrology
    print('Attempting Hydrology clip.')
    ok, clipHydro = clipRaster( rastHydroCost, boundary)

    # Check for errors, exit if needed
    if not ok:
        print('Error with Hydrology clip')
        return False, None
        
    # Clip landcover
    print('Attempting Land cover clip.')
    ok, clipLandcover = clipRaster( rastLandcover, boundary)

    # Check for errors, exit if needed
    if not ok:
        print('Error with Land cover clip.')
        return False, None
    ########################################

    ########################################
    # Reclassify each raster according to weights
    field = "Value"
    
    okSlope, weightSlope = convertSlope( rastSlope, field, slopeCutoff)

    okHydro, weightHydro = convertHydro( rastHydro, field, hydroCutoff)

    okLC, weightLandcover = convertLandcover( rastLandcover, field, landcoverValues)
    ########################################

    ########################################
    # If output file name not provided, generate output file name
    if outputRast == None:
        outputRast = genOutputName():     #This function should return a name for the output file
    ########################################

    ########################################
    # Perform raster calculations on given rasters
    outputRast = calcModel( weightSlope, weightHydro, weightLandcover)
    ########################################
    
    # Save the output raster

    # If successful, return value True and output file name
    return True, outputRast

    
