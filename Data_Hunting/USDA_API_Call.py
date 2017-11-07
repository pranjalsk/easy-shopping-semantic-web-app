
#Extract nutrient information from USDA

import urllib2
import json
import csv


nutrients = [203, 204, 205, 208, 255, 269, 301]

food_groups = {'0100':'Dairy&Eggs', '0700':'Sausages&Meats', '0900':'Fruit&Juices','1100':'Vegetables&Juices', '1800':'BakedProducts'}

nurture =''
for nutr in nutrients:
	nurture += 'nutrients=' + str(nutr) + '&'

for key in food_groups.keys():
	url = 'http://api.nal.usda.gov/ndb/nutrients?format=json&api_key='+'pblpHteeO6G9DOFARnTXB6kxEQdCmeHVlJcc6MXB'+'&'+nurture+'fg='+key+'&max=1500'
	json_obj = urllib2.urlopen(url)
	data_dict = json.load(json_obj)
	
	title = food_groups[key]+'.csv'
	location = 'E:\\Studies\\ASU MS in SE\\Fall 2017\\SER 594\\Project\\' + title
	food_nutrients = open(location, 'w')
	csvwriter = csv.writer(food_nutrients)
	
	Product_Head=data_dict['report']['groups'][0]['description']
	Prod_total = data_dict['report']['total']
	Foods = data_dict['report']['foods']
	csvwriter.writerow([Product_Head, 'Weight', 'Measure', 'Protein', 'Sugars', 'Fat', 'Carbohydrate', 'Calcium', 'Energy', 'Water'])
	
	for food in Foods:
		Food_nm = food['name']
		Food_wt = food['weight']
		Food_msr= food['measure']
		Prot =str(food['nutrients'][0]['gm']) +' '+ food['nutrients'][0]['unit']
		sugr =str(food['nutrients'][1]['gm']) +' '+ food['nutrients'][1]['unit']
		fat  =str(food['nutrients'][2]['gm']) +' '+ food['nutrients'][2]['unit']
		carb =str(food['nutrients'][3]['gm']) +' '+ food['nutrients'][3]['unit']
		calc =str(food['nutrients'][4]['gm']) +' '+ food['nutrients'][4]['unit']
		ener =str(food['nutrients'][5]['gm']) +' '+ food['nutrients'][5]['unit']
		watr =str(food['nutrients'][6]['gm']) +' '+ food['nutrients'][6]['unit']
		csvwriter.writerow([Food_nm, Food_wt, Food_msr, Prot, sugr, fat, carb, calc, ener, watr])
	print 'CSV Loaded'
	
food_nutrients.close()