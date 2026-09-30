# nucleo/configuracion.py
"""Capa 1 — Configuración: lo único que llega de afuera del código."""
import os

from dotenv import load_dotenv

load_dotenv()


class Configuracion:
    """Se lee una sola vez, al arrancar. El resto del proyecto no toca os.environ."""
    base_datos: str = os.environ["DATABASE_URL"]   # la URL de Neon la trae el ambiente
    nombre_app: str = "Productos"


CONFIGURACION = Configuracion()