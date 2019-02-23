#Q8
#Return the count of records in the CallsforService feature class.

import os, sys, arcpy
from arcpy import env
env.overwriteOutput = True

#set local variables
workspace_path = r"C:\Users\Buffie\Documents\1 GIS\610\Exercise_3_ArcPy_test\Police.gdb"
env.workspace = workspace_path
fc_to_count = "CallsforService"
in_rows = workspace_path + "\\" + fc_to_count

#get count
print("How many calls for service are in this dataset of police calls?")
#arcpy.GetCount_management (in_rows)
print("There are...")
print(arcpy.GetCount_management(in_rows))
print("calls.")