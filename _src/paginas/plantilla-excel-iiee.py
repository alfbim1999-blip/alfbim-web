"""Página de la Plantilla Excel IIEE ALF (gratuitas): pozo a tierra, iluminación y caída de tensión."""
import json


def pagina(g):
    section, sec_head, outs, shots, steps = g["section"], g["sec_head"], g["outs"], g["shots"], g["steps"]
    E, wa = g["E"], g["wa"]
    pid = "plantilla-excel-iiee"
    ins = g["P"][pid]["instalador"]
    REP = "tutoriales/Ejemplo_Reporte_Plantilla_Excel_IIEE_ALF.pdf"

    jsonld = '<script type="application/ld+json">' + json.dumps({
        "@context": "https://schema.org", "@type": "SoftwareApplication",
        "name": "Plantilla Excel IIEE ALF", "softwareVersion": ins["version"],
        "operatingSystem": "Windows", "applicationCategory": "DesignApplication",
        "description": "Excel gratuito para instalaciones eléctricas: pozo a tierra por el método de Wenner, iluminación por "
                       "el método de los lúmenes con la EM.010-2019 y caída de tensión y sección del conductor con el CNE-Utilización.",
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "PEN"},
        "url": "https://www.alfbim.com/" + pid,
        "publisher": {"@type": "Organization", "name": "ALF_BIM"},
    }, ensure_ascii=False) + "</script>"

    resumen = section(
        sec_head("Qué calcula", "Las tres verificaciones que pide todo proyecto eléctrico",
                 "Un libro de Excel de 7 hojas, sin macros, con la normativa peruana vigente: el Código Nacional de "
                 "Electricidad – Utilización (CNE-U) y la Norma EM.010 de 2019. Cada hoja sale en A4 para el reporte en PDF.")
        + outs([
            ("POZO_TIERRA", '<a href="#pozo-a-tierra">Pozo a tierra</a>', "Resistividad por Wenner, resistencia de un pozo con relleno tratado y número de pozos para llegar a la resistencia objetivo.", [], " out-hl"),
            ("ILUMINACION", '<a href="#iluminacion">Iluminación</a>', "Método de los lúmenes con los valores del Anexo de la EM.010-2019, número y distribución de luminarias.", []),
            ("CAIDA_TENSION", '<a href="#caida-de-tension">Caída de tensión</a>', "Corriente, interruptor, capacidad del conductor y sección por caída de tensión con la Regla 050-102.", []),
            ("ILUM_AMBIENTES", "Cuadro de iluminación", "Hasta 25 ambientes en una sola tabla, con su uso y su iluminancia requerida.", []),
            ("CIRCUITOS", "Cuadro de alimentadores y circuitos", "Hasta 25 tramos con la caída de tensión acumulada y el límite del 4 %.", []),
            ("TABLAS", "Tablas normativas", "Tablas del CNE-U, la EM.010-2019, BS 7430, rellenos, luminarias y factores de utilización.", []),
        ], "outs outs-3"),
        "funciones", first=True)

    pozo = section(
        sec_head("Puesta a tierra", "Cálculo de pozo a tierra por el método de Wenner",
                 "Ingresas las lecturas del telurómetro y la hoja calcula la resistividad del terreno, la resistencia de un pozo "
                 "y cuántos pozos necesitas para cumplir la resistencia objetivo.")
        + outs([
            ("WENNER", "Resistividad del terreno", "8 lecturas en 2 direcciones perpendiculares, con gráfico (IEEE Std 81).",
             ["Resistividad de diseño: promedio, máxima o manual", "Factor estacional si mediste en época seca o húmeda", "Aviso de terreno homogéneo"]),
            ("POZO", "Varilla y relleno", "Varilla según la Regla 060-702 del CNE-U y resistencia del pozo con relleno tratado (IEEE Std 80).",
             ["Longitud ≥ 2 m y diámetro mínimo", "Comparación de 7 rellenos", "Metrado del relleno y dosis"]),
            ("POZOS", "Número de pozos", "Pozos en línea para la resistencia objetivo, con la Regla 060-712 y la BS 7430.",
             ["≤ 25 Ω, ≤ 10 Ω pararrayos o ≤ 5 Ω electrónicos", "Separación mínima entre pozos", "Conductor de puesta a tierra (Tabla 17)"]),
        ], "outs outs-3")
        + '<p class="fine">La Tabla 17 del CNE-U se entra con la <b>capacidad (A)</b> del conductor de acometida, no con su sección; la hoja lo hace así, leída de la copia autenticada del MINEM.</p>',
        "pozo-a-tierra")

    ilum = section(
        sec_head("Iluminación", "Iluminación por el método de los lúmenes con la EM.010-2019",
                 "Eliges el uso del ambiente y la hoja trae los requisitos del Anexo de la EM.010 vigente "
                 "(R.M. 083-2019-VIVIENDA): iluminancia mantenida, UGRL, uniformidad y Ra.")
        + outs([
            ("REQUISITOS", "Em, UGRL, Uo y Ra", "Listas desplegables por tipo de edificación y uso, con las 288 filas del Anexo.",
             ["No usa la tabla de 2006 con «calidad A–E»", "Factor de mantenimiento a criterio del proyectista"]),
            ("CÁLCULO", "Número de luminarias", "Índice del local, factor de utilización, número de luminarias y grilla.",
             ["Verificación de Em, separación y Ra", "Potencia instalada y W/m²"]),
            ("PLANO", "Distribución en planta", "Esquema a escala con la ubicación de las luminarias en el ambiente.",
             ["Cuadro de hasta 25 ambientes", "Listo para la memoria"]),
        ], "outs outs-3")
        + shots([
            ("img/plantilla-excel-iiee/distribucion_luminarias.jpg", 1500, 858,
             "Hoja ILUMINACION del reporte: resultado de 8 luminarias panel LED de 60 por 60 centímetros y esquema de distribución en planta de una oficina.",
             "Resultado y distribución en planta de una oficina (ejemplo)", "wide"),
        ]),
        "iluminacion")

    caida = section(
        sec_head("Conductores", "Caída de tensión y sección del conductor con el CNE-Utilización",
                 "Del dato de potencia a la designación del conductor, con las mismas tablas que usa MaximaDemandaALF, cotejadas con el CNE-U oficial.")
        + outs([
            ("CORRIENTE", "Corriente e interruptor", "Corriente de diseño 1.25·I (050-104) e interruptor termomagnético normalizado.",
             ["Monofásico o trifásico", "Mínimo del proyectista"]),
            ("CAPACIDAD", "Capacidad del conductor", "Tabla 2 del CNE-U con los factores de temperatura (5A) y de agrupamiento (5C).",
             ["Cobre, PVC 70 °C", "Hasta 240 mm²"]),
            ("CAÍDA", "Sección por caída de tensión", "Límites de la Regla 050-102: 2.5 % por tramo y 4 % en total.",
             ["Longitud máxima del circuito", "Conductor de protección y tubería"]),
        ], "outs outs-3"),
        "caida-de-tension")

    ejemplo = section(
        sec_head("El reporte", "Así sale el reporte en PDF",
                 'Un edificio de vivienda y oficinas de 4 niveles en Chota, Cajamarca, como ejemplo. '
                 '<a href="%s" target="_blank" rel="noopener">Mira el reporte completo (13 páginas)</a> antes de descargar.' % REP)
        + shots([
            ("img/plantilla-excel-iiee/pdf_pozo_tierra.jpg", 1060, 1500, "Página A4: pozo a tierra con la medición de resistividad por el método de Wenner, el gráfico y la resistividad de diseño.", "Pozo a tierra · Wenner"),
            ("img/plantilla-excel-iiee/pdf_iluminacion.jpg", 1060, 1500, "Página A4: iluminación de interiores por el método de los lúmenes con los requisitos de la EM.010.", "Iluminación · EM.010-2019"),
            ("img/plantilla-excel-iiee/pdf_caida_tension.jpg", 1060, 1500, "Página A4: caída de tensión y sección del conductor de un alimentador.", "Caída de tensión y sección"),
        ], "shots shots-pdf", "margin-top:.5rem")
        + shots([
            ("img/plantilla-excel-iiee/pdf_circuitos.jpg", 1500, 1060, "Página A4 apaisada: cuadro de alimentadores y circuitos con la caída de tensión acumulada de cada tramo.", "Cuadro de alimentadores y circuitos con la caída acumulada", "wide"),
        ]),
        "ejemplo")

    por_que = section(
        sec_head("Por qué esta", "Hecha con la norma vigente, no con la de siempre")
        + outs([
            ("EM.010-2019", "La tabla de iluminación vigente", "Muchas plantillas siguen con la tabla de 2006. Esta usa el Anexo de 2019, cotejado con dos copias de El Peruano.", [], " out-hl"),
            ("VERIFICADA", "1 492 comprobaciones, 0 diferencias", "Verificación independiente con 80 casos aleatorios y casos límite, y probada en Excel de Windows.", []),
            ("ALCANCE", "Lo que no hace", "Terreno homogéneo (sin mallas ni dos capas), sin cortocircuito. El UGRL y la Uo se verifican con DIALux o Relux.", []),
        ], "outs outs-3")
        + '<p class="fine">Es una herramienta de apoyo: los planos y memorias de instalaciones eléctricas los revisa y firma un ingeniero electricista o mecánico electricista colegiado.</p>'
        + '<div class="sec-head" style="margin-top:3.5rem;margin-bottom:1.5rem"><p class="eyebrow">Línea eléctrica ALF</p>'
          '<h2>Del cálculo rápido al proyecto completo</h2></div>'
        + outs([
            ("PRÓXIMAMENTE", "MaximaDemandaALF", "Cuadro de cargas, máxima demanda, alimentadores, interruptores y caída de tensión, con la memoria de cálculo en Word.",
             ['<a href="%s" target="_blank" rel="noopener">Avísame cuando salga →</a>' % E(wa("Hola ALF_BIM, quiero enterarme cuando salga MaximaDemandaALF."))]),
            ("PRÓXIMAMENTE", "ElectricasALF", "Circuitos, cuadro de cargas por tablero, diagrama unifilar y metrados por salidas, dentro de Revit.",
             ['<a href="%s" target="_blank" rel="noopener">Avísame cuando salga →</a>' % E(wa("Hola ALF_BIM, quiero enterarme cuando salga ElectricasALF."))]),
            ("GRATIS", '<a href="planosalf.html">PlanosALF</a>', "Crea y exporta en lote las láminas IE-01, IE-02… desde Excel, con el índice de planos.",
             ['<a href="planosalf.html">Ver PlanosALF →</a>']),
        ], "outs outs-3"),
        "por-que")

    return {
        "id": pid,
        "title": "Plantilla Excel IIEE gratis: pozo a tierra Wenner, iluminación EM.010-2019 y caída de tensión | ALF_BIM",
        "desc": "Excel gratuito para instalaciones eléctricas en el Perú: cálculo de pozo a tierra por el método de Wenner, "
                "iluminación por el método de los lúmenes con la EM.010-2019 y caída de tensión y sección del conductor con "
                "el CNE-Utilización. Sin macros, con reporte en PDF.",
        "og_title": "Plantilla Excel IIEE ALF · Pozo a tierra, iluminación y caída de tensión, gratis",
        "jsonld": jsonld,
        "nav": [("#pozo-a-tierra", "Pozo a tierra"), ("#iluminacion", "Iluminación"), ("#caida-de-tension", "Caída de tensión"), ("#preguntas", "Preguntas")],
        "hero": {
            "crumb": "Plantilla Excel IIEE",
            "h1": "Pozo a tierra, iluminación y caída de tensión", "h1em": "en un Excel gratis",
            "lede": "Calcula la resistividad por el método de Wenner y el número de pozos, la iluminación con la EM.010-2019 "
                    "y la sección del conductor por caída de tensión con el CNE-Utilización. Todo en un libro de Excel, "
                    "con reporte en PDF para la memoria.",
            "cta2": ("#ejemplo", "Ver el reporte de ejemplo"),
            "trial": 'Gratis · versión %s · <a href="%s" target="_blank" rel="noopener">Reporte de ejemplo (PDF)</a>' % (ins["version"], REP),
            "meta": ["CNE-Utilización", "EM.010-2019", "Sin macros"],
            "img": {"src": "img/plantilla-excel-iiee/wenner.jpg", "w": 1500, "h": 876,
                    "alt": "Hoja POZO_TIERRA: tabla de lecturas del método de Wenner en dos direcciones, resistividad aparente de cada lectura y gráfico de resistividad contra separación de picas.",
                    "cap": "Hoja POZO_TIERRA · lecturas Wenner (ejemplo)",
                    "legend": ["Resistividad aparente por lectura", "Dos direcciones perpendiculares"]},
        },
        "tiles": [
            ("#descargar", "down", "Descargar gratis", "Excel de 7 hojas, sin macros"),
            ("#pozo-a-tierra", "bolt", "Pozo a tierra Wenner", "Resistividad y número de pozos"),
            (REP, "doc", "Reporte de ejemplo", "13 páginas en PDF"),
        ],
        "secciones": [resumen, pozo, ilum, caida, ejemplo, por_que],
        "faq": [
            ("¿Qué versión de la EM.010 usa?", "La vigente, aprobada por la R.M. 083-2019-VIVIENDA, con su Anexo «Requisitos mínimos de iluminación»: iluminancia mantenida (Em), UGRL, uniformidad (Uo) y Ra. No usa la tabla de 2006 con «calidad A–E»."),
            ("¿Qué resistencia de puesta a tierra debo lograr?", "Eliges el objetivo según el uso: hasta 25 Ω por la Regla 060-712 del CNE-U, 10 Ω para pararrayos o 5 Ω para equipos electrónicos (práctica recomendada). La hoja calcula cuántos pozos necesitas."),
            ("¿Calcula mallas de puesta a tierra?", "No. El cálculo considera terreno homogéneo y pozos con varilla. Mallas y terrenos de dos capas quedan fuera de esta versión."),
            ("¿Los valores de los rellenos sirven para el expediente?", "Son referenciales. Para el expediente usa la resistividad que garantiza el fabricante del relleno, en la opción «Relleno manual»."),
            ("¿Qué resistividad usa en la caída de tensión?", "0.0175 Ω·mm²/m a 20 °C por defecto, la usual en el Perú. Puedes cambiarla a 0.0225 (70 °C), más conservadora, y agregar la reactancia si la necesitas."),
            ("¿Tiene macros?", "No. Es un Excel con fórmulas, sin macros. Las hojas están protegidas sin contraseña."),
            ("¿Quién firma los resultados?", "Es una herramienta de apoyo. Los planos y memorias de instalaciones eléctricas los firma un ingeniero electricista o mecánico electricista colegiado."),
        ],
        "dl_titulo": "Descarga la Plantilla Excel IIEE gratis",
        "dl_texto": "Excel de 7 hojas, sin macros: pozo a tierra, iluminación, cuadro de ambientes, caída de tensión y cuadro de circuitos. Antes de descargar puedes ver el reporte de ejemplo en PDF.",
        "dl_extra": '<a class="btn btn-ghost" href="%s" target="_blank" rel="noopener">Reporte de ejemplo (PDF)</a>' % REP,
        "plataforma": "Microsoft Excel",
        "tm": "Excel es marca de Microsoft. DIALux y Relux son marcas de sus titulares. La Plantilla Excel IIEE es un desarrollo "
              "independiente de ALF_BIM y no están afiliadas a ellas.",
    }
