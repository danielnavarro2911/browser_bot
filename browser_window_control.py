from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

class Browser:
    def __init__(self, URL='', locator_type='XPATH', incognito=False, headless=False):
        self.default_locator_type = {
            'XPATH': By.XPATH,
            'CLASS_NAME': By.CLASS_NAME,
            'ID': By.ID,
            'CSS_SELECTOR': By.CSS_SELECTOR,
            'NAME': By.NAME,
            'TAG_NAME': By.TAG_NAME
        }[locator_type]  # Asignar el tipo de localización por defecto
        
        chrome_options = Options()
        if incognito:
            chrome_options.add_argument("--incognito")
        if headless:
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--window-size=1920,1080")
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(URL)
        
    def click(self, locator, time=10, locator_type=None):
        
        if locator_type is None:
            locator_type = self.default_locator_type
        else:
            locator_type = self.get_locator_type(locator_type)
        
        WebDriverWait(self.driver, time).until(EC.element_to_be_clickable((locator_type, locator))).click()
        
    def write(self, texto, locator, time=10, locator_type=None):
        
        if locator_type is None:
            locator_type = self.default_locator_type
        else:
            locator_type = self.get_locator_type(locator_type)
        
        WebDriverWait(self.driver, time).until(EC.element_to_be_clickable((locator_type, locator))).send_keys(texto)
        
    def presence(self, locator, time=10, locator_type=None):

        if locator_type is None:
            locator_type = self.default_locator_type
        else:
            locator_type = self.get_locator_type(locator_type)
        
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located((locator_type, locator)))

    def get_locator_type(self, type_):
        return {
            'XPATH': By.XPATH,
            'CLASS_NAME': By.CLASS_NAME,
            'ID': By.ID,
            'CSS_SELECTOR': By.CSS_SELECTOR,
            'NAME': By.NAME,
            'TAG_NAME': By.TAG_NAME
        }[type_]
    
    def get_(self,URL):
        self.driver.get(URL)
    
    def close(self):
        self.driver.close()
