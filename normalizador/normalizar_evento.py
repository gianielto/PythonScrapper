# def normalizar_evento_para_db(evento, mapa_actividades=None, mapa_intereses=None):
#     """
#     Convierte el evento generado por el scraper al formato esperado
#     por la tabla actividad_especifica.
#     """

#     mapa_actividades = mapa_actividades or {}
#     mapa_intereses = mapa_intereses or {}

#     fecha_inicio = evento.get("fecha_inicio")
#     fecha_fin = evento.get("fecha_limite")

#     horarios = None
#     if fecha_inicio or fecha_fin:
#         horarios = f"{fecha_inicio or ''} - {fecha_fin or ''}".strip(" - ")

#     actividad_nombre = evento.get("actividad_g")
#     interes_nombre = evento.get("interes")

#     id_actividad = mapa_actividades.get(actividad_nombre)
#     id_interes = mapa_intereses.get(interes_nombre)

#     data = {
#         "nombre": evento.get("nombre"),
#         "descripcion": evento.get("descripcion"),
#         "imagen": evento.get("imagen"),

#         "lat": evento.get("lat"),
#         "lng": evento.get("lng"),

#         "horarios": horarios,

#         "id_actividad_general": id_actividad,
#         "id_interes": id_interes
#     }

#     return data


# def normalizar_eventos(eventos, mapa_actividades=None, mapa_intereses=None):
#     eventos_normalizados = []

#     for evento in eventos:
#         normalizado = normalizar_evento_para_db(
#             evento,
#             mapa_actividades,
#             mapa_intereses
#         )

#         if normalizado.get("nombre"):
#             eventos_normalizados.append(normalizado)

#     return eventos_normalizados
# def normalizar_evento(evento, mapa_actividades, mapa_intereses):

#     actividad_nombre = evento["actividad_g"]
#     interes_nombre = evento["interes"]

#     return {
#         "nombre": evento["nombre"],
#         "descripcion": evento["descripcion"],
#         "imagen": evento["imagen"],
#         "lat": None,
#         "lng": None,
#         "horarios": evento["fecha_inicio"],
#         "id_actividad_general": mapa_actividades.get(actividad_nombre),
#         "id_interes": mapa_intereses.get(interes_nombre),
#         "url_evento": evento.get("url")
#     }
def construir_horarios(evento):

    inicio = evento.get("fecha_inicio")
    fin = evento.get("fecha_limite")

    if not inicio:
        return None

    if fin:
        return f"{inicio} - {fin}"

    return inicio


def normalizar_evento(evento, mapa_actividades, mapa_intereses):

    actividad_nombre = evento.get("actividad_g")
    interes_nombre = evento.get("interes")

    # 🔎 Buscar IDs en los mapas
    id_actividad = mapa_actividades.get(actividad_nombre)
    id_interes = mapa_intereses.get(interes_nombre)

    # ⚠️ Validaciones
    if id_actividad is None:
        print(f"Actividad no encontrada en BD: {actividad_nombre}")

    if id_interes is None:
        print(f"Interes no encontrado en BD: {interes_nombre}")

    # 📦 Objeto listo para insertar
    return {
        "nombre": evento.get("nombre"),
        "descripcion": evento.get("descripcion"),
        "imagen": evento.get("imagen"),
        "lat": None,
        "lng": None,
        "horarios": construir_horarios(evento),
        "id_actividad_general": id_actividad,
        "id_interes": id_interes,
        "url_evento": evento.get("url")
    }
