from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """
    Clase Page Object para la pantalla del carrito de SauceDemo.
    Contiene locators y acciones relacionadas al carrito de compras.
    """

    _TITLE = (By.CLASS_NAME, "title")
    _CART_ITEMS = (By.CLASS_NAME, "cart_item")
    _PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    _REMOVE_BACKPACK_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    _CHECKOUT_BUTTON = (By.ID, "checkout")
    _CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")

    def __init__(self, driver):
        self.driver = driver

    def obtener_titulo(self):
        return self.driver.find_element(*self._TITLE).text

    def obtener_items_carrito(self):
        return self.driver.find_elements(*self._CART_ITEMS)

    def obtener_cantidad_items(self):
        return len(self.obtener_items_carrito())

    def remover_producto_backpack(self):
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(self._REMOVE_BACKPACK_BUTTON)
    ).click()
        return self

    def esperar_carrito_vacio(self):
        WebDriverWait(self.driver, 10).until(
        lambda driver: len(driver.find_elements(*self._CART_ITEMS)) == 0
    )
        return self

    def ir_a_checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self._CHECKOUT_BUTTON)
        ).click()
        return self
    
    def obtener_nombre_producto(self):
        return self.driver.find_element(*self._PRODUCT_NAME).text