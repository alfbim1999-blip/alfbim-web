"""Página de RedesInterioresALF (ALF-17). Fuentes: VENTA/07_RedesInteriores/LEEME.txt (versión 1.0.4), Manual y Normativa 1.0
y las capturas de 5_MARCA/capturas."""
import json


def pagina(g):
    section, sec_head, outs, shots, steps = g["section"], g["sec_head"], g["outs"], g["shots"], g["steps"]
    P = g["P"]
    pid = "redesinterioresalf"
    ins = P[pid]["instalador"]
    img = "img/redesinterioresalf/"

    funciones = section(
        sec_head("Qué hace", "Agua fría, agua caliente y desagüe, tramo por tramo",
                 "Dibujas la red como una lista de tramos, de nudo a nudo. El programa calcula cada tramo con la IS.010, marca en rojo lo "
                 "que no cumple con su numeral y prepara la memoria, el Excel y las láminas.")
        + outs([
            ("AGUA", "Agua fría y caliente", "Unidades de gasto y gasto probable por el método de Hunter.",
             ["Diámetros por velocidad",
              "Hazen-Williams con las pérdidas de cada accesorio",
              "Agua caliente enlazada al calentador"]),
            ("PRESIÓN", "Presión en cada salida", "Encuentra el aparato más desfavorable y la presión que necesita la red en su origen.",
             ["Presión estática",
              "Aumento automático de diámetros si no alcanza",
              "Tanque elevado o red pública"]),
            ("DESAGÜE", "Desagüe y ventilación", "Unidades de descarga y diámetros de ramales, montantes y colectores.",
             ["Pendientes desde las cotas o la mínima de la norma",
              "Cajas y registros",
              "Ventilación"]),
        ], cls="outs outs-3"),
        "funciones", first=True)

    ejemplo = section(
        sec_head("El resultado", "Así sale una vivienda de dos pisos",
                 "El ejemplo de la vivienda unifamiliar en Chota, con tanque elevado y terma: 0.50 L/s de gasto en la red de agua fría y "
                 "22 unidades de descarga en el desagüe. Todo cumple la IS.010.")
        + shots([
            (img + "ui_agua.jpg", 1500, 823,
             "Página Redes de agua fría y caliente: tabla de tramos con unidades de gasto, caudal, diámetro, velocidad y pérdidas, el aparato más desfavorable y los accesorios del tramo.",
             "Agua fría: tramos, presiones y accesorios"),
            (img + "ui_desague.jpg", 1500, 823,
             "Página Desagüe y ventilación: 22 unidades de descarga, colector de 4 pulgadas y una montante, con cada tramo verificado con su anexo de la IS.010.",
             "Desagüe: ramales, montantes y colectores"),
            (img + "ui_esquema.jpg", 1500, 823,
             "Esquema de la red de agua fría desde el tanque elevado, con el diámetro y el caudal de cada tramo y la presión de cada nudo; el aparato más desfavorable en ámbar.",
             "Esquema de la red con presiones"),
            (img + "ui_no_cumple.jpg", 1500, 823,
             "Ejemplo de edificio multifamiliar de cinco pisos: un tramo de desagüe con pendiente de 1 % sale en rojo como «No cumple».",
             "Lo que no cumple sale en rojo"),
        ])
        + '<p class="fine" style="margin-top:1.2rem">Sin licencia, la memoria, el PDF, el Excel de expediente y las láminas llevan la marca '
          '«VERSIÓN DE EVALUACIÓN». El cálculo en pantalla es completo.</p>',
        "ejemplo")

    entrega = section(
        sec_head("Qué entrega", "Todo lo que pide el expediente de la especialidad")
        + outs([
            ("WORD Y PDF", "Memoria descriptiva y de cálculo", "En Times New Roman, con carátula y los logos de la empresa y la entidad.",
             ["Control de revisiones",
              "Encabezado y pie en cada página",
              "Firma del responsable"], " out-hl"),
            ("EXCEL", "Excel de expediente", "Con fórmulas, listo para imprimir.",
             ["Cálculo por tramos",
              "Agua fría, caliente y desagüe",
              "Excel de tramos aparte"]),
            ("LÁMINAS", "Esquemas en A3", "Con rótulo, para el plano de la especialidad.",
             ["Esquema de agua por red",
              "Esquema de desagüe",
              "Exportación en imagen"]),
        ], cls="outs outs-3")
        + '<p class="fine">Los criterios de cálculo y sus numerales están en el documento '
          '<a href="tutoriales/Normativa_RedesInterioresALF_1.0.pdf" target="_blank" rel="noopener">Normativa y criterios (PDF)</a>.</p>',
        "entrega", tono="tone-stone")

    revit = section(
        sec_head("Con Revit", "Trabaja junto a SanitariasALF",
                 "RedesInterioresALF abre el proyecto que exporta SanitariasALF desde tu modelo de Revit, calcula las redes y le devuelve los "
                 "diámetros para que los aplique en el modelo.")
        + steps([
            ("Crea el proyecto", "Desde cero, desde un ejemplo o con el archivo que exporta SanitariasALF desde Revit."),
            ("Arma las redes", "Tramos de nudo a nudo con sus aparatos y accesorios. Las celdas amarillas son datos; las grises, resultados."),
            ("Revisa y exporta", "Corrige lo que sale en rojo y exporta la memoria, el Excel y las láminas."),
        ]),
        "revit")

    faq_items = [
        ("¿Qué norma usa?", "La Norma IS.010 del RNE, con el numeral 6.5 según el D.S. 017-2012-VIVIENDA."),
        ("¿Necesito Revit?", "No. RedesInterioresALF funciona solo en Windows. Si usas SanitariasALF en Revit, puede leer su proyecto y devolverle los diámetros."),
        ("¿Calcula el agua caliente?", "Sí. La red de agua caliente se enlaza al calentador y se calcula con el mismo método que la de agua fría."),
        ("¿Qué pasa si un tramo no cumple?", "Sale en rojo con su numeral de la IS.010. En agua, el programa puede aumentar los diámetros automáticamente hasta que la presión alcance."),
        ("¿Necesito Microsoft Word?", "Para la memoria en Word, no. Para exportar el PDF desde el programa, sí."),
        ("¿Qué incluye la versión gratuita?", "Todo el cálculo, completo en pantalla, y los ejemplos. Sin licencia, la memoria, el PDF, el Excel de expediente y las láminas salen con la marca «VERSIÓN DE EVALUACIÓN»."),
        ("¿Quién firma la memoria?", "El ingeniero responsable del proyecto, que revisa los resultados. RedesInterioresALF es una herramienta de cálculo."),
    ]

    jsonld = '<script type="application/ld+json">' + json.dumps({
        "@context": "https://schema.org", "@type": "SoftwareApplication", "name": "RedesInterioresALF",
        "applicationCategory": "EngineeringApplication", "operatingSystem": "Windows 10, Windows 11",
        "softwareVersion": ins["version"], "url": "https://www.alfbim.com/redesinterioresalf",
        "description": "Redes interiores de agua fría, agua caliente y desagüe según la IS.010, con memoria en Word, Excel de expediente y láminas A3.",
        "offers": {"@type": "Offer", "price": str(P[pid]["precio"]["mensual"]), "priceCurrency": "PEN"},
        "author": {"@type": "Person", "name": "Anderson Irigoín Colunche"}}, ensure_ascii=False) + "</script>"

    return {
        "id": pid,
        "title": "RedesInterioresALF · Agua fría, caliente y desagüe con la IS.010",
        "og_title": "RedesInterioresALF · Redes interiores de agua y desagüe con la IS.010",
        "desc": "Calcula las redes interiores de agua fría, agua caliente y desagüe con la IS.010: Hunter, Hazen-Williams, presión en cada salida, "
                "diámetros de ramales, montantes y colectores. Memoria en Word, Excel de expediente y láminas A3. Versión gratuita para Windows.",
        "nav": [("#funciones", "Funciones"), ("#ejemplo", "Ejemplo"), ("#entrega", "Entregables"),
                ("#precios", "Precios"), ("#preguntas", "Preguntas")],
        "hero": {
            "crumb": "RedesInterioresALF para Windows",
            "h1": "Redes de agua y desagüe con la IS.010",
            "lede": "RedesInterioresALF calcula tramo por tramo las redes interiores de agua fría, agua caliente y desagüe de una edificación. "
                    "Lo que no cumple sale en rojo con su numeral, y al final exportas la memoria en Word, el Excel de expediente y las láminas.",
            "cta2": ("#ejemplo", "Ver el ejemplo"),
            "trial": 'Gratis para calcular · <a href="%s" target="_blank" rel="noopener">Manual (PDF)</a>' % P[pid]["manual"],
            "meta": ["Windows 10 / 11", "IS.010", "Se conecta con SanitariasALF"],
            "img": {"src": img + "ui_esquema.jpg", "w": 1500, "h": 823,
                    "alt": "Esquema de la red de agua fría de la vivienda de ejemplo desde el tanque elevado, con el diámetro y el caudal de cada tramo y la presión de cada nudo.",
                    "cap": "Esquema de agua fría · vivienda en Chota (ejemplo)",
                    "legend": ["Diámetro y caudal de cada tramo", "Presión en cada nudo"]},
        },
        "tiles": [
            ("#descargar", "down", "Descargar gratis", "Instalador para Windows 10 y 11"),
            ("#funciones", "drop", "Agua y desagüe", "Hunter y Hazen-Williams, IS.010"),
            ("#entrega", "doc", "Memoria, Excel y láminas", "Listos para el expediente"),
        ],
        "secciones": [funciones, ejemplo, entrega, revit],
        "faq": faq_items,
        "dl_titulo": "Descarga RedesInterioresALF",
        "dl_texto": "Instalador para Windows 10 y 11 de 64 bits; no necesita administrador. Trae ejemplos de vivienda unifamiliar y de edificio multifamiliar.",
        "dl_extra": '<a class="btn btn-ghost" href="tutoriales/Normativa_RedesInterioresALF_1.0.pdf" target="_blank" rel="noopener">Normativa (PDF)</a>',
        "plataforma": "Windows 10 / 11",
        "tm": "Revit es marca registrada de Autodesk, Inc. Word y Excel son marcas de Microsoft. RedesInterioresALF es un desarrollo independiente de ALF_BIM y no está afiliado a ellas.",
        "jsonld": jsonld,
    }
