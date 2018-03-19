#todo - add print lines saying what the script is currently doing. add the ability specific the user name for the directory path.

#MODULES
import os
import json
import csv

#DIRECTORY
os.chdir('C:\\Users\\micha\\Saved Games\\Frontier Developments\\Elite Dangerous\\ED Mission Tracker\\Factions')
#print(os.getcwd())

#JSON DATA
data = json.load(open('stations.json', 'r')) #json target file
d = data

num_lines = sum(1 for line in data) #COUNTS LINES FOR RANGE
print(num_lines)

#WRITE TO CSV
outF = open('Station Database.csv', 'w', newline = '') #opens target csv
outW = csv.writer(outF)
outW.writerow(['Station ID', 'Name', 'System ID', 'Landing Pad', 'Arrival Distance', 'Type'])

for n in range(num_lines):
    outW.writerow([d[n]['id'], d[n]['name'], d[n]['system_id'], d[n]['max_landing_pad_size'], d[n]['distance_to_star'], d[n]['type'], d[n]['has_docking']])
    
print('Station Database has been updated.')
input()
