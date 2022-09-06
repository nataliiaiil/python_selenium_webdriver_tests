from selenium import webdriver

driver = webdriver.Firefox()
try:
    driver.get('https://google.com/')
finally:
    driver.quit()