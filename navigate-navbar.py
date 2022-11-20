# Import the following modules
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Get GoogleDriver
driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))

# Go to Ace's Barbershop Website and maximize the window
driver.get('http://acesbarber.shop')
driver.maximize_window()
# Wait for 5 seconds
time.sleep(5)

# Nagivate to Services 
link = driver.find_element(By.LINK_TEXT, 'SERVICES')
link.click()

#Wait for 5 seconds
time.sleep(5)
# Nagivate to Barbers Profile 
link = driver.find_element(By.LINK_TEXT, "BARBERS")
link.click()

#Wait for 5 seconds
time.sleep(5)
# Nagivate to Contact Information
link = driver.find_element(By.LINK_TEXT, "CONTACT")
link.click()

#Wait for 5 seconds
time.sleep(5)
# Nagivate to About Us
link = driver.find_element(By.LINK_TEXT, "ABOUT US")
link.click()

#Wait for 5 seconds
time.sleep(5)
# Nagivate to Home
link = driver.find_element(By.LINK_TEXT, "ACE'S BARBERSHOP")
link.click()
time.sleep(5)

# End test
driver.quit()
