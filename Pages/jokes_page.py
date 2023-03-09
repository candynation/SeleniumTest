from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Pages.base_page import BasePage

class JokesPage(BasePage):
    #locator
    TITLE = (By.ID, 'txtTitle')
    NEXT_BUTTON = (By.ID, 'btnNext')
    PREVIOUS_BUTTON = (By.ID, 'btnPrevious')
    QUESTION = (By.ID,'txtQuestion')
    ANSWER_BUTTON = (By.ID,'btnAnswer')
    ANSWER = (By.ID, 'txtAnswer')


    def get_tab_title(self):
        return self.get_title()

    def get_title(self):
        return self.find(self.TITLE).text

    def click_next_button(self):
        self.find(self.NEXT_BUTTON).click()

    def click_previous_button(self):
        self.find(self.PREVIOUS_BUTTON).click()
    
    def get_question(self): 
        return self.find(self.QUESTION).text

    def click_answer_button(self): 
        self.find(self.ANSWER_BUTTON).click()
    
    def get_answer(self): 
        return self.find(self.ANSWER).text
    
    def is_answer_displayed(self): 
        return self.find(self.ANSWER).is_displayed()
    
    def click_hide_button(self): 
        return self.find(self.ANSWER_BUTTON).click()

    def get_answer_button_value(self): 
        self.wait_for(self.ANSWER).text
        return self.find(self.ANSWER_BUTTON).get_attribute("value")
    
 