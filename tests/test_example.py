import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage

def test_open_homepage():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    home = HomePage(driver)
    home.open()
    assert "Example Domain" in driver.title
    driver.quit()
