"""Página de PlazosALF (ALF-09). Fuentes: Manual y Normativa de PlazosALF 1.0 (docs/MANUAL.md, docs/NORMATIVA.md),
VENTA/09_PlazosObra/LEEME.txt, claude/ALF-09_PlazosALF_estado.md y las capturas de la interfaz (logs/capturas)."""
import json


def pagina(g):
    section, sec_head, outs, shots, steps = g["section"], g["sec_head"], g["outs"], g["shots"], g["steps"]
    P = g["P"]
    ins = P["plazosalf"]["instalador"]
    img = "img/plazosalf/"

    funciones = section(
        sec_head("Qué hace", "Los plazos de la obra, al día y con su artículo",
                 "Registras o importas el cuaderno de obra y PlazosALF calcula cada vencimiento con la Ley N.° 32069 y su Reglamento "
                 "(D.S. N.° 009-2025-EF, modificado por el D.S. N.° 001-2026-EF). Cada paso dice quién actúa, desde cuándo corre y qué pasa si no se cumple.")
        + outs([
            ("CUADERNO", "Cuaderno de obra", "Cada asiento abre o completa su trámite: una consulta, el inicio o fin de una causal, un adicional.",
             ["Sugiere el tipo de asiento al escribirlo",
              "Importa Excel, CSV, texto y PDF con texto",
              "Sigue las citas «Consulta N.° 01» o «asiento N.° 9»"]),
            ("TRÁMITES", "15 trámites", "Inicio del plazo, consultas, ampliaciones, adicionales, suspensión, recepción, liquidación y más.",
             ["Aprobación ficta y efectos automáticos",
              "Garantías con renovación encadenada",
              "Controversias con JPRD y arbitraje"]),
            ("PLAZO", "Plazo de ejecución", "Término original y vigente, ampliaciones, suspensiones y atraso, en una línea de tiempo.",
             ["Penalidad por mora con su fórmula",
              "Fecha de control distinta de hoy",
              "Diseño y construcción, con su componente diseño"]),
            ("ALERTAS", "Avisos de vencimiento", "Un tablero con lo vencido y lo que está por vencer, ordenado por urgencia.",
             ["Recordatorio diario de Windows",
              "Aviso por correo y por WhatsApp",
              "Calendario .ics para Google, Outlook o el celular"]),
            ("BORRADORES", "Asientos, cartas y actas", "38 plantillas que se llenan con los datos de la obra, los asientos, las fechas y el artículo.",
             ["Copiar el texto para la Pladicop",
              "Word o PDF en Times New Roman",
              "Registrar la carta y fijar la fecha del paso"]),
            ("CALENDARIO", "Feriados al día", "Sábados, domingos, feriados nacionales, Semana Santa y días no laborables del sector público.",
             ["Se actualizan en línea desde alfbim.com",
              "Feriados regionales o locales de tu obra",
              "Archivo firmado: el programa rechaza uno alterado"]),
        ], cls="outs outs-3"),
        "funciones", first=True)

    ejemplo = section(
        sec_head("El resultado", "Así se ve una obra en control",
                 "El ejemplo de una obra educativa en Anguía, Chota, con control al 20/10/2026: término vigente al 22/09/2026 con "
                 "10 días de ampliación (una aprobada en forma ficta), culminación anotada el 25/09/2026 y 3 días de atraso, "
                 "con una penalidad por mora de S/ 42,210.53.")
        + shots([
            (img + "ui_tramite_ampliacion.jpg", 1500, 844,
             "Ficha de la ampliación de plazo N.° 1 por lluvias intensas: causal, días solicitados, días que opina el supervisor y la tabla de pasos con responsable, plazo, desde, vence, fecha real y estado.",
             "Ampliación de plazo: cada paso con su plazo y estado"),
            (img + "ui_cuaderno.jpg", 1500, 844,
             "Cuaderno de obra con los asientos del ejemplo, su tipo, el trámite que abren o completan y el texto.",
             "Cuaderno de obra: cada asiento con su trámite"),
            (img + "ui_plazo.jpg", 1500, 844,
             "Página Plazo de ejecución: inicio, término vigente, plazo transcurrido, atraso, penalidad por mora, monto vigente y línea de tiempo con ampliaciones.",
             "Plazo de ejecución y penalidad por mora"),
            (img + "ui_borrador_carta.jpg", 1500, 844,
             "Borrador de la carta de solicitud de ampliación de plazo, llenado con los datos de la obra, los asientos y el artículo del Reglamento.",
             "Borrador de carta, listo para completar y exportar"),
        ], style="margin-top:.5rem")
        + '<p class="fine" style="margin-top:1.2rem">Sin licencia, las cartas, asientos, actas, el informe y el Excel llevan la marca '
          '«VERSIÓN DE EVALUACIÓN». El control de plazos, las alertas y el calendario son completos.</p>',
        "ejemplo")

    alertas = section(
        sec_head("Alertas", "Te avisa antes de que venza",
                 "No hace falta abrir el programa todos los días: el recordatorio diario revisa tus obras recientes y te avisa si algo "
                 "está vencido o por vencer.")
        + outs([
            ("WINDOWS", "Recordatorio diario", "Una tarea de Windows revisa tus obras a la hora que elijas y muestra una notificación junto al reloj.", [], " out-hl"),
            ("CORREO", "Resumen por correo", "Una vez al día, solo si hay algo urgente, a los destinatarios que elijas: residente, supervisor, gerente."),
            ("WHATSAPP", "Aviso por WhatsApp", "Automático con el servicio gratuito CallMeBot, o con el botón «Compartir por WhatsApp», sin configurar nada."),
        ], cls="outs outs-3")
        + shots([
            (img + "ui_calendario.jpg", 1500, 844,
             "Calendario de vencimientos de octubre de 2026 con los días inhábiles en gris y la lista de próximos vencimientos.",
             "Calendario de vencimientos, exportable a .ics"),
            (img + "ui_dc_tablero.jpg", 1500, 844,
             "Tablero de alertas de la obra de ejemplo de diseño y construcción (centro de salud), con una consulta vencida en rojo y el atraso del componente diseño con su penalidad.",
             "Diseño y construcción: lo vencido sale en rojo"),
        ])
        + '<p class="fine">La contraseña del correo y la clave de WhatsApp se guardan cifradas para tu usuario de Windows. '
          'Los feriados y días no laborables del sector público se descargan de www.alfbim.com con «Herramientas → Actualizar feriados '
          'y días no laborables», y el recordatorio diario los actualiza solo.</p>',
        "alertas")

    pasos = section(
        sec_head("Cómo funciona", "Tres pasos para tener la obra en control")
        + steps([
            ("Crea la obra", "Nombre, Entidad, contratista, monto, plazo, fecha del contrato y tu rol: contratista, supervisor o Entidad. "
             "El programa crea el control del inicio, la recepción y la liquidación."),
            ("Carga el cuaderno", "Registra los asientos o impórtalos desde Excel, CSV, texto o el PDF del cuaderno de la Pladicop. "
             "Cada asiento abre o completa su trámite."),
            ("Actúa a tiempo", "Revisa el tablero, anota las fechas reales y prepara los borradores de asientos, cartas y actas, "
             "o el informe de control de plazos en Word, PDF o Excel."),
        ])
        + '<p class="fine">Criterios de cómputo: días calendario salvo que el Reglamento diga «días hábiles» (art. 105.3); se excluye el día '
          'inicial y, si el último día es inhábil, vence el siguiente hábil (Código Civil, art. 183). Cada plazo con su artículo está en '
          '<a href="tutoriales/Normativa_PlazosALF_1.0.pdf" target="_blank" rel="noopener">Normativa y criterios de cómputo (PDF)</a>.</p>',
        "")

    faq_items = [
        ("¿Qué norma usa?", "La Ley N.° 32069, Ley General de Contrataciones Públicas, y su Reglamento (D.S. N.° 009-2025-EF), con las modificaciones del D.S. N.° 001-2026-EF, vigentes desde el 14 de enero de 2026. Para la JPRD, la Directiva N.° 002-2025-OECE-CD."),
        ("¿Sirve para el contratista, el supervisor y la Entidad?", "Sí. Eliges tu rol al crear la obra y las acciones a tu cargo salen en negrita en el tablero."),
        ("¿Puedo importar el cuaderno de la Pladicop?", "Sí, si el PDF tiene texto: se buscan los encabezados «Asiento N.° …» y su fecha. Un PDF escaneado no tiene texto; en ese caso usa la plantilla de Excel."),
        ("¿Cómo se actualizan los feriados?", "Con «Herramientas → Actualizar feriados y días no laborables», que descarga de www.alfbim.com los días no laborables del sector público y los cambios de feriados publicados después de esta versión. El recordatorio diario lo hace solo. También puedes agregar feriados regionales o locales para tu obra."),
        ("¿Funciona en diseño y construcción?", "Sí. Registras el monto y el plazo del componente diseño y el programa controla la entrega y aprobación del expediente, su penalidad y el inicio del componente obra."),
        ("¿Qué incluye la versión gratuita?", "Todo el control de plazos, las alertas y el calendario. Con la licencia, que es por computadora, las cartas, asientos, actas, el informe y el Excel salen sin la marca «VERSIÓN DE EVALUACIÓN»."),
        ("¿Reemplaza la revisión legal?", "No. Es una herramienta de apoyo: revisa siempre los plazos y los borradores con el contrato, las bases y la norma antes de firmarlos."),
    ]

    jsonld = '<script type="application/ld+json">' + json.dumps({
        "@context": "https://schema.org", "@type": "SoftwareApplication", "name": "PlazosALF",
        "applicationCategory": "BusinessApplication", "operatingSystem": "Windows 10, Windows 11",
        "softwareVersion": ins["version"], "url": "https://www.alfbim.com/plazosalf",
        "description": "Control de plazos de obras públicas con la Ley 32069 y su Reglamento: cuaderno de obra, alertas y borradores de cartas y asientos.",
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "PEN"},
        "author": {"@type": "Person", "name": "Anderson Irigoín Colunche"}}, ensure_ascii=False) + "</script>"

    return {
        "id": "plazosalf",
        "title": "PlazosALF · Plazos de obra con la Ley 32069 y alertas",
        "og_title": "PlazosALF · Control de plazos de obra con la Ley 32069",
        "desc": "Calcula los plazos de la ejecución de obras públicas con la Ley 32069 y su Reglamento desde el cuaderno de obra: "
                "ampliaciones, consultas, adicionales, recepción y liquidación, con alertas por correo y WhatsApp y borradores de cartas y asientos. Gratis para Windows.",
        "nav": [("#funciones", "Funciones"), ("#ejemplo", "Ejemplo"), ("#alertas", "Alertas"),
                ("#precios", "Precios"), ("#preguntas", "Preguntas")],
        "hero": {
            "crumb": "PlazosALF para Windows",
            "h1": "Los plazos de tu obra,",
            "h1em": "con la Ley 32069",
            "lede": "PlazosALF lee el cuaderno de obra y calcula los vencimientos de cada trámite: inicio, consultas, ampliaciones, "
                    "adicionales, suspensión, recepción, liquidación, garantías y controversias. Te avisa de lo que está por vencer "
                    "y prepara los borradores de asientos, cartas y actas.",
            "cta2": ("#ejemplo", "Ver la obra de ejemplo"),
            "trial": 'Gratis con todas las funciones · <a href="%s" target="_blank" rel="noopener">Manual (PDF)</a>' % P["plazosalf"]["manual"],
            "meta": ["Windows 10 / 11", "Ley 32069 · D.S. 009-2025-EF", "Modificado por el D.S. 001-2026-EF"],
            "img": {"src": img + "ui_inicio.jpg", "w": 1500, "h": 844,
                    "alt": "Tablero de alertas de PlazosALF al 20/10/2026 para la obra de ejemplo de la I.E. en Anguía: término vigente 22/09/2026, plazo culminado, ampliaciones de 10 días y penalidad por mora de S/ 42,210.53, con las acciones con plazo.",
                    "cap": "Tablero de alertas · obra de ejemplo",
                    "legend": ["Vencimientos por urgencia", "Base legal de cada acción"]},
        },
        "tiles": [
            ("#descargar", "down", "Descargar gratis", "Instalador para Windows 10 y 11"),
            ("#alertas", "bell", "Alertas por correo y WhatsApp", "Recordatorio diario de vencimientos"),
            ("#ejemplo", "doc", "38 plantillas", "Asientos, cartas y actas"),
        ],
        "secciones": [funciones, ejemplo, alertas, pasos],
        "faq": faq_items,
        "dl_titulo": "Descarga PlazosALF gratis",
        "dl_texto": "Instalador para Windows 10 y 11; no necesita Python. Trae obras de ejemplo, incluida una de diseño y construcción, "
                    "y la plantilla de asientos en Excel.",
        "dl_extra": '<a class="btn btn-ghost" href="tutoriales/Normativa_PlazosALF_1.0.pdf" target="_blank" rel="noopener">Normativa (PDF)</a>',
        "plataforma": "Windows 10 / 11",
        "tm": "Word, Excel y Outlook son marcas de Microsoft. Google Calendar es marca de Google. WhatsApp es marca de Meta. "
              "PlazosALF es un desarrollo independiente de ALF_BIM y no está afiliado a ellas.",
        "jsonld": jsonld,
    }
