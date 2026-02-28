# extrae los IDs de eventos de una página de resultados de Eventbrite
import requests
from bs4 import BeautifulSoup


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
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error al obtener la página: {e}")
        return set()

    soup = BeautifulSoup(response.text, "lxml")

    ul_eventos = soup.find(
        "ul",
        class_=lambda x: x and "SearchResultPanelContentEventCardList-module__eventList" in x
    )

    if not ul_eventos:
        return set()

    event_ids = {
        enlace.get("data-event-id")
        for enlace in ul_eventos.find_all("a", attrs={"data-event-id": True})
        if enlace.get("data-event-id")
    }

    return event_ids
