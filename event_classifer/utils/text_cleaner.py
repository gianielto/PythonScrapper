# event_classifier/utils/text_cleaner.py

"""
Módulo para limpieza y normalización de texto.
Se utiliza antes de pasar el texto a los clasificadores.
"""

import re
import unicodedata
from ..config import STOPWORDS


def clean_text(text):
    """
    Limpia y normaliza un texto:
    - Minusculas
    - Elimina acentos
    - Quita caracteres especiales
    - Elimina stopwords simples

    :param text: string
    :return: texto limpio (string)
    """

    if not text:
        return ""

    # 1. Minusculas
    text = text.lower()

    # 2. Eliminar acentos y caracteres Unicode especiales
    text = unicodedata.normalize("NFD", text)
    text = text.encode("ascii", "ignore").decode("utf-8")

    # 3. Quitar caracteres no alfanuméricos (excepto espacios)
    text = re.sub(r"[^\w\s]", " ", text)

    # 4. Reemplazar multiples espacios por uno solo
    text = re.sub(r"\s+", " ", text).strip()

    # 5. Eliminar stopwords simples
    words = [word for word in text.split() if word not in STOPWORDS]

    return " ".join(words)
