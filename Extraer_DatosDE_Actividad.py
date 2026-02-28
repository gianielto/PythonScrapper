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
    url = f"https://www.eventbriteapi.com/v3/events/{event_id}/"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()

    evento_filtrado = {
        "nombre": data.get("name", {}).get("text"),
        "descripcion": data.get("description", {}).get("text"),
        "imagen": data.get("logo", {}).get("original", {}).get("url") if data.get("logo") else None,
        "fecha_inicio": data.get("start", {}).get("local"),
        "fecha_fin": data.get("end", {}).get("local"),
        "fecha_limite": data.get("end", {}).get("local")
    }

    return evento_filtrado
