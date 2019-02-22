#Q12
#Retrieve records from the GeneralOffense feature class which meet the following criteria:
#a. Return only records that’re within the last 90 days and have its field locationTranslation = Residence/Home
#Edit: *a.	Return only records that has the OffenseCus = BURGLARY FORCE and have its field locationTranslation = Residence/Home*
#Finally, write the results to a CSV file.
print("Let's get only the crimes that are home burglaries in a csv file...")

import os, sys, arcpy, datetime, calendar, csv, pprint
from arcpy import env
env.overwriteOutput = True
pp = pprint.PrettyPrinter(indent=4)

#set local variables
#
workspace_path = r"C:\Users\Buffie\Documents\1 GIS\610\Exercise_3_ArcPy_test\Police.gdb"
env.workspace = workspace_path
Gen_Off = "General_Offense"
in_layer = workspace_path + "\\" + Gen_Off
selection_type = "NEW_SELECTION"

"""
#Old DateTime Stuff
#
#https://stackoverflow.com/questions/38794935/python-get-last-month-and-year
#time variables
today = datetime.date.today()
days90 = datetime.timedelta(days=90)
#start_date = datetime.date.today() + datetime.timedelta(-30)
#datetime.datetime.now() - datetime.timedelta(days=30)
past_90_days = (today - days90)
#where clause would include "AND past_90_days = True"

#example from StackOverflow
import datetime, calendar
year = 2014
month = 1
num_days = calendar.monthrange(year, month)[1]
days = [datetime.date(year, month, day) for day in range(1, num_days+1)]
days

#example from StackOverflow
from calendar import Calendar
Calendar().monthdayscalendar(2014,1)
[[0, 0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18, 19], [20, 21, 22, 23, 24, 25, 26], [27, 28, 29, 30, 31, 0, 0]]
month = Calendar().itermonthdates(2014,1)
print [day for day in month if day.month == 1]

#example from StackOverflow
import datetime
d0 = datetime.datetime(year=2014, month=1, day=1)
d1 = datetime.datetime(year=2014, month=2, day=1)
print (d1 - d0).days
31

#example from StackOverflow
from calendar import monthrange
monthrange(2014, 2)
(5, 28)
a = monthrange(2014, 2)
range(1, a[1]+1)
"""


#SQL where clause
#
#use triple quote containers
#EXAMPLE1
#arcpy.SelectLayerByAttribute_management("states", "NEW_SELECTION", 
#                                        "[NAME] = 'California'")
#
#EXAMPLE2
#where = """ "StudyID" = '%s' """ % name
#
#EXAMPLE3, ...<> means not equal
#QF5 = "Week"
#QF6 = "Wk"
#WC4 = """ '{}' <> '{}' AND '{}' <> '' """.format(QF5,QF6,QF6)

#SQL where clause
#
V1 = 'locationTranslation'
V2 = 'Residence/Home'
V3 = 'OffenseCustom'
V4 = 'BURGLARY FORCE'
where = """ '{}' = '{}' AND '{}' = '{}' """.format(V1,V2,V3,V4)

#select by attribute
#.......when printing Selection to check the results, it prints "General_Offense_Layer2", I don't know what this is doing.
#
#SelectLayerByAttribute_management (in_layer_or_view, {selection_type}, {where_clause}, {invert_where_clause})
#Selection = arcpy.SelectLayerByAttribute_management(in_layer, selection_type, where)
#for row in Selection:
#    print(row)
#print("Selected layer by attributes.")


#write selection to csv
#.......For some reason, using the where clause here, this result is just an empty csv with only field headers and nothing else.
#
print("Exporting selection to csv...")
#table to table conversion
#arcpy.TableToTable_conversion(in_rows, out_path, out_name, {where_clause}, {field_mapping}, {config_keyword})
in_rows = in_layer
out_path = r"C:\Users\Buffie\Documents\1 GIS\610\Exercise_3_ArcPy_test"
out_name = "HomeBurg_PoliceCalls.csv"
arcpy.TableToTable_conversion(in_rows, out_path, out_name, where)
print("Done printing to csv file.")


#with open 'w' method
#
#{ERROR, so did a different way, also don't understand, "item.id" does not have an attribute "id"... same with "OBJECTID"...}
#create an array of fields that we want to use as column headers
#fix...OBJECTID,occ_dt,place_name,Offense_Custom,locationTranslation = [],[],[],[],[]
#fix...writer.writerow([OBJECTID, occ_dt, place_name, Offense_Custom, locationTranslation])
#modified from class 12 notes
#fields = ['OBJECTID', 'shape', 'occ_dt', 'obfAddress', 'x_rand', 'y_rand', 'disclaimer', 'place_name', 'OffenseCustom', 'locationTranslation']
#with open(r"C:\Users\Buffie\Documents\1 GIS\610\Exercise_3_ArcPy_test\Police_Calls_90_days.csv", 'w', encoding="utf-8", newline='') as outfile:
#    csvfile = csv.writer(outfile)
#    csvfile.writerow(fields)
#    for item in Selection:
#        row = [item.OBJECTID, item.shape, item.occ_dt, item.obfAddress, item. x_rand, item.y_rand, item.disclaimer, item.place_name, item.OffenseCustom, item.locationTranslation]
#        csvfile.writerow(row)
#        pp.pprint(row)