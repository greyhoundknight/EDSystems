#int() returns the value or string as a whole number, can be negative.
#float() returns the value or string as a decimal, can be negative.

#MODULES
import os
import json
import csv
import math

#DIRECTORY
os.chdir('C:\\Users\\micha\\Saved Games\\Frontier Developments\\Elite Dangerous\\ED Mission Tracker\\Factions')
#print(os.getcwd())   #PRINTS THE DIRECTORY PATH

#LOAD JSON DATA
data = json.load(open('systems_populated.json', 'r')) #JSON INPUT FILE
d = data
num_lines = sum(1 for line in data) - 1
print(num_lines)

# LOAD CSV DATA
potFile = open('All Systems.csv', 'r')
potReader = csv.reader(potFile)
potData = list(potReader)
p = potData

# WRITE TO CSV
outF = open('Systems Comparison24.csv', 'w', newline = '') #CSV OUTPUT FILE
outW = csv.writer(outF)
outW.writerow(['Allegiance', 'System ID', 'Name', 'Sol (Ly)', '', 'Allegiance', 'System ID', 'Name', 'Distance', 'Nearby Systems'])

for i in range(num_lines): 
    xi = p[i][2]
    yi = p[i][3]
    zi = p[i][4]

    sysnum = 1
    for n in range(num_lines): 
        xn = d[n]['x']
        yn = d[n]['y']
        zn = d[n]['z']
        sqrt = math.sqrt((float(xi)-float(xn))**2 + (float(yi)-float(yn))**2 + (float(zi)-float(zn))**2)
        if float(sqrt) <= 15.0 and not float(sqrt) == 0.0:    #Ly DISTANCE LIMIT
            sysnum = sysnum + 1

    if int(sysnum) != 1 and int(sysnum) <= 2:        #SYSTEM LIMIT
        solrt = math.sqrt((float(xi)-float(0))**2 + (float(yi)-float(0))**2 + (float(zi)-float(0))**2)
        for n in range(num_lines):
            xn = d[n]['x']
            yn = d[n]['y']
            zn = d[n]['z']
            sqrt = math.sqrt((float(xi)-float(xn))**2 + (float(yi)-float(yn))**2 + (float(zi)-float(zn))**2)
            if float(sqrt) <= 10.0 and not float(sqrt) == 0.0:    #Ly DISTANCE LIMIT
                subsysnum = 0
                for m in range(num_lines):
                    xm = d[m]['x']
                    ym = d[m]['y']
                    zm = d[m]['z']
                    subsqrt = math.sqrt((float(xm)-float(xn))**2 + (float(ym)-float(yn))**2 + (float(zm)-float(zn))**2)
                    if float(subsqrt) <= 15.0 and not float(subsqrt) == 0.0:    #Ly DISTANCE LIMIT
                        subsysnum = subsysnum + 1
                outW.writerow([p[i][5], p[i][0], p[i][1], solrt, '', p[n][5], d[n]['id'], d[n]['name'], sqrt, subsysnum])
                
    print ('Processed ' + str(i+1) + ' of ' + str(num_lines) + ' Systems')

outF.close()
input()
