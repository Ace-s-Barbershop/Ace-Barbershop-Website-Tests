# Import the following modules
import selenium
import time
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Ask the tester a valid username and password
username = input("Please provide a valid email: ")
password = getpass()

# Get GoogleDriver
driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))


# Go to Ace's Barbershop Website and navigate to login view and maximize the window
driver.get('https://www.acesbarber.shop/loginPage')
driver.maximize_window()
# Wait for 5 seconds
time.sleep(5)

# Log in with username and password provided by tester. After succesful login, it should navigate to Profile View with user info
driver.find_element(By.ID, 'loginpage-username').send_keys(username)
time.sleep(5)
driver.find_element(By.ID, 'loginpage-password').send_keys(password)
time.sleep(5)
driver.find_element(By.ID, 'loginpage-button').click()
time.sleep(5)

#end test
driver.quit()