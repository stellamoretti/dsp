# -*- coding: utf-8 -*-
# The football.csv file contains the results from the English Premier League.
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv
import pprint

with open('football.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    dict_list = []
    for row in reader:
        dict_list.append(row)

#pprint.pprint(dict_list)

# Create dictionary of team / absolute difference between goals for and against

differences = []

for t in dict_list:
    diff = {}
    diff.update({'Team': t['Team'], 'Difference': abs(int(t['Goals']) - int(t['Goals Allowed']))})
    differences.append(dict(diff))

# pprint.pprint(differences)

# Print the team with the smallest difference

answer = min(differences, key=lambda x:x['Difference'])

print answer['Team']
