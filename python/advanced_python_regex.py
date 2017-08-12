# ADVANCED PYTHON EXERCISES

import csv
import re
import pprint

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

# Q1 - Find how many different degrees there are, and their frequencies

def count_degrees():
    degrees = [c['degree'] for c in clean_dict_list]
    split_degrees =[]
    for s in degrees:
        split_degrees.extend(s.split(' '))
    return {deg: split_degrees.count(deg) for deg in split_degrees}

degrees_count = count_degrees()

print "There are %d different types of degrees." % len(degrees_count)
pprint.pprint(degrees_count)

#-----------------------------------------------------------------------------#

# Q2 - Find how many different titles there are, and their frequencies

def discover_titles():
    return [c['title'] for c in clean_dict_list]

titles = discover_titles()
#print titles

def count_titles():
    return {t: titles.count(t) for t in titles}

titles_count = count_titles()
#pprint.pprint(titles_count)

def match_titles():

    asso = re.compile('Associate.*')
    asso_list = filter(asso.match, titles)
    print "There are %d Associate Professors." % len(asso_list)

    assi = re.compile('Assistant.*')
    assi_list = filter(assi.match, titles)
    print "There are %d Assistant Professors." % len(assi_list)

    prof = re.compile('Prof.*')
    prof_list = filter(prof.match, titles)
    print "There are %d Professors." % len(prof_list)

match_titles()

#-----------------------------------------------------------------------------#

# Q3 - Search for email addresses and put them in a list. Print the list of
# email addresses.

def search_emails():
    return [c['email'] for c in clean_dict_list]

emails = search_emails()
pprint.pprint(emails)

def count_domains():
    domains = []
    for e in emails:
        domain = re.search('@[\w.]+',e)
        domains.append(domain.group())
    #pprint.pprint(domains)
    return {do: domains.count(do) for do in domains}

domains_count = count_domains()
pprint.pprint(domains_count)
