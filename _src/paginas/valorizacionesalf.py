"""Página de ValorizacionesALF (ALF-08). Fuentes: docs/MANUAL.md, docs/CRITERIOS.md y docs/VALIDACION_REAL.md de
04_Valorizaciones, VENTA/04_Valorizaciones/LEEME.txt y las capturas de la interfaz (logs/capturas, obra de ejemplo).
Se publica como «Próximamente» mientras dure la pausa de la web (24-oct-2026); la página completa queda guardada."""
import json


def pagina(g):
    section, sec_head, outs, shots, steps = g["section"], g["sec_head"], g["outs"], g["shots"], g["steps"]
    P = g["P"]
    p = P["valorizacionesalf"]
    ins = p["instalador"]
    img = "img/valorizacionesalf/"

    funciones = section(
        sec_head("Qué hace", "La valorización del mes, con su reajuste y sus descuentos",
                 "Importas el presupuesto del S10, el residente anota los metrados del mes y ValorizacionesALF calcula la valorización "
                 "completa con la Ley N.° 32069 o la Ley N.° 30225: el coeficiente K con los índices del INEI, los adelantos, el tope "
                 "por atraso, los adicionales y el informe listo para firmar.")
        + outs([
            ("PRESUPUESTO", "Del S10 al programa", "Lee el Excel o el PDF del expediente: presupuesto, pie, fórmulas polinómicas y cronograma valorizado.",
             ["Revisa que cada parcial sea metrado × precio",
              "Subpresupuestos con su propia fórmula",
              "PDF escaneado con OCR (experimental)"]),
            ("REAJUSTE", "Coeficiente K", "D.S. N.° 011-79-VC con los índices oficiales del INEI, incluido el cambio de base de 2026.",
             ["Índices de 2019 a la fecha incluidos",
              "Botón para traer los meses nuevos de El Peruano",
              "K provisional y regularización"]),
            ("ADELANTOS", "Amortizaciones y deducciones", "Adelanto directo, de materiales y por avance, con su descuento en cada valorización.",
             ["A × V / C sobre el contrato principal",
              "Reajuste que no corresponde: Am × (K/Ka − 1)",
              "Saldo en la valorización final"]),
            ("ATRASO", "Tope por atraso (art. 7-B)", "Si la obra se atrasa, el reajuste no supera al del avance programado; al recuperar, se devuelve.",
             ["Calendario contractual, reprogramado y acelerado",
              "Alerta del 80 % (art. 207)",
              "Cuadro de control en el informe"]),
            ("MODIFICACIONES", "Adicionales y deductivos", "Adicionales con su fórmula y fecha base, mayores metrados y deductivos con su resolución.",
             ["Contrato vigente e incidencia",
              "Aviso de Contraloría y tope del 50 %",
              "Penalidad por mora con su fórmula"]),
            ("INFORMES", "PDF y Excel para firmar", "Informe en Times New Roman con cifras clave, curva S, K, control 7-B, adelantos, firmas y anexo por partidas.",
             ["Residente presenta, supervisor aprueba",
              "Observaciones por partida",
              "Excel listo para imprimir en A4"]),
        ], cls="outs outs-3"),
        "funciones", first=True)

    ejemplo = section(
        sec_head("El resultado", "Así se ve una valorización",
                 "La obra de ejemplo es una institución educativa en Anguía, Chota (Cajamarca), con los índices INEI oficiales del área 2: "
                 "tres valorizaciones de mayo a julio de 2026 con K de 1.032, 1.030 y 1.034, adelanto directo y de materiales.")
        + shots([
            (img + "ui_valorizacion.jpg", 1500, 878,
             "Valorización del mes con los metrados presentados por el residente y los aprobados por el supervisor, partida por partida.",
             "Metrados del mes: residente y supervisor"),
            (img + "ui_resumen.jpg", 1500, 878,
             "Pestaña Resumen: costo directo, gastos generales, utilidad, valorización bruta, reajuste, deducciones por adelantos, amortizaciones, IGV y total a facturar.",
             "Resumen: de la valorización bruta al total a facturar"),
            (img + "ui_reajuste_k.jpg", 1500, 878,
             "Pestaña Reajuste (K): índices INEI usados, K de cada fórmula con su detalle monomio por monomio y control del reajuste por atraso.",
             "Reajuste K monomio por monomio"),
            (img + "ui_curva_s.jpg", 1500, 878,
             "Calendario valorizado y curva S del avance programado frente al ejecutado, con la línea del calendario contractual.",
             "Calendario y curva S"),
        ], style="margin-top:.5rem")
        + '<p class="fine" style="margin-top:1.2rem">Sin licencia, el programa funciona completo; los informes PDF y Excel llevan la marca '
          '«VERSIÓN DE EVALUACIÓN». <a href="%s" target="_blank" rel="noopener">Ver un informe de muestra (PDF)</a>.</p>'
        % "tutoriales/Muestra_Valorizacion_ValorizacionesALF.pdf",
        "ejemplo")

    validacion = section(
        sec_head("Validado", "Igual al céntimo que una liquidación real",
                 "Cargamos en el programa la liquidación que FONDEPES recalculó en 2025 para el saldo de obra del desembarcadero de Huacho "
                 "(cuatro fórmulas polinómicas, adelanto directo, obra atrasada) y comparamos cifra por cifra con el informe de la Entidad.")
        + outs([
            ("K", "16 coeficientes de reajuste", "Cuatro fórmulas, de octubre de 2024 a enero de 2025, con los índices de la biblioteca del programa.", [], " out-hl"),
            ("REAJUSTE", "S/ 13,475.18", "Doce reajustes por fórmula, con el control por atraso del art. 7-B: mismo total que la Entidad."),
            ("ADELANTO", "S/ 304.13", "Doce deducciones del reajuste que no corresponde por el adelanto directo y sus tres amortizaciones."),
        ], cls="outs outs-3")
        + '<p class="fine">La penalidad por mora del mismo informe (S/ 149,961.14) también sale igual. El tope por atraso con '
          'recorte se validó con la liquidación de PRONIED (Sullana) y con una obra del GORE Ica. '
          'El detalle está en <a href="tutoriales/Validacion_ValorizacionesALF_1.0.pdf" target="_blank" rel="noopener">Validación con '
          'expedientes reales (PDF)</a> y los criterios en <a href="tutoriales/Normativa_ValorizacionesALF_1.0.pdf" target="_blank" '
          'rel="noopener">Normativa y criterios de cálculo (PDF)</a>.</p>',
        "validacion")

    pasos = section(
        sec_head("Cómo funciona", "Del presupuesto al informe en cuatro pasos")
        + steps([
            ("Crea la obra", "Régimen, sistema de contratación, gastos generales, utilidad, factor de relación, fecha del presupuesto base, "
             "plazo y departamento (el programa propone el área INEI)."),
            ("Importa el expediente", "El presupuesto, las fórmulas y el cronograma valorizado del S10, en Excel o PDF. Registra los adelantos."),
            ("Valoriza cada mes", "El residente anota los metrados y presenta; el supervisor corrige, observa o aprueba."),
            ("Exporta y firma", "Informe PDF y Excel con el reajuste, las deducciones, la curva S y el anexo por partidas."),
        ]),
        "")

    faq_items = [
        ("¿Qué norma usa?", "El D.S. N.° 011-79-VC para el reajuste, con la Ley N.° 32069 y su Reglamento (D.S. N.° 009-2025-EF) o la Ley N.° 30225 y su Reglamento, según el contrato. Cada cálculo tiene su artículo en el documento de criterios."),
        ("¿Trae los índices del INEI?", "Sí, los oficiales desde 2019, con el cambio de base de 2026 (base diciembre 2025 = 100, 13 áreas y empalme del art. 8 de la R.J. N.° 016-2026-INEI). El botón «Actualizar índices INEI» trae los meses nuevos de El Peruano."),
        ("¿Qué pasa si la fórmula usa un índice que el INEI no publica?", "El programa lo avisa (por ejemplo el 74 o el 22), sugiere el afín del Diccionario de Elementos del INEI y registra el reemplazo con el documento de la Entidad que lo aprueba."),
        ("¿Sirve para el residente y el supervisor?", "Sí. El residente registra los metrados y presenta la valorización; el supervisor fija el metrado aprobado, deja observaciones por partida y la aprueba. La obra se guarda en un archivo .alfv que se puede compartir."),
        ("¿Puedo empezar con una obra que ya está en ejecución?", "Sí. Importas el avance anterior ya pagado y los adelantos ya amortizados, y sigues desde la valorización siguiente."),
        ("¿Qué incluye la versión gratuita?", "Todo el cálculo. Con la licencia, que es por computadora, el informe PDF y el Excel salen sin la marca «VERSIÓN DE EVALUACIÓN». También viene en el Pack Obra."),
        ("¿Reemplaza la revisión del profesional?", "No. Es una herramienta de cálculo: el residente y el supervisor revisan y firman la valorización."),
    ]

    jsonld = '<script type="application/ld+json">' + json.dumps({
        "@context": "https://schema.org", "@type": "SoftwareApplication", "name": "ValorizacionesALF",
        "applicationCategory": "BusinessApplication", "operatingSystem": "Windows 10, Windows 11",
        "softwareVersion": ins["version"], "url": "https://www.alfbim.com/valorizacionesalf",
        "description": "Valorizaciones de obra pública con reajuste por fórmula polinómica (D.S. 011-79-VC), índices INEI, adelantos, "
                       "tope por atraso, adicionales e informe PDF, según la Ley 32069 y la Ley 30225.",
        "offers": {"@type": "Offer", "price": str(p["precio"]["mensual"]), "priceCurrency": "PEN"},
        "author": {"@type": "Person", "name": "Anderson Irigoín Colunche"}}, ensure_ascii=False) + "</script>"

    return {
        "id": "valorizacionesalf",
        "title": "ValorizacionesALF · Valorizaciones de obra con reajuste K",
        "og_title": "ValorizacionesALF · Valorizaciones de obra pública con reajuste K",
        "desc": "Valorizaciones de obra pública con la Ley 32069 y la Ley 30225: coeficiente K con los índices INEI (incluido el cambio de base "
                "de 2026), adelantos, tope por atraso del art. 7-B, adicionales, penalidades e informe PDF listo para firmar. Para Windows.",
        "nav": [("#funciones", "Funciones"), ("#ejemplo", "Ejemplo"), ("#validacion", "Validación"),
                ("#precios", "Precios"), ("#preguntas", "Preguntas")],
        "hero": {
            "crumb": "ValorizacionesALF para Windows",
            "h1": "Tu valorización del mes,",
            "h1em": "con el reajuste bien hecho",
            "lede": "ValorizacionesALF calcula la valorización de obra pública con la Ley N.° 32069 o la Ley N.° 30225: el coeficiente K con los "
                    "índices del INEI, las amortizaciones y deducciones por adelantos, el tope por atraso, los adicionales y el informe en PDF "
                    "y Excel para el residente y el supervisor.",
            "cta2": ("#validacion", "Ver la validación"),
            "trial": 'Gratis con todas las funciones · <a href="%s" target="_blank" rel="noopener">Manual (PDF)</a>' % p["manual"],
            "meta": ["Windows 10 / 11", "D.S. 011-79-VC", "Ley 32069 · Ley 30225"],
            "img": {"src": img + "ui_resumen.jpg", "w": 1500, "h": 878,
                    "alt": "Resumen de la valorización N.° 03 de julio de 2026 de la obra de ejemplo: valorización bruta, reajuste con K = 1.034, deducciones por adelantos, amortizaciones, IGV y total a facturar.",
                    "cap": "Resumen de la valorización · obra de ejemplo",
                    "legend": ["K con índices INEI", "Adelantos y tope 7-B"]},
        },
        "tiles": [
            ("#descargar", "down", "Descargar gratis", "Instalador para Windows 10 y 11"),
            ("#validacion", "check", "Igual al céntimo", "Validado con una liquidación de FONDEPES"),
            ("#ejemplo", "doc", "Informe para firmar", "PDF y Excel en Times New Roman"),
        ],
        "secciones": [funciones, ejemplo, validacion, pasos],
        "faq": faq_items,
        "dl_titulo": "Descarga ValorizacionesALF gratis",
        "dl_texto": "Instalador para Windows 10 y 11; no necesita Python ni permisos de administrador. Trae la obra de ejemplo y casos reales "
                    "(FONDEPES, PRONIED, GORE Ica y GORE Tumbes) para comparar.",
        "dl_extra": '<a class="btn btn-ghost" href="tutoriales/Normativa_ValorizacionesALF_1.0.pdf" target="_blank" rel="noopener">Normativa (PDF)</a>',
        "plataforma": "Windows 10 / 11",
        "tm": "S10 es marca de S10 Costos y Presupuestos. Excel es marca de Microsoft. ValorizacionesALF es un desarrollo independiente de ALF_BIM "
              "y no está afiliado a ellas ni a las Entidades citadas.",
        "jsonld": jsonld,
    }
