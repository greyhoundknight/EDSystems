#todo - add print lines saying what the script is currently doing. add the ability specific the user name for the directory path.

#MODULES
import os
import json
import csv

#DIRECTORY
os.chdir('C:\\Users\\micha\\Saved Games\\Frontier Developments\\Elite Dangerous\\ED Mission Tracker\\Factions')
#print(os.getcwd())

#JSON DATA
data = json.load(open('systems_populated.json', 'r')) #LOADS JSON FILE
d = data

num_lines = sum(1 for line in data) #COUNTS LINES FOR RANGE
print(num_lines)

#WRITE TO CSV
outF = open('Systems Database.csv', 'w', newline = '')
outW = csv.writer(outF)
outW.writerow(['System ID', 'Name', 'x', 'y', 'z', 'Allegiance', 'Economy', 'Power', 'Permit', 'Minor Factions'])

for n in range(num_lines):
    outW.writerow([d[n]['id'], d[n]['name'], d[n]['x'], d[n]['y'], d[n]['z'], d[n]['allegiance'], d[n]['primary_economy'], d[n]['power'], d[n]['needs_permit'], d[n]['minor_faction_presences']])

outF.close()
print('System Database has been updated.')
input()
