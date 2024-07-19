import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def browser():
    options = Options()
    options.add_argument("--headless") 
    service = ChromeService(executable_path="chromedriver_path")  
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()
