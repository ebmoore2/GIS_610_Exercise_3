#Q12
#Retrieve records from the GeneralOffense feature class which meet the following criteria:
#a. Return only records that’re within the last 90 days and have its field locationTranslation = Residence/Home
#Edit: *a.	Return only records that has the OffenseCus = BURGLARY FORCE and have its field locationTranslation = Residence/Home*
#Finally, write the results to a CSV file.
print("Let's get only the crimes that are home burglaries in a csv file...")


#step 1
#import
#
import os, sys, arcpy, datetime, calendar, csv, pprint
from arcpy import env
env.overwriteOutput = True
#pp = pprint.PrettyPrinter(indent=4)


#step 2
#set local variables
#
workspace_path = r"C:\Users\Buffie\Documents\1 GIS\610\Exercise_3_ArcPy_test\Police.gdb"
env.workspace = workspace_path
Gen_Off = "General_Offense"
in_layer = workspace_path + "\\" + Gen_Off


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
#
#Old DateTime Stuff
"""


#step 3
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
                #
                #SQL where clause
                #
V1 = 'locationTranslation'
V2 = 'Residence/Home'
V3 = 'OffenseCustom'
V4 = 'BURGLARY FORCE'
where = """ '{}' = '{}' AND '{}' = '{}' """.format(V1,V2,V3,V4)


#step 4
#select by attribute
#.......when printing Selection to check the results, it prints "General_Offense_Layer2", I don't know what this is doing.
#
#SelectLayerByAttribute_management (in_layer_or_view, {selection_type}, {where_clause}, {invert_where_clause})
arcpy.SelectLayerByAttribute_management(in_layer, "NEW_SELECTION", where)
#this should update in_layer to be selecting, so when you export it only takes the selected records.
print("Selected layer by attributes.")


#step 5
#with open 'w' method & SearchCursor
#
print("Writing to csv file...")
fields = ['OBJECTID', 'shape', 'occ_dt', 'obfAddress', 'x_rand', 'y_rand', 'disclaimer', 'place_name', 'OffenseCustom', 'locationTranslation'] 
outCsv = r"C:\Users\Buffie\Documents\1 GIS\610\Exercise_3_ArcPy_test\HomeBurg_Calls.csv"
#
#
#
#arcpy.SearchCursor(in_table, field_names, {where_clause}, {spatial_reference}, {explode_to_points}, {sql_clause})
# *********************when including the "where" as in where_clause, the csv is just EMPTY**************************
#................without "where" it just exports the entire csv without selecting out "Home/Res" and "BURGLARY FORCE"............
with open(outCsv, 'w', encoding="utf-8", newline='') as new_csv:  
    writer = csv.writer(new_csv)  
    writer.writerow(fields)  # writes header containing list of fields  
    rows = arcpy.da.SearchCursor(in_layer, fields)
    for row in rows:  
        writer.writerow(row)  # writes fc contents to output csv  
    del rows
print("Done writing to csv file.")