"""Página de la Plantilla Excel Estructuras ALF (gratuita, E.060)."""
import json


def pagina(g):
    section, sec_head, outs, shots, steps = g["section"], g["sec_head"], g["outs"], g["shots"], g["steps"]
    pid = "plantilla-excel-estructuras"
    ins = g["P"][pid]["instalador"]
    REP = "tutoriales/Ejemplo_Reporte_Estructuras_ALF.pdf"

    jsonld = '<script type="application/ld+json">' + json.dumps({
        "@context": "https://schema.org", "@type": "SoftwareApplication",
        "name": "Plantilla Excel Estructuras ALF", "softwareVersion": ins["version"],
        "operatingSystem": "Windows", "applicationCategory": "DesignApplication",
        "description": "Plantilla Excel gratuita para el diseño en concreto armado con la Norma E.060: vigas, columnas, placas, "
                       "losas, aligerados, escaleras, zapatas y muros de contención.",
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "PEN"},
        "url": "https://www.alfbim.com/" + pid,
        "publisher": {"@type": "Organization", "name": "ALF_BIM"},
    }, ensure_ascii=False) + "</script>"

    funciones = section(
        sec_head("Qué calcula", "15 hojas para diseñar una edificación de concreto armado",
                 "Copias los momentos y cortantes de tu análisis (ETABS o SAP2000) en las celdas amarillas y cada hoja "
                 "diseña y verifica el elemento con la Norma E.060-2009, con las cargas de la E.020, el sismo de la E.030 "
                 "y las escaleras de la A.010.")
        + outs([
            ("VIGA", "Diseño de vigas", "Hasta 6 secciones por viga, con las reglas del capítulo 21 para sistemas sismorresistentes.",
             ["Doble armadura con f's real, 1 o 2 capas", "Cortante por capacidad y confinamiento", "Anclajes del refuerzo"]),
            ("COLUMNA", "Columnas a flexocompresión", "Diagramas de interacción en X y en Y con las 9 combinaciones.",
             ["Flexión biaxial por Bresler", "Esbeltez con amplificación de momentos", "Columna fuerte–viga débil, Ash, Lo y So"]),
            ("PLACA", "Placas y muros de corte", "Flexocompresión y cortante amplificado Vu = Vua·Mn/Mua.",
             ["αc, ρh y ρv", "Elementos de borde (21.9.7)", "Diagrama de interacción"]),
            ("LOSAS", "Losa maciza y aligerado", "Losa en dos direcciones por coeficientes (13.7, casos 1 a 9) y aligerado de 1 a 5 tramos.",
             ["As mínimo por 1.2·Mcr y bastones", "Cortante del aligerado", "Deflexiones con Ie de Branson y diferidas"]),
            ("ESCALERA", "Escalera con descanso", "Tramo con descanso: geometría según la A.010, metrado de cargas, flexión y cortante.",
             ["Geometría y predimensionamiento", "Verificación por cortante (E.060 11.3)", "Croquis del tramo que se actualiza solo"]),
            ("ZAPATAS", "Zapatas y cimientos", "Aislada con momentos biaxiales, conectada de lindero, combinada y cimiento corrido.",
             ["Punzonamiento con transferencia de momento", "Viga de conexión e invertida", "Cimiento corrido de concreto simple"]),
            ("MURO", "Muro de contención en voladizo", "Con empuje sísmico por Mononobe–Okabe y diente (llave de corte).",
             ["Estabilidad y presiones sobre el suelo", "Diseño de la pantalla y de la zapata", "Diente con 50 % del empuje pasivo"]),
            ("APOYO", "Predimensionamiento y anclajes", "Predimensiona losas, vigas, columnas y placas, y calcula longitudes de desarrollo.",
             ["ld, ganchos, ldc y empalmes", "Tablas de varillas y cargas E.020", "Coeficientes de losas de la E.060"]),
        ]),
        "funciones", first=True)

    ejemplo = section(
        sec_head("El reporte", "Así sale el reporte en PDF",
                 'Cada hoja ya está configurada en A4 y ajustada al ancho: en Excel, Archivo → Exportar → Crear PDF. '
                 'El reporte de los ejemplos tiene 43 páginas; <a href="%s" target="_blank" rel="noopener">míralo completo antes de descargar</a>.' % REP)
        + shots([
            ("img/plantilla-excel-estructuras/pdf_viga.jpg", 1059, 1497, "Página A4 del reporte: diseño de viga sísmica según la NTE E.060, con datos de entrada, propiedades y diseño por flexión.", "Viga sísmica · E.060 cap. 10, 11 y 21"),
            ("img/plantilla-excel-estructuras/pdf_columna.jpg", 1059, 1497, "Página A4 del reporte: diseño de columna a flexocompresión biaxial con la tabla de combinaciones de carga.", "Columna · flexocompresión biaxial"),
            ("img/plantilla-excel-estructuras/pdf_zapata.jpg", 1059, 1497, "Página A4 del reporte: zapata aislada con momentos, presiones del terreno y verificación de punzonamiento.", "Zapata aislada con momentos"),
        ], "shots shots-pdf", "margin-top:.5rem")
        + shots([
            ("img/plantilla-excel-estructuras/pdf_escalera.jpg", 1059, 1497, "Página A4 del reporte: diseño de escalera de un tramo con descanso según la NTE E.060.", "Escalera de un tramo con descanso"),
            ("img/plantilla-excel-estructuras/pdf_muro.jpg", 1059, 1497, "Página A4 del reporte: croquis de la sección del muro de contención en voladizo, que se actualiza con los datos.", "Muro de contención · croquis de la sección"),
            ("img/plantilla-excel-estructuras/pdf_inicio.jpg", 1059, 1497, "Página A4 de la hoja INICIO con los datos del proyecto, el índice de hojas y las instrucciones de uso.", "Hoja INICIO: datos del proyecto e índice"),
        ], "shots shots-pdf")
        + shots([
            ("img/plantilla-excel-estructuras/croquis_zapata.jpg", 1380, 890, "Croquis en planta de la zapata aislada con la columna y la sección crítica de punzonamiento, que se actualiza con los datos.", "Croquis de la zapata en planta: se actualiza con los datos", "wide"),
        ])
        + '<p class="fine">Los datos del proyecto que llenas en la hoja INICIO salen en el encabezado de cada página del reporte.</p>',
        "ejemplo")

    como = section(
        sec_head("Cómo se usa", "Tres pasos, del análisis al reporte")
        + steps([
            ("Llena el proyecto", "En la hoja INICIO escribe el proyecto, la ubicación y el responsable. Salen en el encabezado de cada reporte."),
            ("Copia los esfuerzos", "Las celdas amarillas son datos y las grises, resultados. Copia los momentos, cortantes y cargas axiales de tu análisis y revisa los «CUMPLE» de cada verificación."),
            ("Exporta a PDF", "Archivo → Exportar → Crear PDF. Cada hoja ya está en A4 y ajustada al ancho. Las hojas están protegidas sin contraseña, por si necesitas adaptarlas."),
        ]),
        "como")

    verif = section(
        sec_head("Verificación", "Fórmulas revisadas contra el texto oficial",
                 "La plantilla aplica la NTE E.060-2009 (D.S. 010-2009-VIVIENDA), verificada artículo por artículo contra el texto oficial.")
        + outs([
            ("FÓRMULAS", "2 846 fórmulas sin errores", "Probadas con escenarios límite en todas las hojas y en Excel de Windows.", [], " out-hl"),
            ("REVISIÓN", "Tres revisiones independientes", "Diagramas de interacción, Mononobe–Okabe, zapata combinada, deflexiones, esbeltez y f's, comparados con cálculos propios.", []),
            ("ALCANCE", "Diseño, no análisis", "No reemplaza a ETABS o SAP2000: los esfuerzos vienen de tu modelo. Losas y aligerados usan el método de coeficientes de la norma.", []),
        ], "outs outs-3")
        + '<p class="fine">Es una herramienta de apoyo: los resultados los revisa y firma un ingeniero civil colegiado.</p>'
        + '<div class="sec-head" style="margin-top:3.5rem;margin-bottom:1.5rem"><p class="eyebrow">Siguiente paso</p>'
          '<h2>Del Excel al modelo de Revit</h2></div>'
        + outs([
            ("DE PAGO", '<a href="aceroalf.html">AceroALF</a>', "Con el acero ya diseñado, colócalo en Revit en minutos y saca las vistas, la planilla de acero y las láminas.",
             ['<a href="aceroalf.html">Conocer AceroALF →</a>'], " out-hl"),
            ("GRATIS", '<a href="planosalf.html">PlanosALF</a>', "Crea y exporta en lote las láminas de estructuras (E-01, E-02…) desde un Excel, con el índice de planos.",
             ['<a href="planosalf.html">Ver PlanosALF →</a>']),
            ("PRÓXIMAMENTE", "MemoriaEstructuralALF", "Se conecta a ETABS, verifica la E.030 y arma la memoria de cálculo en Word.",
             ['<a href="%s" target="_blank" rel="noopener">Avísame cuando salga →</a>' % g["E"](g["wa"]("Hola ALF_BIM, quiero enterarme cuando salga MemoriaEstructuralALF."))]),
        ], "outs outs-3"),
        "verificacion")

    return {
        "id": pid,
        "title": "Plantilla Excel de concreto armado E.060 gratis: vigas, columnas, zapatas | ALF_BIM",
        "desc": "Plantilla Excel gratuita para diseñar en concreto armado con la Norma E.060: vigas, columnas con diagrama "
                "de interacción, placas, losas, aligerados, escaleras, zapatas aisladas, conectadas y combinadas, y muros "
                "de contención con sismo. 15 hojas, sin macros, con reporte en PDF.",
        "og_title": "Plantilla Excel Estructuras ALF · Concreto armado con la E.060, gratis",
        "jsonld": jsonld,
        "nav": [("#funciones", "Qué calcula"), ("#ejemplo", "Reporte"), ("#verificacion", "Verificación"), ("#preguntas", "Preguntas")],
        "hero": {
            "crumb": "Plantilla Excel Estructuras",
            "h1": "Concreto armado", "h1em": "con la E.060, en Excel",
            "lede": "Una plantilla de 15 hojas para diseñar vigas, columnas, placas, losas, aligerados, escaleras, zapatas y "
                    "muros de contención con la Norma E.060. Copias los esfuerzos de tu análisis y sale el reporte en PDF, "
                    "listo para la memoria de cálculo.",
            "cta2": ("#ejemplo", "Ver el reporte de ejemplo"),
            "trial": 'Gratis · versión %s · <a href="%s" target="_blank" rel="noopener">Reporte de ejemplo (PDF, 43 páginas)</a>' % (ins["version"], REP),
            "meta": ["15 hojas", "Sin macros", "E.060 · E.020 · E.030"],
            "img": {"src": "img/plantilla-excel-estructuras/diagrama_interaccion.jpg", "w": 1380, "h": 750,
                    "alt": "Hoja COLUMNA del reporte: diagrama de interacción φPn–φMn en la dirección X con los puntos de las combinaciones de carga en rojo.",
                    "cap": "Hoja COLUMNA · diagrama de interacción (ejemplo)",
                    "legend": ["Curva φPn–φMn por dirección", "Puntos rojos: combinaciones de carga"]},
        },
        "tiles": [
            ("#descargar", "down", "Descargar gratis", "Excel de 15 hojas, sin macros"),
            ("#funciones", "layers", "Del predimensionamiento al muro", "Vigas, columnas, losas, zapatas"),
            (REP, "doc", "Reporte de ejemplo", "43 páginas A4 en PDF"),
        ],
        "secciones": [funciones, ejemplo, como, verif],
        "faq": [
            ("¿Qué versión de la E.060 usa?", "La NTE E.060-2009 (D.S. 010-2009-VIVIENDA), verificada contra el texto oficial. Usa las cargas de la E.020, el sismo de la E.030 y las dimensiones de escaleras de la A.010."),
            ("¿Tiene macros?", "No. Es un Excel con fórmulas, sin macros, así que no tienes que habilitar contenido para usarla."),
            ("¿Reemplaza a ETABS o SAP2000?", "No. La plantilla diseña y verifica los elementos; los momentos, cortantes y cargas axiales los copias de tu análisis estructural."),
            ("¿Puedo modificar las hojas?", "Sí. Las hojas están protegidas sin contraseña para que no borres una fórmula por error; puedes desprotegerlas si necesitas adaptarlas."),
            ("¿En qué programa la probaron?", "En Microsoft Excel para Windows. Otros programas de hojas de cálculo pueden abrirla, pero no la garantizamos en ellos."),
            ("¿Quién firma los resultados?", "Es una herramienta de apoyo. Los resultados los revisa y firma un ingeniero civil colegiado."),
        ],
        "dl_titulo": "Descarga la plantilla gratis",
        "dl_texto": "Excel de 15 hojas para el diseño en concreto armado con la E.060, sin macros. Antes de descargar puedes ver el reporte de los ejemplos en PDF.",
        "dl_extra": '<a class="btn btn-ghost" href="%s" target="_blank" rel="noopener">Reporte de ejemplo (PDF)</a>' % REP,
        "plataforma": "Microsoft Excel",
        "tm": "Excel es marca de Microsoft. ETABS y SAP2000 son marcas de Computers and Structures, Inc. "
              "La Plantilla Excel Estructuras es un desarrollo independiente de ALF_BIM y no está afiliada a ellas.",
    }
