import time 
 
import pandas as pd 
from selenium import webdriver 
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('/usr/local/bin/chromedriver_mac64/chromedriver')
driver.get("https://medicintildyr.dk/?category_ids=c700243e-828c-423b-b477-7f233db01e5d")

time.sleep(2)

scroll_pause_time = 1
screen_height = driver.execute_script("return window.screen.height;")
i = 1

while True: 
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
    i += 1
    time.sleep(scroll_pause_time)
    # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
    scroll_height = driver.execute_script("return document.body.scrollHeight;")  
    # Break the loop when the height we need to scroll to is larger than the total scroll height
    if (screen_height) * i > scroll_height:
        break 


list_url = ([my_elem.get_attribute("href") for my_elem in driver.find_elements(By.CSS_SELECTOR, 'a.drug-card')])

driver.quit()

list_url_content = []
for i in list_url:
    list_url_content.append(i)
    
urls = pd.DataFrame({'url': list_url_content})
#urls.to_csv('urls.csv', index=False)
    
    



