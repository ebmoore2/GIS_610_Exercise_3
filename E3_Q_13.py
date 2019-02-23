#Q13
#From the Blackboard assignment Exercise 3,
#download the zipped directory labeled (‘Question 13’)
#and unzip its contents onto your local computer.
#Then create a file geodatabase. Using the code that we covered in class,
#import all of the shapefiles in the folder to the geodatabase.
#Finally, clip the census tracts that fall within the Maricopa County boundary
#and write them to a new feature class in your geodatabase.
print("Let's save the Q13 shapefiles into a new gdb, and clip all the data to Maricopa County...")

import os, sys, arcpy
from IPython.display import display
from arcgis.gis import GIS
gis = GIS("pro")
from arcpy import env
env.overwriteOutput = True

#set workspace
#
workspace_path = r"C:\Users\Buffie\Documents\1 GIS\610\Exercise_3_ArcPy_test"
env.workspace = workspace_path

#set local variables
#
fgdb_name = "MaricopaCensusTracts"
tract = "tl_2018_04_tract"
county = "tl_2018_us_county"
Input_Features1 = workspace_path + "\\" + tract
Input_Features2 = workspace_path + "\\" + county
Output_Geodatabase = workspace_path + "\\" + fgdb_name
in1 = "tl_2018_04_tract"
out1 = "Maricopa_tracts_2018"
in_features1 = workspace_path + "\\" + fgdb_name + "\\" + in1
clip_features = r"C:\Users\Buffie\Documents\1 GIS\640\RioRisk\Feb3Moore_RioRisk.gdb\Maricopa_county.shp" #my local Maricopa boundary
out_feature_class1 = workspace_path + "\\" + fgdb_name + "\\" + out1

#create a gdb
#
print("Creating a gdb...")
arcpy.CreateFileGDB_management(workspace_path, fgdb_name)
print("Done creating a gdb.")

#import shapefiles into this new gdb
#
print("Importing shapefiles...")
#arcpy.FeatureClassToGeodatabase_conversion (Input_Features, Output_Geodatabase)
arcpy.FeatureClassToGeodatabase_conversion(Input_Features1, Output_Geodatabase)
arcpy.FeatureClassToGeodatabase_conversion(Input_Features2, Output_Geodatabase)
print("Done importing shapefiles.")


#clip all the shapefiles into the Maricopa County boundary and copy into a new feature class
#
print("Clipping tracts to Maricopa County...")
#arcpy.Clip_analysis(in_features, clip_features, out_feature_class, {cluster_tolerance})
arcpy.Clip_analysis(in_features1, clip_features, out_feature_class1)
print("Done clipping tracts to Maricopa County.")