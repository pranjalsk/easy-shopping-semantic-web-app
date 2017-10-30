# Source:Wallmart API
# API KEY: AIzaSyBs6Av8AeOqVL_cnEhxe7dmjtPqcFFrwM0

#Walmart Stores Location using the Walmart API.
import csv
import sys
import urllib2
import json
reload(sys)
sys.setdefaultencoding("utf8")

apiKey = 'fnx5k2fpwxjcmhh6ncrwtg2v'
url = 'http://api.walmartlabs.com/v1/stores?format=json&city=' + 'tempe' + '&apiKey=' + apiKey
dict_locations = json.load(urllib2.urlopen(url))

csv_file = open('CSV/Walmart_Stores.csv', 'w')
csvwriter = csv.writer(csv_file)
csvwriter.writerow(['Store', 'Store_name', 'Latitude', 'Longitude', 'Street_Address', 'Zip', 'Store_Phone_Num'])

for store in dict_locations:
	Street_Address = store['streetAddress'] + ', ' +store['city'] + ', ' + store['stateProvCode']
	csvwriter.writerow(['Walmart', store['name'], store['coordinates'][1], store['coordinates'][0], Street_Address, store['zip'], store['phoneNumber']])	

csv_file.close()
print 'CSV Loaded'
