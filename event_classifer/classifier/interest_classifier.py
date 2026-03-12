# event_classifier/classifier/interest_classifier.py

from ..semantic.interests import INTERESTS
from ..utils.scoring import keyword_score
from ..config import DEFAULT_INTEREST, DEBUG_MODE


def detect_interest(text, category):
    """
    Detecta el interés de un evento según su texto y categoría.

    :param text: Texto limpio del evento (nombre + descripción)
    :param category: categoría previamente detectada
    :return: interés (string)
    """

    possible_interests = INTERESTS.get(category, {})

    if not possible_interests:
        if DEBUG_MODE:
            print(
                f"[InterestClassifier] No se encontraron intereses para la categoría '{category}'. Usando default.")
        return DEFAULT_INTEREST

    scores = {}

    # Calcular score por cada interés posible
    for interest, keywords in possible_interests.items():
        score = keyword_score(text, keywords)
        scores[interest] = score
        if DEBUG_MODE:
            print(
                f"[InterestClassifier] Interest: '{interest}' Score: {score}")

    # Elegir interés con mayor score
    best_interest = max(scores, key=scores.get)
    best_score = scores[best_interest]

    if best_score == 0:
        # Fallback si no hay coincidencias
        if DEBUG_MODE:
            print(
                f"[InterestClassifier] Ningún interés coincidió. Usando default '{DEFAULT_INTEREST}'.")
        return DEFAULT_INTEREST

    return best_interest
