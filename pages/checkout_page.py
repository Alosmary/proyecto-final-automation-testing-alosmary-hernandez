from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """
    Clase Page Object para el flujo de checkout de SauceDemo.
    Contiene locators y acciones relacionadas al formulario y confirmación de compra.
    """

    _FIRST_NAME_INPUT = (By.ID, "first-name")
    _LAST_NAME_INPUT = (By.ID, "last-name")
    _POSTAL_CODE_INPUT = (By.ID, "postal-code")
    _CONTINUE_BUTTON = (By.ID, "continue")
    _FINISH_BUTTON = (By.ID, "finish")
    _TITLE = (By.CLASS_NAME, "title")
    _COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver

    def completar_datos_checkout(self, nombre, apellido, codigo_postal):
        first_name = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self._FIRST_NAME_INPUT)
        )
        first_name.clear()
        first_name.send_keys(nombre)

        last_name = self.driver.find_element(*self._LAST_NAME_INPUT)
        last_name.clear()
        last_name.send_keys(apellido)

        postal_code = self.driver.find_element(*self._POSTAL_CODE_INPUT)
        postal_code.clear()
        postal_code.send_keys(codigo_postal)

        return self

    def continuar(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self._CONTINUE_BUTTON)
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(self._TITLE, "Checkout: Overview")
        )

        return self

    def finalizar_compra(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self._FINISH_BUTTON)
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(self._TITLE, "Checkout: Complete!")
        )

        return self

    def obtener_titulo(self):
        return self.driver.find_element(*self._TITLE).text

    def obtener_mensaje_confirmacion(self):
        return self.driver.find_element(*self._COMPLETE_HEADER).text