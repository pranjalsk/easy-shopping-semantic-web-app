# This code extracts all the Bakery products data from Safeway.com
# and makes csv file of the same

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv
chrome_path="C:\Python27\chromedriver\chromedriver.exe"
driver=webdriver.Chrome(chrome_path)
wait = WebDriverWait(driver, 10)
driver.get("https://shop.safeway.com/ecom/home")
inputZip=driver.find_element_by_id("Register_ZipCode")
inputZip.send_keys('85281')
driver.find_element_by_name("Browse").click()
driver.find_element_by_xpath('''//*[@id="toPushFooter"]/div[1]/div/div[9]/ul/li[2]/a''').click()
driver.get("https://shop.safeway.com/ecom/shop-by-aisle")
menu = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "area-navigateMenu")))
unordered_list = menu.find_elements_by_tag_name('ul')
alcohol = []
alcohol_price = []
# Scraping all alcohol items and their prices
driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Wine-Beer-Spirits/Beer-Ciders-Malts/Cider")
cider = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in cider:
    alcohol.append(item.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    alcohol_price.append(pri.get_attribute('value'))
    
driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Wine-Beer-Spirits/Beer-Ciders-Malts/Craft-Microbrew")
craft_microbrews = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in craft_microbrews:
    alcohol.append(s.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    alcohol_price.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Wine-Beer-Spirits/Beer-Ciders-Malts/Imported-Beer")
imported_beer = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in imported_beer:
    alcohol.append(s.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    alcohol_price.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Wine-Beer-Spirits/Domestic-Wine/Red--Cabernet-Sauvignon")
red_caberber_sauvignon = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in red_caberber_sauvignon:
    alcohol.append(s.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    alcohol_price.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Wine-Beer-Spirits/Domestic-Wine/Red--Merlot")
red_merlot = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in red_merlot:
    alcohol.append(s.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    alcohol_price.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Wine-Beer-Spirits/Domestic-Wine/White--Chardonnay")
white_chardonnay = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in white_chardonnay:
    alcohol.append(s.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    alcohol_price.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Wine-Beer-Spirits/Domestic-Wine/White--Riesling")
white_riesling = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in white_riesling:
    alcohol.append(s.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    alcohol_price.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Wine-Beer-Spirits/Domestic-Wine/Red--Pinot-Noir")
red_pinot_noir = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in red_pinot_noir:
    alcohol.append(s.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    alcohol_price.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Wine-Beer-Spirits/Imported-Wine/Italian-Wines")
italian_wines = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in italian_wines:
    alcohol.append(s.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    alcohol_price.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Wine-Beer-Spirits/Specialty-Wine-Champagne/Champagne-Sparkling-Wine")
champage = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in champage:
    alcohol.append(s.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    alcohol_price.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Wine-Beer-Spirits/Spirits/Whiskey")
whiskey = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in whiskey:
    alcohol.append(s.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    alcohol_price.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Wine-Beer-Spirits/Spirits/Scotch")
scotch = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in scotch:
    alcohol.append(s.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    alcohol_price.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Wine-Beer-Spirits/Spirits/Vodka")
vodka = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in vodka:
    alcohol.append(s.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    alcohol_price.append(pri.get_attribute('value'))

# Writing stuff to csv
title = 'Safeway_alcohol.csv'
location = 'E:\\Studies\\ASU MS in SE\\Fall 2017\\SER 594\\Project\\' + title
csv_file = open(location, 'wb')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Product', 'Price'])
for i in range(len(alcohol)):
    csv_writer.writerow([alcohol[i],alcohol_price[i]])
csv_file.close()


