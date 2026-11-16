"""Página de Simulacion4DALF (ALF-23). Fuentes: Manual_Simulacion4DALF_1.1.pdf, VENTA/19_Simulacion4DALF/LEEME.txt,
claude/ALF-23_Simulacion4DALF_estado.md."""
import json


def pagina(g):
    section, sec_head, outs, steps = g["section"], g["sec_head"], g["outs"], g["steps"]
    P = g["P"]
    ins = P["simulacion4dalf"]["instalador"]

    funciones = section(
        sec_head("Qué hace", "Tu cronograma, dentro del modelo de Revit",
                 "Simulacion4DALF une cada actividad del cronograma de obra con sus elementos del modelo y de sus vínculos, y muestra "
                 "la obra avanzar por fechas con colores. Con las valorizaciones, compara lo programado con lo real.")
        + outs([
            ("VÍNCULO", "Actividades ↔ elementos", "Por los Id de MetradosALF y PresupuestoALF, por reglas y a mano.",
             ["Modelo + vínculos (EST, ARQ, IISS, IIEE)",
              "Tramos por piso de CronogramaALF",
              "Lo dudoso marcado para revisar"]),
            ("4D", "La obra por fechas", "Por construir, en preparación, en ejecución, en acabados y terminado.",
             ["Paso por día, semana o mes",
              "Ladrillos de techo con su losa",
              "Sin tocar materiales: filtros de vista"]),
            ("PROCESO", "Alertas constructivas", "Avisa si algo empieza antes de que termine lo que lo sostiene.",
             ["Columnas, vigas, losas y muros",
              "Vaciado monolítico de vigas y losa",
              "Los acabados no cuentan como apoyo"]),
            ("REAL", "Programado vs. real", "Con el .alfv de ValorizacionesALF o cortes a mano.",
             ["Atrasado en rojo, adelantado en verde",
              "Curva S programada y real",
              "Desfase por actividad"]),
            ("SALIDAS", "Imágenes y reporte", "Láminas Full HD con franja, series para video y Excel.",
             ["Cobertura del vínculo y alertas",
              "Simulación por fechas",
              "Times New Roman, sin rutas"]),
            ("INFORME", "InformeMensualALF", "Láminas para el panel fotográfico y el anexo PDF del mes.",
             ["Programado vs. real al corte",
              "Curva S y actividades con desfase",
              "Sin duplicar al reenviar"]),
        ], cls="outs outs-3"),
        "funciones", first=True)

    pasos = section(
        sec_head("Cómo funciona", "Cuatro pasos dentro de Revit")
        + steps([
            ("Elige el cronograma", "El .alfcr de CronogramaALF o el XML de MS Project, y las fuentes del vínculo (presupuesto y metrados)."),
            ("Revisa el vínculo", "Cada actividad con sus elementos, la cobertura, lo que queda sin actividad y las alertas."),
            ("Aplica al modelo", "Las fechas van a los parámetros ALF4D_* y se crea la vista «ALF 4D - Simulación»."),
            ("Simula y exporta", "Recorre las fechas, compara con lo real y exporta imágenes, Excel y el anexo del informe."),
        ]),
        "")

    faq_items = [
        ("¿Qué versiones necesito?", "Revit 2023, 2024, 2025, 2026 o 2027 en Windows 10 u 11. No hace falta instalar Python ni MS Project."),
        ("¿Sirve con MS Project?", "Sí: guarda el cronograma como XML (Archivo → Guardar como → XML). Con CronogramaALF las fechas son las mismas de su Gantt, con los tramos por piso."),
        ("¿Cambia mi modelo?", "Solo escribe parámetros ALF4D_* y crea una vista con filtros. No cambia materiales ni geometría, y «Quitar 4D» lo deja como estaba, también en los vínculos."),
        ("¿Y los modelos vinculados?", "Lee sus elementos y, si quieres colores en ellos, escribe los parámetros en sus archivos (pregunta antes y guarda un respaldo)."),
        ("¿Cómo funciona la prueba gratis?", "En el botón «Licencia» escribes tu correo y pulsas «Enviarme el código». Con el código de 6 dígitos se activan 14 días con todas las funciones. Hay una prueba por persona y por PC."),
        ("¿Reemplaza al residente?", "No. Es una herramienta de apoyo: el cronograma, el vínculo y las alertas los revisa el profesional responsable."),
    ]

    jsonld = '<script type="application/ld+json">' + json.dumps({
        "@context": "https://schema.org", "@type": "SoftwareApplication", "name": "Simulacion4DALF",
        "applicationCategory": "DesignApplication", "operatingSystem": "Windows 10, Windows 11",
        "softwareVersion": ins["version"], "url": "https://www.alfbim.com/simulacion4dalf",
        "description": "Complemento de Revit que une el cronograma de obra con el modelo BIM: simulación 4D por fechas, programado vs. real, alertas de proceso constructivo, imágenes y reportes.",
        "offers": {"@type": "Offer", "price": str(P["simulacion4dalf"]["precio"]["mensual"]), "priceCurrency": "PEN"},
        "author": {"@type": "Person", "name": "Anderson Irigoín Colunche"}}, ensure_ascii=False) + "</script>"

    return {
        "id": "simulacion4dalf",
        "title": "Simulacion4DALF · Simulación 4D en Revit con tu cronograma",
        "og_title": "Simulacion4DALF · La obra por fechas dentro del modelo de Revit",
        "desc": "Complemento de Revit 2023–2027 que une el cronograma de obra (CronogramaALF o MS Project) con el modelo y sus vínculos: "
                "simulación 4D por fechas, programado vs. real con las valorizaciones, alertas de proceso constructivo, imágenes, Excel y anexo para el informe mensual. Prueba gratis 14 días.",
        "nav": [("#funciones", "Funciones"), ("#precios", "Precios"), ("#preguntas", "Preguntas")],
        "hero": {
            "crumb": "Simulacion4DALF para Revit",
            "h1": "Simulación 4D",
            "h1em": "con tu cronograma de obra",
            "lede": "Simulacion4DALF une cada actividad del cronograma con sus elementos de Revit y muestra la obra avanzar por fechas. "
                    "Compara lo programado con lo real, avisa de faltas al proceso constructivo y prepara las imágenes del informe.",
            "cta2": ("#funciones", "Ver qué hace"),
            "trial": 'Prueba gratis 14 días con todas las funciones · <a href="%s" target="_blank" rel="noopener">Manual (PDF)</a>' % P["simulacion4dalf"]["manual"],
            "meta": ["Revit 2023–2027", "CronogramaALF · MS Project", "ValorizacionesALF"],
            "img": {"cap": "Cronograma → modelo → obra por fechas", "panel": '<ul class="hpanel">'
                    '<li><span class="hc">01</span><b>Vínculo</b><span class="hu">Id · reglas</span><small>Actividades con sus elementos del modelo y de los vínculos.</small></li>'
                    '<li><span class="hc">02</span><b>Fechas</b><span class="hu">4D</span><small>Por construir, en ejecución, en acabados, terminado.</small></li>'
                    '<li><span class="hc">03</span><b>Real</b><span class="hu">valorizaciones</span><small>Atrasado y adelantado; curva S.</small></li>'
                    '<li><span class="hc">04</span><b>Informe</b><span class="hu">láminas · Excel</span><small>Para el informe mensual de la obra.</small></li>'
                    '</ul>'},
        },
        "tiles": [
            ("#descargar", "down", "Prueba gratis 14 días", "Instalador para Revit 2023–2027"),
            ("#funciones", "layers", "Modelo y vínculos", "Estructuras, arquitectura e instalaciones"),
            ("#funciones", "check", "Alertas de proceso", "Lo que empieza antes de su apoyo"),
        ],
        "secciones": [funciones, pasos],
        "faq": faq_items,
        "dl_titulo": "Descarga Simulacion4DALF y pruébalo 14 días",
        "dl_texto": "Instalador para Revit 2023–2027 en Windows 10 y 11, con el manual. Al terminar, abre Revit y busca la pestaña Simulacion4DALF.",
        "plataforma": "Revit 2023–2027",
        "tm": "Autodesk y Revit son marcas registradas de Autodesk, Inc. Microsoft Project y Excel son marcas de Microsoft. "
              "Simulacion4DALF es un desarrollo independiente de ALF_BIM y no está afiliado a ellas.",
        "jsonld": jsonld,
    }
