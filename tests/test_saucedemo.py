from selenium.webdriver.common.by import By
from utils.helpers import login


def test_login_exitoso(driver):
    """
    Valida que el usuario pueda iniciar sesión correctamente
    y sea redirigido a la pantalla de inventario.
    """
    login(driver)

    title = driver.find_element(By.CLASS_NAME, "title").text
    app_logo = driver.find_element(By.CLASS_NAME, "app_logo").text

    assert "/inventory.html" in driver.current_url
    assert title == "Products"
    assert app_logo == "Swag Labs"


def test_catalogo_muestra_productos_y_elementos_importantes(driver):
    """
    Valida que el catálogo de productos cargue correctamente,
    mostrando título, productos visibles, menú y filtro.
    """
    login(driver)

    title = driver.find_element(By.CLASS_NAME, "title").text
    productos = driver.find_elements(By.CSS_SELECTOR, "[data-test='inventory-item']")

    assert title == "Products"
    assert len(productos) > 0

    primer_producto = productos[0]

    nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text

    assert nombre_producto != ""
    assert precio_producto.startswith("$")

    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")

    assert menu.is_displayed()
    assert filtro.is_displayed()

    print(f"Primer producto listado: {nombre_producto} - Precio: {precio_producto}")


def test_agregar_primer_producto_al_carrito(driver):
    """
    Valida que se pueda agregar el primer producto del catálogo al carrito
    y que el producto agregado aparezca correctamente en la pantalla del carrito.
    """
    login(driver)

    productos = driver.find_elements(By.CSS_SELECTOR, "[data-test='inventory-item']")
    assert len(productos) > 0

    primer_producto = productos[0]

    nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
    boton_agregar = primer_producto.find_element(By.CSS_SELECTOR, "button.btn_inventory")

    boton_agregar.click()

    contador_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert contador_carrito == "1"

    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    carrito.click()

    productos_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(productos_carrito) == 1

    nombre_producto_carrito = productos_carrito[0].find_element(By.CLASS_NAME, "inventory_item_name").text

    assert nombre_producto_carrito == nombre_producto