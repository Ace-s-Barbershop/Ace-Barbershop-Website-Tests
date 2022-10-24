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
driver.get('http://localhost:5500/')
driver.maximize_window()
# Wait for 2 seconds
time.sleep(2)

# Nagivate to Services 
link = driver.find_element(By.LINK_TEXT, 'SERVICES')
link.click()

#Wait for 2 seconds
time.sleep(2)
# Nagivate to About Us
link = driver.find_element(By.LINK_TEXT, 'ABOUT US')
link.click()

#Wait for 2 seconds
time.sleep(2)
# Nagivate to Appointment. Since no signed in user, should navigate to Sign In View
link = driver.find_element(By.LINK_TEXT, "APPOINTMENT")
link.click()
time.sleep(2)

# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")