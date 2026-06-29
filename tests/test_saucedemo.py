import pytest
from pages import cart_page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.helpers import leer_csv_login
from pages.checkout_page import CheckoutPage
from utils.logger import obtener_logger

pytestmark = pytest.mark.ui
logger = obtener_logger()




def test_login_exitoso(driver):
    """
    Valida que el usuario pueda iniciar sesión correctamente
    y sea redirigido a la pantalla de inventario.
    """

    logger.info("Iniciando test: login exitoso")

    LoginPage(driver).abrir().login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)

    assert "/inventory.html" in driver.current_url
    assert inventory_page.obtener_titulo() == "Products"
    assert inventory_page.obtener_logo() == "Swag Labs"

    logger.info("Login exitoso validado correctamente")


def test_catalogo_muestra_productos_y_elementos_importantes(driver):
    """
    Valida que el catálogo de productos cargue correctamente,
    mostrando título, productos visibles, menú y filtro.
    """

    LoginPage(driver).abrir().login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)

    nombre_producto = inventory_page.obtener_nombre_primer_producto()
    precio_producto = inventory_page.obtener_precio_primer_producto()

    assert inventory_page.obtener_titulo() == "Products"
    assert inventory_page.obtener_cantidad_productos() > 0
    assert nombre_producto != ""
    assert precio_producto.startswith("$")
    assert inventory_page.menu_esta_visible()
    assert inventory_page.filtro_esta_visible()

    print(f"Primer producto listado: {nombre_producto} - Precio: {precio_producto}")


def test_agregar_primer_producto_al_carrito(driver):
    """
    Valida que se pueda agregar el producto Sauce Labs Backpack al carrito.
    """

    LoginPage(driver).abrir().login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.agregar_producto_backpack()

    assert inventory_page.obtener_cantidad_carrito() == "1"
    assert inventory_page.obtener_nombre_producto_backpack() == "Sauce Labs Backpack"

def test_producto_agregado_se_visualiza_en_carrito(driver):
    """
    Valida que un producto agregado desde el inventario
    se visualice correctamente dentro del carrito.
    """

    LoginPage(driver).abrir().login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.agregar_producto_backpack()
    inventory_page.ir_al_carrito()

    cart_page = CartPage(driver)

    assert "/cart.html" in driver.current_url
    assert cart_page.obtener_titulo() == "Your Cart"
    assert cart_page.obtener_cantidad_items() == 1
    assert cart_page.obtener_nombre_producto() == "Sauce Labs Backpack"   

def test_remover_producto_del_carrito(driver):
    """
    Valida que un producto agregado al carrito
    pueda removerse correctamente.
    """

    LoginPage(driver).abrir().login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.agregar_producto_backpack()
    inventory_page.ir_al_carrito()

    cart_page = CartPage(driver)

    assert cart_page.obtener_cantidad_items() == 1

    cart_page.remover_producto_backpack()

    cart_page.esperar_carrito_vacio()

    assert cart_page.obtener_cantidad_items() == 0

    assert cart_page.obtener_cantidad_items() == 0  

@pytest.mark.parametrize("usuario, clave, debe_funcionar", leer_csv_login())
def test_login_parametrizado_desde_csv(driver, usuario, clave, debe_funcionar):
    """
    Valida el login con distintos usuarios obtenidos desde un archivo CSV.
    Incluye casos positivos y negativos.
    """

    LoginPage(driver).abrir().login(usuario, clave)

    if debe_funcionar:
        assert "/inventory.html" in driver.current_url
    else:
        assert "/inventory.html" not in driver.current_url
        assert LoginPage(driver).obtener_mensaje_error() != ""  

@pytest.mark.e2e
def test_checkout_completo(driver):
    """
    Valida el flujo completo de compra:
    login, agregar producto al carrito, checkout y confirmación final.
    """

    logger.info("Iniciando test E2E: checkout completo")

    LoginPage(driver).abrir().login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.agregar_producto_backpack()
    inventory_page.ir_al_carrito()

    logger.info("Producto agregado al carrito")

    cart_page = CartPage(driver)

    assert cart_page.obtener_titulo() == "Your Cart"
    assert cart_page.obtener_cantidad_items() == 1

    cart_page.ir_a_checkout()

    checkout_page = CheckoutPage(driver)

    assert checkout_page.obtener_titulo() == "Checkout: Your Information"

    checkout_page.completar_datos_checkout(
        "Alosmary",
        "Hernandez",
        "1000"
    )

    checkout_page.continuar()

    assert checkout_page.obtener_titulo() == "Checkout: Overview"

    checkout_page.finalizar_compra()

    assert checkout_page.obtener_titulo() == "Checkout: Complete!"
    assert checkout_page.obtener_mensaje_confirmacion() == "Thank you for your order!"

    logger.info("Checkout completo finalizado correctamente")