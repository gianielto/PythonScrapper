# import re
# import unicodedata
# from taxonomia import TAXONOMIA


# def normalizar(texto):
#     texto = (texto or "").lower()
#     texto = unicodedata.normalize("NFD", texto)
#     texto = texto.encode("ascii", "ignore").decode("utf-8")
#     return " ".join(texto.split())


# # TAXONOMIA = {
# #     "Artes escénicas": {
# #         "intereses": {
# #             "Comedia": [
# #                 "stand up", "standup", "comediante", "comedia", "show comico",
# #                 "impro", "improvisacion", "monologo", "humor", "open mic"
# #             ],
# #             "Drama": [
# #                 "drama", "romantico", "romance", "tragedia", "melodrama",
# #                 "teatro dramatico", "puesta en escena"
# #             ],
# #             "Ciencia Ficción / Fantasía": [
# #                 "fantasia", "magia", "ficcion", "ciencia ficcion", "medieval",
# #                 "rol en vivo", "cosplay", "anime"
# #             ],
# #             "Danza Folclórica / Tradicional": [
# #                 "samba", "folclor", "tradicional", "regional", "flamenco",
# #                 "danza folklorica", "bailable"
# #             ],
# #             "Danza Moderna": [
# #                 "danza moderna", "danza urbana", "hip hop dance", "street dance",
# #                 "jazz funk"
# #             ],
# #             "Danza Clásica (Ballet)": [
# #                 "ballet", "danza clasica", "ballet clasico"
# #             ],
# #             "Contemporánea": [
# #                 "contemporanea", "danza contemporanea", "performance"
# #             ],
# #             "Terror / Suspenso": [
# #                 "terror", "suspenso", "misterio", "thriller", "paranormal"
# #             ],
# #             "Acción / Aventura": [
# #                 "accion", "aventura", "epico", "heroe", "fantastico"
# #             ]
# #         },
# #         "actividad_g": {
# #             "show standup": [
# #                 "stand up", "standup", "comediante", "comedia", "open mic"
# #             ],
# #             "Obra de teatro": [
# #                 "obra", "teatro", "puesta en escena", "funcion teatral", "dramaturgia"
# #             ],
# #             "opera": ["opera", "zarzuela", "recital escenico"],
# #             "cine": [
# #                 "cine", "pelicula", "proyeccion", "cortometraje", "film",
# #                 "documental", "muestra de cine"
# #             ],
# #             "danza": [
# #                 "danza", "samba", "ballet", "coreografia", "baile", "ensamble"
# #             ]
# #         }
# #     },
# #     "Comunidad": {
# #         "intereses": {
# #             "académico": [
# #                 "conferencia", "charla", "programa", "academico", "seminario",
# #                 "simposio", "masterclass", "clase abierta", "capacitacion"
# #             ],
# #             "corporativos": [
# #                 "gala", "industria", "networking", "empresarial", "startup",
# #                 "negocios", "liderazgo", "emprendimiento", "negocio", "ventas", "marketing", "finanzas", "inversion", "capital de riesgo",
# #                 "venture capital", "pitch", "demo day", "emprendedoras", "panel de inversionistas", "foro empresarial", "conferencia de negocios", "evento corporativo",
# #                 "emprendedor"

# #             ],
# #             "eventos culturales": [
# #                 "cultural", "arte", "festival", "museo", "patrimonio",
# #                 "tradicion", "comunidad", "colectivo", "mercado creativo"
# #             ],
# #             "fantasia": [
# #                 "recorrido interactivo", "experiencia inmersiva", "escape room",
# #                 "inmersiva", "interactivo"
# #             ],
# #             "ciencia": [
# #                 "ciencia", "tecnologia", "innovacion", "robotica", "ia",
# #                 "inteligencia artificial", "astronomia", "investigacion", "tecnico", "divulgacion cientifica", "bootcamp"


