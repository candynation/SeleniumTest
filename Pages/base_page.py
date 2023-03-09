
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
    
    def wait_for(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
        
    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_elements_list(self, locator):
        return self.driver.find_elements(*locator)

    def get_title(self):
        return self.driver.title
    
    def wait_for_invisibility(self,locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))
    
    def wait_for_clickable(self,locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
    