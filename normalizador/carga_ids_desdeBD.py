
from supabase import create_client, Client
import os

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def normalizar(texto):
    return texto.lower().strip()


def cargar_mapa_actividades():

    res = supabase.table("actividades").select("id,nombre").execute()

    mapa = {}

    for fila in res.data:
        mapa[normalizar(fila["nombre"])] = fila["id"]

    return mapa


def cargar_mapa_intereses():

    res = supabase.table("intereses").select("id,nombre").execute()

    mapa = {}

    for fila in res.data:
        mapa[normalizar(fila["nombre"])] = fila["id"]

    return mapa
