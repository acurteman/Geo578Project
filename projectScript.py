# Main script for project goes in this file.

# Define function name and arguments. Possible inputs: DEM, hydrology file, Landcover file,
# bounding box to clip all rasters, number of hydrology bands, distance of hydrology bands,
# number of slope bands, cut off points for slope bands, boolean value to include hydrology,
# output file name,  list of landcover values.
# def createArchModel( rastDEM, rastHydro = None, rastLandcover = None, boundary,
#                                           numHydroBands = 3, hydroBandDist = 100, numSlopeBands = 4,
#                                           slopeCutoff = [15, 30, 45], addHydro = False, outputRast = None,
#                                           landcoverValues = None):

    # Clip all rasters by the given boundaries
    # clipRasters( rastDEM, rastHydro, rastLandcover, boundary):

    # Load all rasters passed to the function
    # loadRasters( rastDEM, rastHydro, rastLandcover):

    # If landcover raster is present, and no values passed, have user input values for each landcover type
    # landcoverValues = getLandcoverValues( rastLandcover)       This function should return a list of values
    #                                                                                                           for each unique value in the landcover
    #                                                                                                           raster.

    # If hydrology was not passed, but desired, generate from DEM
    # rastHydro = genHydro( rastHydro):     This function should return a raster/shapefile conaining hydrology

    # If output file name not provided, generate output file name
    # outputRast = genOutputName( rastDEM):     This function should return a name for the output file

    # Perform raster calculations on given rasters
    # outputRast = calcModel( rastDEM, rastHydro, rastLandcover, numHydroBands, hydroBandDist,
    #                                               numSlopeBands, slopeCutoff, outputRast):    This function should return
    #                                                                                                                               a raster that is the result of
    #                                                                                                                               the model calculations

    # Save the output raster

    # If successfull, return value True and output file name
    # return True, outputRast

    
