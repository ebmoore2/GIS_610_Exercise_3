#Q13
#From the Blackboard assignment Exercise 3,
#download the zipped directory labeled (‘Question 13’)
#and unzip its contents onto your local computer.
#Then create a file geodatabase. Using the code that we covered in class,
#import all of the shapefiles in the folder to the geodatabase.
#Finally, clip the census tracts that fall within the Maricopa County boundary
#and write them to a new feature class in your geodatabase.
print("Let's save the Q13 shapefiles into a new gdb, and clip all the data to Maricopa County...")

#step 1
#import
#
import os, sys, arcpy
from IPython.display import display
from arcgis.gis import GIS
gis = GIS("pro")
from arcpy import env
env.overwriteOutput = True


#step 2
#set workspace
#
workspace_path = r"C:\Users\Buffie\Documents\1 GIS\610\Exercise_3_ArcPy_test"
env.workspace = workspace_path


#step 3
#set local variables
#
#(for step 4)
fgdb_name = "GIS_610_E3_Q13.gdb"
#
#(for step 5)
Q13shps = "Question_13_shps"
tract = "tl_2018_04_tract.shp"
county = "tl_2018_us_county.shp"
Input_Features1 = workspace_path + "\\" + Q13shps + "\\" + tract
Input_Features2 = workspace_path + "\\" + Q13shps + "\\" + county
Output_Geodatabase = workspace_path + "\\" + fgdb_name
out_name1 = "Tracts_2018"
out_name2 = "US_Counties_2018"
#
#(for step 6)
in_layer = workspace_path + "\\" + fgdb_name + "\\" + out_name2
#SQL where clause
Key1 = "NAME"
Key2 = "Maricopa"
where_clause = """ '{}' = '{}' """.format(Key1,Key2)
#
#(for step 7)
out_name3 = "Maricopa_County_2018"
#
#(for step 8)
in_features = workspace_path + "\\" + fgdb_name + "\\" + out_name1
clip_features = workspace_path + "\\" + fgdb_name + "\\" + out_name3
out_name4 = "Maricopa_Tracts_2018"
out_path4 = workspace_path + "\\" + fgdb_name + "\\" + out_name4


#step 4
#create a gdb
#
print("Creating a gdb...")
arcpy.CreateFileGDB_management(workspace_path, fgdb_name)
print("Done creating a gdb.")



#step 5
#import shapefiles into this new gdb
#
print("Importing shapefiles...")
#arcpy.FeatureClassToFeatureClass_conversion (in_features, out_path, out_name, {where_clause}, {field_mapping}, config_keyword)
arcpy.FeatureClassToFeatureClass_conversion(Input_Features1, Output_Geodatabase, out_name1)
arcpy.FeatureClassToFeatureClass_conversion(Input_Features2, Output_Geodatabase, out_name2)
print("Done importing shapefiles.")


#step 6
#select Maricopa County from Counties layer and export
#
print("Selecting Maricopa County")
#arcpy.SelectLayerByAttribute_management (in_layer_or_view, {selection_type}, {where_clause}, {invert_where_clause})
arcpy.SelectLayerByAttribute_management(in_layer, "NEW_SELECTION", where_clause)
print("Done selecting Maricopa County.")


#step 7
#export selection
### At this point, successfully exported shapefiles, but when trying these next steps, the selection isn't coming through?
###It copies everything without selecting the Maricopa County.
#
print("Export selection...")
arcpy.FeatureClassToFeatureClass_conversion(in_layer, Output_Geodatabase, out_name3, where_clause)
print("Done exporting Maricopa selection.")


#step 8
#clip all the shapefiles into the Maricopa County boundary and copy into a new feature class
#
print("Clipping tracts to Maricopa County...")
#arcpy.Clip_analysis(in_features, clip_features, out_feature_class, {cluster_tolerance})
arcpy.Clip_analysis(in_features, clip_features, out_path4)
print("Done clipping tracts to Maricopa County.")