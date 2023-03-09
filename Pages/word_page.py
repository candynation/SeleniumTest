from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Pages.base_page import BasePage

class WordPage(BasePage):
    
    TABTITLE=(By.TAG_NAME,'title')
    TITLE = (By.ID, 'txtTitle')
    NEXT_BUTTON = (By.ID, 'btnNext')
    PREVIOUS_BUTTON = (By.ID, 'btnPrevious')
    INPUT_WORD = (By.ID,'inputWord')
    SUBMIT_BUTTON = (By.ID, 'btnSubmit')
    WORD_LIST = (By.CLASS_NAME,"wordList")
    TOAST_MESSAGE=(By.ID, "txtToast")
    TOAST_MESSAGE_SHOW=(By.CLASS_NAME,"toast")
    MAIN_CONTAINER=(By.ID,"main_container")
    TO_WORD = (By.ID, 'txtWordTo')
    FROM_WORD = (By.ID, 'txtWordFrom')
    ENTERED_WORD_LIST=(By.TAG_NAME, "h2")

    
    def click_next_button(self):
        self.find(self.NEXT_BUTTON).click()

    def click_previous_button(self):
        self.find(self.PREVIOUS_BUTTON).click()
   
    def get_tab_title(self):
        return self.get_title()

    def get_page_title(self):
        return self.find(self.TITLE).text

    def get_to_word(self):
        return self.find(self.TO_WORD).text
    
    def get_from_word(self):
        return self.find(self.FROM_WORD).text

    def input_word(self,word): 
        self.wait_for(self.INPUT_WORD).send_keys(word)
    
    def find_word_in_text_field(self): 
        return self.find(self.INPUT_WORD).get_attribute("value")

    def clear_input_value(self):
        return self.find(self.INPUT_WORD).clear()
    
    def click_submit_button(self):
        self.find(self.SUBMIT_BUTTON).click()

    def enter_and_submit_word(self,word):
        self.input_word(word)
        self.click_submit_button()

    def find_word_list(self):
        return self.find(self.WORD_LIST)

    def get_list_of_entered_words(self):
        wordList = self.find_word_list()
        return wordList.find_elements(*self.ENTERED_WORD_LIST)

    def is_toast_messages_show(self):
        return self.wait_for(self.TOAST_MESSAGE_SHOW)

    def is_toast_messages_shown(self):
        length = len(self.find_elements_list(self.TOAST_MESSAGE_SHOW))
        if length > 0:
            return True
        else: 
            return False

    def get_toast_list(self):
        return  len(self.find_elements_list(self.TOAST_MESSAGE_SHOW))

    def find_toast_message(self):
        return self.find(self.TOAST_MESSAGE).text
    

        