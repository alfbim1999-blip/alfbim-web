"""Página de MemoriaEstructuralALF (ALF-06). Fuentes: VENTA/05_MemoriaEstructural/6_INTERNO/FICHA_WEB_MemoriaEstructuralALF.md,
VENTA/05_MemoriaEstructural/LEEME.txt (versión 1.2.1) y las capturas de 5_MARCA/capturas."""
import json


def pagina(g):
    section, sec_head, outs, shots, steps = g["section"], g["sec_head"], g["outs"], g["shots"], g["steps"]
    P = g["P"]
    pid = "memoriaestructuralalf"
    ins = P[pid]["instalador"]
    img = "img/memoriaestructuralalf/"

    funciones = section(
        sec_head("Qué hace", "La E.030 verificada punto por punto, desde tu modelo de ETABS",
                 "Conectas el programa a ETABS: lee los resultados, verifica la Norma E.030 (2026 o 2018) y redacta la memoria de cálculo "
                 "con tablas, gráficos y el artículo de la norma en cada verificación.")
        + outs([
            ("ETABS", "Lee el modelo", "Por la API de ETABS: si faltan resultados, corre el análisis.",
             ["Niveles, masas, modos y cortantes",
              "Derivas, muros (piers) y losas",
              "Casos y combinaciones"]),
            ("PARÁMETROS", "Z, U, S, TP y TL", "Zona sísmica por distrito, con el Anexo II de la E.030-2026.",
             ["Vs30 interpolado y Ts",
              "Estudio de sitio",
              "Sistema estructural y R según el cortante en los muros"]),
            ("IRREGULARIDADES", "Calculadas con el modelo", "Cada una con su sustento; Ia e Ip según la versión de la norma.",
             ["Torsional, piso blando, masa y geometría vertical",
              "Discontinuidad de muros y esquinas entrantes",
              "Diafragma y sistemas no paralelos"]),
            ("ANÁLISIS", "Estático y dinámico", "Período modal, hn/CT o Rayleigh, C, k y la distribución de fuerzas.",
             ["Cortante mínimo y factor de escala",
              "Centros de masa y de rigidez",
              "Peso sísmico"]),
            ("DERIVAS", "Derivas, junta y redundancia", "Con 0.75·R o 0.85·R según el sistema.",
             ["Junta sísmica",
              "Redundancia (art. 53)",
              "Datos para los planos"]),
            ("E.030 EN ETABS", "Aplica la norma en el modelo", "Opcional: antes guarda una copia del modelo.",
             ["Espectro de diseño y casos espectrales",
              "30 % en la dirección perpendicular y excentricidad 0.05",
              "Coeficientes estáticos y factor de escala"]),
        ], cls="outs outs-3"),
        "funciones", first=True)

    resultado = section(
        sec_head("El resultado", "Así se ve un edificio verificado",
                 "Las verificaciones salen en tarjetas, con su valor, el límite de la norma y si cumple. Lo que no cumple sale en rojo, "
                 "con el artículo que lo pide.")
        + shots([
            (img + "ui_resultados_graficos.jpg", 1300, 731,
             "Pestaña Gráficos de los resultados: espectro de pseudoaceleraciones de la E.030-2026 y derivas de entrepiso por piso en X y en Y, con el límite de la norma.",
             "Espectro de la E.030-2026 y derivas por piso"),
            (img + "ui_irregularidades.jpg", 1300, 731,
             "Página de irregularidades en altura y en planta calculadas con el modelo de ETABS, con su sustento.",
             "Irregularidades calculadas con el modelo"),
            (img + "ui_proyecto.jpg", 1300, 731,
             "Página Datos del proyecto: edificio de muros de concreto de 9 niveles en Miraflores, Lima, con la zona sísmica 4 (Z = 0.45) tomada del Anexo II de la E.030-2026.",
             "Zona sísmica por distrito (Anexo II)"),
        ])
        + '<p class="fine" style="margin-top:1.2rem">Las muestras son de tres modelos de prueba: muros de concreto de 9 niveles (E.030-2026), '
          'vivienda de albañilería confinada (E.030-2026) y concreto armado con pórticos y sistema dual (E.030-2018).</p>',
        "resultado")

    entrega = section(
        sec_head("Qué entrega", "La memoria de cálculo, lista para el expediente")
        + outs([
            ("WORD Y PDF", "Memoria de cálculo", "En Times New Roman, con carátula e índice.",
             ["Generalidades, normas y modelo",
              "Parámetros, espectro, peso sísmico y análisis modal",
              "Análisis estático y dinámico, irregularidades y derivas",
              "Resumen de verificaciones, conclusiones, recomendaciones y firma"], " out-hl"),
            ("EXCEL", "Resultados por hoja", "Para revisar cada número o llevarlo a otro documento.",
             ["Parámetros y espectro",
              "Modal, estático y dinámico",
              "Derivas e irregularidades"]),
            ("GRÁFICOS", "Para la memoria y los planos", "En imagen, listos para pegar.",
             ["Espectro de diseño",
              "Derivas y cortantes por nivel",
              "Planta con el centro de masa y el de rigidez"]),
        ], cls="outs outs-3")
        + '<p class="fine">De dónde sale cada verificación y su artículo está en el documento '
          '<a href="tutoriales/Normativa_MemoriaEstructuralALF_1.0.pdf" target="_blank" rel="noopener">Criterios normativos (PDF)</a>.</p>',
        "entrega", tono="tone-stone")

    validado = section(
        sec_head("Validado", "Probado con memorias firmadas y modelos reales",
                 "Reproduce los valores de una memoria de cálculo firmada (edificio de muros, E.030-2018): espectro, período por Rayleigh, "
                 "C, k, ZUCS/R, factor de escala y junta. Se probó de punta a punta con cinco modelos de ETABS reales: albañilería confinada, "
                 "muros de concreto, pórticos y sistema dual.")
        + steps([
            ("Abre tu modelo en ETABS", "Con el análisis corrido o sin correr: el programa lo corre si faltan resultados."),
            ("Lee el modelo", "Indica el distrito, la categoría y el suelo. El programa calcula los parámetros y el sistema estructural."),
            ("Revisa las verificaciones", "Cada tarjeta dice si cumple y por qué. Si quieres, aplica la E.030 en ETABS y vuelve a leer."),
            ("Exporta la memoria", "Word, PDF y Excel con los gráficos, listos para el expediente."),
        ])
        + shots([
            (img + "ui_resultados.jpg", 1300, 731,
             "Página Resultados y memoria del edificio de 9 niveles: R de 3.60, períodos, cortante dinámico frente al estático y deriva máxima, con dos verificaciones que no cumplen y su artículo de la norma.",
             "Resultados: lo que no cumple, con su artículo"),
        ]),
        "validado")

    faq_items = [
        ("¿Qué versión de ETABS necesito?", "ETABS 21 con su licencia, en la misma computadora (probado con ETABS 21.1). El programa se conecta a ETABS por su API."),
        ("¿Aplica la E.030-2026 o la 2018?", "Las dos. La versión 2026 (R.M. N.° 183-2026-VIVIENDA) y la 2018 para los proyectos comprendidos en la disposición transitoria."),
        ("¿Modifica mi modelo de ETABS?", "Solo si eliges «Aplicar la E.030 en ETABS». Antes de hacerlo guarda una copia del modelo."),
        ("¿Qué pasa si mi espectro tiene otro R o ya está escalado?", "El programa lo reconoce, también el sismo moderado de la E.070, y lleva todo a la escala de la norma."),
        ("¿Necesito Microsoft Word?", "Para la memoria en Word, no. Para exportar el PDF desde el programa, sí."),
        ("¿Qué incluye la versión gratuita?", "Todas las verificaciones, completas en pantalla. Sin licencia, la memoria en Word y PDF lleva marca de agua y el Excel sale marcado y protegido."),
        ("¿Quién firma la memoria?", "El ingeniero civil colegiado responsable del proyecto. El programa verifica el análisis y redacta la memoria; no reemplaza su criterio."),
    ]

    jsonld = '<script type="application/ld+json">' + json.dumps({
        "@context": "https://schema.org", "@type": "SoftwareApplication", "name": "MemoriaEstructuralALF",
        "applicationCategory": "EngineeringApplication", "operatingSystem": "Windows 10, Windows 11",
        "softwareVersion": ins["version"], "url": "https://www.alfbim.com/memoriaestructuralalf",
        "description": "Verificación sísmica E.030 (2026 y 2018) desde ETABS y memoria de cálculo estructural en Word, PDF y Excel.",
        "offers": {"@type": "Offer", "price": str(P[pid]["precio"]["mensual"]), "priceCurrency": "PEN"},
        "author": {"@type": "Person", "name": "Anderson Irigoín Colunche"}}, ensure_ascii=False) + "</script>"

    return {
        "id": pid,
        "title": "MemoriaEstructuralALF · Verificación E.030 desde ETABS y memoria de cálculo",
        "og_title": "MemoriaEstructuralALF · De tu modelo de ETABS a la memoria E.030",
        "desc": "Conecta el programa a ETABS, verifica la Norma E.030 (2026 o 2018) punto por punto y genera la memoria de cálculo estructural "
                "en Word y PDF con tablas, gráficos y el artículo de la norma. Versión gratuita para Windows.",
        "nav": [("#funciones", "Funciones"), ("#resultado", "Resultado"), ("#entrega", "Entregables"),
                ("#precios", "Precios"), ("#preguntas", "Preguntas")],
        "hero": {
            "crumb": "MemoriaEstructuralALF para Windows",
            "h1": "De ETABS a la memoria E.030, en minutos",
            "lede": "MemoriaEstructuralALF lee tu modelo de ETABS, verifica la Norma E.030 (2026 o 2018) punto por punto y redacta la memoria "
                    "de cálculo en Word y PDF, con tablas, gráficos y el artículo de la norma en cada verificación.",
            "cta2": ("#resultado", "Ver un edificio verificado"),
            "trial": 'Gratis para verificar · <a href="%s" target="_blank" rel="noopener">Manual (PDF)</a>' % P[pid]["manual"],
            "meta": ["Windows 10 / 11", "ETABS 21", "E.030 2026 y 2018"],
            "img": {"src": img + "ui_resultados.jpg", "w": 1300, "h": 731,
                    "alt": "Página de resultados de MemoriaEstructuralALF con las tarjetas de R, períodos, cortante mínimo y derivas, y la tabla de verificaciones de la E.030.",
                    "cap": "Resultados de la verificación",
                    "legend": ["Verificaciones con su artículo de la E.030", "Lo que no cumple sale en rojo"]},
        },
        "tiles": [
            ("#descargar", "down", "Descargar gratis", "Instalador para Windows 10 y 11"),
            ("#funciones", "layers", "E.030 2026 y 2018", "Zona sísmica por distrito"),
            ("#entrega", "doc", "Memoria en Word y PDF", "Times New Roman, lista para el expediente"),
        ],
        "secciones": [funciones, resultado, entrega, validado],
        "faq": faq_items,
        "dl_titulo": "Descarga MemoriaEstructuralALF",
        "dl_texto": "Instalador para Windows 10 y 11 de 64 bits; no necesita administrador. Necesitas ETABS 21 con licencia en la misma computadora.",
        "dl_extra": '<a class="btn btn-ghost" href="tutoriales/Normativa_MemoriaEstructuralALF_1.0.pdf" target="_blank" rel="noopener">Criterios normativos (PDF)</a>',
        "plataforma": "Windows 10 / 11 · ETABS 21",
        "tm": "ETABS es marca registrada de Computers and Structures, Inc. Word y Excel son marcas de Microsoft. MemoriaEstructuralALF es un desarrollo independiente de ALF_BIM y no está afiliado a ellas.",
        "jsonld": jsonld,
    }
