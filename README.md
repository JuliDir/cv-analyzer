# CV Analyzer con IA

Aplicacion en Python + Streamlit para evaluar el ajuste de un candidato a una vacante a partir de su CV en PDF.

## Que hace este proyecto

Este sistema permite:
- Cargar un CV en formato PDF.
- Extraer automaticamente el texto del CV.
- Comparar el perfil del candidato contra una descripcion de puesto.
- Obtener una evaluacion estructurada con fortalezas, areas de mejora y porcentaje de ajuste.

## Demo visual

![Demo CV Analyzer](assets/cv-analyzer-demo.gif)

## Stack tecnico

- Python 3.10+
- Streamlit
- LangChain
- OpenAI (modelo: gpt-4o-mini)
- Pydantic
- PyPDF2

## Estructura del proyecto

```text
cv_analyzer/
├── app.py
├── models/
│   └── cv_model.py
├── prompts/
│   └── cv_prompts.py
├── services/
│   ├── cv_evaluator.py
│   └── pdf_processor.py
└── ui/
    └── streamlit_ui.py
```

## Requisitos previos

- Python 3.10 o superior
- Una API key de OpenAI

## Configuracion local

1. Clona el repositorio.
2. Crea y activa un entorno virtual.
3. Instala dependencias.
4. Configura variables de entorno.
5. Ejecuta Streamlit.

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
# Edita .env y agrega tu OPENAI_API_KEY
streamlit run app.py
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edita .env y agrega tu OPENAI_API_KEY
streamlit run app.py
```

## Variables de entorno

Crear un archivo `.env` con:

```env
OPENAI_API_KEY=tu_api_key_aqui
```

## Como usar

1. Sube un CV en PDF desde la interfaz.
2. Escribe la descripcion del puesto con requisitos claros.
3. Haz clic en "Analizar Candidato".
4. Revisa la evaluacion y la recomendacion final.

## Limitaciones

- El resultado depende de la calidad del PDF y de la descripcion del puesto.
- CVs escaneados como imagen pueden generar extraccion incompleta.
- La evaluacion automatica no reemplaza una decision humana de reclutamiento.

## Consideraciones eticas

Este proyecto es de apoyo al analisis de perfiles. No debe utilizarse como unico criterio de contratacion. Se recomienda:
- Revision humana de resultados.
- Evaluacion estandarizada entre candidatos.
- Monitoreo de posibles sesgos.

## Roadmap

- Exportacion del analisis a PDF o JSON.
- Historial de evaluaciones.
- Soporte multilenguaje.
- Mejora de criterios y trazabilidad de scoring.

## Licencia

Este proyecto se distribuye bajo licencia MIT. Ver `LICENSE`.
