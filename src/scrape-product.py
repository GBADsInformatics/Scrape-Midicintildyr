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

def search_list(lists, search_string):

	res = any(search_string in sublist for sublist in lists)
	return(res)

urls = pd.read_csv('urls.csv')

for i in range(0, len(urls)):

	driver = webdriver.Chrome('/usr/local/bin/chromedriver_mac64/chromedriver')

	url = urls['url'].loc[i]
	
	driver.get(url)

	time.sleep(2)

	drug_title = driver.find_elements(By.CLASS_NAME, 'drug-title')
	sub_title = driver.find_elements(By.CLASS_NAME, 'input-row subtitle')
	nvr = driver.find_elements(By.CLASS_NAME, 'input-row')

	# make list of items 

	if i == 0:
		break

	output = []
	for i in nvr:
		output.append(i.text)

	for i in drug_title:
		title = i.text

	driver.quit()

	search_dict = {
		'Drug name':[],
		'Drug sub title':[],
		'Aktive substanser':[],
		'Pakning':[], # Need - 
		# When Pris ikke opsylt omit - 
		'NVR':[],
		'Forbrugerpris':[],
		'Dyr':[],
		# Pigs 
		'Tilbageholdelsestid':[],
		'Udleveringsbestemmelse':[],
		'ATC-kode':[],
		'Firma':[],
		'SPC':[],
		'Administrationsveje':[]
	}

	obsolete_price = search_list(output, 'Pris ikke oplyst')
	species_gris = search_list(output, 'Gris')
	species_svin = search_list(output, 'svin')

	for i in output: 
		items = i.split('\n')
		items = i.split('\n')

		for j in items: 
			if j in search_dict.keys():
				search_dict = prep_items(items, search_dict, j)
	
	print('%s;%s;%s;%s;%s;%s' % (title, output[0], obsolete_price, url, species_svin, species_gris))
