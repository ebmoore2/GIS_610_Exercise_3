#Q5
#Make a GDB

#Create a geodatabase. Then, using the following list, generate feature classes for each of the
#elements in the list:
#featureList = [‘CapitalCities’, ‘Landmarks’, ‘HistoricPlaces’, ‘StateNames’, ‘Nationalities’,
#‘Rivers’]

import os
import sys
import arcpy

from arcpy import env
env.overwriteOutput = True

#change your feature class name here
fc_name0 = "CapitalCities"
fc_name1 = "Landmarks"
fc_name2 = "HistoricPlaces"
fc_name3 = "StateNames"
fc_name4 = "Nationalities"
fc_name5 = "Rivers"

#output directory here
current_dir = os.getcwd() 
#geodatabase name here
fgdb_name = 'GIS_610_E3_Q5.gdb'
#workspace path here
workspace_path = current_dir + '\\' + fgdb_name

fc_path0 = workspace_path + '\\'  + fc_name0
fc_path1 = workspace_path + '\\'  + fc_name1
fc_path2 = workspace_path + '\\'  + fc_name2
fc_path3 = workspace_path + '\\'  + fc_name3
fc_path4 = workspace_path + '\\'  + fc_name4
fc_path5 = workspace_path + '\\'  + fc_name5
    
#SR Definition
SRDefinition="PROJCS['WGS_1984_Web_Mercator_Auxiliary_Sphere',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Mercator_Auxiliary_Sphere'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',0.0],PARAMETER['Standard_Parallel_1',0.0],PARAMETER['Auxiliary_Sphere_Type',0.0],UNIT['Meter',1.0]];-22041257.773878 -33265068.6042249 10000;-100000 10000;-100000 10000;0.001;0.001;0.001;IsHighPrecision"

#create a gdb
arcpy.CreateFileGDB_management(current_dir, fgdb_name)

#Create the Feature Class(es)
arcpy.CreateFeatureclass_management(out_path=workspace_path
                                    , out_name=fc_name0
                                    , geometry_type="POINT"
                                    , template=""
                                    , has_m="DISABLED"
                                    , has_z="DISABLED"
                                    , spatial_reference=SRDefinition
                                    , config_keyword=""
                                    , spatial_grid_1="0"
                                    , spatial_grid_2="0"
                                    , spatial_grid_3="0"
                                    )
arcpy.CreateFeatureclass_management(out_path=workspace_path
                                    , out_name=fc_name1
                                    , geometry_type="POINT"
                                    , template=""
                                    , has_m="DISABLED"
                                    , has_z="DISABLED"
                                    , spatial_reference=SRDefinition
                                    , config_keyword=""
                                    , spatial_grid_1="0"
                                    , spatial_grid_2="0"
                                    , spatial_grid_3="0"
                                    )
arcpy.CreateFeatureclass_management(out_path=workspace_path
                                    , out_name=fc_name2
                                    , geometry_type="POINT"
                                    , template=""
                                    , has_m="DISABLED"
                                    , has_z="DISABLED"
                                    , spatial_reference=SRDefinition
                                    , config_keyword=""
                                    , spatial_grid_1="0"
                                    , spatial_grid_2="0"
                                    , spatial_grid_3="0"
                                    )
arcpy.CreateFeatureclass_management(out_path=workspace_path
                                    , out_name=fc_name3
                                    , geometry_type="POLYGON"
                                    , template=""
                                    , has_m="DISABLED"
                                    , has_z="DISABLED"
                                    , spatial_reference=SRDefinition
                                    , config_keyword=""
                                    , spatial_grid_1="0"
                                    , spatial_grid_2="0"
                                    , spatial_grid_3="0"
                                    )
arcpy.CreateFeatureclass_management(out_path=workspace_path
                                    , out_name=fc_name4
                                    , geometry_type="POLYGON"
                                    , template=""
                                    , has_m="DISABLED"
                                    , has_z="DISABLED"
                                    , spatial_reference=SRDefinition
                                    , config_keyword=""
                                    , spatial_grid_1="0"
                                    , spatial_grid_2="0"
                                    , spatial_grid_3="0"
                                    )
arcpy.CreateFeatureclass_management(out_path=workspace_path
                                    , out_name=fc_name5
                                    , geometry_type="POLYLINE"
                                    , template=""
                                    , has_m="DISABLED"
                                    , has_z="DISABLED"
                                    , spatial_reference=SRDefinition
                                    , config_keyword=""
                                    , spatial_grid_1="0"
                                    , spatial_grid_2="0"
                                    , spatial_grid_3="0"
                                    )
print("Done creating feature classes")
print("All done. Your fgdb was created at " + workspace_path)
print("Your feature classes are called " + fc_name0 + fc_name1 + fc_name2 + fc_name3 + fc_name4 + fc_name5)
