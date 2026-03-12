# event_classifier/utils/scoring.py

"""
Módulo de scoring para clasificador de eventos.
Se encarga de calcular la coincidencia entre texto y listas de keywords.
"""

from ..config import MIN_WORD_LENGTH, STOPWORDS


def keyword_score(text, keywords):
    """
    Calcula un score basado en la cantidad de keywords encontradas en el texto.

    :param text: Texto limpio (string)
    :param keywords: Lista de palabras clave (strings)
    :return: score (int)
    """

    score = 0
    words_in_text = set(text.split())

    for keyword in keywords:
        # Normalizamos keyword
        kw_clean = keyword.lower().strip()
        # Solo keywords con longitud suficiente
        if len(kw_clean) < MIN_WORD_LENGTH:
            continue

        # Coincidencia exacta
        if kw_clean in words_in_text:
            score += 1
            continue

        # Coincidencia parcial: si alguna palabra de la keyword aparece
        kw_words = set(kw_clean.split()) - STOPWORDS
        if kw_words & words_in_text:
            score += 1

    return score
