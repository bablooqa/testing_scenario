import time
import pytest
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("email, password, expected", [
    ("valid@example.com", "correctpassword", "Welcome"),
    ("invalid@example.com", "wrongpassword", "Invalid credentials")
])
def test_login(driver, email, password, expected):
    driver.get("https://example.com/login")

    # Locate and fill email and password fields
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "loginButton").click()

    # Validate login result
    time.sleep(2)  # Wait for response
    message = driver.find_element(By.ID, "loginMessage").text
    assert expected in message

def test_registration(driver):
    driver.get("https://example.com/register")

    # Fill registration form
    driver.find_element(By.ID, "registerEmail").send_keys("newuser@example.com")
    driver.find_element(By.ID, "registerPassword").send_keys("newpassword")
    driver.find_element(By.ID, "confirmPassword").send_keys("newpassword")
    driver.find_element(By.ID, "registerButton").click()

    # Validate registration success
    time.sleep(2)
    success_message = driver.find_element(By.ID, "registerMessage").text
    assert "Registration successful" in success_message

def test_google_sign_in(driver):
    driver.get("https://example.com")

    # Click Google Sign-In button
    driver.find_element(By.ID, "googleSignInButton").click()

def test_social_login(driver):
    driver.get("https://example.com")

    # Click Social Login button (e.g., Facebook)
    driver.find_element(By.ID, "facebookSignInButton").click()

def test_password_reset(driver):
    driver.get("https://example.com/forgot-password")

    # Fill password reset form
    driver.find_element(By.ID, "resetEmail").send_keys("user@example.com")
    driver.find_element(By.ID, "resetButton").click()

    # Validate password reset email sent
    time.sleep(2)
    reset_message = driver.find_element(By.ID, "resetMessage").text
    assert "Password reset email sent" in reset_message
