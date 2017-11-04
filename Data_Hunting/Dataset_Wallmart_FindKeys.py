# to Extract catagories from the wallmart api

import urllib2
import json
import csv

url = 'http://api.walmartlabs.com/v1/taxonomy?format=json&key=' + 'fnx5k2fpwxjcmhh6ncrwtg2v'
dict_product_catagories = json.load(urllib2.urlopen(url))

wallmart_product_catagories = open('CSV/Walmart_Catagories.csv', 'w')
csvwriter = csv.writer(wallmart_product_catagories)
for parent in dict_product_catagories['categories']:
    csvwriter.writerow([parent['id'], parent['name'], parent['path']])
    if 'children' in parent.keys():
        for child_1 in parent['children']:
            csvwriter.writerow([child_1['id'], child_1['name'], child_1['path']])
            if 'children' in child_1.keys():
                for child_2 in child_1['children']:
                    csvwriter.writerow([child_2['id'], child_2['name'], child_2['path']])

wallmart_product_catagories.close()    
print 'CSV Loaded'

