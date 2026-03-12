# extrae los IDs de eventos de una página de resultados de Eventbrite
import json
import re

import requests
from bs4 import BeautifulSoup

EVENT_URL_REGEX = re.compile(r"/e/[^\"'\\]+-(\d{6,})")
EVENT_ID_REGEX = re.compile(r"data-event-id=[\"'](\d{6,})[\"']")


def extraer_ids_de_json(valor):
    ids = set()

    if isinstance(valor, dict):
        for llave, contenido in valor.items():
            if llave in {"url", "item", "@id"} and isinstance(contenido, str):
                ids.update(EVENT_URL_REGEX.findall(contenido))
            else:
                ids.update(extraer_ids_de_json(contenido))
    elif isinstance(valor, list):
        for item in valor:
            ids.update(extraer_ids_de_json(item))
    elif isinstance(valor, str):
        ids.update(EVENT_URL_REGEX.findall(valor))

    return ids


def extraer_event_ids(url):
    """
    Extrae los IDs de eventos de una página de resultados de Eventbrite.

    Args:
        url (str): URL de la página de eventos.

    Returns:
        set: Conjunto de IDs encontrados.
    """
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, timeout=20)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error al obtener la página: {e}")
        return set()

    soup = BeautifulSoup(response.text, "lxml")
    event_ids = {
        elemento.get("data-event-id")
        for elemento in soup.select("[data-event-id]")
        if elemento.get("data-event-id")
    }

    for script in soup.find_all("script", type="application/ld+json"):
        contenido = script.string or script.get_text(strip=True)
        if not contenido:
            continue

        try:
            data = json.loads(contenido)
        except json.JSONDecodeError:
            continue

        event_ids.update(extraer_ids_de_json(data))

    event_ids.update(EVENT_ID_REGEX.findall(response.text))
    event_ids.update(EVENT_URL_REGEX.findall(response.text))

    return event_ids
