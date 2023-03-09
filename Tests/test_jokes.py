import pytest
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import logging

log = logging.getLogger(__name__)

def test_check_tab_title(jokesHome):
    log.info("test_check_tab_title")
    tabTitle = jokesHome.get_tab_title()
    assert tabTitle == "Jokes", "tab title is not correct!"

def test_check_page_title(jokesHome):
    log.info("test_check_page_title")
    title = jokesHome.get_title()
    assert title == "Jokes", "title is not correct!"

def test_question_index_page(jokesHome):
    log.info("test_question_index_page")
    question = jokesHome.get_question()
    assert question == "Why was the math book sad?", "Jokes is not correct, check the next button functionality!"

def test_click_answer_button(jokesHome):
    log.info("test_click_answer_button")
    jokesHome.click_answer_button()
    answerDisplayed = jokesHome.is_answer_displayed()
    assert answerDisplayed == True, "Answer is not displayed"

def test_check_answer_after_clicking_answer_button(jokesHome):
    log.info("test_check_answer_after_clicking_answer_button")
    jokesHome.click_answer_button()
    answer = jokesHome.get_answer()
    assert answer == "Because it had too many problems.", "Answer is not correct"

def test_hide_button_shown_after_answer_button(jokesHome):
    log.info("test_hide_button_shown_after_answer_button")
    jokesHome.click_answer_button()
    hideButton = jokesHome.get_answer_button_value()
    assert hideButton == "Hide Answer", "Hide Answer button value is not correct"

def test_hide_button_hide_the_answer(jokesHome):
    log.info("test_hide_button_hide_the_answer")
    jokesHome.click_answer_button()
    jokesHome.click_answer_button()
    answerDisplayed = jokesHome.is_answer_displayed()
    assert answerDisplayed == False, "Answer is not hidden"

def test_click_next_button(jokesHome):
    log.info("test_click_next_button")
    jokesHome.click_next_button()
    jokeQuestion = jokesHome.get_question()
    assert jokeQuestion == "Why did the tomato turn red?", "Jokes is not correct, check the next button functionality!"
    jokesHome.click_answer_button()
    jokeAnswer = jokesHome.get_answer()
    assert jokeAnswer == "Because it saw the salad dressing!", "Jokes is not correct, check the next button functionality!"


def test_click_previous_button(jokesHome):
    log.info("test_click_previous_button")
    jokesHome.click_previous_button()
    jokeQuestion = jokesHome.get_question()
    assert jokeQuestion == "What do you call a boomerang that doesn't come back?", "Jokes is not correct, check the previous button functionality!"
    jokesHome.click_answer_button()
    jokeAnswer = jokesHome.get_answer()
    assert jokeAnswer == "A stick.", "Jokes is not correct, check the next button functionality!"


def test_check_jokes_text_after_clicking_next_a_few_time(jokesHome):
    log.info("test_check_jokes_text_after_clicking_next_a_few_time")
    jokesHome.click_next_button()
    jokesHome.click_next_button()
    jokesHome.click_next_button()
    jokesHome.click_next_button()
    jokesHome.click_next_button()
    jokesHome.click_next_button()
    jokeQuestion = jokesHome.get_question()
    assert jokeQuestion == "Why did the banana go to the doctor?", "Jokes is not correct, check the next button functionality!"
    jokesHome.click_answer_button()
    jokeAnswer = jokesHome.get_answer()
    assert jokeAnswer == "Because it wasn't peeling well.", "Jokes is not correct, check the next button functionality!"

