from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException   
import time
import sys

class RunSelenium():
    def __init__(self):
        self.driver = ''
    def driverSetup(self):
        
        WINDOW_SIZE = "1080,720"
        chrome_options = Options()  
        #chrome_options.add_argument("--headless")  
        chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--allow-running-insecure-content")
        chrome_options.add_argument("test-type")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--profile-directory=Default")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--disable-plugins-discovery")
        chrome_options.add_argument("--incognito")
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        
        print("starting Chrome")

        driver = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)
        driver.wait = WebDriverWait(driver, 100)
        return driver