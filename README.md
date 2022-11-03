# Ace’s Barbershop Website Selenium Automated Tests

These tests are automated tests using Selenium to test the functionality of Ace's Barbershop Website. Please refer to thie README.md or the System Test report to learn how to run these tests.

## Tools 

* Windows Operating System
* Google Chrome Browser
* Terminal/Powershell
  - Powershell free and available online: https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.2
* Python3
  - Available: https://www.python.org/downloads/
* Selenium Python Plug In (Version 4.5.0)
  - More information: https://selenium-python.readthedocs.io/installation.html
* Webdriver_manager Python Plug In (Version 3.8.4)
* Packaging Python Plug In (Version 21.3)
* ChromeDriver
  - More information: https://chromedriver.chromium.org/downloads


## Setup
1. First make sure you are on a Windows Operating Systems and that you have Google Chrome downloaded
2. Next make sure you have terminal or powershell. If not download using links above in tools
3. First, download Python3. Please follow the link provided in the tools.
4. Pull the GitHub repository provided in the tools to your local machine. Make sure you are on the correct path (Path to the test files). 
  - Example: 
    ```
    C:\Users\user\Desktop\Ace-Barbershop-Website-Tests>
    ```
5. Then make sure you install selenium, webdriver_manager, and packaging. To install those plug ins
  - For example, in terminal/powershell:
    ```
    C:\Users\user\Desktop\Ace-Barbershop-Website-Tests>pip3 install selenium==4.50
    
    C:\Users\user\Desktop\Ace-Barbershop-Website-Tests>pip3 install webdriver_manager==3.8.4

    C:\Users\user\Desktop\Ace-Barbershop-Website-Tests>pip3 install packaging==21.3
    ```
6. To run any test file, file path should be:
    ```
    C:\Users\user\Desktop\Ace-Barbershop-Website-Tests>Python <Python Test File Name>
    ```
