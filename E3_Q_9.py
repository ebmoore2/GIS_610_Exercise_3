#Q9
#Create a feature class (you may re-use the geodatabase from Question 5).
#Add a field to your feature class. Then add a domain to the just created field.
#Finally, add at least 5 values to your domain. (*Your domain may be of any type)

import os, sys, arcpy
from arcpy import env
env.overwriteOutput = True

#set local variables
workspace_path = r"C:\Users\Buffie\Documents\1 GIS\610\Exercise_3_ArcPy_test\Police.gdb"
env.workspace = workspace_path
fc_name = "MoonRocks"
fc_path = workspace_path + '\\' + fc_name
new_field = "RockType"
domain_name = "Types"
SRDefinition="PROJCS['WGS_1984_Web_Mercator_Auxiliary_Sphere',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Mercator_Auxiliary_Sphere'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',0.0],PARAMETER['Standard_Parallel_1',0.0],PARAMETER['Auxiliary_Sphere_Type',0.0],UNIT['Meter',1.0]];-22041257.773878 -33265068.6042249 10000;-100000 10000;-100000 10000;0.001;0.001;0.001;IsHighPrecision"

#create domains with 5 different values to the domain
#CreateDomain_management (in_workspace, domain_name, {domain_description}, {field_type}, {domain_type}, {split_policy}, {merge_policy})
  
arcpy.CreateDomain_management(workspace_path, domain_name, 'This is the predominant rock of the polygon region.', 'TEXT', 'CODED', 'DUPLICATE', 'DEFAULT')

#AddCodedValueToDomain_management (in_workspace, domain_name, code, code_description)
arcpy.AddCodedValueToDomain_management(workspace_path, domain_name, 0, 'MareBasalt_Lowland')
arcpy.AddCodedValueToDomain_management(workspace_path, domain_name, 1, 'Anorthosite_Highland')
arcpy.AddCodedValueToDomain_management(workspace_path, domain_name, 2, 'ImpactMelt')
arcpy.AddCodedValueToDomain_management(workspace_path, domain_name, 3, 'ImpactBreccia')
arcpy.AddCodedValueToDomain_management(workspace_path, domain_name, 4, 'Regolith')

print('Done adding Domains')

#create new feature class
arcpy.CreateFeatureclass_management(out_path=workspace_path
                                    , out_name=fc_name
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
print('Done creating feature class')

#add a field to feature class
#AddField_management (in_table, field_name, field_type, {field_precision}, 
#{field_scale}, {field_length}, {field_alias}, {field_is_nullable}, {field_is_required}, {field_domain})
arcpy.AddField_management(fc_path, new_field,'TEXT','','','500','new_field','NULLABLE','NON_REQUIRED','' )

#set domain to the field
#AssignDomainToField_management (in_table, field_name, domain_name, {subtype_code})
arcpy.AssignDomainToField_management(fc_path, new_field, domain_name)

print('Done adding field information')

#results statements
print('All done. Your fc was created at ' + workspace_path)
print('Your feature class is called ' + fc_name)
print("The field added is called 'new_field', and the domains are set.")