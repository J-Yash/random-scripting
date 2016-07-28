#Python script to login to facebook using Chrome web browser

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
elem = driver.find_element_by_id("email")
elem.send_keys("Username")
elem1 = driver.find_element_by_id("pass")
elem1.send_keys("Password")
elem1.send_keys(Keys.ENTER)


