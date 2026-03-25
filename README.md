# 🕷️ PythonScrapper — Pipeline de Eventos en Guadalajara

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup4-59666C?style=for-the-badge&logo=python&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)

</div>

---

## Descripción

Pipeline automatizado de extracción, procesamiento y clasificación de eventos culturales y de ocio en **Guadalajara, México**, scrapeando datos desde **Eventbrite**.

El sistema no solo extrae datos — los filtra geográficamente, los clasifica por tipo de actividad usando un clasificador propio, y los persiste en Supabase con un score de confianza por evento.

---

## 🏗️ Pipeline de Datos

```
Eventbrite (hasta 8 páginas)
        │
        ▼
┌─────────────────────────┐
│  Extracción de IDs      │  extraerID_Actividades.py
│  (paginación + dedup)   │
└────────────┬────────────┘
             │ IDs únicos
             ▼
┌─────────────────────────┐
│  Extracción paralela    │  Extraer_DatosDE_Actividad.py
│  ThreadPoolExecutor     │  6 workers concurrentes
│  (detalles por evento)  │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│  Filtros                │
│  · Solo Guadalajara/GDL │
│  · Excluye online       │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│  Clasificación          │  event_classifer/
│  · Actividad general    │
│  · Interés              │
│  · Categoría            │
│  · Score de confianza   │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│  Persistencia           │  guardarEventos.py
│  · Supabase (DB)        │
│  · eventos.txt (local)  │
└─────────────────────────┘
```

---

## ✨ Características

- **Scraping paginado** de Eventbrite con detección automática de fin de resultados
- **Concurrencia real** con `ThreadPoolExecutor` (6 workers) para procesar eventos en paralelo
- **Filtro geográfico** por Guadalajara/GDL sobre nombre de venue, dirección y ciudad
- **Clasificador propio** de eventos con score de confianza (`event_classifer/`)
- **Normalización Unicode** para comparación robusta de texto en español
- **Salida dual**: Supabase + archivo local `eventos.txt`
- Ordenamiento por fecha + score de clasificación

---

## 📂 Estructura del Proyecto

```
PythonScrapper/
├── main.py                        # Orquestador del pipeline
├── extraerID_Actividades.py       # Extrae IDs de eventos por página
├── Extraer_DatosDE_Actividad.py   # Obtiene detalles de cada evento
├── guardarEventos.py              # Persiste en Supabase y .txt
├── event_classifer/               # Clasificador de tipo de evento
│   └── classifier/
│       └── classify_event.py
├── normalizador/                  # Utilidades de normalización de texto
├── eventos.txt                    # Salida local (generada al correr)
└── requirements.txt
```

---

## 📊 Datos extraídos por evento

```python
{
    "nombre":              "Nombre del evento",
    "descripcion":         "...",
    "imagen":              "URL de imagen",
    "actividad_g":         "Música / Arte / Deporte / ...",
    "interes":             "Categoría de interés",
    "clase":               "Clasificación detallada",
    "score_clasificacion": 0.92,           # Confianza del clasificador
    "fecha_inicio":        "2025-01-15",
    "fecha_limite":        "2025-01-15",
    "venue_nombre":        "Centro Cultural...",
    "ciudad":              "Guadalajara",
    "direccion_completa":  "...",
    "url_evento":          "https://eventbrite.com.mx/..."
}
```

---

## ⚙️ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/gianielto/PythonScrapper.git
cd PythonScrapper
```

### 2. Crear entorno virtual e instalar dependencias

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configurar variables de entorno

Crea un archivo `.env` con tus credenciales de Supabase:

```env
SUPABASE_URL=https://tu-proyecto.supabase.co
SUPABASE_KEY=tu_anon_key
```

---

## ▶️ Uso

```bash
python main.py
```

El script recorre hasta 8 páginas de Eventbrite, procesa los eventos en paralelo y genera:
- Registros en tu tabla de Supabase
- Archivo `eventos.txt` con todos los eventos estructurados

Puedes ajustar el comportamiento modificando estas constantes en `main.py`:

```python
MAX_PAGINAS = 8    # Páginas a recorrer en Eventbrite
MAX_WORKERS = 6    # Workers concurrentes para extracción de detalles
```

---

## 🗺️ Roadmap

- [ ] Filtro por fecha activo (actualmente desactivado para pruebas)
- [ ] Soporte para múltiples ciudades
- [ ] Scheduler para ejecución automática diaria
- [ ] API REST para consultar eventos clasificados
- [ ] Dashboard de visualización

---

## 👤 Autor

**Daniel Torres** — [@gianielto](https://github.com/gianielto)  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/dantocru/)
