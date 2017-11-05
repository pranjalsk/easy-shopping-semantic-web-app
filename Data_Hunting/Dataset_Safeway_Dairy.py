# Crawl Safeway website to collect data about dairy products 

import time
import csv
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_path="C:\Python27\chromedriver\chromedriver.exe"
driver=webdriver.Chrome(chrome_path)
wait = WebDriverWait(driver, 10)

dairy = []
dairy_ietm_price = []

driver.get("https://shop.safeway.com/ecom/home")
zipcode=driver.find_element_by_id("Register_ZipCode")
zipcode.send_keys('85281')
driver.find_element_by_name("Browse").click()
driver.find_element_by_xpath('''//*[@id="toPushFooter"]/div[1]/div/div[9]/ul/li[2]/a''').click()

driver.get("https://shop.safeway.com/ecom/shop-by-aisle")
navigationMenu = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "area-navigateMenu")))
unordered_list = navigationMenu.find_elements_by_tag_name('ul')

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Dairy-Eggs-Cheese/Butter-Sour-Cream/Margarine-Spreads")
spreads = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in spreads:
    dairy.append(s.text)
item_price = driver.find_elements_by_class_name("id-price-qty")
for item in item_price:
    itempr = item.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    price = itempr.find_element_by_tag_name('input')
    dairy_ietm_price.append(price.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Dairy-Eggs-Cheese/Butter-Sour-Cream/Butter")
da = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in da:
    dairy.append(item.text)
item_price = driver.find_elements_by_class_name("id-price-qty")
for item in item_price:
    itempr = item.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    price = itempr.find_element_by_tag_name('input')
    dairy_ietm_price.append(price.get_attribute('value'))
    
driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Dairy-Eggs-Cheese/Cheese/SpreadProcessed-Cheese")
spreadcheese = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in spreadcheese:
    dairy.append(s.text)
item_price = driver.find_elements_by_class_name("id-price-qty")
for item in item_price:
    itempr = item.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    price = itempr.find_element_by_tag_name('input')
    dairy_ietm_price.append(price.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Dairy-Eggs-Cheese/Butter-Sour-Cream/Sour-Cream")
cream = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in cream:
    dairy.append(s.text)
item_price = driver.find_elements_by_class_name("id-price-qty")
for item in item_price:
    itempr = item.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    price = itempr.find_element_by_tag_name('input')
    dairy_ietm_price.append(price.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Dairy-Eggs-Cheese/Eggs/Eggs")
eggs = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in eggs:
    dairy.append(s.text)
item_price = driver.find_elements_by_class_name("id-price-qty")
for item in item_price:
    itempr = item.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    price = itempr.find_element_by_tag_name('input')
    dairy_ietm_price.append(price.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Dairy-Eggs-Cheese/Eggs/Eggs")
cotcheese = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in cotcheese:
    dairy.append(s.text)
item_price = driver.find_elements_by_class_name("id-price-qty")
for item in item_price:
    itempr = item.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    price = itempr.find_element_by_tag_name('input')
    dairy_ietm_price.append(price.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Dairy-Eggs-Cheese/Yogurt/Greek-Yogurt")
greekyog = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in greekyog:
    dairy.append(s.text)
item_price = driver.find_elements_by_class_name("id-price-qty")
for item in item_price:
    itempr = item.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    price = itempr.find_element_by_tag_name('input')
    dairy_ietm_price.append(price.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Dairy-Eggs-Cheese/Cheese/Sandwich-Cheese")
sandcheese = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in sandcheese:
    dairy.append(s.text)
item_price = driver.find_elements_by_class_name("id-price-qty")
for item in item_price:
    itempr = item.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    price = itempr.find_element_by_tag_name('input')
    dairy_ietm_price.append(price.get_attribute('value'))



driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Dairy-Eggs-Cheese/Milk-Cream/Milk")
milk = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in milk:
    dairy.append(s.text)
item_price = driver.find_elements_by_class_name("id-price-qty")
for item in item_price:
    itempr = item.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    price = itempr.find_element_by_tag_name('input')
    dairy_ietm_price.append(price.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Dairy-Eggs-Cheese/Milk-Cream/Creamer")
creamer = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in creamer:
    dairy.append(s.text)
item_price = driver.find_elements_by_class_name("id-price-qty")
for item in item_price:
    itempr = item.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    price = itempr.find_element_by_tag_name('input')
    dairy_ietm_price.append(price.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Dairy-Eggs-Cheese/Milk-Cream/Milk-Alternatives")
milkalt = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in milkalt:
    dairy.append(s.text)
item_price = driver.find_elements_by_class_name("id-price-qty")
for item in item_price:
    itempr = item.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    price = itempr.find_element_by_tag_name('input')
    dairy_ietm_price.append(price.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Dairy-Eggs-Cheese/Milk-Cream/Milk--Flavored")
flavmilk = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in flavmilk:
    dairy.append(s.text)
item_price = driver.find_elements_by_class_name("id-price-qty")
for item in item_price:
    itempr = item.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    price = itempr.find_element_by_tag_name('input')
    dairy_ietm_price.append(price.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Dairy-Eggs-Cheese/Milk-Cream/Milk--Lactose-Free")
lactmilk = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in lactmilk:
    dairy.append(s.text)
item_price = driver.find_elements_by_class_name("id-price-qty")
for item in item_price:
    itempr = item.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    price = itempr.find_element_by_tag_name('input')
    dairy_ietm_price.append(price.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Dairy-Eggs-Cheese/Yogurt/Yogurt")
yogurt = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in yogurt:
    dairy.append(s.text)
item_price = driver.find_elements_by_class_name("id-price-qty")
for item in item_price:
    itempr = item.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    price = itempr.find_element_by_tag_name('input')
    dairy_ietm_price.append(price.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Dairy-Eggs-Cheese/Yogurt/Kids-Yogurt")
kidsyog = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in kidsyog:
    dairy.append(s.text)
item_price = driver.find_elements_by_class_name("id-price-qty")
for item in item_price:
    itempr = item.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    price = itempr.find_element_by_tag_name('input')
    dairy_ietm_price.append(price.get_attribute('value'))

csv_file = open('CSV/Safeway_Dairy.csv', 'wb')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Product', 'Price'])
for i in range(len(dairy)):
    csv_writer.writerow([dairy[i],dairy_ietm_price[i]])
csv_file.close()

print 'CSV loaded'
    

