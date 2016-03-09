# Main script for project goes in this file.

# Import needed modules:
from projectFunctions import *
from arcpy import env

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
        rastDEM = paramDict['rastDEM'] # File name of the DEM
        vectHydro = paramDict['vectHydro'] # File name of the hydrology shapefile
        rastHydro = paramDict['rastHydro'] # File name of the hydrology raster that will be generated
        rastHydroCost = paramDict['rastHydroCost'] # File name of the cost distance raster to be generated
        rastLandcover = paramDict['rastLandcover'] # File name of the NLCD raster
        rastSlope = paramDict['rastSlope'] # File name of the slope raster to be generated
        boundFile = paramDict['boundary'] # File name of the feature to be used to extract boundaries
        slopeCutoff = paramDict['slopeCutoff'] # List of slope conversion boundaries
        hydroCutoff = paramDict['hydroCutoff'] # List of cost distance conversion boundaries
        outputRast = paramDict['outputRast'] # Name of the final output raster
        landcoverValues = paramDict['landcoverValues'] # List of landcover conversion values
        cellSize = paramDict['cellSize'] # Cell size to standardize to
        workDir = paramDict['wd'] # Directory path to the directory with needed files
        
        print('rastDEM: {0} \nvectHydro: {1} \nrastHydro: {2} \nrastHydroCost: {3} \nrastLandcover: {4} \nrastSlope: {5} \nboundFile: {6} \nslopeCutoff: {7} \nhydroCutoff: {8} \noutputRast: {9} \nlandcoverValues: {10} \ncellSize: {11} \nworkDir: {12}'.format(rastDEM, vectHydro, rastHydro, rastHydroCost, rastLandcover, rastSlope, boundFile, slopeCutoff, hydroCutoff, outputRast, landcoverValues, cellSize, workDir))

    else:
        print('Error loading parameters')
        return False, None
    ######################################
    
    ######################################
    env.workspace = workDir
    ######################################
    
    ######################################
    print('Getting boundaries')
    try:
        ok, boundary = getBounds(boundFile)
    except:
        print('Error with getBounds')
        return False, None
    
    print(boundary)
    ######################################
    
    ########################################
    # Convert DEM to slope here:
    print('Converting DEM to slope.')
    ok, rastSlope = genSlope(rastDEM, rastSlope)
    ########################################

    ######################################
    # Genereate hydrology raster here
    print('Generating Hydrology cost distance raster.')
    ok, rastHydroCost = genHydroRast(vectHydro, rastSlope, rastHydro, cellSize, rastHydroCost)
    ######################################

    ######################################
    # Clip all rasters by the given boundaries

    # Clipping the Slope
    print('Attempting Slope clip.')
    ok, clipSlope = clipRaster( rastSlope, boundary, 'clipSlope')

    #Check for errors, exit if needed
    if not ok:
        print('Error with DEM clip.')
        return False, None

    # Clip Hydrology
    print('Attempting Hydrology clip.')
    ok, clipHydro = clipRaster( rastHydroCost, boundary, 'clipHydro')

    # Check for errors, exit if needed
    if not ok:
        print('Error with Hydrology clip')
        return False, None
        
    # Clip landcover
    print('Attempting Land cover clip.')
    ok, clipLandcover = clipRaster( rastLandcover, boundary, 'clipLandcover')

    # Check for errors, exit if needed
    if not ok:
        print('Error with Land cover clip.')
        return False, None
    ########################################

    ########################################
    # Reclassify each raster according to weights
    field = "VALUE"

    print('Reclassifying slope raster.')
    okSlope, weightSlope = rastReclassify( clipSlope, field, slopeCutoff, 'weightSlope')

    print('Reclassifying hydrology raster.')
    okHydro, weightHydro = rastReclassify( clipHydro, field, hydroCutoff, 'weightHydro')

    print('Reclassifying Landcover raster.')
    okLC, weightLandcover = rastReclassify( clipLandcover, field, landcoverValues, 'weightLC')

    if not okSlope or not okHydro or not okLC:
        print('Problem with reclassify, exiting function')
        return False, None
    ########################################

    ########################################
    # If output file name not provided, generate output file name
    if outputRast == None:
        outputRast = genOutputName()     #This function should return a name for the output file
    ########################################

    ########################################
    # Perform raster calculations on given rasters
    outputRast = calcModel( weightSlope, weightHydro, weightLandcover, outputRast)
    ########################################
    
    # Save the output raster

    # If successful, return value True and output file name
    return True, outputRast

    print('VICTORY!')

    
params = 'parameters.txt'
createArchModel(params)
