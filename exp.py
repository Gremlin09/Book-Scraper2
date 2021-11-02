import warnings
import time
from selenium import webdriver
warnings.filterwarnings(action='ignore')
options= webdriver.ChromeOptions()
#options.add_argument('start-maximized')
driver= webdriver.Chrome()
driver.get("https://www.goodreads.com/search?q=")
search_box = driver.find_element_by_xpath('//*[@id="search_query_main"]')
book=input('enter book name')
search_box.send_keys(book)
button=driver.execute_script("return document.querySelector('.searchBox__button.searchBox--large__button')")
driver.execute_script("arguments[0].click();",button)
try:
    popup=driver.execute_script("return document.querySelector('body > div:nth-child(3) > div > div > div.modal__close > button')")
    driver.execute_script("arguments[0].click();", popup)
except: pass
book=driver.execute_script("return document.querySelector('.bookTitle span')")
driver.execute_script("arguments[0].click();",book)
try:
	more=driver.execute_script("return document.querySelector('#description > a')")
	driver.execute_script("arguments[0].click();",more)
	#des=driver.execute_script("return document.querySelector('.selectorgadget_selected').textContent")
except: pass
des = driver.execute_script("return document.querySelector('#description span').textContent")
time.sleep(2)
print(des)
driver.quit()
