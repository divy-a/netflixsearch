
import random
import json
import csv
from fuzzywuzzy import fuzz, process


data = [] 
allData = []
with open('netflixsearch/data/netflix_titles.csv', mode='r', encoding='utf-8') as file:
    csvFile = csv.DictReader(file)
    for lines in csvFile:
        data.append(lines['title'])
        allData.append(lines)


print('money'.startswith('Money Heist: From Tokyo to Berlin'.lower()))


def get_results(query, max_results, adv):
    starts_withs = []
    contains = []
    results = []
    query = query.lower()
    for id, dat in enumerate(data):

        if (len(starts_withs) == int(max_results)):
            break

        if dat.lower().startswith(query):
            starts_withs.append({'id': id,
                                 'data': dat})

        elif query in dat.lower():
            contains.append({'id': id,
                            'data': dat})
            
    results = (starts_withs + contains)[0:int(max_results)]


    print(adv)
    if(adv=='true'):
        
        fuzzy_result = process.extract(
            query, data, scorer=fuzz.token_sort_ratio, limit=10)
        fuzzys = [{'id': r[1], 'data': r[0]} for r in fuzzy_result]

        return get_uniques(starts_withs + contains + fuzzys)[0:int(max_results)]

    else:
        return results

def get_uniques(list):

    seen_ids = []

    unique_objects = []

    for object in list:
        if object['id'] not in seen_ids:
            unique_objects.append(object)
            seen_ids.append(object['id'])

    return unique_objects


if __name__ == '__main__':
    print(get_results('black friday', 10))
