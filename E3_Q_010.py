#Q10
#Perform a spatial join between the census tracts feature class and the general offense feature class.
print("Let's do a spatial join...")

import os, sys, arcpy
from arcpy import env
env.overwriteOutput = True

#set local variables
workspace_path = r"C:\Users\Buffie\Documents\1 GIS\610\Exercise_3_ArcPy_test\Police.gdb"
env.workspace_path = workspace_path
target_tracts = "Tracts"
join_calls = "General_Offense"
out_calls = "Calls_by_Tracts"
target_features = workspace_path + "\\" + target_tracts
join_features = workspace_path + "\\" + join_calls
out_feature_class = workspace_path + "\\" + out_calls

#join all police call points inside the census tracks they spatially lay within
#SpatialJoin_analysis (target_features, join_features, out_feature_class, 
#{join_operation}, {join_type}, {field_mapping}, {match_option}, {search_radius}, {distance_field_name})
arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class)
print("Successfully joined general offense points to census tracts polygons within new feature class 'Calls_by_Tracts'.")