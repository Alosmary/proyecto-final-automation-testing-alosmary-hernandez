from selenium.webdriver.common.by import By


class LoginPage:
    """
    Clase Page Object para la pantalla de login de SauceDemo.
    Contiene los locators y las acciones relacionadas al login.
    """

    URL = "https://www.saucedemo.com/"

    _USERNAME_INPUT = (By.ID, "user-name")
    _PASSWORD_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.ID, "login-button")
    _ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    _LOGO = (By.CLASS_NAME, "login_logo")

    def __init__(self, driver):
        self.driver = driver

    def abrir(self):
        self.driver.get(self.URL)
        return self

    def completar_usuario(self, usuario):
        self.driver.find_element(*self._USERNAME_INPUT).clear()
        self.driver.find_element(*self._USERNAME_INPUT).send_keys(usuario)
        return self

    def completar_clave(self, clave):
        self.driver.find_element(*self._PASSWORD_INPUT).clear()
        self.driver.find_element(*self._PASSWORD_INPUT).send_keys(clave)
        return self

    def hacer_click_login(self):
        self.driver.find_element(*self._LOGIN_BUTTON).click()
        return self

    def login(self, usuario, clave):
        self.completar_usuario(usuario)
        self.completar_clave(clave)
        self.hacer_click_login()
        return self

    def obtener_mensaje_error(self):
        return self.driver.find_element(*self._ERROR_MESSAGE).text

    def obtener_logo(self):
        return self.driver.find_element(*self._LOGO).text