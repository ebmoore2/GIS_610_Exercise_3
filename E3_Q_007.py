#Q7
#Write Python code that selects a subset of the records
# from a given feature class and writes those features 
# to a different feature class. You may choose which 
# feature class that your code uses.

import os, sys, arcpy
from arcpy import env
env.overwriteOutput = True

workspace_path = r"C:\Users\Buffie\Documents\1 GIS\610\Exercise_3_ArcPy_test\Police.gdb"
env.workspace = workspace_path

#set local variables
old_fc = "General_Offense"
in_features = workspace_path + "\\" + old_fc
fc_name = "MoonWater_Q7_copy"
out_feature_class = workspace_path + '\\'  + fc_name

print("Copying features from 'General_Offense' to 'MoonWater_copy_fc' within the 'Police.gdb'...")
#copy features from one feature class to another
#arcpy.CopyFeatures_management (in_features, out_feature_class, {config_keyword}, {spatial_grid_1}, {spatial_grid_2}, {spatial_grid_3})
arcpy.CopyFeatures_management(in_features, out_feature_class)

print("Copy features successful.")