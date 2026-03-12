# # event_classifier/main.py

# from .classifier.classify_event import classify_event


# def main():
#     """
#     Punto de entrada del clasificador.
#     Crea un evento de prueba y ejecuta la clasificación.
#     """

#     event = {
#         "name": "Fracasados Anónimos In-House Humana11",
#         "description": (
#             "Empresarios comparten sus mayores fracasos en los negocios "
#             "con humor, aprendizaje y cerveza."
#         ),
#         "image": "https://img.evbuc.com/example.jpg",
#         "venue": "Humana11",
#         "city": "Guadalajara"
#     }

#     result = classify_event(event)

#     print("\n===== RESULTADO DE CLASIFICACIÓN =====")
#     print(f"Categoría: {result['category']}")
#     print(f"Interés: {result['interest']}")
#     print(f"Actividad general: {result['activity']}")
#     print(f"Confidence: {result['confidence']}")
#     print("======================================\n")


# if __name__ == "__main__":
#     main()
