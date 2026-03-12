# event_classifier/classifier/classify_event.py

from ..utils.text_cleaner import clean_text
from .category_classifier import detect_category
from .interest_classifier import detect_interest
from .activity_classifier import detect_activity
from ..config import NAME_WEIGHT, DESCRIPTION_WEIGHT, BASE_CONFIDENCE, CONFIDENCE_INCREMENT, MAX_CONFIDENCE, LOW_CONFIDENCE, DEBUG_MODE


def classify_event(event):
    """
    Clasifica un evento en categoría, interés y actividad general.

    :param event: dict con al menos 'name' y 'description'
    :return: dict con keys 'category', 'interest', 'activity', 'confidence'
    """

    text_name = clean_text(event.get("nombre", ""))
    text_description = clean_text(event.get("descripcion", ""))
    category = clean_text(event.get("categoria_nombre", ""))
    combined_text = f"{text_name} {text_description} {category}"

    if DEBUG_MODE:
        print(f"[ClassifyEvent] Texto combinado: {combined_text}")

    category = detect_category(combined_text)

    interest = detect_interest(combined_text, category)

    activity = detect_activity(combined_text, category)

    confidence = BASE_CONFIDENCE

    if category == "comunidad" or interest == "evento cultural" or activity == "visitas":
        confidence = LOW_CONFIDENCE
    else:
        # Incremento simple por coincidencias de palabras clave
        confidence += CONFIDENCE_INCREMENT

    # Limitar al máximo
    confidence = min(confidence, MAX_CONFIDENCE)

    return {
        "category": category,
        "interest": interest,
        "activity": activity,
        "confidence": round(confidence, 2),
        "textocombinado": combined_text
    }
