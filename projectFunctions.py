# Functions for final project go here.

# The first return value for each function should be a boolean value representing if the
# function was successfull or not.

# Load all rasters passed to the function
# def loadRasters( rastDEM, rastHydro, rastLandcover):

# Clip all rasters by the given boundaries
# def clipRasters( rastDEM, rastHydro, rastLandcover):

# If landcover raster is present, have user input values for each landcover type
# def getLandcoverValues( rastLandcover)    This function should return a list of values
#                                                                               for each unique value in the landcover raster.

# If hydrology was not passed, but desired, generate from DEM
# def genHydro( rastHydro):     This function should return a raster/shapefile conaining hydrology

# If output file name not provided, generate output file name
# def genOutputName( rastDEM):       This function should return a name for the output file

# Perform raster calculations on given rasters
# def calcModel( rastDEM, rastHydro, rastLandcover, numHydroBands, hydroBandDist,
#                               numSlopeBands, slopeCutoff):    This function should return
#                                                                                           a raster that is the result of
#                                                                                           the model calculations
