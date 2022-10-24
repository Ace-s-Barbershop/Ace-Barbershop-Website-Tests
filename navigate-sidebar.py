#Import the following modules
import selenium
import time
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Get GoogleDriver
driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))

# Ask the tester a valid username and password
username = input("Please provide a valid email: ")
password = getpass()

# Go to Ace's Barbershop Website and maximize the window
driver.get('http://localhost:5500/')
driver.maximize_window()
# Wait for 2 seconds
time.sleep(2)

# Nagivate to sidebar 
link = driver.find_element(By.CSS_SELECTOR, '.css-vubbuv')
link.click()

#Wait for 2 seconds
time.sleep(2)
# Nagivate to Log In
link = driver.find_element(By.LINK_TEXT, 'Login')
link.click()

# Wait for 2 seconds
time.sleep(2)

# Log in with username and password provided by tester. After succesful login, it should navigate to Profile View with user info
driver.find_element(By.ID, 'loginpage-username').send_keys(username)
time.sleep(2)
driver.find_element(By.ID, 'loginpage-password').send_keys(password)
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '.css-s6ckjm').click()

# Wait for 2 seconds
time.sleep(2)
# Nagivate to sidebar again
link = driver.find_element(By.CSS_SELECTOR, '.css-vubbuv')
link.click()

#Wait for 2 seconds
time.sleep(2)
# Nagivate to Appointments. Since there is a signed user, the appointments views should render properly
link = driver.find_element(By.LINK_TEXT, 'Book Appointment')
link.click()

# Wait for 2 seconds
time.sleep(2)
# Nagivate to sidebar again
link = driver.find_element(By.CSS_SELECTOR, '.css-vubbuv')
link.click()

#Wait for 2 seconds
time.sleep(2)
# Nagivate to Home
link = driver.find_element(By.LINK_TEXT, 'Home')
link.click()

# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")