from supabase import create_client, Client
import os

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def guardar_eventos_supabase(eventos):
    for evento in eventos:
        data = {
            "nombre": evento["nombre"],
            "descripcion": evento["descripcion"],
            "imagen": evento["imagen"],
            "horarios": f"{evento['fecha_inicio']} - {evento['fecha_limite']}",
            "actividad_general": evento["actividad_g"],
            "interes": evento["interes"],
            "clase": evento["clase"]
        }
        try:
            supabase.table("actividad_especifica").insert(data).execute()
        except Exception as e:
            print(f"Error guardando evento '{evento['nombre']}': {e}")

    print(f"{len(eventos)} eventos guardados en Supabase.")
