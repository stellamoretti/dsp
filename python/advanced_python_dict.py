# ADVANCED PYTHON EXERCISES
# Part III - Dictionary

import csv
import re
import pprint
from collections import defaultdict

#-----------------------------------------------------------------------------#


# Open and read CSV file:

with open('faculty.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    dict_list = []
    for row in reader:
        dict_list.append(row)

#pprint.pprint(dict_list)

# Clean dictionary (remove whitespace from keys and values):

def clean_dictionary():
    clean_dict_list = []
    for d in dict_list:
        clean_d = {k.strip():v.strip() for k, v in d.iteritems()}
        clean_dict_list.append(dict(clean_d))
    return clean_dict_list

clean_dict_list = clean_dictionary()

#pprint.pprint(clean_dict_list)

#-----------------------------------------------------------------------------#

# Split name into first name and last name, delete full name key

def split_name():
    for d in clean_dict_list:
        n = d['name']
        name = re.search(r'(\S+)\s(\S+)\s*(\S*)',n)
        name_split = name.group(1,2,3)
        if name.group(3) == '':
            first_name = name.group(1)
            surname = name.group(2)
        else:
            first_name = ' '.join(name.group(1,2))
            surname = name.group(3)
        d.update({'first name': first_name, 'surname': surname})
        del d['name']
    return clean_dict_list

new_dict_list = split_name()

#pprint.pprint(new_dict_list)

#-----------------------------------------------------------------------------#

# Shorten the title for each faculty member (Associate Professor, Assistannt
# Professor or Professor)

def short_title():
    for d in new_dict_list:
        t = d['title']
        match1 = re.search(r'Assi.+',t)
        if match1:
            d.update({'title': 'Assistant Professor'})
        match2 = re.search(r'Asso.+',t)
        if match2:
            d.update({'title': 'Associate Professor'})
        match3 = re.search(r'Prof.+',t)
        if match3:
            d.update({'title': 'Professor'})
    return new_dict_list

newer_dict_list = short_title()

#pprint.pprint(newer_dict_list)

#-----------------------------------------------------------------------------#

# Q6
# Rearrange dictionary and group by surname

def create_faculty_dict():
    faculty_dict = defaultdict(list)
    for d in newer_dict_list:
        k = d['surname']
        v = [d['degree'], d['title'], d['email']]
        faculty_dict[k].append(v)
    return faculty_dict

faculty_dict = create_faculty_dict()

#pprint.pprint(faculty_dict)

#-----------------------------------------------------------------------------#

# Q7
# Rearrange keys in faculty dictionary

def create_professor_dict():
    professor_dict = {}
    for d in newer_dict_list:
        k = (d['first name'],d['surname'])
        v = [d['degree'], d['title'], d['email']]
        professor_dict.update({k:v})
    return professor_dict

professor_dict = create_professor_dict()

#print professor_dict

#-----------------------------------------------------------------------------#

# Q8
# Put professor dictionary in alphabetical order by surname

def create_professor_dict_2():
    professor_dict_2 = {}
    for d in newer_dict_list:
        k = (d['surname'],d['first name'])
        v = [d['degree'], d['title'], d['email']]
        professor_dict_2.update({k:v})
    return sorted(professor_dict_2.items())

professor_dict_2 = create_professor_dict_2()

#print professor_dict_2

#
