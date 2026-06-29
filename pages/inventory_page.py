from selenium.webdriver.common.by import By


class InventoryPage:
    """
    Clase Page Object para la pantalla de inventario/productos de SauceDemo.
    Contiene locators y acciones relacionadas al catálogo de productos.
    """

    _TITLE = (By.CLASS_NAME, "title")
    _APP_LOGO = (By.CLASS_NAME, "app_logo")
    _PRODUCTS = (By.CSS_SELECTOR, "[data-test='inventory-item']")
    _PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    _PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")
    _MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    _PRODUCT_FILTER = (By.CLASS_NAME, "product_sort_container")
    
    _ADD_BACKPACK_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    _REMOVE_BACKPACK_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    _CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    _CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    _BACKPACK_NAME = (By.ID, "item_4_title_link")

    def __init__(self, driver):
        self.driver = driver

    def obtener_titulo(self):
        return self.driver.find_element(*self._TITLE).text

    def obtener_logo(self):
        return self.driver.find_element(*self._APP_LOGO).text

    def obtener_productos(self):
        return self.driver.find_elements(*self._PRODUCTS)

    def obtener_cantidad_productos(self):
        return len(self.obtener_productos())

    def obtener_nombre_primer_producto(self):
        primer_producto = self.obtener_productos()[0]
        return primer_producto.find_element(*self._PRODUCT_NAME).text

    def obtener_precio_primer_producto(self):
        primer_producto = self.obtener_productos()[0]
        return primer_producto.find_element(*self._PRODUCT_PRICE).text

    def menu_esta_visible(self):
        return self.driver.find_element(*self._MENU_BUTTON).is_displayed()

    def filtro_esta_visible(self):
        return self.driver.find_element(*self._PRODUCT_FILTER).is_displayed()   

    def agregar_producto_backpack(self):
        self.driver.find_element(*self._ADD_BACKPACK_BUTTON).click()
        return self

    def remover_producto_backpack(self):
        self.driver.find_element(*self._REMOVE_BACKPACK_BUTTON).click()
        return self

    def obtener_cantidad_carrito(self):
        return self.driver.find_element(*self._CART_BADGE).text

    def ir_al_carrito(self):
        self.driver.find_element(*self._CART_LINK).click()
        return self

    def obtener_nombre_producto_backpack(self):
        return self.driver.find_element(*self._BACKPACK_NAME).text