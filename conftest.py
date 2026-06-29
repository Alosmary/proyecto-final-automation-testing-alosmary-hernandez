import os
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    chrome_options = Options()

    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
        "autofill.profile_enabled": False,
        "autofill.credit_card_enabled": False,
    })

    chrome_options.add_argument("--disable-save-password-bubble")
    chrome_options.add_argument("--disable-features=PasswordManagerOnboarding,PasswordLeakDetection,PasswordCheck")
    chrome_options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Captura una pantalla automáticamente cuando falla un test UI.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            screenshots_dir = os.path.join("reports", "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_name = f"{item.name}_{timestamp}.png"
            screenshot_path = os.path.join(screenshots_dir, screenshot_name)

            driver.save_screenshot(screenshot_path)