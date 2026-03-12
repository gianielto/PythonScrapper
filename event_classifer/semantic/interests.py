# event_classifier/semantics/interests.py

"""
Diccionario de intereses por categoría.
Se usa en interest_classifier.py para detectar el interés correcto dentro de cada categoría.
"""

INTERESTS = {

    "musica": {
        "pop": [
            "pop", "pop music", "pop concert", "pop show", "top hits", "chart music", "radio hits", "mainstream",
            "teen pop", "dance pop", "synth pop", "electropop", "pop festival", "pop live", "pop tour", "pop session"
        ],
        "rock": [
            "rock", "metal", "indie", "alternativo", "rock music", "rock concert", "alternative", "hard rock",
            "punk", "grunge", "classic rock", "progressive rock", "garage rock", "rock festival", "rock tour",
            "psychedelic rock", "emo", "post punk", "soft rock", "rock live"
        ],
        "hiphop": [
            "hip hop", "rap", "trap", "hiphop", "rap concert", "urban music", "rap battle", "freestyle", "rap session",
            "boom bap", "old school hip hop", "new school hip hop", "gangsta rap", "conscious rap", "underground hip hop",
            "rap festival", "cypher", "hip hop dance", "turntablism"
        ],
        "reggaeton": [
            "reggaeton", "reggaeton party", "reggaeton concert", "reggaeton session", "reggaeton hits", "latino urbano",
            "trap latino", "dembow", "perreo", "reggaeton urbano", "reggaeton festival", "reggaeton live"
        ],
        "electronica": [
            "edm", "techno", "house", "trance", "dj set", "dj session", "electronic", "electronic music", "dance music",
            "rave", "festival edm", "tech house", "deep house", "progressive house", "dubstep", "drum and bass",
            "electronica live", "electro pop", "minimal techno", "hardstyle"
        ],
        "r&b": [
            "r&b", "soul", "rnb", "rhythm and blues", "neo soul", "urban r&b", "contemporary r&b", "smooth r&b",
            "quiet storm", "r&b live", "r&b concert", "motown", "funk", "blue-eyed soul"
        ],
        "latina": [
            "salsa", "bachata", "cumbia", "latin music", "musica latina", "merengue", "reggae latino", "salsa night",
            "tropical music", "latin pop", "latin dance", "vallenato", "flamenco latino", "latin festival", "latin concert"
        ],
        "k-pop": [
            "kpop", "k pop", "k-pop music", "kpop dance", "kpop concert", "idol group", "boy band kpop", "girl group kpop",
            "kpop fanmeeting", "kpop showcase", "kpop tour", "kpop stage", "kpop live"
        ],
        "country": [
            "country", "country music", "western", "bluegrass", "folk country", "americana", "country live",
            "honky tonk", "country festival", "country tour", "country singer", "country duo"
        ],
        "jazz": [
            "jazz", "blues", "jazz music", "blues music", "smooth jazz", "jazz night", "jazz festival",
            "bebop", "swing", "cool jazz", "jazz fusion", "big band", "improv jazz", "acid jazz", "vocal jazz", "jazz concert"
        ],
        "clasica": [
            "orquesta", "sinfonica", "clasica", "classical", "classical music", "symphony", "opera", "chamber music",
            "concert hall", "baroque", "romantic classical", "modern classical", "solo recital", "classical festival",
            "sacred music", "classical live", "classical concert", "philarmonic"
        ]
    },

    "artes_escenicas": {
        "drama": [
            "drama", "dramaturgia", "dramatic play", "play", "tragedia", "teatro serio", "obra teatral",
            "drama contemporáneo", "drama clásico", "drama psicológico", "drama histórico", "drama social",
            "drama experimental", "drama familiar", "drama romántico", "drama histórico", "dramatic reading",
            "romantico", "romance", "tragedia", "melodrama", "obra dramatica"
        ],
        "comedia": [
            "comedia", "humor", "standup", "stand up", "comedy show", "humorístico", "improv", "monologo",
            "sketch", "funny play", "parodia", "sátira", "slapstick", "comedia romántica", "comedia negra",
            "comediante", "cabaret", "comedia musical", "comic relief",    "open mic",  "show comico"
        ],
        "accion/aventura": [
            "accion", "aventura", "action", "adventure", "action movie", "thrill", "adrenalina",
            "thriller", "espionaje", "superheroes", "stunts", "fight choreography", "martial arts",
            "blockbuster", "action show", "chase scene", "explosions",
            "epico", "heroe", "superheroe", "batalla"
        ],
        "terror/suspenso": [
            "terror", "horror", "suspenso", "thriller", "scary", "haunted", "horror night",
            "psychological horror", "gore", "slasher", "paranormal", "ghost story", "horror play",
            "horror film", "dark theatre", "macabre", "spooky", "suspense thriller",
            "misterio",  "espeluznante"
        ],
        "cinecia_ficcion/fantasia": [
            "sci fi", "fantasia", "fantasía", "science fiction", "fantasy", "sf", "space opera",
            "futuristic", "magic", "magical", "cyberpunk", "steampunk", "dystopia", "utopia",
            "time travel", "sci fi play", "fantasy show", "fantastic theatre",
            "ficcion", "ciencia ficcion", "magia", "cosplay", "anime", "aventura", "fantastico", "inmersivo", "recorrido interactivo"
        ],
        "ballet": [
            "ballet", "danza clásica", "classical dance", "ballet show", "ballet performance",
            "pointe", "pas de deux", "variation", "ballet gala", "story ballet", "contemporary ballet"
        ],
        "contemporanea": [
            "contemporaneo", "contemporánea", "contemporary dance", "modern dance", "experimental dance",
            "improvisation dance", "fusion dance", "physical theatre", "performance art", "site-specific dance",
            "contact improvisation", "dance installation"
        ],
        "danza_folklorica": [
            "folklorico", "folclorica", "tradicional", "folk dance", "traditional dance", "cultural dance",
            "danzas tipicas", "danza regional", "danza autóctona", "festival folklórico", "ritual dance",
            "heritage dance", "ethnic dance"
        ],
        "danza_urbana": [
            "hip hop dance", "breakdance", "danza urbana", "street dance", "urban dance", "freestyle dance",
            "dance battle", "popping", "locking", "krump", "house dance", "voguing", "urban showcase",
            "crew performance", "b-boying", "b-girling"
        ]
    },

    "comunidad": {
        "eventos_culturales": [
            "cultura", "arte", "historia", "museo", "galería", "exposición", "expo", "showcase",
            "patrimonio", "evento cultural", "festival cultural", "feria de arte", "tour cultural",
            "noche cultural", "taller creativo", "cuenta cuentos", "intercambio cultural",
            "evento folclórico", "feria de artesanía", "charla de artistas",
            "tradicion", "colectivo", "mercado creativo", "exposicion", "travel & outdoor", "religion & spirituality", "food & drink"
        ],
        "politico": [
            "política", "gobierno", "política pública", "debate", "asamblea ciudadana", "elecciones",
            "compromiso cívico", "mitin político", "sesión parlamentaria", "reunión legislativa",
            "foro político", "taller de políticas públicas", "seminario político", "campaña", "evento cívico", " government & politics"
        ],
        "ciencia": [
            "ciencia", "tecnología", "investigación", "innovación", "charla tecnológica", "feria de ciencias",
            "evento STEM", "taller científico", "laboratorio de innovación", "hackathon",
            "presentación de investigación", "conferencia científica", "expo tecnológica",
            "reunión de tecnología", "tour de laboratorio",
            "innovacion", "robotica", "ia", "inteligencia artificial", "astronomia", "investigacion", "divulgacion cientifica", "bootcamp", "tech workshop",
            "science & technology"
        ],
        "academico": [
            "universidad", "educación", "estudio", "clase", "curso", "seminario", "taller",
            "sesión de estudio", "coloquio", "simposio", "conferencia académica", "presentación de investigación",
            "panel académico", "encuentro estudiantil", "círculo de aprendizaje", "programa de mentoría",
            "foro académico"
            "conferencia", "charla",  "masterclass", "clase abierta", "capacitacion", "foro", "panel"
        ],
        "corporativos": [
            "negocios", "empresarios", "startup", "emprendimiento", "empresa", "conferencia",
            "networking", "pitch", "charla de negocios", "ventas", "gala", "industria",
            "evento empresarial", "liderazgo", "marketing", "finanzas", "inversión", "capital de riesgo",
            "demo day", "panel de inversionistas", "cumbre empresarial", "reunión ejecutiva",
            "lanzamiento de producto", "taller corporativo", "retiro corporativo", "business & professional"
            "empresarial", "negocio",
        ],
        "deportiva": [
            "deporte", "atletas", "evento deportivo", "partido", "torneo", "carrera", "juego",
            "entrenamiento", "maratón", "triatlón", "evento de ciclismo", "competencia de natación",
            "partido de fútbol", "partido de baloncesto", "torneo de rugby", "partido de hockey",
            "sesión de fitness", "clínica deportiva", "deportes juveniles", "actividad deportiva de equipo"
        ]
    },

    "deportes": {
        "futbol": ["futbol", "soccer", "football", "futbol match", "soccer game", "liga", "premier league", "champions league"],
        "automovilismo": ["formula", "rally", "nascar", "motorsport", "race", "auto racing", "car race", "grand prix"],
        "tenis": ["tenis", "tennis", "tennis match", "grand slam", "tennis tournament"],
        "baloncesto": ["basket", "nba", "baloncesto", "basketball", "hoops", "basket game"],
        "basebol": ["beisbol", "baseball", "baseball game", "mlb", "home run"],
        "box": ["boxeo", "boxing", "boxing match", "knockout", "boxing event"],
        "lucha": ["lucha libre", "wrestling", "wrestling show", "pro wrestling", "fight night"],
        "artes_marciales": ["mma", "karate", "taekwondo", "martial arts", "judo", "combat sport", "bjj"],
        "americano": ["futbol americano", "american football", "nfl", "gridiron"]
    },

    "actividad_fisica": {
        "leve": ["leve", "suave", "ligera", "light exercise", "easy run", "walk", "stretch", "gentle hike"],
        "moderada": ["moderada", "media", "medium exercise", "moderate run", "jogging", "cycling", "hike", "dance workout"],
        "alta": ["alta", "intensa", "dura", "high intensity", "hard run", "marathon", "intense workout", "bootcamp", "crossfit", "hiit"]
    }
}
