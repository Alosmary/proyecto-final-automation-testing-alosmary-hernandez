# Pre-entrega Automation Testing - SauceDemo

## Propósito del proyecto

Este proyecto corresponde a la pre-entrega del curso de Automation Testing.

El objetivo es automatizar flujos básicos de navegación web utilizando Selenium WebDriver con Python, aplicando buenas prácticas de testing como organización de tests, uso de fixtures, funciones auxiliares y generación de reportes HTML.

El sitio utilizado para las pruebas es:

https://www.saucedemo.com/

## Tecnologías utilizadas

- Python
- Selenium WebDriver
- Pytest
- Pytest HTML
- Git
- GitHub

## Flujos automatizados

El proyecto incluye la automatización de los siguientes casos:

1. Login exitoso con usuario válido.
2. Validación del catálogo de productos.
3. Agregado de producto al carrito y validación del ítem agregado.

## Estructura del proyecto

```text
pre-entrega-automation-testing-alosmary-hernandez/
│
├── tests/
│   └── test_saucedemo.py
│
├── utils/
│   ├── __init__.py
│   └── helpers.py
│
├── reports/
│   ├── assets/
│   ├── screenshots/
│   └── reporte.html
│
├── conftest.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Instalación del proyecto

Clonar el repositorio:

```bash
git clone https://github.com/Alosmary/pre-entrega-automation-testing-alosmary-hernandez.git
```

Ingresar a la carpeta del proyecto:

```bash
cd pre-entrega-automation-testing-alosmary-hernandez
```

Crear un entorno virtual:

```bash
python -m venv .venv
```

Activar el entorno virtual en Windows:

```bash
.venv\Scripts\activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución de pruebas

Para ejecutar los tests desde la raíz del proyecto:

```bash
pytest tests/test_saucedemo.py -v
```

## Generar reporte HTML

Para ejecutar las pruebas y generar el reporte HTML:

```bash
pytest tests/test_saucedemo.py -v --html=reports/reporte.html
```

El reporte se genera en:

```text
reports/reporte.html
```

## Evidencias

El proyecto cuenta con generación automática de capturas de pantalla en caso de fallos.

Las capturas se guardan en:

```text
reports/screenshots/
```

## Casos automatizados

### Login exitoso

Valida que el usuario `standard_user` pueda iniciar sesión correctamente con la contraseña `secret_sauce`.

Validaciones principales:

- Redirección a `/inventory.html`.
- Visualización del título `Products`.
- Visualización del logo `Swag Labs`.

### Catálogo de productos

Valida que la pantalla de inventario cargue correctamente.

Validaciones principales:

- Título de la pantalla.
- Presencia de productos visibles.
- Nombre y precio del primer producto.
- Menú lateral visible.
- Filtro de ordenamiento visible.

### Carrito de compras

Valida que se pueda agregar el primer producto del catálogo al carrito.

Validaciones principales:

- Incremento del contador del carrito.
- Navegación al carrito.
- Visualización del producto agregado.