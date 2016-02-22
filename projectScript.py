# Main script for project goes in this file.

# Import needed modules:
from projectFuctions import *
from arcpy import Raster

# Define function name and arguments. Possible inputs: DEM, hydrology file, Landcover file,
# bounding box to clip all rasters, number of hydrology bands, distance of hydrology bands,
# number of slope bands, cut off points for slope bands, boolean value to include hydrology,
# output file name,  list of landcover values.
def createArchModel( rastDEM, rastHydro = None, rastLandcover = None, boundary,
                     numHydroBands = 3, hydroBandDist = 100, numSlopeBands = 4,
                     slopeCutoff = [15, 30, 45], addHydro = False, outputRast = None,
                     landcoverValues = None):

    # Clip all rasters by the given boundaries
    # Clipping the DEM
    print('Attempting DEM clip.')
    ok, clipDEM = clipRaster( rastDEM, rastHydro, rastLandcover, boundary):

    #Check for errors, exit if needed
    if not ok:
        print('Error with DEM clip.')
        return False, None

    # If hydrology is given, clip
    if not rastHydro == None:
        print('Attempting Hydrology clip.')
        ok, clipHydro = clipRaster( rastHydro, boundary)

        # Check for errors, exit if needed
        if not ok:
            print('Error with Hydrology clip')
            return False, None
        
    # If land cover is given, clip
    if not rastLandcover == None:
        print('Attempting Land cover clip.')
        ok, clipLandcover = clipRaster( rastLandcover, boundary)

        # Check for errors, exit if needed
        if not ok:
            print('Error with Land cover clip.')
            return False, None

    # Load all clipped rasters
    DEM = Raster(clipDEM)
    Hydro = Raster(clipHydro)
    Landcover = Raster(clipLandcover)

    # If landcover raster is present, and no values passed, have user input values for each landcover type
    # landcoverValues = getLandcoverValues( rastLandcover)       This function should return a list of values
    #                                                                                                           for each unique value in the landcover
    #                                                                                                           raster.

    # If hydrology was not passed, but desired, generate from DEM
    if rastHydro == None and addHydro == True:
        print('Generating Hydrology.')
        rastHydro = genHydro( rastHydro):     #This function should return a raster/shapefile conaining hydrology

    # If output file name not provided, generate output file name
    if outputRast == None:
        outputRast = genOutputName():     #This function should return a name for the output file

    # Perform raster calculations on given rasters
    # outputRast = calcModel( rastDEM, rastHydro, rastLandcover, numHydroBands, hydroBandDist,
    #                                               numSlopeBands, slopeCutoff, outputRast):    This function should return
    #                                                                                                                               a raster that is the result of
    #                                                                                                                               the model calculations

    # Save the output raster

    # If successfull, return value True and output file name
    # return True, outputRast

    
