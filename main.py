from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
import unicodedata

from Extraer_DatosDE_Actividad import obtener_detalle_evento
from extraerID_Actividades import extraer_event_ids
# from Clasificar_Actividad import clasificar_evento
from event_classifer.classifier.classify_event import classify_event as clasificar_evento
from guardarEventos import guardar_eventos_supabase


# def main():
#     eventExample = {
#         "nombre": "PUNTO EMPRESARIAL 2026",
#         "descripcion": "El encuentro empresarial que marca el rumbo 2026–2028: informe, toma de compromiso y líderes que transforman Jalisco.",
#         "imagen": "https://ejemplo.com/imagenes/festival-jazz-guadalajara.jpg",
#         "actividad_g": "musica",
#         "interes": "cultura",
#         "clase": "festival",
#         "fecha_inicio": "2026-05-15T19:00:00",
#         "fecha_limite": "2026-05-17T23:30:00",
#         "venue_nombre": "Teatro Degollado",
#         "ciudad": "Guadalajara",
#         "categoria_nombre": "Business & Professional",
#         "url_evento": "https://ejemplo.com/eventos/festival-jazz-guadalajara",
#         "direccion_completa": "Calle Degollado s/n, Zona Centro, 44100 Guadalajara, Jalisco, México",
#         "score_clasificacion": 0.93
#     }

#     js = clasificar_evento(eventExample)
#     print(js)


# if __name__ == "__main__":
#     main()


BASE_URL = "https://www.eventbrite.com.mx/d/mexico--guadalajara/all-events/"
MAX_PAGINAS = 8
MAX_WORKERS = 6


def normalizar_texto(texto):
    texto = (texto or "").lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = texto.encode("ascii", "ignore").decode("utf-8")
    return " ".join(texto.split())


def es_evento_de_hoy(fecha_inicio, fecha_objetivo):
    if not fecha_inicio:
        return False

    return fecha_inicio[:10] == fecha_objetivo


def es_evento_en_guadalajara(detalle):
    if detalle.get("es_online"):
        return False

    campos = [
        detalle.get("ciudad"),
        detalle.get("venue_nombre"),
        detalle.get("direccion_1"),
        detalle.get("direccion_2"),
        detalle.get("direccion_completa"),
    ]
    texto = " ".join(normalizar_texto(campo) for campo in campos if campo)

    return "guadalajara" in texto or " gdl " in f" {texto} "


def recolectar_ids(max_paginas):
    ids = set()
    paginas_sin_nuevos = 0

    for pagina in range(1, max_paginas + 1):
        url = f"{BASE_URL}?page={pagina}"
        ids_pagina = extraer_event_ids(url)
        nuevos = ids_pagina - ids

        print(
            f"Pagina {pagina}: {len(ids_pagina)} IDs detectados, "
            f"{len(nuevos)} nuevos."
        )

        if nuevos:
            ids.update(nuevos)
            paginas_sin_nuevos = 0
        else:
            paginas_sin_nuevos += 1

        if paginas_sin_nuevos >= 2:
            break

    return ids


def procesar_evento(event_id, fecha_hoy):
    detalle = obtener_detalle_evento(event_id)

    # Filtro temporal desactivado para pruebas.
    # if not es_evento_de_hoy(detalle.get("fecha_inicio"), fecha_hoy):
    # return None # Filtro temporal desactivado para pruebas.

    if not es_evento_en_guadalajara(detalle):
        return None

    clasificacion = clasificar_evento(detalle)

    return {
        "nombre": detalle.get("nombre"),
        "descripcion": detalle.get("descripcion"),
        "imagen": detalle.get("imagen"),
        "actividad_g": clasificacion.get("activity"),
        "interes": clasificacion.get("interest"),
        "clase": clasificacion.get("category"),
        "fecha_inicio": detalle.get("fecha_inicio"),
        "fecha_limite": detalle.get("fecha_limite"),
        "venue_nombre": detalle.get("venue_nombre"),
        "ciudad": detalle.get("ciudad"),
        "categoria_nombre": detalle.get("categoria_nombre"),
        "url_evento": detalle.get("url_evento"),
        "direccion_completa": detalle.get("direccion_completa"),
        "score_clasificacion": clasificacion.get("confidence")
    }


def guardar_eventos(eventos):
    guardar_eventos_supabase(eventos)
    with open("eventos.txt", "w", encoding="utf-8") as f:
        f.write("===== EVENTOS ESTRUCTURADOS =====\n\n")

        for i, evento in enumerate(eventos, 1):
            f.write(f"EVENTO #{i}\n")
            f.write(f"Nombre: {evento['nombre']}\n")
            f.write(f"Descripción: {evento['descripcion']}\n")
            f.write(f"Imagen: {evento['imagen']}\n")
            f.write(f"Actividad general: {evento['actividad_g']}\n")
            f.write(f"Interés: {evento['interes']}\n")
            f.write(f"Clase: {evento['clase']}\n")
            f.write(f"Fecha inicio: {evento['fecha_inicio']}\n")
            f.write(f"Fecha límite: {evento['fecha_limite']}\n")
            f.write(f"Venue: {evento['venue_nombre']}\n")
            f.write(f"Ciudad: {evento['ciudad']}\n")
            f.write(f"Dirección: {evento['direccion_completa']}\n")
            f.write(f"Score clasificación: {evento['score_clasificacion']}\n")
            f.write(f"Categoría: {evento['categoria_nombre']}\n")
            f.write(f"URL Evento: {evento['url_evento']}\n")
            f.write("-" * 60 + "\n\n")


def main():
    fecha_hoy = datetime.now().date().isoformat()
    ids = recolectar_ids(MAX_PAGINAS)
    print(f"IDs únicos encontrados: {len(ids)}")

    eventos = []

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futuros = {
            executor.submit(procesar_evento, event_id, fecha_hoy): event_id
            for event_id in ids
        }

        for futuro in as_completed(futuros):
            event_id = futuros[futuro]

            try:
                evento = futuro.result()
            except Exception as e:
                print(f"Error con el evento {event_id}: {e}")
                continue

            if evento:
                eventos.append(evento)

    eventos.sort(
        key=lambda evento: (
            evento["fecha_inicio"] or "",
            -(evento["score_clasificacion"] or 0),
            normalizar_texto(evento["nombre"])
        )
    )

    guardar_eventos(eventos)

    print(
        f"\nSe encontraron {len(eventos)} eventos para la fecha {fecha_hoy}.")
    print("Archivo 'eventos.txt' generado correctamente.")


if __name__ == "__main__":
    main()
