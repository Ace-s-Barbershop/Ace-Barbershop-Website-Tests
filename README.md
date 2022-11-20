# Ace’s Barbershop Website Selenium Automated Tests

These tests are automated tests using Selenium to test the functionality of Ace's Barbershop Website. Please refer to this README.md or the System Test report to learn how to run these tests.

## Tools 

* Windows Operating System (Windows 10 or above)
* Google Chrome Browser (Latest Version)
* Command Prompt/Terminal/Powershell (Latest Version)
  - Powershell free and available online: https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.2
* Python3 (Latest Version)
  - Available: https://www.python.org/downloads/
* Selenium Python Plug In (Version 4.5.0)
  - More information: https://selenium-python.readthedocs.io/installation.html
* Webdriver_manager Python Plug In (Version 3.8.4)
* Packaging Python Plug In (Version 21.3)
* ChromeDriver
  - More information: https://chromedriver.chromium.org/downloads

## Setup
1. First make sure you are on a Windows Operating Systems and that you have Google Chrome downloaded
2. Make sure you have Command Prompt, Terminal, or Powershell. If not, download Powershell using links above in tools.
3. Download Python3. Please follow the link provided in the tools.
4. Pull the GitHub repository provided in the tools to your local machine. 
5. Open Command Prompt/Terminal/Powershell and go to the directory of the pulled GitHub repository (Powershell link available in tools). Make sure you are on the correct path (Path to the test files).
  - For example, the directory path in Command Prompt/Terminal/Powershell could be:
    ```
    C:\Users\user\Desktop\Ace-Barbershop-Website-Tests-main>
    ```
6. In the correct directory path, make sure you install selenium, webdriver_manager, and packaging. To install those plugins:
  - For example, in Command Prompt/Terminal/Powershell:
    ```
    C:\Users\user\Desktop\Ace-Barbershop-Website-Tests-main>pip3 install selenium==4.50
    
    C:\Users\user\Desktop\Ace-Barbershop-Website-Tests-main>pip3 install webdriver_manager==3.8.4

    C:\Users\user\Desktop\Ace-Barbershop-Website-Tests-main>pip3 install packaging==21.3
    ```
7. After installing the three plugins and still in the correct directory path, type the following to run the test files (<Python Test File Name> would change a specific file name provided in each the test cases in section 2 Functional Test: Automation via Selenium): 
  - For example, in Command Prompt/Terminal/Powershell:
    ```
    C:\Users\user\Desktop\Ace-Barbershop-Website-Tests-main>Python <Python Test File Name>
    ```
