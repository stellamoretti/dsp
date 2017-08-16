# -*- coding: utf-8 -*-
# The football.csv file contains the results from the English Premier League.
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv
import pprint

'''

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

'''

# Alternative method based on HackerRank guidance:

def read_data(filename):
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)
        goals = list(reader)
        for li in goals:
            li[1:] = map(int, li[1:])
        return goals

goals = read_data('football.csv')

def get_index_with_min_abs_score_difference(goals):
    for team in goals:
        diff = abs(team[5] - team[6])
        team.append(diff)
    min_diff = min([t[8] for t in goals])
    count = 0
    for team in goals:
        if team[8] == min_diff:
            count += 1
    if count > 1:
        return 'There is more than one match.'
    else:
        for team in goals:
            if team[8] == min_diff:
                index_value = goals.index(team)
                return index_value

index_value =  get_index_with_min_abs_score_difference(goals)

def get_team(index_value, parsed_data):
    match = parsed_data[index_value]
    return match[0]

print get_team(index_value, goals)











#
