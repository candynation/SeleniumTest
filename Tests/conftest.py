import pytest
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import sys 
sys.path.append('..')
#from os import path 
from Pages.word_page import WordPage
from Pages.jokes_page import JokesPage

def pytest_addoption(parser):
    
    parser.addoption('--browser', action='store', default ='chrome')
    parser.addoption('--url', action='store', default = 'localhost')
   

@pytest.fixture
def browser(request):
    browser = request.config.getoption('browser').lower()
    if browser not in ['chrome','firefox','safari']:
        raise ValueError('--browser value must be chrome,firefox,safari')
    return browser

@pytest.fixture
def url(request):
    url = request.config.getoption('url')
    if url not in ['jokes','wordLadder', 'localhost']:
        raise ValueError('--url value must be jokes, wordLadder or localhost')
    return url

@pytest.fixture
def driver(browser, url):
    if (browser == 'chrome'):
        driver = webdriver.Chrome()
    
    if url == 'jokes': 
        URL = 'http://jokes.candychansgames.com/'
    elif url == 'wordLadder': 
        URL = 'http://wordladder.candychansgames.com/'
    elif url == 'localhost': 
        URL = 'http://127.0.0.1:5000'

    driver.get(URL)
    yield driver
    driver.quit()

@pytest.fixture
def wordHome(driver):
    return WordPage(driver)

@pytest.fixture
def jokesHome(driver):
    return JokesPage(driver)


