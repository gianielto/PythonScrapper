# event_classifier/semantics/activities.py

"""
Diccionario de actividades generales por categoría.
Se usa en activity_classifier.py para detectar la actividad correcta.
"""

ACTIVITIES = {

    "musica": {
        "concierto": ["concierto", "en vivo", "live set", "presentacion en vivo", "showcase", "tocada", "recital", "gig", "fiesta", "festival", "tour"],
        "escuchar_album/playlist": ["escuchar album", "ouvir álbum", "listen to album", "playlist", "listening party", "session", "streaming"]
    },

    "artes_escenicas": {
        "show standup": ["stand up", "standup", "comediante", "comedia", "open mic", "monologo", "show comico"],
        "obra de teatro": ["obra", "teatro", "puesta en escena", "funcion teatral", "dramaturgia", "drama"],
        "opera": ["opera", "zarzuela", "recital escenico", "musical"],
        "cine": ["cine", "pelicula", "proyeccion", "cortometraje", "film", "documental", "muestra de cine", "screening"],
        "danza": ["danza", "samba", "ballet", "coreografia", "baile", "ensamble", "performance dance"]
    },

    "comunidad": {
        "visitas": ["recorrido", "visita guiada", "tour", "walking tour", "universidad", "museo", "ruta cultural"],
        "feria": ["feria", "congreso", "muestra", "bazar", "mercado", "evento comunitario"],
        "conferencia": ["conferencia", "seminario", "talk", "charla", "panel", "masterclass", "presentacion", "charla", "panel", "conversatorio", "mesa redonda", "q&a"],

        "social running": ["running", "carrera", "club de corredores", "entrenamiento grupal"]
    },

    "deportes": {
        "ver": ["vs", "jornada", "partido", "match", "temporada", "final", "semifinal"],
        "asistir": ["evento deportivo", "torneo", "competencia", "campeonato"]
    },

    "actividad_fisica": {
        "correr": ["correr", "running", "jogging", "trotar"],
        "caminar": ["caminar", "walk", "paseo", "stroll"],
        "hiking": ["hiking", "senderismo", "trek", "trail", "hike"]
    }
}
