from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
find = driver.find_element
try:
    driver.get('https://the-internet.herokuapp.com/')
    find(By.LINK_TEXT, 'Form Authentication').click()
    find(By.ID, 'username').clear()
    find(By.ID, 'username').send_keys('tomsmith')
    find(By.ID, 'password').clear()
    find(By.ID, 'password').send_keys('SuperSecretPassword!')
finally:
    driver.quit()