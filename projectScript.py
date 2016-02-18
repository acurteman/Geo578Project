# Main script for project goes in this file.

# Define function name and arguments. Possible inputs: DEM, hydrology file, Landcover file,
# bounding box to clip all rasters, number of hydrology bands, distance of hydrology bands,
# number of slope bands, cut off points for slope bands, boolean value to include hydrology,
# output file name,  list of landcover values.
# def createArchModel( rastDEM, rastHydro = None, rastLandcover = None, boundary,
#                                           numHydroBands = 3, hydroBandDist = 100, numSlopeBands = 4,
#                                           slopeCutoff = [15, 30, 45], addHydro = False, outputRast = None,
#                                           landcoverValues = None):

    # Load all rasters passed to the function
    # loadRasters( rastDEM, rastHydro, rastLandcover):

    # Clip all rasters by the given boundaries
    # rastDEM, rastHydro, rastLandcover = clipRasters( rastDEM, rastHydro, rastLandcover, boundary):

    # If landcover raster is present, and no values passed, have user input values for each landcover type
    # landcoverValues = getLandcoverValues( rastLandcover)

    # If hydrology was not passed, but desired, generate from DEM
    # rastHydro = genHydro( rastHydro):

    # Perform raster calculations on given rasters
    # calcModel( rastDEM, rastHydro, rastLandcover, numHydroBands, hydroBandDist,
    #                               numSlopeBands, slopeCutoff):

    # If output file name not provided, generate output file name
    # outputRast = genOutputName( rastDEM):

    # If successfull, return value True and output file name
    # return True, outputRast

    
