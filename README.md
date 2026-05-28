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
│   ├── screenshots/
│   └── reporte.html
│
├── conftest.py
├── requirements.txt
├── README.md
└── .gitignore