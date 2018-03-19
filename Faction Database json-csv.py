#MODULES
import os
import json
import csv

#DIRECTORY
os.chdir('C:\\Users\\micha\\Saved Games\\Frontier Developments\\Elite Dangerous\\ED Mission Tracker\\Factions')
print(os.getcwd())

#LOAD .JSON DATA
data = json.load(open('factions.json', 'r'))
d = data

#COUNT LINES IN FILE FOR RANGE
num_lines = sum(1 for line in data)
print(num_lines)

#WRITE TO CSV
outF = open('Faction Database.csv', 'w', newline = '')
outW = csv.writer(outF)
outW.writerow(['Faction ID', 'Name', 'Allegiance', 'Government', 'State'])


for n in range(num_lines):
    outW.writerow([d[n]['id'], d[n]['name'], d[n]['allegiance'], d[n]['government'], d[n]['state']])

outF.close()
print('Faction Database has been updated.')
input()
