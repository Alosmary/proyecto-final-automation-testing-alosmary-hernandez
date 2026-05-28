from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "https://www.saucedemo.com/"
USER = "standard_user"
PASSWORD = "secret_sauce"


def login(driver):
    """
    Realiza el login con un usuario válido en SauceDemo.
    """
    driver.get(BASE_URL)

    username_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )

    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_input.send_keys(USER)
    password_input.send_keys(PASSWORD)
    login_button.click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("/inventory.html")
    )