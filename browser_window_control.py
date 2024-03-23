from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

class browser:
    def __init__(self,URL=''):
        self.URL=URL
        self.driver=webdriver.Firefox()
        self.open()
    def open(self):
        self.driver.get(self.URL)
        
    def click(self,xpath,time=10):
        
        ''''Function that waits a specific time (default 10 seg) for the element (xpath) to be clickeable and then click it'''
   
        WebDriverWait(self.driver, time).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
    def write(self,texto,xpath,time=10):
        ''''Function that waits a specific time (default 10 seg) for the element (xpath) to be clickeable and then write on it'''
    
        WebDriverWait(self.driver, time).until(EC.element_to_be_clickable((By.XPATH, xpath))).send_keys(texto)
    def presence(self,xpath,time=10):
        ''''Function that waits a specific time (default 10 seg) for the element (xpath) to be clickeable. This can be used to detect when a page is ready 
        or to extract data'''
        return WebDriverWait(self.driver, self.time).until(EC.element_to_be_clickable((By.XPATH, self.xpath)))
    def close(self):
        self.driver.close()