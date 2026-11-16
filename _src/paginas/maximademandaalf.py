"""Página de MaximaDemandaALF (ALF-13). Fuentes: VENTA/03_MaximaDemanda/6_INTERNO/FICHA_WEB_MaximaDemandaALF.md,
VENTA/03_MaximaDemanda/LEEME.txt (versión 1.0.5) y las muestras de 2_MUESTRAS."""
import json


def pagina(g):
    section, sec_head, outs, shots, steps = g["section"], g["sec_head"], g["outs"], g["shots"], g["steps"]
    P = g["P"]
    pid = "maximademandaalf"
    ins = P[pid]["instalador"]
    img = "img/maximademandaalf/"

    funciones = section(
        sec_head("Qué hace", "Del área de cada ambiente al alimentador de cada tablero",
                 "Ingresas las áreas y las cargas, o las importas de Revit o de Excel. El programa calcula la máxima demanda con la Sección 050 "
                 "del CNE-Utilización y dimensiona los alimentadores tablero por tablero.")
        + outs([
            ("050", "Máxima demanda", "Por unidad y del conjunto, con la regla de cada uso.",
             ["Viviendas (050-200) y departamentos (050-202)",
              "Escuelas (050-204), salud (050-206) y hoteles (050-208)",
              "Otros usos con la Tabla 14 y cálculo por equipos (EM.010)"]),
            ("ALIMENTADORES", "Conductor, interruptor y tubería", "Corriente de diseño y escalonamiento de interruptores.",
             ["Conductor por la Tabla 2, con factores de temperatura y agrupamiento",
              "Diferencial de 30 mA y conductor de protección",
              "Caída de tensión acumulada desde el medidor (050-102)"]),
            ("TABLEROS", "Del medidor a cada subtablero", "Árbol medidor → TG → TD → TS.",
             ["Balance de fases en trifásico",
              "220 V de 3 hilos o 380/220 V",
              "Cuadro de cargas por tablero con circuitos típicos"]),
        ], cls="outs outs-3")
        + outs([
            ("OSINERGMIN", "Potencia a contratar", "Con el tipo de conexión en baja tensión, de C1.1 a C4.x.", [], " out-hl"),
            ("REVIT", "Importa los ambientes", "Desde la tabla de habitaciones de Revit o desde un Excel."),
            ("NORMA", "Reglas cotejadas", "Cada regla del CNE-U se comparó con el texto oficial en octubre de 2026."),
        ], cls="outs outs-3"),
        "funciones", first=True)

    ejemplo = section(
        sec_head("El resultado", "Así sale un edificio multifamiliar",
                 "El ejemplo del edificio multifamiliar de 5 pisos, trifásico 380/220 V: cuatro departamentos tipo A, cuatro tipo B, un local "
                 "y los servicios generales, cada uno con su interruptor, su conductor y su caída de tensión acumulada.")
        + shots([
            (img + "esquema_multifamiliar.jpg", 1698, 866,
             "Esquema general de alimentadores del edificio multifamiliar de 5 pisos: tableros TD-A y TD-B (cuatro de cada uno), TD-L1 y TSG, cada uno con su ITM, conductor NH-80, longitud, máxima demanda y caída de tensión acumulada. Lleva la marca «VERSIÓN DE EVALUACIÓN».",
             "Esquema general de alimentadores (versión de evaluación)", "wide"),
        ])
        + '<p class="fine" style="margin-top:1.2rem">Sin licencia, la memoria, el PDF, el Excel y los diagramas salen con la marca '
          '«VERSIÓN DE EVALUACIÓN». El cálculo en pantalla es completo.</p>',
        "ejemplo")

    entrega = section(
        sec_head("Qué entrega", "Memoria, cuadro de cargas y unifilares")
        + outs([
            ("WORD Y PDF", "Memoria descriptiva y de cálculo", "En Times New Roman, con índice y firma.",
             ["Bases de cálculo con las reglas citadas",
              "Detalle numérico de cada alimentador",
              "Cuadros de cargas, unifilares y conclusiones"], " out-hl"),
            ("EXCEL", "Cuadro de cargas", "Con formato de expediente.",
             ["Máxima demanda",
              "Alimentadores",
              "Cuadros por tablero y criterios"]),
            ("PNG", "Diagramas unifilares", "Listos para el plano.",
             ["Esquema general",
              "Un diagrama por tablero"]),
        ], cls="outs outs-3")
        + '<p class="fine">Las reglas y los criterios de cálculo están en el documento '
          '<a href="tutoriales/Normativa_MaximaDemandaALF_1.0.pdf" target="_blank" rel="noopener">Normativa y criterios de cálculo (PDF)</a>.</p>',
        "entrega", tono="tone-stone")

    pasos = section(
        sec_head("Cómo funciona", "Tres pasos, del proyecto a la memoria")
        + steps([
            ("Crea el proyecto", "Elige el uso y el sistema, o abre un ejemplo: vivienda unifamiliar, edificio multifamiliar o institución educativa."),
            ("Ingresa las cargas", "Áreas y cargas por ambiente, o impórtalas de Revit o Excel. Arma el árbol de tableros."),
            ("Exporta", "Memoria en Word y PDF, cuadro de cargas en Excel y diagramas unifilares."),
        ]),
        "")

    faq_items = [
        ("¿Qué norma usa?", "El CNE-Utilización 2006 (R.M. 037-2006-MEM/DM y R.M. 175-2008-MEM/DM), Sección 050 y sus tablas, y la Norma EM.010 del RNE."),
        ("¿Qué usos cubre?", "Viviendas, departamentos y su conjunto, escuelas, establecimientos de salud, hoteles, los demás usos de la Tabla 14, un uso personalizado y el cálculo por equipos."),
        ("¿Puedo importar los ambientes de Revit?", "Sí, desde la tabla de habitaciones de Revit o desde un Excel."),
        ("¿Calcula la caída de tensión?", "Sí, acumulada desde el medidor hasta cada tablero, según la Regla 050-102."),
        ("¿Necesito Microsoft Word?", "Para la memoria en Word, no. Para exportar el PDF desde el programa, sí; sin Word puedes abrir el .docx y guardarlo como PDF."),
        ("¿Qué incluye la versión gratuita?", "Todo el cálculo, completo en pantalla, y los ejemplos. Sin licencia, la memoria, el PDF, el Excel y los diagramas salen con la marca «VERSIÓN DE EVALUACIÓN»."),
        ("¿Quién firma la memoria?", "El ingeniero electricista o mecánico electricista colegiado responsable. MaximaDemandaALF es una herramienta de cálculo."),
    ]

    jsonld = '<script type="application/ld+json">' + json.dumps({
        "@context": "https://schema.org", "@type": "SoftwareApplication", "name": "MaximaDemandaALF",
        "applicationCategory": "EngineeringApplication", "operatingSystem": "Windows 10, Windows 11",
        "softwareVersion": ins["version"], "url": "https://www.alfbim.com/maximademandaalf",
        "description": "Máxima demanda, alimentadores, cuadro de cargas y memoria de cálculo de instalaciones eléctricas según el CNE-Utilización.",
        "offers": {"@type": "Offer", "price": str(P[pid]["precio"]["mensual"]), "priceCurrency": "PEN"},
        "author": {"@type": "Person", "name": "Anderson Irigoín Colunche"}}, ensure_ascii=False) + "</script>"

    return {
        "id": pid,
        "title": "MaximaDemandaALF · Máxima demanda y cuadro de cargas con el CNE-Utilización",
        "og_title": "MaximaDemandaALF · Máxima demanda, alimentadores y memoria de IIEE",
        "desc": "Calcula la máxima demanda con la Sección 050 del CNE-Utilización, los alimentadores con su interruptor, conductor y caída de tensión, "
                "y entrega la memoria en Word y PDF, el cuadro de cargas en Excel y los unifilares. Versión gratuita para Windows.",
        "nav": [("#funciones", "Funciones"), ("#ejemplo", "Ejemplo"), ("#entrega", "Entregables"),
                ("#precios", "Precios"), ("#preguntas", "Preguntas")],
        "hero": {
            "crumb": "MaximaDemandaALF para Windows",
            "h1": "Máxima demanda y cuadro de cargas con el CNE",
            "lede": "MaximaDemandaALF calcula la máxima demanda de viviendas, edificios, colegios y locales con la Sección 050 del CNE-Utilización, "
                    "dimensiona los alimentadores de cada tablero y entrega la memoria de cálculo en Word y PDF, el cuadro de cargas en Excel y los unifilares.",
            "cta2": ("#ejemplo", "Ver el ejemplo"),
            "trial": 'Gratis para calcular · <a href="%s" target="_blank" rel="noopener">Manual (PDF)</a>' % P[pid]["manual"],
            "meta": ["Windows 10 / 11", "CNE-Utilización 2006", "EM.010"],
            "img": {"cap": "Del área al alimentador", "panel": '<ul class="hpanel">'
                    '<li><span class="hc">050</span><b>Máxima demanda</b><span class="hu">por unidad y conjunto</span><small>Viviendas, departamentos, escuelas, salud, hoteles y Tabla 14.</small></li>'
                    '<li><span class="hc">T2</span><b>Conductor</b><span class="hu">Tabla 2</span><small>Con factores de temperatura y agrupamiento.</small></li>'
                    '<li><span class="hc">ITM</span><b>Interruptores</b><span class="hu">escalonados</span><small>Termomagnético, diferencial de 30 mA y conductor de protección.</small></li>'
                    '<li><span class="hc">ΔV</span><b>Caída de tensión</b><span class="hu">050-102</span><small>Acumulada desde el medidor hasta cada tablero.</small></li>'
                    '<li><span class="hc">kW</span><b>Potencia a contratar</b><span class="hu">Osinergmin</span><small>Con el tipo de conexión en baja tensión.</small></li>'
                    '</ul>'},
        },
        "tiles": [
            ("#descargar", "down", "Descargar gratis", "Instalador para Windows 10 y 11"),
            ("#funciones", "bolt", "Sección 050 del CNE-U", "Reglas cotejadas con el texto oficial"),
            ("#entrega", "doc", "Memoria en Word y PDF", "Cuadro de cargas en Excel y unifilares"),
        ],
        "secciones": [funciones, ejemplo, entrega, pasos],
        "faq": faq_items,
        "dl_titulo": "Descarga MaximaDemandaALF",
        "dl_texto": "Instalador para Windows 10 y 11 de 64 bits; no necesita administrador. Trae tres ejemplos: vivienda unifamiliar, edificio "
                    "multifamiliar de 5 pisos e institución educativa con tablero general.",
        "dl_extra": '<a class="btn btn-ghost" href="tutoriales/Normativa_MaximaDemandaALF_1.0.pdf" target="_blank" rel="noopener">Normativa (PDF)</a>',
        "plataforma": "Windows 10 / 11",
        "tm": "Revit es marca registrada de Autodesk, Inc. Word y Excel son marcas de Microsoft. MaximaDemandaALF es un desarrollo independiente de ALF_BIM y no está afiliado a ellas.",
        "jsonld": jsonld,
    }
