import time 
import pandas as pd 
from selenium import webdriver 
from selenium.webdriver.common.by import By
import sys

def prep_items(items, dict, name):
	items = items[1:]
	for j in items: 
		dict[name].append(j)
	return(dict)

# Read in urls of interest 
urls = pd.read_csv('data/prices_pigs.csv')

# Create empty df with headers 
df = pd.DataFrame(columns=['pakning', 'nvr', 'price', 'atc-kode', 'url'])

# Go through each url to gather information
for i in range(0, len(urls)):

    driver = webdriver.Chrome('/usr/local/bin/chromedriver_mac64/chromedriver')

    url = urls['url'].loc[i]
        
    driver.get(url)

    time.sleep(5)

    nvr = driver.find_elements(By.CLASS_NAME, 'package')
    atc = driver.find_elements(By.CLASS_NAME, 'input-row')

    # Get atc-kode 
    search_dict = {
        'ATC-kode':[], 
    }

    output = []
    for i in atc:
        output.append(i.text)

    for i in output: 
        items = i.split('\n')
        items = i.split('\n')

        for j in items: 
            if j in search_dict.keys():
                search_dict = prep_items(items, search_dict, j)
    
    atc_kode = str(search_dict['ATC-kode'][0])

    # Get pakning, nvr, price
    info = []

    for i in nvr: 
        info.append(i.text)

    for i in range(0, len(info)):
         info[i] = info[i].split('\n')
         info[i].append(atc_kode)
         info[i].append(url)
         df.loc[len(df)] = info[i]

    driver.quit()

df.to_csv('data/price_pigs_scraped.csv', index=False)
