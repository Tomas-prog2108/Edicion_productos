# main.py
from contextlib import asynccontextmanager
from fastapi import FastAPI

from nucleo.configuracion import CONFIGURACION          # capa 1
from nucleo.conexion import db                     # capa 1
from presentacion.rutas.vistas import router as productos        # capa 3



@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.connect(CONFIGURACION.base_datos)    # main es quien une las piezas
    yield
    await db.close()

app = FastAPI(lifespan=lifespan)
app.include_router(productos)

