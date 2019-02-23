#Q6
#add new field to the feature class "calls for service"


import os, sys, arcpy

from arcpy import env
env.overwriteOutput = True


# set local variables
#current_dir = os.getcwd() 
#Police_gdb = r"C:\Users\Buffie\Documents\1 GIS\610\Exercise_3_ArcPy_test\Police.gdb"
workspace_path = r"C:\Users\Buffie\Documents\1 GIS\610\Exercise_3_ArcPy_test\Police.gdb"
env.workspace = workspace_path
fc_name = "CallsforService"
in_table = workspace_path + '\\'  + fc_name
field = "Crime_Explanation"

#Add a new field to the calls called "Crime_Explanation"
#arcpy.AddField_management (in_table, field_name, field_type, {field_precision}, 
#                     {field_scale}, {field_length}, {field_alias}, {field_is_nullable}, 
#                     {field_is_required}, {field_domain})

arcpy.AddField_management(in_table, field,'TEXT','','','500','Crime_Explanation','NULLABLE','NON_REQUIRED','' )

print("Successfully created new field named 'Crime_Explanation' within 'CallsforService' featureclass.")
print("Calculating this new field may take a minute...")

#If the crime type is a burglary, input "This is a burglary"
#CalculateField_management (in_table, field, expression, {expression_type}, {code_block})

expression = "Reclass(!CFSType!)"
codeblock = """
def Reclass(arg):
    if "Burglary Call" in arg:
        return "This is a burglary"
    else:
        return "This is not a burglary"
"""

arcpy.CalculateField_management(in_table, field, expression, "PYTHON3", codeblock)

print("Successfully calculated field to explain burglary instances.")