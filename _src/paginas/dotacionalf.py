"""Página de DotacionALF (ALF-16). Fuentes: Manual y Normativa de DotacionALF 1.0 (docs/MANUAL.md, docs/NORMATIVA.md),
VENTA/06_Dotacion/LEEME.txt, claude/ALF-16_DotacionALF_estado.md y las capturas de la interfaz (logs/capturas)."""
import json


def pagina(g):
    section, sec_head, outs, shots, steps = g["section"], g["sec_head"], g["outs"], g["shots"], g["steps"]
    P = g["P"]
    ins = P["dotacionalf"]["instalador"]
    img = "img/dotacionalf/"

    funciones = section(
        sec_head("Qué hace", "Todo el sistema de agua fría, en una sola memoria",
                 "Recorres siete páginas en orden y los resultados se recalculan con cada cambio. Al final exportas la memoria "
                 "de cálculo en Word, su PDF, el Excel y el esquema del sistema.")
        + outs([
            ("2.2", "Dotación diaria", "Vivienda por persona según el clima, con la R.M. 0107-2025-VIVIENDA, y todos los usos del 2.2.",
             ["169, 155 y 129 L/persona/día (cálido, templado, frío)",
              "Población del Cuadro N.° 02 de la A.020",
              "Régimen anterior para proyectos en trámite"]),
            ("ANEXO 3", "Máxima demanda simultánea", "Método de Hunter, por grupos de aparatos repetidos.",
             ["Uso privado (Anexo 1) o público (Anexo 2)",
              "Columna de tanque o de válvula (fluxómetro)",
              "Agua caliente y termas (3.2 y 3.4)"]),
            ("2.4", "Cisterna y tanque elevado", "Volumen útil según el sistema y dimensiones en múltiplos de 5 cm.",
             ["Cisterna ≥ ¾ Dd y tanque ≥ ⅓ Dd en el sistema mixto",
              "Alturas libres y rebose del 2.4 i) a m)",
              "Tanque prefabricado de 600 a 10 000 L o de concreto"]),
            ("4", "Agua contra incendio", "El programa sugiere el criterio según la altura y los niveles de la edificación.",
             ["IS.010 4.2 (25 m³) y 4.3 (40 m³)",
              "A.130 art. 69 (28 m³), caudal × tiempo o manual",
              "La reserva se suma al depósito elegido"]),
            ("2.3", "Medidor y alimentación", "La tubería se elige de menor a mayor diámetro con Hazen-Williams y las pérdidas locales.",
             ["Pérdida del medidor limitada al 50 % de la carga",
              "Accesorios con su K editable",
              "Velocidad máxima del 2.3 f)"]),
            ("2.5", "Equipo de bombeo", "Caudal, diámetros del Anexo 5, altura dinámica total y potencia comercial.",
             ["NPSH disponible con la altitud del distrito",
              "Dos equipos alternados",
              "Hidroneumático y presión constante"]),
        ], cls="outs outs-3"),
        "funciones", first=True)

    ejemplo = section(
        sec_head("El resultado", "Así sale un proyecto",
                 "El ejemplo de la vivienda unifamiliar de tres pisos en Chota, en clima frío: 798 L/día de dotación, cisterna de 1.02 m³, "
                 "tanque elevado prefabricado de 1.10 m³ y un equipo de bombeo de 0.5 HP. Todas las verificaciones cumplen.")
        + shots([
            (img + "ui_dotacion.jpg", 1500, 844,
             "Página Dotación diaria: 798 L/día para 6 personas con la dotación por clima, tabla de viviendas con dormitorios y personas, y otros usos como áreas verdes.",
             "Dotación por persona según el clima"),
            (img + "ui_almacenamiento.jpg", 1500, 844,
             "Página Almacenamiento y agua contra incendio: sistema cisterna con bombeo y tanque elevado, dimensiones de la cisterna y tanque prefabricado.",
             "Cisterna, tanque elevado y reserva contra incendio"),
            (img + "ui_bombeo.jpg", 1500, 844,
             "Página Equipo de bombeo: caudal de 0.820 L/s, succión de 1 1/4 e impulsión de 1 pulgada, altura dinámica total de 17.04 m, potencia de 1 × 0.5 HP y NPSH disponible de 5.76 m, con los accesorios de succión e impulsión.",
             "Equipo de bombeo: ADT, potencia y NPSH"),
            (img + "ui_resultados_multifamiliar.jpg", 1500, 844,
             "Resultados del ejemplo de edificio multifamiliar en Lima: 10 150 L/día, cisterna de 7.74 m³, tanque de 5.00 m³ y bombeo de 2 × 3 HP, con la tabla de verificaciones.",
             "Ejemplo multifamiliar: resultados y verificaciones"),
        ], style="margin-top:.5rem")
        + shots([
            (img + "pdf_caratula.jpg", 1059, 1497,
             "Carátula de la memoria descriptiva y de cálculo del sistema de agua fría en Times New Roman.",
             "Memoria: carátula"),
            (img + "pdf_dotacion.jpg", 1059, 1497,
             "Página de la memoria con la dotación diaria, el almacenamiento y la regulación.",
             "Memoria: dotación y almacenamiento"),
            (img + "pdf_esquema.jpg", 1059, 1497,
             "Página de la memoria con el esquema del sistema con equipo hidroneumático y el resumen de verificaciones.",
             "Memoria: esquema y verificaciones"),
        ], cls="shots shots-pdf")
        + '<p class="fine" style="margin-top:1.2rem">Las páginas de la memoria son de un proyecto de prueba con equipo hidroneumático. '
          'Sin licencia, la memoria, el PDF y el Excel llevan la marca «VERSIÓN DE EVALUACIÓN». El cálculo en pantalla es completo.</p>',
        "ejemplo")

    norma = section(
        sec_head("Norma", "Con la dotación por clima de 2025",
                 "La R.M. N.° 0107-2025-VIVIENDA (El Peruano, 12-abr-2025) cambió la dotación de vivienda: ahora es por persona y depende "
                 "del clima. Muchas plantillas siguen usando la tabla anterior por área del lote y por dormitorios.")
        + outs([
            ("VIGENTE", "Por persona y clima", "Un departamento de 3 dormitorios en clima templado da 4 × 155 = 620 L/día. "
             "Con la tabla anterior eran 1 200 L/día.", [], " out-hl"),
            ("CLIMA", "Mapa del SENAMHI", "Escribe el símbolo del mapa, por ejemplo B(i)C′, y el programa lee el carácter térmico. "
             "El símbolo queda citado en la memoria."),
            ("ANTERIOR", "Proyectos en trámite", "El texto anterior se aplica solo a proyectos con expediente aprobado o licencia en "
             "trámite antes del 12-abr-2025."),
        ], cls="outs outs-3")
        + '<p class="fine">De dónde sale cada número, y qué es norma y qué es criterio del proyectista, está en el documento '
          '<a href="tutoriales/Normativa_DotacionALF_1.0.pdf" target="_blank" rel="noopener">Normativa y criterios de cálculo (PDF)</a>. '
          'La memoria declara los criterios en un apartado propio.</p>',
        "norma")

    pasos = section(
        sec_head("Cómo funciona", "Tres pasos, del proyecto a la memoria")
        + steps([
            ("Crea el proyecto", "Elige vivienda unifamiliar, multifamiliar, local educativo, oficinas o comercio, o abre un ejemplo. "
             "Indica el distrito: el programa propone su altitud para el NPSH."),
            ("Completa las páginas", "Dotación, aparatos, almacenamiento, alimentación y bombeo. Las celdas amarillas son editables y "
             "todo se recalcula al instante."),
            ("Exporta", "Memoria en Word con formato de expediente, PDF, Excel con el cálculo por hojas y el esquema del sistema en PNG."),
        ])
        + shots([
            (img + "ui_aparatos.jpg", 1500, 844,
             "Página Aparatos sanitarios con grupos de aparatos, unidades de gasto y máxima demanda simultánea por Hunter.",
             "Aparatos y máxima demanda simultánea (Hunter)"),
            (img + "ui_alimentacion.jpg", 1500, 844,
             "Página Medidor y tubería de alimentación con la presión en la red, accesorios y selección del diámetro.",
             "Medidor y tubería de alimentación"),
        ]),
        "")

    faq_items = [
        ("¿Por qué la cisterna sale más pequeña que con mi plantilla?", "Desde 2025 la dotación de vivienda es por persona según el clima. Un departamento de 3 dormitorios en clima templado da 4 × 155 = 620 L/día; con la tabla anterior eran 1 200 L/día."),
        ("¿Puedo usar la norma anterior?", "Solo si el proyecto tiene expediente aprobado o licencia en trámite antes del 12 de abril de 2025. Se elige «texto anterior» en Datos del proyecto."),
        ("¿Qué edificaciones cubre?", "Vivienda unifamiliar y multifamiliar, locales educativos, oficinas, comercio y los demás usos del 2.2 de la IS.010: hospedaje, restaurantes, salud, industria, áreas verdes, entre otros."),
        ("¿Necesito Microsoft Word?", "Para la memoria en Word, no. Para exportar el PDF desde el programa, sí."),
        ("¿Qué pasa si el programa se cierra de golpe?", "Cada 3 minutos guarda una copia de respaldo si hay cambios. Al volver a abrir el proyecto o el programa, te ofrece recuperarlos."),
        ("¿Qué incluye la versión gratuita?", "Todo el cálculo, completo en pantalla, y los ejemplos. Sin licencia, la memoria, el PDF y el Excel salen con la marca «VERSIÓN DE EVALUACIÓN». La licencia es por computadora."),
        ("¿Quién firma la memoria?", "El ingeniero responsable del proyecto, que revisa los resultados. DotacionALF es una herramienta de apoyo."),
    ]

    jsonld = '<script type="application/ld+json">' + json.dumps({
        "@context": "https://schema.org", "@type": "SoftwareApplication", "name": "DotacionALF",
        "applicationCategory": "EngineeringApplication", "operatingSystem": "Windows 10, Windows 11",
        "softwareVersion": ins["version"], "url": "https://www.alfbim.com/dotacionalf",
        "description": "Dotación, cisterna, tanque elevado, agua contra incendio y equipo de bombeo según la IS.010, con memoria en Word.",
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "PEN"},
        "author": {"@type": "Person", "name": "Anderson Irigoín Colunche"}}, ensure_ascii=False) + "</script>"

    return {
        "id": "dotacionalf",
        "title": "DotacionALF · Dotación, cisterna, tanque y bombeo con la IS.010",
        "og_title": "DotacionALF · Dotación por clima 2025, cisterna, tanque y bombeo",
        "desc": "Calcula la dotación con la tabla por clima de la R.M. 0107-2025-VIVIENDA, la cisterna y el tanque elevado, la reserva "
                "contra incendio, la alimentación y el equipo de bombeo según la IS.010, con la memoria en Word. Gratis para Windows.",
        "nav": [("#funciones", "Funciones"), ("#ejemplo", "Ejemplo"), ("#norma", "Norma"),
                ("#precios", "Precios"), ("#preguntas", "Preguntas")],
        "hero": {
            "crumb": "DotacionALF para Windows",
            "h1": "Dotación y bombeo",
            "h1em": "con la IS.010",
            "lede": "DotacionALF calcula el sistema de agua fría de una edificación: la dotación con la tabla por clima de 2025, la cisterna "
                    "y el tanque elevado, la reserva contra incendio, el medidor, la tubería de alimentación y el equipo de bombeo. "
                    "Entrega la memoria de cálculo en Word, el PDF y el Excel.",
            "cta2": ("#ejemplo", "Ver el proyecto de ejemplo"),
            "trial": 'Gratis con todas las funciones · <a href="%s" target="_blank" rel="noopener">Manual (PDF)</a>' % P["dotacionalf"]["manual"],
            "meta": ["Windows 10 / 11", "R.M. 0107-2025-VIVIENDA", "NPSH según la altitud"],
            "img": {"src": img + "ui_resultados.jpg", "w": 1500, "h": 844,
                    "alt": "Página de resultados de DotacionALF para la vivienda unifamiliar de ejemplo en Chota: dotación de 798 L/día, cisterna de 1.02 m³, tanque elevado de 1.10 m³, máxima demanda de 0.820 L/s, alimentación de 1/2 pulgada y bombeo de 1 × 0.5 HP, con las verificaciones que cumplen.",
                    "cap": "Resultados · vivienda en Chota (ejemplo)",
                    "legend": ["Dotación, cisterna, tanque y bombeo", "Verificaciones con su artículo de la IS.010"]},
        },
        "tiles": [
            ("#descargar", "down", "Descargar gratis", "Instalador para Windows 10 y 11"),
            ("#norma", "drop", "Dotación por clima 2025", "R.M. 0107-2025-VIVIENDA"),
            ("#ejemplo", "doc", "Memoria en Word", "Times New Roman, lista para el expediente"),
        ],
        "secciones": [funciones, ejemplo, norma, pasos],
        "faq": faq_items,
        "dl_titulo": "Descarga DotacionALF gratis",
        "dl_texto": "Instalador para Windows 10 y 11; no necesita Python. Trae tres ejemplos: vivienda en Chota, edificio multifamiliar "
                    "en Lima y colegio en Cajamarca.",
        "dl_extra": '<a class="btn btn-ghost" href="tutoriales/Normativa_DotacionALF_1.0.pdf" target="_blank" rel="noopener">Normativa (PDF)</a>',
        "plataforma": "Windows 10 / 11",
        "tm": "Word y Excel son marcas de Microsoft. DotacionALF es un desarrollo independiente de ALF_BIM y no está afiliado a ellas.",
        "jsonld": jsonld,
    }
