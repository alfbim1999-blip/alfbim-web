"""Página de EtabsRevitALF (ALF-22). Fuentes: Manual_EtabsRevitALF_1.0.pdf, VENTA/17_EtabsRevitALF/LEEME.txt,
claude/ALF-22_EtabsRevitALF_estado.md."""
import json


def pagina(g):
    section, sec_head, outs, steps = g["section"], g["sec_head"], g["outs"], g["steps"]
    P = g["P"]
    ins = P["etabsrevitalf"]["instalador"]

    funciones = section(
        sec_head("Qué hace", "Del modelo de Revit al ETABS listo para analizar",
                 "Dos botones en la pestaña EtabsRevitALF de Revit: Exportar a ETABS, que crea el modelo de análisis con la norma peruana, "
                 "y Traer cambios de ETABS, que devuelve a Revit las secciones que cambiaste después del análisis.")
        + outs([
            ("GEOMETRÍA", "Pisos, nudos y secciones", "Del modelo estructural de Revit (a mano o creado con CadRevitALF).",
             ["Columnas rectangulares, circulares, en L y en T",
              "Vigas al eje de sus apoyos, con excentricidad y brazos rígidos",
              "Placas y muros de albañilería con sus vanos"]),
            ("LOSAS", "El aligerado como se modela", "Una losa en una dirección con el peso de la E.020.",
             ["Sin viguetas ni ladrillos en el modelo de análisis",
              "Losas macizas como membrana o shell",
              "Diafragma rígido por piso"]),
            ("CARGAS", "E.020", "Carga viva por uso o por ambiente de la arquitectura vinculada.",
             ["Acabados y tabiquería",
              "Muros de ladrillo como cargas lineales sobre vigas",
              "Azotea y coberturas livianas"]),
            ("SISMO", "E.030 2026 y 2018", "Con el motor de MemoriaEstructuralALF.",
             ["Zona por distrito, U, S y R",
              "Fuente de masa por categoría, SEX/SEY, espectro y casos SDX/SDY",
              "Factor de escala por el cortante mínimo"]),
            ("COMBINACIONES", "E.060", "1.4CM+1.7CV, 1.25(CM+CV)±S, 0.9CM±S y envolvente.",
             ["Proyecto de MemoriaEstructuralALF (.alfme) listo",
              "Botón para abrir MemoriaEstructuralALF",
              "Modelo guardado como .EDB nuevo"]),
            ("IDA Y VUELTA", "De ETABS a Revit", "Los cambios de sección vuelven a tu modelo.",
             ["Columnas, vigas y placas con su tipo a la medida",
              "Reporte de lo cambiado y de lo que no",
              "Para seguir con AceroALF y MetradosALF"]),
        ], cls="outs outs-3"),
        "funciones", first=True)

    lectura = section(
        sec_head("Cómo lo hace", "Las uniones que harías a mano",
                 "Revit modela lo físico; ETABS necesita nudos. EtabsRevitALF une los extremos, lleva las vigas al eje de columnas y placas, "
                 "deja excentricidades donde la viga está corrida y te muestra en una vista previa todo lo que ajustó.")
        + outs([
            ("NUDOS", "Unión con tolerancia", "Extremos cercanos se unen; las vigas que no llegan se alargan hasta su apoyo.", [], " out-hl"),
            ("ANALÍTICO", "Modelo analítico de Revit", "Si tu proyecto lo tiene (2023+), manda su ubicación y sus liberaciones."),
            ("MAPEO", "Tipos de Revit → ETABS", "Cada tipo con su rol, sección y f'c; el mapeo queda en tu perfil."),
            ("VISTA PREVIA", "En colores, por piso", "Verde exportado, naranja ajustado, rojo dudoso; clic para ver la ficha."),
            ("REPORTE", "Todo en Excel", "Lo exportado, cada ajuste de nudos, lo no exportado y por qué, y las cargas."),
            ("VALIDADO", "Contra modelos hechos a mano", "Mismos pesos, períodos y derivas en los modelos de prueba."),
        ], cls="outs outs-3"),
        "lectura")

    pasos = section(
        sec_head("Cómo funciona", "Cinco pasos dentro de Revit")
        + steps([
            ("Elige elementos y pisos", "Columnas, vigas, placas y losas; los niveles que serán pisos; la base del modelo."),
            ("Revisa el mapeo", "Cada tipo de Revit con su rol en ETABS y su sección. Las viguetas del aligerado no se exportan."),
            ("Cargas y sismo", "Distrito, categoría, suelo, sistema y versión de la E.030; uso y cargas de la E.020."),
            ("Mira la vista previa", "Nudos unidos, excentricidades y lo dudoso, piso por piso."),
            ("Crea el ETABS", "El .EDB, el reporte Excel y el proyecto de MemoriaEstructuralALF."),
        ]),
        "")

    faq_items = [
        ("¿Qué versiones necesito?", "Revit 2023, 2024, 2025, 2026 o 2027 y ETABS 21 o superior con su licencia, en el mismo equipo (Windows 10 u 11)."),
        ("¿Sirve con mi modelo hecho a mano?", "Sí. Lee columnas, vigas, muros y losas de cualquier plantilla; con la plantilla ALF_BIM_ESTRUCTURAS y los modelos de CadRevitALF reconoce además los aligerados con viguetas."),
        ("¿Cómo exporta el aligerado?", "Como una sola losa en una dirección (membrana) con el peso del aligerado de la E.020, en la dirección de las viguetas. Las viguetas y los ladrillos no se exportan."),
        ("¿Aplica la E.030 2026?", "Sí, y también la 2018. Usa el motor de MemoriaEstructuralALF: zona por distrito, U, S, R, espectro, casos dinámicos y factor de escala."),
        ("¿Puedo devolver los cambios a Revit?", "Sí. «Traer cambios de ETABS» lee las secciones del modelo que creó EtabsRevitALF y cambia los tipos de columnas, vigas y placas en Revit, con reporte."),
        ("¿Cómo funciona la prueba gratis?", "En el botón «Licencia» escribes tu correo y pulsas «Enviarme el código». Con el código de 6 dígitos se activan 14 días con todas las funciones. Hay una prueba por persona y por PC."),
        ("¿Reemplaza al ingeniero?", "No. Prepara el modelo; el ingeniero estructural responsable lo revisa y valida, con sus cargas, sus parámetros sísmicos y sus resultados."),
    ]

    jsonld = '<script type="application/ld+json">' + json.dumps({
        "@context": "https://schema.org", "@type": "SoftwareApplication", "name": "EtabsRevitALF",
        "applicationCategory": "DesignApplication", "operatingSystem": "Windows 10, Windows 11",
        "softwareVersion": ins["version"], "url": "https://www.alfbim.com/etabsrevitalf",
        "description": "Complemento de Revit que crea el modelo de ETABS desde el modelo estructural de Revit con la norma peruana (E.020, E.030, E.060) y devuelve a Revit los cambios de sección.",
        "offers": {"@type": "Offer", "price": str(P["etabsrevitalf"]["precio"]["mensual"]), "priceCurrency": "PEN"},
        "author": {"@type": "Person", "name": "Anderson Irigoín Colunche"}}, ensure_ascii=False) + "</script>"

    return {
        "id": "etabsrevitalf",
        "title": "EtabsRevitALF · De Revit a ETABS con la norma peruana",
        "og_title": "EtabsRevitALF · Del modelo de Revit al ETABS listo para analizar",
        "desc": "Complemento de Revit 2023–2027 que crea el modelo de ETABS desde el modelo estructural de Revit: nudos unidos, excentricidades, "
                "aligerados en una dirección, cargas de la E.020, sismo de la E.030 (2026 y 2018) y combinaciones de la E.060, con vista previa, reporte Excel e ida y vuelta. Prueba gratis 14 días.",
        "nav": [("#funciones", "Funciones"), ("#lectura", "Cómo lo hace"),
                ("#precios", "Precios"), ("#preguntas", "Preguntas")],
        "hero": {
            "crumb": "EtabsRevitALF para Revit",
            "h1": "De Revit a ETABS",
            "h1em": "con la norma peruana",
            "lede": "EtabsRevitALF toma tu modelo estructural de Revit y crea el modelo de ETABS listo para analizar: nudos, secciones, aligerados, "
                    "cargas de la E.020, sismo de la E.030 y combinaciones de la E.060. Y trae de vuelta a Revit las secciones que cambies.",
            "cta2": ("#lectura", "Ver cómo lo hace"),
            "trial": 'Prueba gratis 14 días con todas las funciones · <a href="%s" target="_blank" rel="noopener">Manual (PDF)</a>' % P["etabsrevitalf"]["manual"],
            "meta": ["Revit 2023–2027", "ETABS 21+", "E.020 · E.030 · E.060"],
            "img": {"cap": "Revit → ETABS → Revit", "panel": '<ul class="hpanel">'
                    '<li><span class="hc">01</span><b>Geometría</b><span class="hu">nudos · secciones</span><small>Columnas L y T, vigas, placas, aligerados y macizas.</small></li>'
                    '<li><span class="hc">02</span><b>Cargas</b><span class="hu">E.020</span><small>CV por ambiente, acabados y tabiques como cargas lineales.</small></li>'
                    '<li><span class="hc">03</span><b>Sismo</b><span class="hu">E.030</span><small>Masa, espectro, casos y factor de escala.</small></li>'
                    '<li><span class="hc">04</span><b>Combinaciones</b><span class="hu">E.060</span><small>Listo para analizar y diseñar.</small></li>'
                    '<li><span class="hc">↩</span><b>Ida y vuelta</b><span class="hu">secciones</span><small>Los cambios de ETABS vuelven a Revit.</small></li>'
                    '</ul>'},
        },
        "tiles": [
            ("#descargar", "down", "Prueba gratis 14 días", "Instalador para Revit 2023–2027"),
            ("#funciones", "layers", "Norma peruana", "E.020, E.030 y E.060"),
            ("#lectura", "check", "Vista previa en colores", "Nada se crea sin que lo veas"),
        ],
        "secciones": [funciones, lectura, pasos],
        "faq": faq_items,
        "dl_titulo": "Descarga EtabsRevitALF y pruébalo 14 días",
        "dl_texto": "Instalador para Revit 2023–2027 en Windows 10 y 11, con el manual. Necesitas ETABS 21 o superior. Al terminar, abre Revit y busca la pestaña EtabsRevitALF.",
        "plataforma": "Revit 2023–2027 · ETABS 21+",
        "tm": "Autodesk y Revit son marcas registradas de Autodesk, Inc. ETABS es marca registrada de Computers and Structures, Inc. Excel es marca de Microsoft. "
              "EtabsRevitALF es un desarrollo independiente de ALF_BIM y no está afiliado a ellas.",
        "jsonld": jsonld,
    }
