from pathlib import Path
from datetime import datetime

import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    """
    Prepara el navegador para cada prueba.
    Se abre antes del test y se cierra cuando termina.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Genera una captura de pantalla automática si un test falla.
    La imagen se guarda dentro de reports/screenshots.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver is not None:
            screenshots_dir = Path("reports/screenshots")
            screenshots_dir.mkdir(parents=True, exist_ok=True)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_path = screenshots_dir / f"{item.name}_{timestamp}.png"

            driver.save_screenshot(str(screenshot_path))

            pytest_html = item.config.pluginmanager.getplugin("html")

            if pytest_html:
                extras = getattr(report, "extras", [])
                extras.append(pytest_html.extras.image(str(screenshot_path)))
                report.extras = extras