# #             ],
# #             "deportiva": [
# #                 "carrera", "running", "club", "reto", "torneo comunitario"
# #             ]
# #         },
# #         "actividad_g": {
# #             "Visitas": [
# #                 "recorrido", "visita guiada", "tour", "walking tour", "ruta cultural"
# #             ],
# #             "conferencias": [
# #                 "conferencia", "programa", "seminario", "simposio", "ponencia"
# #             ],
# #             "charlas": [
# #                 "charla", "panel", "conversatorio", "mesa redonda", "q&a"
# #             ],
# #             "ferias": [
# #                 "feria", "expo", "congreso", "muestra", "bazar", "mercado"
# #             ],
# #             "social running": [
# #                 "running", "carrera", "club de corredores", "entrenamiento grupal"
# #             ]
# #         }
# #     },
# #     "Música": {
# #         "intereses": {
# #             "Pop": ["pop", "indie pop", "synth pop"],
# #             "Rock": ["rock", "rock alternativo", "metal", "punk", "grunge", "garage"],
# #             "Hip Hop / Rap": ["hip hop", "rap", "freestyle", "trap", "batalla"],
# #             "Reggaetón": ["reggaeton", "urbano", "perreo", "latin urban"],
# #             "Música electrónica (EDM)": [
# #                 "edm", "electronica", "dj", "house music", "techno", "trance", "rave"
# #             ],
# #             "R&B": ["r&b", "soul", "neo soul"],
# #             "Música latina": ["latina", "salsa", "bachata", "cumbia", "regional"],
# #             "Jazz": ["jazz", "blues", "big band", "jam session"],
# #             "Clásica": ["clasica", "orquesta", "sinfonica", "ensamble de cuerdas"],
# #             "Country": ["country", "folk", "bluegrass"]
# #         },
# #         "actividad_g": {
# #             "Concierto": [
# #                 "concierto", "en vivo", "live set", "presentacion en vivo",
# #                 "showcase", "tocada", "recital", "gig"
# #             ],
# #             "escuchar álbum o playlist": [
# #                 "album", "playlist", "listening party", "session"
# #             ]
# #         }
# #     },
# #     "Deportes": {
# #         "intereses": {
# #             "Fútbol": ["futbol", "soccer", "liga mx", "partido de futbol"],
# #             "Automovilismo": ["formula", "automovilismo", "rally", "karting"],
# #             "Tenis": ["tenis", "padel"],
# #             "Baloncesto": ["basket", "baloncesto", "basquetbol", "nba"],
# #             "Béisbol": ["beisbol", "softbol"],
# #             "box": ["box", "boxeo"],
# #             "lucha": ["lucha", "wrestling", "lucha libre"],
# #             "artes marciales": ["artes marciales", "mma", "jiu jitsu", "karate", "taekwondo"],
# #             "americano": ["americano", "football", "nfl", "tocho"]
# #         },
# #         "actividad_g": {
# #             "Ver partido": [
# #                 "vs", "jornada", "partido", "match", "temporada", "final", "semifinal"
# #             ],
# #             "asistir": [
# #                 "evento deportivo", "torneo", "competencia", "campeonato"
# #             ]
# #         }
# #     },
# #     "Actividad física": {
# #         "intereses": {
# #             "leve": ["caminata", "senderismo ligero", "wellness walk", "movilidad"],
# #             "moderada": ["hiking", "trekking", "clase funcional", "pilates", "yoga"],
# #             "alta": ["maraton", "carrera", "crossfit", "spartan", "triatlon"]
# #         },
# #         "actividad_g": {
# #             "Salir a correr": ["running", "trote", "club runner", "5k", "10k"],
# #             "correr": ["carrera", "maraton", "medio maraton", "trail run"],
# #             "caminar": ["caminata", "walking", "senderismo"],
# #             "hiking": ["hiking", "trekking", "montanismo"],
# #             "entrenar": ["crossfit", "yoga", "pilates", "fitness"]
# #         }
# #     }
# # }


# def preparar_taxonomia():
#     taxonomia_normalizada = {}

#     for clase, data in TAXONOMIA.items():
#         taxonomia_normalizada[clase] = {"intereses": {}, "actividad_g": {}}

#         for tipo in ("intereses", "actividad_g"):
#             for etiqueta, keywords in data[tipo].items():
#                 taxonomia_normalizada[clase][tipo][etiqueta] = [
#                     normalizar(keyword) for keyword in keywords
#                 ]

#     return taxonomia_normalizada


# TAXONOMIA_NORMALIZADA = preparar_taxonomia()


# def contar_keyword(texto, keyword):
#     patron = rf"(?<!\w){re.escape(keyword)}(?!\w)"
#     coincidencias = re.findall(patron, texto)

#     if not coincidencias:
#         return 0

#     peso = 3 if " " in keyword else 2
#     return len(coincidencias) * peso


# def calcular_score(texto, keywords):
#     return sum(contar_keyword(texto, keyword) for keyword in keywords)


# def mejor_etiqueta(texto, mapa):
#     mejor_nombre = None
#     mejor_score = 0

#     for nombre, keywords in mapa.items():
#         score = calcular_score(texto, keywords)
#         if score > mejor_score:
#             mejor_nombre = nombre
#             mejor_score = score

