import pytest
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import logging

log = logging.getLogger(__name__)


def test_check_tab_title(wordHome):
    log = logging.info('test_check_tab_title')
    tab = wordHome.get_tab_title()
    assert tab == "Welcome to WordLadder", "Tab should be Welcome to WordLadder"

def test_check_page_title(wordHome):
    log = logging.info('test_check_page_title')
    title = wordHome.get_page_title()
    assert title == "Welcome to WordLadder", "Title should be Welcome to WordLadder"

def test_firstWord(wordHome):
    log = logging.info('test_firstWord')
    fromWord =wordHome.get_from_word()
    toWord = wordHome.get_to_word()
    assert fromWord == "ball","Wrong from word"
    assert toWord == "spin", "Wrong to word"
 
def test_next_button(wordHome):
    log = logging.info('test_next_button')
    wordHome.click_next_button()
    fromWord =wordHome.get_from_word()
    toWord = wordHome.get_to_word()
    assert fromWord == "bird","Wrong from word" 
    assert  toWord =="nest" , "Wrong to word"

def test_previous_button(wordHome):
    log = logging.info('test_previous_button')
    wordHome.click_previous_button()
    fromWord =wordHome.get_from_word()
    toWord = wordHome.get_to_word()
    assert fromWord == "leaf", "Wrong from word"
    assert  toWord =="life", "Wrong to word"


def test_check_blank_text_error(wordHome):
    log = logging.info('test_check_blank_text_error') 
    wordHome.click_submit_button()
    toast_message = wordHome.find_toast_message()
    assert toast_message == "Enter a word"
    entered_word = wordHome.find_word_in_text_field()
    assert entered_word == "","The input field should be empty"

def test_check_same_text_error(wordHome): 
    log = logging.info('test_check_same_text_error')
    wordHome.input_word("bill")
    wordHome.click_submit_button()
    wordHome.input_word("bill")
    wordHome.click_submit_button()
    toast_message = wordHome.find_toast_message()
    assert toast_message == "Enter a different word"
    entered_word = wordHome.find_word_in_text_field()
    assert entered_word == "bill", "The input field should have word bill"


def test_check_less_than_four_chars_error(wordHome):
    log = logging.info('test_check_less_than_four_chars_error') 
    wordHome.input_word("bil")
    wordHome.click_submit_button()
    toast_message = wordHome.find_toast_message()
    assert toast_message == "Enter a 4 letter word"
    entered_word = wordHome.find_word_in_text_field()
    assert entered_word == "bil", "The input field should have word bil"


def test_check_change_more_than_1_chars_error(wordHome): 
    log = logging.info('test_check_change_more_than_1_chars_error')
    wordHome.input_word("will")
    wordHome.click_submit_button()
    toast_message = wordHome.find_toast_message()
    assert toast_message == "Please change 1 letter"
    entered_word = wordHome.find_word_in_text_field()
    assert entered_word == "will", "The input field should have word will"

def test_check_invalid_word_error(wordHome): 
    log = logging.info('test_check_invalid_word_error')
    wordHome.input_word("yall")
    wordHome.click_submit_button()
    toast_message = wordHome.find_toast_message()
    assert toast_message == "This is not a valid word"
    entered_word = wordHome.find_word_in_text_field()
    assert entered_word == "yall", "The input field should have word yall"

def test_enter_word(wordHome):
    log = logging.info('test_enter_word')
    wordHome.input_word("bill")
    wordHome.click_submit_button()
    wordList = wordHome.get_list_of_entered_words()
    assert len(wordList)== 1, "Length should be 1"
    assert wordList[-1].text == "bill", "Entered word should be bill"

def test_toast_disappear_after_entering_new_word(wordHome): 
    log = logging.info('test_toast_disappear_after_entering_new_word')
    wordHome.enter_and_submit_word("yall")
    length = wordHome.get_toast_list()
    is_show = wordHome.is_toast_messages_shown()
    assert is_show == True, "Toast message should be shown"
    wordHome.clear_input_value()
    wordHome.enter_and_submit_word("wall")
    is_show = wordHome.is_toast_messages_shown()
    assert is_show == False, "Toast message should be dismissed"


def test_end_game(wordHome):
    log = logging.info('test_end_game')
    wordHome.click_next_button()
    wordHome.click_next_button()
    wordHome.click_next_button()
    wordHome.click_next_button()
    wordHome.click_next_button()
    fromWord =wordHome.get_from_word()
    assert fromWord == "dawn", "Wrong from word"
    toWord = wordHome.get_to_word()
    assert toWord =="dusk", "Wrong to word"
    wordHome.enter_and_submit_word("down")
    list_of_entered_words = wordHome.get_list_of_entered_words()
    assert list_of_entered_words[-1].text == "down", "Last entered word should be down"
    wordHome.enter_and_submit_word("town")
    list_of_entered_words = wordHome.get_list_of_entered_words()
    assert list_of_entered_words[-1].text == "town", "Last entered word should be town"
    wordHome.enter_and_submit_word("toon")
    list_of_entered_words = wordHome.get_list_of_entered_words()
    assert list_of_entered_words[-1].text == "toon", "Last entered word should be toon"
    wordHome.enter_and_submit_word("took")
    list_of_entered_words = wordHome.get_list_of_entered_words()
    assert list_of_entered_words[-1].text == "took", "Last entered word should be took"
    wordHome.enter_and_submit_word("dook")
    list_of_entered_words = wordHome.get_list_of_entered_words()
    assert list_of_entered_words[-1].text == "dook", "Last entered word should be dook"
    wordHome.enter_and_submit_word("dock")
    list_of_entered_words = wordHome.get_list_of_entered_words()
    assert list_of_entered_words[-1].text == "dock", "Last entered word should be dock"
    wordHome.enter_and_submit_word("duck")
    list_of_entered_words = wordHome.get_list_of_entered_words()
    assert list_of_entered_words[-1].text == "duck", "Last entered word should be duck"
    win = wordHome.find_toast_message()
    assert win == "You did it!"
    