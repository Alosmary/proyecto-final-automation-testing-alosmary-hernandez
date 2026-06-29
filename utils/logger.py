import logging
import os
from logging.handlers import RotatingFileHandler


def obtener_logger(nombre="automation_suite"):
    """
    Configura y devuelve un logger para registrar eventos importantes
    durante la ejecución de las pruebas.
    """

    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger(nombre)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = RotatingFileHandler(
            "logs/suite.log",
            maxBytes=1_000_000,
            backupCount=3,
            encoding="utf-8"
        )

        formato = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        handler.setFormatter(formato)
        logger.addHandler(handler)

    return logger