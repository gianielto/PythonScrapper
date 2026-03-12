# event_classifier/config.py

"""
Configuración global del clasificador de eventos.
Aquí se definen valores por defecto, pesos y parámetros de scoring.
"""

# ================================
# VALORES DEFAULT (NO NULL POLICY)
# ================================

DEFAULT_CATEGORY = "comunidad"
DEFAULT_INTEREST = "general"
DEFAULT_ACTIVITY = "evento"


# ================================
# SCORING CONFIG
# ================================

# Peso de coincidencias encontradas en el nombre del evento
NAME_WEIGHT = 2

# Peso de coincidencias encontradas en la descripción
DESCRIPTION_WEIGHT = 1

# Score mínimo para considerar una clasificación válida
MIN_SCORE_THRESHOLD = 1


# ================================
# CONFIDENCE CONFIG
# ================================

# Confidence si se usó fallback
LOW_CONFIDENCE = 0.30

# Confidence base cuando hay coincidencias
BASE_CONFIDENCE = 0.50

# Incremento por cada keyword encontrada
CONFIDENCE_INCREMENT = 0.10

# Confidence máximo permitido
MAX_CONFIDENCE = 0.95


# ================================
# TEXT PROCESSING
# ================================

# Longitud mínima de palabra considerada
MIN_WORD_LENGTH = 3

# Stopwords simples en español (puedes ampliarlas luego)
STOPWORDS = {
    "de", "la", "el", "los", "las", "un", "una",
    "y", "o", "en", "con", "para", "por", "del"
}


# ================================
# DEBUG
# ================================

# Si True imprime información de clasificación
DEBUG_MODE = False
