"""Página de ElectricasALF (ALF-14). Fuentes: 02_Electricas/docs/MANUAL.md, README.md, banco de ideas (ALF-14).
Sin capturas hasta estrenarlo con un modelo real (pedido del 24-oct-2026)."""
import json


def pagina(g):
    section, sec_head, outs, steps = g["section"], g["sec_head"], g["outs"], g["steps"]
    P = g["P"]
    ins = P["electricasalf"]["instalador"]

    funciones = section(
        sec_head("Qué hace", "El expediente de IIEE, sacado del modelo de Revit",
                 "Cuatro botones en la pestaña ElectricasALF de Revit. Trabaja con lo que ya modelas en Revit MEP —tableros, circuitos, "
                 "luminarias, tomacorrientes, interruptores, salidas de fuerza y tuberías— y lo convierte en lo que pide un expediente peruano.")
        + outs([
            ("C-1 · C-2", "Circuitos", "Nombra los circuitos al estilo peruano en el orden de cada tablero (TG, TD-01…).",
             ["Deduce el tipo: alumbrado, tomacorrientes, fuerza, motor, reserva",
              "Cuenta las salidas y avisa si pasan del máximo",
              "Escribe el código en el «Nombre de carga» de Revit"]),
            ("CNE-U", "Cuadro de cargas", "Un cuadro por tablero con formato de expediente, en una vista de Revit y en Excel.",
             ["P.I., factor de demanda y máxima demanda",
              "ITM, diferencial 30 mA, conductor y tubería PVC-SAP",
              "Caída de tensión por circuito y acumulada"]),
            ("UNIFILAR", "Diagrama unifilar", "Se dibuja solo en vistas de dibujo listas para las láminas IE.",
             ["Unifilar de cada tablero con sus circuitos y derivaciones",
              "Esquema general: medidor → TG → TD",
              "Exporta un DWG por vista"]),
            ("METRADOS", "Metrados por salidas", "Partidas como se presupuestan en Perú, con su sustento.",
             ["Salidas por punto: centro de luz, braquete, tomacorriente, interruptor…",
              "Tubería por diámetro y conductor por calibre",
              "Tableros, ITM y diferenciales → Excel y hoja S10"]),
            ("PLANTILLA", "Plantilla ALF", "Deja la plantilla o el proyecto listo para trabajar con la norma peruana.",
             ["Tensiones 220 V y 380/220 V y sus sistemas de distribución",
              "Corrige familias de otros países (120/208 V, tableros de 1 polo)",
              "Parámetros ALF_*, tablas y limpieza de lo que no se usa"]),
            ("AJUSTES", "Configuración", "Los criterios se guardan en el modelo: todo el equipo calcula igual.",
             ["Factor de potencia, método de instalación y temperatura",
              "W por salida y factores de demanda",
              "Datos del proyecto y del proyectista"]),
        ], cls="outs outs-3"),
        "funciones", first=True)

    norma = section(
        sec_head("Cómo calcula", "Con el CNE-Utilización, regla por regla",
                 "ElectricasALF usa el mismo motor de cálculo que MaximaDemandaALF. Cada resultado queda en parámetros ALF_* de los "
                 "circuitos y tableros, para usarlos en tablas de planificación y etiquetas.")
        + outs([
            ("050-104", "Interruptores", "In ≥ 1.25 × I, con mínimos por tipo de circuito y escalonamiento con el mayor ITM aguas abajo.", [], " out-hl"),
            ("TABLA 2", "Conductores", "Capacidad de corriente del CNE-U por método de instalación, con factores de temperatura y agrupamiento."),
            ("050-102", "Caída de tensión", "2.5 % en alimentadores y derivados y 4 % total, acumulada desde el medidor."),
            ("160-108", "Motores", "La máxima demanda del tablero suma sus tableros aguas abajo y el 25 % del motor mayor."),
            ("30 mA", "Diferenciales", "En tomacorrientes y cargas de fuerza; conductor de protección según IEC 60364-5-54."),
            ("R-S-T", "Balance de fases", "Reparto automático en tableros trifásicos, con la opción de fijar la fase de un circuito."),
        ], cls="outs outs-3")
        + '<p class="fine">Las observaciones (caída de tensión excedida, circuito sin longitud, desbalance, circuito sin carga) salen en rojo '
          'en la ventana, en el cuadro y en el parámetro ALF_Observaciones. El botón «Diagnóstico» guarda un .txt con el contenido eléctrico del modelo para revisarlo o pedir soporte.</p>',
        "norma")

    entrega = section(
        sec_head("Lo que entrega", "Vistas de Revit, Excel y DWG",
                 "Todo en Times New Roman y con formato de expediente. Al repetir un comando, las vistas se actualizan en el mismo lugar "
                 "y los planos que las contienen se conservan.")
        + outs([
            ("VISTAS", "Cuadros de cargas", "Una vista de dibujo por tablero, lista para colocar en la lámina IE."),
            ("VISTAS", "Unifilares", "Unifilar por tablero y esquema general de alimentadores; también en DWG."),
            ("EXCEL", "Cuadro de cargas", "Alimentadores, cuadro por tablero, máxima demanda por regla del CNE-U y criterios adoptados."),
            ("EXCEL", "Metrados", "Resumen por partida y sustento de salidas, tableros, canalizaciones y conductores."),
            ("S10", "Hoja S10", "Ítem, descripción, unidad y metrado para copiar al presupuesto o pasar a PresupuestoALF."),
            ("TABLAS", "Tablas de Revit", "Cuadro de cargas, tableros, salidas por partida y tuberías por diámetro, con los parámetros ALF_*."),
        ], cls="outs outs-3"),
        "entrega")

    pasos = section(
        sec_head("Cómo funciona", "Tres pasos dentro de Revit")
        + steps([
            ("Prepara la plantilla", "Pulsa «Plantilla ALF» una vez en tu plantilla o proyecto: crea los parámetros, las tensiones de 220 V y 380/220 V, "
             "los sistemas de distribución y corrige las familias eléctricas que vienen con datos de otro país."),
            ("Modela como siempre", "Tableros con su sistema de distribución, salidas y circuitos asignados a cada tablero. Las tuberías son opcionales: "
             "si no las modelas, el metrado las estima con el recorrido de cada circuito."),
            ("Calcula y entrega", "«Circuitos» pone los códigos C-1, C-2…; «Cuadro de cargas» dimensiona ITM, conductores, tubería y caída de tensión; "
             "«Unifilar» dibuja los diagramas y «Metrados» genera el Excel con sustento y hoja S10."),
        ]),
        "")

    faq_items = [
        ("¿Qué versiones de Revit soporta?", "Revit 2023, 2024, 2025, 2026 y 2027 en Windows. El instalador detecta las versiones instaladas; también puedes elegirlas a mano."),
        ("¿Cómo funciona la prueba gratis?", "En el botón «Licencia» escribes tu correo y pulsas «Enviarme el código». Con el código de 6 dígitos que llega al correo se activan 14 días con todas las funciones. Hay una prueba por persona y por PC."),
        ("¿Necesito una plantilla especial?", "No. El botón «Plantilla ALF» prepara tu propia plantilla o tu proyecto: parámetros, tensiones, sistemas de distribución y tablas."),
        ("Mi tablero no deja elegir sistema de distribución, ¿qué hago?", "Suele pasar con familias de otros países (120 V, 208 V o tableros de 1 polo). Ejecuta «Plantilla ALF»: corrige esas familias y las deja en 220 V con 2 polos."),
        ("¿Necesito MaximaDemandaALF?", "No. ElectricasALF ya trae el mismo motor de cálculo del CNE-U. MaximaDemandaALF sirve cuando quieres la memoria de cálculo en Word sin abrir Revit."),
        ("¿Sirve mi clave de AceroALF, SanitariasALF o MetradosALF?", "No. Cada programa tiene su propia clave, ligada al Id de máquina que muestra su botón «Licencia»."),
        ("¿Hay licencia para estudiantes?", "Sí: 3 meses gratis, de uso no comercial. Los cuadros, unifilares y Excel llevan la marca «VERSIÓN ESTUDIANTE»."),
        ("¿Reemplaza al ingeniero electricista?", "No. Es una herramienta de apoyo: los resultados dependen del modelo y de los criterios que eliges, y el proyecto lo revisa y firma el ingeniero electricista o mecánico-electricista responsable."),
    ]

    jsonld = '<script type="application/ld+json">' + json.dumps({
        "@context": "https://schema.org", "@type": "SoftwareApplication", "name": "ElectricasALF",
        "applicationCategory": "DesignApplication", "operatingSystem": "Windows 10, Windows 11",
        "softwareVersion": ins["version"], "url": "https://www.alfbim.com/electricasalf",
        "description": "Complemento de Revit para instalaciones eléctricas con el CNE-Utilización: circuitos, cuadro de cargas, diagrama unifilar y metrados por salidas.",
        "offers": {"@type": "Offer", "price": str(P["electricasalf"]["precio"]["mensual"]), "priceCurrency": "PEN"},
        "author": {"@type": "Person", "name": "Anderson Irigoín Colunche"}}, ensure_ascii=False) + "</script>"

    return {
        "id": "electricasalf",
        "title": "ElectricasALF · Instalaciones eléctricas en Revit con el CNE-U",
        "og_title": "ElectricasALF · Cuadro de cargas, unifilar y metrados desde Revit",
        "desc": "Complemento de Revit 2023–2027 para instalaciones eléctricas: circuitos C-1, C-2…, cuadro de cargas por tablero con el CNE-Utilización "
                "(ITM, conductor, tubería, caída de tensión), diagrama unifilar en Revit y DWG y metrados por salidas en Excel con hoja S10. Prueba gratis 14 días.",
        "nav": [("#funciones", "Funciones"), ("#norma", "Cómo calcula"), ("#entrega", "Entregables"),
                ("#precios", "Precios"), ("#preguntas", "Preguntas")],
        "hero": {
            "crumb": "ElectricasALF para Revit",
            "h1": "Instalaciones eléctricas",
            "h1em": "desde Revit",
            "lede": "ElectricasALF lee tu modelo de instalaciones eléctricas y entrega lo que pide el expediente: circuitos con nombre peruano, "
                    "cuadros de cargas con el CNE-Utilización, diagramas unifilares y metrados por salidas, sin redibujar nada en AutoCAD.",
            "cta2": ("#norma", "Ver cómo calcula"),
            "trial": 'Prueba gratis 14 días con todas las funciones · <a href="%s" target="_blank" rel="noopener">Manual (PDF)</a>' % P["electricasalf"]["manual"],
            "meta": ["Revit 2023–2027", "CNE-Utilización", "Excel, DWG y S10"],
            "img": {"cap": "La pestaña ElectricasALF · 4 botones", "panel": '<ul class="hpanel">'
                    '<li><span class="hc">BOTÓN 1</span><b>Circuitos</b><span class="hu">C-1, C-2…</span><small>Códigos por tablero, tipo de circuito y salidas contadas.</small></li>'
                    '<li><span class="hc">BOTÓN 2</span><b>Cuadro de cargas</b><span class="hu">CNE-U</span><small>Máxima demanda, ITM, diferencial, conductor, tubería y caída de tensión.</small></li>'
                    '<li><span class="hc">BOTÓN 3</span><b>Unifilar</b><span class="hu">Revit y DWG</span><small>Unifilar por tablero y esquema general de alimentadores.</small></li>'
                    '<li><span class="hc">BOTÓN 4</span><b>Metrados</b><span class="hu">pto · m · und</span><small>Salidas, tuberías, conductores, tableros e interruptores con hoja S10.</small></li>'
                    '<li><span class="hc">AJUSTE</span><b>Plantilla ALF</b><span class="hu">220 V · 380/220 V</span><small>Tensiones, sistemas de distribución y familias listas para la norma peruana.</small></li>'
                    '</ul>'},
        },
        "tiles": [
            ("#descargar", "down", "Prueba gratis 14 días", "Instalador para Revit 2023–2027"),
            ("#entrega", "table", "Cuadros y unifilares", "En Revit, Excel y DWG"),
            ("#norma", "check", "CNE-Utilización", "ITM, conductor y caída de tensión"),
        ],
        "secciones": [funciones, norma, entrega, pasos],
        "faq": faq_items,
        "dl_titulo": "Descarga ElectricasALF y pruébalo 14 días",
        "dl_texto": "Instalador para Revit 2023–2027 en Windows 10 y 11, con el manual. Al terminar, abre Revit y busca la pestaña ElectricasALF.",
        "plataforma": "Revit 2023–2027",
        "tm": "Autodesk y Revit son marcas registradas de Autodesk, Inc. AutoCAD es marca de Autodesk, Inc. Excel es marca de Microsoft. S10 es marca de S10 Software. "
              "ElectricasALF es un desarrollo independiente de ALF_BIM y no está afiliado a ellas.",
        "jsonld": jsonld,
    }
