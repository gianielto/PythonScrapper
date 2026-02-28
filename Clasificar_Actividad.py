import unicodedata
from collections import defaultdict


def normalizar(texto):
    texto = texto.lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = texto.encode("ascii", "ignore").decode("utf-8")
    return texto


TAXONOMIA = {
    "Artes escénicas": {
        "intereses": {
            "Comedia": ["stand up", "comediante", "comedia", "show comico"],
            "Drama": ["drama", "romantico", "romance", "tragedia"],
            "Ciencia Ficción / Fantasía": ["fantasia", "magia", "harry potter", "castillo vagabundo"],
            "Danza Folclórica / Tradicional": ["samba", "folclor", "tradicional"],
            "Danza Moderna": ["danza moderna"],
            "Danza Clásica (Ballet)": ["ballet"],
            "Contemporánea": ["contemporanea"],
            "Terror / Suspenso": ["terror", "suspenso"],
            "Acción / Aventura": ["accion", "aventura"]
        },
        "actividad_g": {
            "show standup": ["stand up", "comediante"],
            "Obra de teatro": ["obra", "teatro"],
            "opera": ["opera"],
            "cine": ["cine", "pelicula", "proyeccion"],
            "danza": ["danza", "samba", "ballet"]
        }
    },

    "Comunidad": {
        "intereses": {
            "académico": ["conferencia", "charla", "programa", "academico"],
            "corporativos": ["gala", "industria", "networking"],
            "eventos culturales": ["cultural", "arte", "festival"],
            "fantasia": ["recorrido interactivo", "experiencia inmersiva"],
            "ciencia": ["ciencia", "tecnologia"],
            "deportiva": ["carrera", "running"]
        },
        "actividad_g": {
            "Visitas": ["recorrido", "visita guiada"],
            "conferencias": ["conferencia", "programa"],
            "charlas": ["charla", "panel"],
            "ferias": ["feria", "expo", "congreso"],
            "social running": ["running", "carrera"]
        }
    },

    "Música": {
        "intereses": {
            "Pop": ["pop"],
            "Rock": ["rock"],
            "Hip Hop / Rap": ["hip hop", "rap"],
            "Reggaetón": ["reggaeton"],
            "Música electrónica (EDM)": ["edm", "electronica", "dj"],
            "R&B": ["r&b"],
            "Música latina": ["latina", "salsa"],
            "Jazz": ["jazz"],
            "Clásica": ["clasica", "orquesta"],
            "Country": ["country"]
        },
        "actividad_g": {
            "Concierto": ["concierto", "en vivo"],
            "escuchar álbum o playlist": ["album", "playlist"]
        }
    },

    "Deportes": {
        "intereses": {
            "Fútbol": ["futbol"],
            "Automovilismo": ["formula", "automovilismo"],
            "Tenis": ["tenis"],
            "Baloncesto": ["basket", "baloncesto"],
            "Béisbol": ["beisbol"],
            "box": ["box"],
            "lucha": ["lucha"],
            "artes marciales": ["artes marciales"],
            "americano": ["americano"]
        },
        "actividad_g": {
            "Ver partido": ["vs", "jornada", "partido"],
            "asistir": ["evento deportivo"]
        }
    },

    "Actividad física": {
        "intereses": {
            "leve": ["caminata"],
            "moderada": ["hiking"],
            "alta": ["maraton", "carrera"]
        },
        "actividad_g": {
            "Salir a correr": ["running"],
            "correr": ["carrera"],
            "caminar": ["caminata"],
            "hiking": ["hiking"]
        }
    }
}


def clasificar_evento(evento):
    texto = normalizar(evento["nombre"] + " " + evento["descripcion"])

    resultados = []

    for clase, data in TAXONOMIA.items():
        score_clase = 0
        mejor_interes = None
        mejor_actividad = None
        max_interes_score = 0
        max_actividad_score = 0

        for interes, keywords in data["intereses"].items():
            score = sum(1 for palabra in keywords if palabra in texto)
            if score > max_interes_score:
                max_interes_score = score
                mejor_interes = interes

        for actividad, keywords in data["actividad_g"].items():
            score = sum(1 for palabra in keywords if palabra in texto)
            if score > max_actividad_score:
                max_actividad_score = score
                mejor_actividad = actividad

        score_clase = max_interes_score + max_actividad_score

        if score_clase > 0:
            resultados.append(
                (clase, mejor_interes, mejor_actividad, score_clase))

    if not resultados:
        return {
            "clase": "Comunidad",
            "interes": "eventos culturales",
            "actividad_g": "Visitas",
            "score": 0
        }

    resultados.sort(key=lambda x: x[3], reverse=True)
    clase, interes, actividad, score = resultados[0]

    return {
        "clase": clase,
        "interes": interes,
        "actividad_g": actividad,
        "score": score
    }