#     return mejor_nombre, mejor_score


# def clasificar_evento(evento):
#     titulo = normalizar(evento.get("nombre"))
#     descripcion = normalizar(evento.get("descripcion"))

#     texto_completo = " ".join(
#         parte for parte in (titulo, descripcion) if parte)
#     texto_prioritario = " ".join(
#         [titulo, titulo, titulo, descripcion]
#     ).strip()

#     resultados = []

#     for clase, data in TAXONOMIA_NORMALIZADA.items():
#         mejor_interes, score_interes = mejor_etiqueta(
#             texto_prioritario, data["intereses"]
#         )
#         mejor_actividad, score_actividad = mejor_etiqueta(
#             texto_completo, data["actividad_g"]
#         )
#         score_clase = score_interes + score_actividad

#         if score_clase > 0:
#             resultados.append(
#                 (clase, mejor_interes, mejor_actividad, score_clase)
#             )

#     if not resultados:
#         return {
#             "clase": "Comunidad",
#             "interes": "eventos culturales",
#             "actividad_g": "Visitas",
#             "score": 0
#         }

#     resultados.sort(key=lambda x: x[3], reverse=True)
#     clase, interes, actividad, score = resultados[0]

#     return {
#         "clase": clase,
#         "interes": interes or "eventos culturales",
#         "actividad_g": actividad or "Visitas",
#         "score": score
#     }
import re
import unicodedata
from taxonomia import TAXONOMIA
# --- Normalización de texto ---


def normalizar(texto):
    texto = (texto or "").lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = texto.encode("ascii", "ignore").decode("utf-8")
    return " ".join(texto.split())


def preparar_taxonomia():
    taxonomia_normalizada = {}

    for clase, data in TAXONOMIA.items():
        taxonomia_normalizada[clase] = {"intereses": {}, "actividad_g": {}}

        for tipo in ("intereses", "actividad_g"):
            for etiqueta, keywords in data[tipo].items():
                taxonomia_normalizada[clase][tipo][etiqueta] = [
                    normalizar(keyword) for keyword in keywords
                ]

    return taxonomia_normalizada


TAXONOMIA_NORMALIZADA = preparar_taxonomia()

# --- Contar coincidencias con peso refinado ---


def contar_keyword(texto, keyword):
    patron = rf"(?<!\w){re.escape(keyword)}(?!\w)"
    coincidencias = re.findall(patron, texto)

    if not coincidencias:
        return 0

    # Peso según longitud del keyword
    if len(keyword.split()) > 1:  # palabras compuestas
        peso = 4
    elif len(keyword) <= 3:        # palabras muy cortas
        peso = 1
    else:
        peso = 2

    return len(coincidencias) * peso

# --- Calcular score total ---


def calcular_score(texto, keywords):
    return sum(contar_keyword(texto, keyword) for keyword in keywords)

# --- Encontrar la mejor etiqueta ---


def mejor_etiqueta(texto, mapa):
    mejor_nombre = None
    mejor_score = 0

    for nombre, keywords in mapa.items():
        score = calcular_score(texto, keywords)
        if score > mejor_score:
            mejor_nombre = nombre
            mejor_score = score

    return mejor_nombre, mejor_score

# --- Clasificar evento usando taxonomía ---


def clasificar_evento(evento):
    titulo = normalizar(evento.get("nombre"))
    descripcion = normalizar(evento.get("descripcion"))

    texto_completo = " ".join(
        parte for parte in (titulo, descripcion) if parte)
    texto_prioritario = " ".join(
        [titulo, titulo, titulo, descripcion]
    ).strip()

    resultados = []

    for clase, data in TAXONOMIA_NORMALIZADA.items():
        mejor_interes, score_interes = mejor_etiqueta(
            texto_prioritario, data["intereses"]
        )
        mejor_actividad, score_actividad = mejor_etiqueta(
            texto_completo, data["actividad_g"]
        )
        score_clase = score_interes + score_actividad

        if score_clase > 0:
            resultados.append(
                (clase, mejor_interes, mejor_actividad, score_clase)
            )

    if not resultados:
        return {
            "clase": "Comunidad",
            "interes": "Eventos Culturales",
            "actividad_g": "Visitas",
            "score": 0
        }

    resultados.sort(key=lambda x: x[3], reverse=True)
    clase, interes, actividad, score = resultados[0]

    return {
        "clase": clase,
        "interes": interes or "Eventos Culturales",
        "actividad_g": actividad or "Visitas",
        "score": score
    }
