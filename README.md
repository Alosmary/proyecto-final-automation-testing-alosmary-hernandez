# Proyecto Final - Automation Testing

## Descripción

Este proyecto corresponde al Trabajo Final Integrador del curso de Automatización de Pruebas.

El objetivo es implementar un framework de testing automatizado en Python que permita validar funcionalidades de interfaz de usuario y servicios API de forma organizada, mantenible y reutilizable.

El framework utiliza Selenium WebDriver para pruebas UI, Requests para pruebas API, Pytest como framework de ejecución y el patrón Page Object Model para separar la lógica de interacción con la aplicación de la lógica de validación de los tests.

---

## Sitio y APIs utilizadas

### Sitio web UI

* SauceDemo
* URL: https://www.saucedemo.com/

### API pública

* JSONPlaceholder
* URL base: https://jsonplaceholder.typicode.com

---

## Tecnologías utilizadas

* Python
* Pytest
* Selenium WebDriver
* Requests
* Page Object Model
* pytest-html
* CSV para datos externos
* Logging
* Git
* GitHub

---

## Estructura del proyecto

```text
proyecto-final-automation-testing-alosmary-hernandez/
│
├── data/
│   └── login_data.csv
│
├── logs/
│   └── suite.log
│
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── reports/
│   ├── assets/
│   ├── screenshots/
│   └── reporte.html
│
├── tests/
│   ├── test_saucedemo.py
│   └── test_api.py
│
├── utils/
│   ├── __init__.py
│   ├── helpers.py
│   └── logger.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Casos automatizados

### Pruebas UI

El proyecto incluye pruebas automatizadas sobre SauceDemo.

Casos principales:

1. Login exitoso.
2. Validación del catálogo de productos.
3. Agregar producto al carrito.
4. Visualizar producto agregado en el carrito.
5. Remover producto del carrito.
6. Login parametrizado desde archivo CSV.
7. Checkout completo end-to-end.

### Pruebas API

El proyecto incluye pruebas automatizadas sobre JSONPlaceholder.

Casos principales:

1. GET de un post por ID.
2. POST para crear un recurso.
3. DELETE para eliminar un recurso.

---

## Datos externos

El proyecto utiliza un archivo CSV para ejecutar pruebas parametrizadas de login.

Ruta:

```text
data/login_data.csv
```

Ejemplo de datos:

```csv
usuario,clave,debe_funcionar
standard_user,secret_sauce,true
locked_out_user,secret_sauce,false
usuario_invalido,clave_invalida,false
```

Estos datos son leídos desde `utils/helpers.py` mediante la función `leer_csv_login()` y utilizados con `pytest.mark.parametrize`.

---

## Instalación del proyecto

### 1. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

### 2. Ingresar al proyecto

```bash
cd proyecto-final-automation-testing-alosmary-hernandez
```

### 3. Crear entorno virtual

```bash
python -m venv .venv
```

### 4. Activar entorno virtual en Windows

```bash
.venv\Scripts\activate
```

### 5. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Ejecución de pruebas

### Ejecutar todas las pruebas

```bash
pytest
```

### Ejecutar todas las pruebas con reporte HTML

```bash
pytest --html=reports/reporte.html --self-contained-html
```

### Ejecutar solo pruebas UI

```bash
pytest -m ui
```

### Ejecutar solo pruebas API

```bash
pytest -m api
```

### Ejecutar solo pruebas E2E

```bash
pytest -m e2e
```

---

## Reporte HTML

El proyecto genera un reporte HTML utilizando `pytest-html`.

Ruta del reporte:

```text
reports/reporte.html
```

El reporte permite visualizar:

* tests ejecutados,
* estado de cada test,
* duración,
* errores encontrados,
* resumen de ejecución.

---

## Screenshots automáticos

El framework captura automáticamente una pantalla cuando una prueba UI falla.

Las capturas se almacenan en:

```text
reports/screenshots/
```

El nombre de cada captura incluye el nombre del test y la fecha/hora de ejecución.

---

## Logging

El proyecto implementa logging para registrar pasos clave durante la ejecución.

Ruta del archivo de logs:

```text
logs/suite.log
```

El archivo registra eventos como:

* inicio de pruebas,
* login exitoso,
* producto agregado al carrito,
* checkout completado,
* errores durante la ejecución.

---

## Page Object Model

El proyecto aplica el patrón Page Object Model.

Las clases ubicadas en la carpeta `pages/` contienen:

* locators,
* métodos de acción,
* lógica de interacción con la UI.

Los archivos ubicados en la carpeta `tests/` contienen:

* casos de prueba,
* asserts,
* validaciones esperadas.

Esta separación permite mejorar la mantenibilidad y reutilización del código.

---

## Markers configurados

Los markers se encuentran configurados en `pytest.ini`.

Markers disponibles:

```text
ui
api
smoke
e2e
```

Ejemplo de uso:

```bash
pytest -m ui
```

---

## Resultados actuales

La ejecución completa del framework finaliza correctamente con:

```text
12 passed
```

Esto incluye pruebas UI, pruebas API, pruebas parametrizadas con CSV y un flujo E2E de checkout completo.

---

## Conclusión

El framework desarrollado permite ejecutar pruebas automatizadas de UI y API de forma consistente, organizada y mantenible.

La implementación de Page Object Model facilita la separación de responsabilidades, mientras que el uso de Pytest permite parametrizar pruebas, ejecutar por markers y generar reportes HTML.

Además, el proyecto incluye manejo de datos externos mediante CSV, capturas automáticas ante fallos y logging para facilitar la depuración.

El proyecto cumple con los requerimientos principales de la entrega final: pruebas UI, pruebas API, reportes, screenshots, logging, datos externos, parametrización, estructura organizada y documentación.
