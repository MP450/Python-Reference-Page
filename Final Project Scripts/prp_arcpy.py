# ArcPy examples
# Sources: GSP 318, esri arcpy documentation
#
# !!! Specify path to use python within ArcGis Pro 
# For CPH lab computers use 
# "c:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe"

##########

# Imports, licensing and environments
import arcpy

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# This allows us to run the script repeatedly without deleting the intermdiate files
arcpy.env.overwriteOutput=True 

##########

# Python modules

#Charts module (arcpy.charts)
#Data Access module (arcpy.da)
#Geocoding module (arcpy.geocoding)
#Image Analysis module (arcpy.ia)
#Mapping module (arcpy.mp)
#Metadata module (arcpy.metadata)
#Network Analyst modules (arcpy.nax and arcpy.na)
#Sharing module (arcpy.sharing)
#Spatial Analyst module (arcpy.sa)
#Workflow Manager (Classic) module (arcpy.wmx)

##########
# Analysis
# Extract
arcpy.analysis.Clip(in_features, clip_features, out_feature_class, {cluster_tolerance})
arcpy.analysis.Select(in_features, out_feature_class, {where_clause})
arcpy.analysis.Split(in_features, split_features, split_field, out_workspace, {cluster_tolerance})
# Overlay
arcpy.analysis.Erase(in_features, erase_features, out_feature_class, {cluster_tolerance})
arcpy.analysis.Intersect(in_features, out_feature_class, {join_attributes}, {cluster_tolerance}, {output_type})
arcpy.analysis.Union(in_features, out_feature_class, {join_attributes}, {cluster_tolerance}, {gaps})
# Proximity
arcpy.analysis.Buffer(in_features, out_feature_class, buffer_distance_or_field, {line_side}, {line_end_type}, {dissolve_option}, {dissolve_field}, {method})
arcpy.analysis.MultipleRingBuffer(Input_Features, Output_Feature_class, Distances, {Buffer_Unit}, {Field_Name}, {Dissolve_Option}, {Outside_Polygons_Only}, {Method})
# Statistics
arcpy.analysis.Statistics(in_table, out_table, {statistics_fields}, {case_field})

# Spatial analysis
# run the aspect tool
OutRaster = arcpy.sa.Aspect(InputPath+"Temp.img")
# Aspect and slope in one function
OutRaster = arcpy.sa.AspectSlope("elevation.tif", 3) # OutRaster = AspectSlope(raster, {z_factor})
OutRaster.save("aspect_slope.tif")

# Appearance
#arcpy.sa.StatisticsHistogram (raster, statistics, histogram)
#arcpy.sa.Stretch (raster, stretch_type, min, max, num_stddev, statistics, dra, {min_percent},
         #max_percent, {gamma}, {compute_gamma}, sigmoid_strength_level)

# Band Indices
#arcpy.sa.BAI (raster, {red_band_id}, {nir_band_id}) # BAI = 1/((0.1 -RED)^2 + (0.06 - NIR)^2)
#arcpy.sa.EVI (raster, {nir_band_id}, {red_band_id}, {blue_band_id}) # EVI = 2.5*(NIR - Red) / (NIR + 6*Red - 7.5*Blue + 1)
#arcpy.sa.NBR (raster, {swir_band_id}, {nir_band_id}) # NBR = (NIR - SWIR) / (NIR+ SWIR)
#arcpy.sa.NDMI (raster, {nir_band_id}, {swir1_band_id}) # NDMI = (NIR - SWIR1)/(NIR + SWIR1)
#arcpy.sa.NDVI (raster, {nir_band_id}, {red_band_id}) # NDVI = ((NIR - R)/(NIR + R))
#arcpy.sa.NDWI (raster, {nir_band_id}, {green_band_id}) # NDWI = (Green - NIR) / (Green + NIR)
#arcpy.sa.SAVI (raster, {nir_band_id}, {red_band_id}, {l}) # SAVI = ((NIR - Red)/(NIR + Red + L)) * (1 + L)

# Conversion
#arcpy.sa.Grayscale (raster, {conversion_parameters})
#arcpy.sa.RasterizeFeatures (raster, feature_class, {class_index_field}, {resolve_overlap_method})

# Data Management
#arcpy.sa.CompositeBand(["Band1.TIF", "Band2.TIF", "Band3.TIF"])
#arcpy.sa.ExtractBand (raster, {band_ids}, {band_names}, {band_wavelengths}, {missing_band_action},
             #{wavelength_match_tolerance})
#arcpy.sa.Resample (raster, {resampling_type}, {input_cellsize}, {output_cellsize})

# Arithmetic
#arcpy.sa.Arithmetic (raster1, raster2, {operation_type}, {extent_type}, {cellsize_type})
#arcpy.sa.RasterCalculator (rasters, input_names, expression, {extent_type}, {cellsize_type})

##########

# Create shaded relief

# Import system modules
import arcpy
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/data"

# input raster
inRasters= = "input_raster.tif"

# use built-in colorramp slope
colorramp_name = "Slope"

# Execute arcpy.sa.ShadedRelief
shadedRelief = ShadedRelief(imagePath1, azimuth=315, altitude=45, z_factor=1, colorramp=colorramp_name, slope_type = "SCALED",
                            ps_power=0.664, psz_factor=0.024, remove_edge_effect=False)
shadedRelief.save("C:/output/shadedrelief_output2.tif")

##########

# save to an IMAGINE (img) file 
OutRaster.save(InputPath+"Aspect.img")