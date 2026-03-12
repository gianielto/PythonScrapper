import requests
from dotenv import load_dotenv
import os

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

if not ACCESS_TOKEN:
    raise ValueError("No se encontró ACCESS_TOKEN en .env")

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

# sesión persistente (MUCHO más rápida)
session = requests.Session()
session.headers.update(headers)

# cache global de categorias
categorias = {}


def cargar_categorias():
    """Descarga todas las categorías una sola vez."""
    url = "https://www.eventbriteapi.com/v3/categories/"

    response = session.get(url, timeout=20)
    response.raise_for_status()

    data = response.json()

    for cat in data.get("categories", []):
        categorias[cat["id"]] = cat["name"]


def obtener_categoria(category_id):
    """Obtiene nombre de categoria desde memoria."""
    if not category_id:
        return None

    return categorias.get(category_id)


def obtener_detalle_evento(event_id):
    """Obtiene información filtrada de un evento."""

    url = f"https://www.eventbriteapi.com/v3/events/{event_id}/?expand=venue"

    try:
        response = session.get(url, timeout=20)

        if response.status_code == 404:
            return None

        response.raise_for_status()

    except requests.exceptions.RequestException:
        return None

    data = response.json()

    venue = data.get("venue") or {}
    address = venue.get("address") or {}

    evento_filtrado = {

        "nombre": data.get("name", {}).get("text") or "",
        "descripcion": data.get("description", {}).get("text") or "",

        "imagen": data.get("logo", {}).get("original", {}).get("url")
        if data.get("logo") else None,

        "fecha_inicio": data.get("start", {}).get("local"),
        "fecha_fin": data.get("end", {}).get("local"),
        "fecha_limite": data.get("end", {}).get("local"),

        "es_online": data.get("online_event", False),

        "venue_nombre": venue.get("name"),

        "ciudad": address.get("city"),
        "region": address.get("region"),
        "pais": address.get("country"),

        "direccion_1": address.get("address_1"),
        "direccion_2": address.get("address_2"),
        "direccion_completa": address.get("localized_address_display"),

        "categoria_nombre": obtener_categoria(data.get("category_id")),

        "url_evento": data.get("url")
    }

    return evento_filtrado


cargar_categorias()
