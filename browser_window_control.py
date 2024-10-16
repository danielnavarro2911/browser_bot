from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Browser:
    def __init__(self, URL='', incognito=False, headless=False, maximized=True):
        chrome_options = Options()
        if incognito:
            chrome_options.add_argument("--incognito")
        if headless:
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--window-size=1920,1080")
        if maximized:
            chrome_options.add_argument("--start-maximized")
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(URL)
        
    def click(self, locator=None, element=None, time=10, locator_type='XPATH', ctrl_click=False):
        if element:
            if ctrl_click:
                ActionChains(self.driver).key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()
            else:
                element.click()
        else:
            locator_type = self.get_locator_type(locator_type)
            element = WebDriverWait(self.driver, time).until(EC.element_to_be_clickable((locator_type, locator)))
            if ctrl_click:
                ActionChains(self.driver).key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()
            else:
                element.click()

    def scroll_to_element(self, locator=None,element=None, time=10,locator_type='XPATH'):
        if element:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        
        else:
            
            locator_type = self.get_locator_type(locator_type)
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located((locator_type, locator)))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def write(self, texto, locator=None, element=None, time=10, locator_type='XPATH'):
        if element:
            element.send_keys(texto)
        else:
            locator_type = self.get_locator_type(locator_type)
            WebDriverWait(self.driver, time).until(EC.element_to_be_clickable((locator_type, locator))).send_keys(texto)

    def presence(self, locator=None, time=10, locator_type='XPATH'):
        locator_type = self.get_locator_type(locator_type)
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located((locator_type, locator)))

    # Modificación en find_element
    def find_element(self, locator, time=10, locator_type='XPATH', element=None):
        locator_type = self.get_locator_type(locator_type)
        
        if element:
            # Buscar dentro del WebElement proporcionado
            return element.find_element(locator_type, locator)
        else:
            # Buscar en todo el DOM
            return WebDriverWait(self.driver, time).until(EC.presence_of_element_located((locator_type, locator)))
    
    def find_elements(self, locator, time=10, locator_type='XPATH'):
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
    
    def get_(self, URL):
        self.driver.get(URL)
        
    def back(self):
        self.driver.back()
    
    def close(self):
        self.driver.close()

    def switch_to_tab(self, index):
        """Navega a la pestaña especificada por su índice (0 para la primera pestaña)."""
        self.driver.switch_to.window(self.driver.window_handles[index])
        
    def close_tab(self):
        """Cierra la pestaña actual y regresa a la última pestaña activa."""
        current_window = self.driver.current_window_handle
        self.driver.close()
        
    def get_current_url(self):
        return self.driver.current_url
