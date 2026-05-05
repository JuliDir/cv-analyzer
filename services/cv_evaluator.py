import os
from langchain_openai import ChatOpenAI
from models.cv_model import AnalisisCV
from prompts.cv_prompts import crear_sistema_prompts

def crear_evaluador_cv():
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("Falta la variable de entorno OPENAI_API_KEY")

    modelo_base = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.2
    )

    modelo_estructurado = modelo_base.with_structured_output(AnalisisCV)
    chat_prompt = crear_sistema_prompts()
    cadena_evaluacion = chat_prompt | modelo_estructurado

    return cadena_evaluacion

def evaluar_candidato(texto_cv: str, descripcion_puesto:str) -> AnalisisCV:
    try:
        cadena_evaluacion = crear_evaluador_cv()

        resultado = cadena_evaluacion.invoke({
            "texto_cv": texto_cv,
            "descripcion_puesto": descripcion_puesto
        })

        return resultado
    
    except Exception as e:
        error_msg = str(e)
        return AnalisisCV(
            nombre_candidato="Error en procesamiento",
            experiencia_años=0,
            habilidades_clave=["No fue posible completar el analisis automaticamente"],
            education="No se puede determinar.",
            experiencia_relevante="Se produjo un error durante la evaluacion del CV.",
            fortalezas=["Requiere revision manual del CV"],
            areas_mejora=[f"Detalle tecnico: {error_msg}", "Verificar OPENAI_API_KEY y conectividad"],
            porcentaje_ajuste=0
        )