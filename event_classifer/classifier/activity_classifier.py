# event_classifier/classifier/activity_classifier.py
# from ..semantics.categories import ACTIVITIES
from ..semantic.activities import ACTIVITIES
from ..utils.scoring import keyword_score
from ..config import DEFAULT_ACTIVITY, DEBUG_MODE


def detect_activity(text, category):
    """
    Detecta la actividad general de un evento según su texto y categoría.

    :param text: Texto limpio del evento (nombre + descripción)
    :param category: Categoría previamente detectada
    :return: actividad general (string)
    """

    # Obtener actividades posibles para la categoría
    possible_activities = ACTIVITIES.get(category, {})

    if not possible_activities:
        if DEBUG_MODE:
            print(
                f"[ActivityClassifier] No se encontraron actividades para la categoría '{category}'. Usando default.")
        return DEFAULT_ACTIVITY

    # Scoring de coincidencias
    scores = {}
    for activity, keywords in possible_activities.items():
        score = keyword_score(text, keywords)
        scores[activity] = score
        if DEBUG_MODE:
            print(
                f"[ActivityClassifier] Activity: '{activity}' Score: {score}")

    # Elegir actividad con mayor score
    best_activity = max(scores, key=scores.get)
    best_score = scores[best_activity]

    if best_score == 0:
        # Fallback si no hay coincidencias
        if DEBUG_MODE:
            print(
                f"[ActivityClassifier] Ninguna actividad coincidió. Usando default '{DEFAULT_ACTIVITY}'.")
        return DEFAULT_ACTIVITY

    return best_activity
