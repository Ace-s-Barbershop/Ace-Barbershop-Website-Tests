#Import the following modules
import selenium
import time
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Ask the tester a valid username and password
username = input("Please provide a valid email: ")
password = getpass()

# Get GoogleDriver
driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))

# Go to Ace's Barbershop Website and maximize the window
driver.get('http://acesbarber.shop')
driver.maximize_window()
# Wait for 5 seconds
time.sleep(5)

# Nagivate to sidebar 
link = driver.find_element(By.CSS_SELECTOR, '.css-ad28e7')
link.click()

#Wait for 5 seconds
time.sleep(5)
# Nagivate to Log In
link = driver.find_element(By.XPATH, "//span[. = 'Login']")
link.click()

# Wait for 5 seconds
time.sleep(5)
# Log in with username and password provided by tester. After succesful login, it should navigate to Profile View with user info
driver.find_element(By.ID, 'loginpage-username').send_keys(username)
time.sleep(5)
driver.find_element(By.ID, 'loginpage-password').send_keys(password)
time.sleep(5)
driver.find_element(By.ID, 'loginpage-button').click()

# Wait for 5 seconds
time.sleep(5)
# Nagivate to sidebar again
link = driver.find_element(By.CSS_SELECTOR, '.css-ad28e7')
link.click()

#Wait for 5 seconds
time.sleep(5)
# Nagivate to Appointments. Since there is a signed user, the appointments views should render properly
link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(((By.XPATH, "//span[. = 'Request an Appointment']"))))
link.click()

# Wait for 5 seconds
time.sleep(5)
# Nagivate to sidebar again
link = driver.find_element(By.CSS_SELECTOR, '.css-ad28e7')
link.click()

#Wait for 5 seconds
time.sleep(5)
# Nagivate to Services
link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(((By.XPATH, "//span[. = 'Services']"))))
link.click()

# Wait for 5 seconds
time.sleep(5)
# Nagivate to sidebar again
link = driver.find_element(By.CSS_SELECTOR, '.css-ad28e7')
link.click()

#Wait for 5 seconds
time.sleep(5)
# Nagivate to Contact Information
link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(((By.XPATH, "//span[. = 'Contact Information']"))))
link.click()

# Wait for 5 seconds
time.sleep(5)
# Nagivate to sidebar again
link = driver.find_element(By.CSS_SELECTOR, '.css-ad28e7')
link.click()

#Wait for 5 seconds
time.sleep(5)
# Nagivate to About Us
link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(((By.XPATH, "//span[. = 'About Us']"))))
link.click()

# Wait for 5 seconds
time.sleep(5)
# Nagivate to sidebar again
link = driver.find_element(By.CSS_SELECTOR, '.css-ad28e7')
link.click()

#Wait for 5 seconds
time.sleep(5)
# Nagivate to Home
link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(((By.XPATH, "//span[. = 'Home']"))))
link.click()
time.sleep(5)

# End test
driver.quit()
