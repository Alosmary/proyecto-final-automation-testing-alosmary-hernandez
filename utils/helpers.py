import csv
from pathlib import Path
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

def leer_csv_login():
    """
    Lee los datos de login desde data/login_data.csv
    y los convierte en una lista de tuplas para parametrizar tests.
    """

    ruta_csv = Path(__file__).resolve().parent.parent / "data" / "login_data.csv"

    casos = []

    with open(ruta_csv, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            usuario = fila["usuario"]
            clave = fila["clave"]
            debe_funcionar = fila["debe_funcionar"].strip().lower() == "true"

            casos.append((usuario, clave, debe_funcionar))

    return casos    