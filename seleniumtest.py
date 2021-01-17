from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
url='https://www.snapdeal.com/'
driver = webdriver.Chrome('./chromedriver')
driver.get(url)
sr=driver.find_element_by_xpath('//*[@id="inputValEnter"]')
sr.send_keys('phone')
driver.find_element_by_xpath('//*[@id="sdHeader"]/div[4]/div[2]/div/div[2]/button').click()