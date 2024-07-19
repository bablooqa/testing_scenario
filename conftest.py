import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    # Initialize WebDriver
    driver = webdriver.Chrome()  # or webdriver.Firefox() for Firefox
    driver.implicitly_wait(10)  # Wait for elements to be available
    yield driver
    driver.quit()  # Clean up and close browser after test
