#For extracting products from the Wallmart api
import json
import csv
import urllib2
import sys;
reload(sys);
sys.setdefaultencoding("utf8")

for i in range(0,6):
	if i == 0:
		csv_title = 'Walmart_frozenfruits.csv'
		url = 'http://api.walmartlabs.com/v1/paginated/items?format=json&category='
		product_key = '976759_976791_1001413'
	elif i == 1:
		csv_title = 'Walmart_frozenveg.csv'
		url = 'http://api.walmartlabs.com/v1/paginated/items?format=json&category='
		product_key = '976759_976791_1001424'
	elif i == 2:
		csv_title = 'Walmart_Bakery.csv'
		url = 'http://api.walmartlabs.com/v1/paginated/items?format=json&category=' 
		product_key = '976759_1071964_976779'
	elif i == 3:
		csv_title = 'Walmart_Dairy.csv'
		url = 'http://api.walmartlabs.com/v1/paginated/items?format=json&category='
		product_key = '976759_1071964_976788'
	elif i == 4: 
		csv_title = 'Walmart_alcohol.csv'
		url = 'http://api.walmartlabs.com/v1/paginated/items?format=json&category='
		product_key = '4044_90548_104900'
	elif i == 5: 
		csv_title = 'Walmart_meat.csv'
		url = 'http://api.walmartlabs.com/v1/paginated/items?format=json&category='
		product_key = '976759_1071964_976796'
	
	csv_File = open('Wallmart_Products_CSVs/' + csv_title, 'w')
	csvwriter = csv.writer(csv_File)
	
	csvwriter.writerow(['Prod_id', 'Prod_name', 'Prod_price', 'Prod_size', 'Prod_stock', 'Prod_brand','Prod_Model', 'Prod_Desc'])
	
	request_url = url + product_key +'&apiproduct_key=fnx5k2fpwxjcmhh6ncrwtg2v'
	json_obj = urllib2.urlopen(request_url)
	data_dict = json.load(json_obj)
	
	for item in data_dict['items']:
		prod_id       = item['itemId']
		prod_name     = item['name']
		prod_price    = ''
		prod_size     = ''
		prod_brand    = ''
		prod_stock    = ''
		prod_model    = ''
		prod_desc     = ''
		if 'salePrice' in item.product_keys(): 
			prod_price= item['salePrice']
		
		if 'size' in item.product_keys():
			prod_size = item['size']
		
		if 'stock' in item.product_keys():
			prod_stock = item['stock']
		
		if 'brandName' in item.product_keys() and 'modelNumber' in item.product_keys():
			prod_brand = item['brandName']
			prod_model = item['modelNumber']
			
		if 'shortDescription' in item.product_keys():
			prod_desc = item['shortDescription']
		
		csvwriter.writerow([prod_id, prod_name, prod_price, prod_size, prod_stock, prod_brand,prod_model, prod_desc])

	csv_File.close() 
	print 'CSV Loaded'
  
