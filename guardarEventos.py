# from supabase import create_client, Client
# import os

# SUPABASE_URL = os.environ.get("SUPABASE_URL")
# SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


# def construir_horarios(evento):

#     inicio = evento.get("fecha_inicio")
#     fin = evento.get("fecha_limite")

#     if not inicio:
#         return None

#     if fin:
#         return f"{inicio} - {fin}"

#     return inicio


# def cargar_mapa_actividades():

#     res = supabase.table("actividades").select("id,nombre").execute()

#     mapa = {}

#     for fila in res.data:
#         mapa[fila["nombre"]] = fila["id"]

#     return mapa


# def cargar_mapa_intereses():

#     res = supabase.table("intereses").select("id,nombre").execute()

#     mapa = {}

#     for fila in res.data:
#         mapa[fila["nombre"]] = fila["id"]

#     return mapa


# def normalizar_evento(evento, mapa_actividades, mapa_intereses):

#     actividad_nombre = evento.get("actividad_g")
#     interes_nombre = evento.get("interes")

#     id_actividad = mapa_actividades.get(actividad_nombre)
#     id_interes = mapa_intereses.get(interes_nombre)

#     if id_actividad is None:
#         print(f"⚠️ Actividad no encontrada: {actividad_nombre}")

#     if id_interes is None:
#         print(f"⚠️ Interés no encontrado: {interes_nombre}")

#     return {
#         "nombre": evento.get("nombre"),
#         "descripcion": evento.get("descripcion"),
#         "imagen": evento.get("imagen"),
#         "lat": None,
#         "lng": None,
#         "horarios": construir_horarios(evento),
#         "id_actividad_general": id_actividad,
#         "id_interes": id_interes,
#         "url_evento": evento.get("url")
#     }


# def guardar_eventos_supabase(eventos):

#     if not eventos:
#         print("No hay eventos para guardar.")
#         return

#     print("Cargando mapas de actividades e intereses...")

#     mapa_actividades = cargar_mapa_actividades()
#     mapa_intereses = cargar_mapa_intereses()

#     eventos_db = []

#     for evento in eventos:

#         evento_db = normalizar_evento(
#             evento,
#             mapa_actividades,
#             mapa_intereses
#         )

#         eventos_db.append(evento_db)

#     try:

#         supabase.table("actividad_especifica") \
#             .upsert(eventos_db, on_conflict="url_evento") \
#             .execute()

#         print(f"✅ {len(eventos_db)} eventos guardados correctamente.")

#     except Exception as e:
#         print(f"❌ Error insertando eventos: {e}")
import unicodedata

from supabase import create_client, Client
import os

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def construir_horarios(evento):
    inicio = evento.get("fecha_inicio")
    fin = evento.get("fecha_limite")

    if not inicio:
        return None
    return f"{inicio} - {fin}" if fin else inicio


def normalizar(texto):
    texto = (texto or "").lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = texto.encode("ascii", "ignore").decode("utf-8")
    return " ".join(texto.split())


def cargar_mapa_actividades():
    res = supabase.table("actividades").select("id,nombre").execute()
    mapa = {}
    for fila in res.data:
        nombre_norm = normalizar(fila["nombre"])
        mapa[nombre_norm] = fila["id"]
    return mapa


def cargar_mapa_intereses():
    res = supabase.table("intereses").select("id,nombre").execute()
    mapa = {}
    for fila in res.data:
        nombre_norm = normalizar(fila["nombre"])
        mapa[nombre_norm] = fila["id"]
    return mapa


def normalizar_evento(evento, mapa_actividades, mapa_intereses):
    actividad_nombre = normalizar(evento.get("actividad_g"))
    interes_nombre = normalizar(evento.get("interes"))

    id_actividad = mapa_actividades.get(actividad_nombre)
    id_interes = mapa_intereses.get(interes_nombre)

    if id_actividad is None or id_interes is None:
        print(
            f"⚠️ Actividad o Interés no encontrado: {evento.get('actividad_g')}, {evento.get('interes')}")
        return None

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


def guardar_eventos_supabase(eventos):
    if not eventos:
        print("No hay eventos para guardar.")
        return

    print("Cargando mapas de actividades e intereses...")
    mapa_actividades = cargar_mapa_actividades()
    mapa_intereses = cargar_mapa_intereses()

    eventos_db = []

    for evento in eventos:
        evento_db = normalizar_evento(evento, mapa_actividades, mapa_intereses)
        if evento_db:
            eventos_db.append(evento_db)

    if not eventos_db:
        print("No hay eventos válidos para guardar después de la normalización.")
        return

    try:
        # Inserción masiva con upsert usando url_evento como clave única
        supabase.table("actividad_especifica") \
            .upsert(eventos_db, on_conflict="url_evento") \
            .execute()
        print(f"✅ {len(eventos_db)} eventos guardados correctamente.")
    except Exception as e:
        print(f"❌ Error insertando eventos: {e}")
