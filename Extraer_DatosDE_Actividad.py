import requests
from dotenv import load_dotenv
import os

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")


def obtener_detalle_evento(event_id):
    """
    Obtiene información filtrada de un evento de Eventbrite por su ID.

    Args:
        event_id (str): ID del evento.

    Returns:
        dict: Diccionario con los campos:
            - nombre
            - descripcion
            - imagen
            - fecha_inicio
            - fecha_fin
            - fecha_limite
    """
    if not ACCESS_TOKEN:
        raise ValueError("No se encontró ACCESS_TOKEN en las variables de entorno.")

    url = f"https://www.eventbriteapi.com/v3/events/{event_id}/?expand=venue"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }

    response = requests.get(url, headers=headers, timeout=20)
    response.raise_for_status()
    data = response.json()
    venue = data.get("venue") or {}
    address = venue.get("address") or {}

    evento_filtrado = {
        "nombre": data.get("name", {}).get("text") or "",
        "descripcion": data.get("description", {}).get("text") or "",
        "imagen": data.get("logo", {}).get("original", {}).get("url") if data.get("logo") else None,
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
        "direccion_completa": address.get("localized_address_display")
    }

    return evento_filtrado
