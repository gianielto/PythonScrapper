# event_classifier/classifier/category_classifier.py

from ..semantic.categories import CATEGORY_KEYWORDS
from ..utils.scoring import keyword_score
from ..config import DEFAULT_CATEGORY, DEBUG_MODE


def detect_category(text):
    """
    Detecta la categoría de un evento según su texto.

    :param text: Texto limpio del evento (nombre + descripción)
    :return: categoría (string)
    """

    scores = {}

    # Calcular score por cada categoría
    for category, keywords in CATEGORY_KEYWORDS.items():
        score = keyword_score(text, keywords)
        scores[category] = score
        if DEBUG_MODE:
            print(
                f"[CategoryClassifier] Category: '{category}' Score: {score}")

    # Elegir categoría con mayor score
    best_category = max(scores, key=scores.get)
    best_score = scores[best_category]

    if best_score == 0:
        # Fallback si no hay coincidencias
        if DEBUG_MODE:
            print(
                f"[CategoryClassifier] Ninguna categoría coincidió. Usando default '{DEFAULT_CATEGORY}'.")
        return DEFAULT_CATEGORY

    return best_category
