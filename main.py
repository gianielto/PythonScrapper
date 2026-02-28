
from Extraer_DatosDE_Actividad import obtener_detalle_evento
from extraerID_Actividades import extraer_event_ids
from Clasificar_Actividad import clasificar_evento


def main():
    url = "https://www.eventbrite.com.mx/d/mexico--guadalajara/arts--events/?page=1"

    ids = extraer_event_ids(url)
    print("IDs encontrados:", ids)

    eventos = []

    for event_id in ids:
        try:

            detalle = obtener_detalle_evento(event_id)

            clasificacion = clasificar_evento(detalle)

            evento_completo = {
                "nombre": detalle.get("nombre"),
                "descripcion": detalle.get("descripcion"),
                "imagen": detalle.get("imagen"),
                "actividad_g": clasificacion.get("actividad_g"),
                "interes": clasificacion.get("interes"),
                "clase": clasificacion.get("clase"),
                "fecha_limite": detalle.get("fecha_limite"),
                "score_clasificacion": clasificacion.get("score")
            }

            eventos.append(evento_completo)

        except Exception as e:
            print(f"Error con el evento {event_id}: {e}")

    with open("eventos.txt", "w", encoding="utf-8") as f:
        f.write("===== EVENTOS ESTRUCTURADOS =====\n\n")

        for i, evento in enumerate(eventos, 1):
            f.write(f"EVENTO #{i}\n")
            f.write(f"Nombre: {evento['nombre']}\n")
            f.write(f"Descripción: {evento['descripcion']}\n")
            f.write(f"Imagen: {evento['imagen']}\n")
            f.write(f"Actividad general: {evento['actividad_g']}\n")
            f.write(f"Interés: {evento['interes']}\n")
            f.write(f"Clase: {evento['clase']}\n")
            f.write(f"Fecha límite: {evento['fecha_limite']}\n")
            f.write(f"Score clasificación: {evento['score_clasificacion']}\n")
            f.write("-" * 60 + "\n\n")

    print("\n Archivo 'eventos.txt' generado correctamente.")


if __name__ == "__main__":
    main()
