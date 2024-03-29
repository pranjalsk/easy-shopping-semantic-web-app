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
meat = []
meat_seafood_price = []

driver.get("https://shop.safeway.com/ecom/home")
zipcode=driver.find_element_by_id("Register_ZipCode")
zipcode.send_keys('85281')
driver.find_element_by_name("Browse").click()
driver.find_element_by_xpath('''//*[@id="toPushFooter"]/div[1]/div/div[9]/ul/li[2]/a''').click()

driver.get("https://shop.safeway.com/ecom/shop-by-aisle")
navigationMenu = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "area-navigateMenu")))
unordered_list = navigationMenu.find_elements_by_tag_name('ul')

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Meat-Seafood/Beef/Beef-Steaks")
beefsteaks = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in beefsteaks:
    meat.append(item.text)
item_price = driver.find_elements_by_class_name("id-price-qty")
for item in item_price:
    itempr = item.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    price = itempr.find_element_by_tag_name('input')
    meat_seafood_price.append(price.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Meat-Seafood/Beef/Ground-Beef")
groundbeef = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in groundbeef:
    meat.append(item.text)
item_price = driver.find_elements_by_class_name("id-price-qty")
for item in item_price:
    itempr = item.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    price = itempr.find_element_by_tag_name('input')
    meat_seafood_price.append(price.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Meat-Seafood/Chicken-Turkey/Turkey")
turkey = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in turkey:
    meat.append(item.text)
item_price = driver.find_elements_by_class_name("id-price-qty")
for item in item_price:
    itempr = item.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    price = itempr.find_element_by_tag_name('input')
    meat_seafood_price.append(price.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Meat-Seafood/Chicken-Turkey/Chicken")
chicken = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in chicken:
    meat.append(item.text)
item_price = driver.find_elements_by_class_name("id-price-qty")
for item in item_price:
    itempr = item.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    price = itempr.find_element_by_tag_name('input')
    meat_seafood_price.append(price.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Meat-Seafood/Lamb")
lamb = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in lamb:
    meat.append(item.text)
item_price = driver.find_elements_by_class_name("id-price-qty")
for item in item_price:
    itempr = item.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    price = itempr.find_element_by_tag_name('input')
    meat_seafood_price.append(price.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Meat-Seafood/Fish-Shellfish/Fish")
fish = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in fish:
    meat.append(item.text)
item_price = driver.find_elements_by_class_name("id-price-qty")
for item in item_price:
    itempr = item.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    price = itempr.find_element_by_tag_name('input')
    meat_seafood_price.append(price.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Meat-Seafood/Fish-Shellfish/Shrimp-Prawns")
shrimp = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in shrimp:
    meat.append(item.text)
item_price = driver.find_elements_by_class_name("id-price-qty")
for item in item_price:
    itempr = item.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    price = itempr.find_element_by_tag_name('input')
    meat_seafood_price.append(price.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Meat-Seafood/Fish-Shellfish/Lobster-Crab")
lobster = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in lobster:
    meat.append(item.text)
item_price = driver.find_elements_by_class_name("id-price-qty")
for item in item_price:
    itempr = item.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    price = itempr.find_element_by_tag_name('input')
    meat_seafood_price.append(price.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Meat-Seafood/SausageHot-Dogs-Bacon/Hot-Dogs-Franks")
hotdogs = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in hotdogs:
    meat.append(item.text)
item_price = driver.find_elements_by_class_name("id-price-qty")
for item in item_price:
    itempr = item.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    price = itempr.find_element_by_tag_name('input')
    meat_seafood_price.append(price.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Meat-Seafood/Pork/Ham")
ham = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in ham:
    meat.append(item.text)
item_price = driver.find_elements_by_class_name("id-price-qty")
for item in item_price:
    itempr = item.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    price = itempr.find_element_by_tag_name('input')
    meat_seafood_price.append(price.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Meat-Seafood/Pork/Pork-Chops-Steaks")
porkchops = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in porkchops:
    meat.append(item.text)
item_price = driver.find_elements_by_class_name("id-price-qty")
for item in item_price:
    itempr = item.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    price = itempr.find_element_by_tag_name('input')
    meat_seafood_price.append(price.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Meat-Seafood/Pork/Pork-Roasts-Tenderloin")
porkroasts = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in porkroasts:
    meat.append(item.text)
item_price = driver.find_elements_by_class_name("id-price-qty")
for item in item_price:
    itempr = item.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    price = itempr.find_element_by_tag_name('input')
    meat_seafood_price.append(price.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Meat-Seafood/Salami-Lunch-Meats/Salami")
salami = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in salami:
    meat.append(item.text)
item_price = driver.find_elements_by_class_name("id-price-qty")
for item in item_price:
    itempr = item.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    price = itempr.find_element_by_tag_name('input')
    meat_seafood_price.append(price.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Meat-Seafood/SausageHot-Dogs-Bacon/Bacon")
bacon = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in bacon:
    meat.append(item.text)
item_price = driver.find_elements_by_class_name("id-price-qty")
for item in item_price:
    itempr = item.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    price = itempr.find_element_by_tag_name('input')
    meat_seafood_price.append(price.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Meat-Seafood/SausageHot-Dogs-Bacon/Breakfast-Sausage")
breaksausage = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in breaksausage:
    meat.append(item.text)
item_price = driver.find_elements_by_class_name("id-price-qty")
for item in item_price:
    itempr = item.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    price = itempr.find_element_by_tag_name('input')
    meat_seafood_price.append(price.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Meat-Seafood/SausageHot-Dogs-Bacon/Dinner-Sausage")
dinnersausage = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in dinnersausage:
    meat.append(item.text)
item_price = driver.find_elements_by_class_name("id-price-qty")
for item in item_price:
    itempr = item.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    price = itempr.find_element_by_tag_name('input')
    meat_seafood_price.append(price.get_attribute('value'))


csv_file = open('CSV/Safeway_Meat.csv' + title, 'wb')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Product', 'Price'])
for i in range(len(meat)):
    csv_writer.writerow([meat[i],meat_seafood_price[i]])
csv_file.close()
print 'CSV loaded'
