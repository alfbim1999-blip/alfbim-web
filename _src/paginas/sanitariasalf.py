"""Página de SanitariasALF (ALF-18). Fuentes: Manual_SanitariasALF_1.0.pdf, VENTA/08_IISS_BIM/LEEME.txt,
claude/ALF-18_IISS_BIM_estado.md (modelo de prueba Vivienda_prueba_IISS)."""
import json


def pagina(g):
    section, sec_head, outs, shots, steps = g["section"], g["sec_head"], g["outs"], g["shots"], g["steps"]
    P = g["P"]
    ins = P["sanitariasalf"]["instalador"]
    img = "img/sanitariasalf/"

    funciones = section(
        sec_head("Qué hace", "Lo que pide el expediente de IISS, sacado del modelo",
                 "Trabaja sobre lo que ya modelas en Revit MEP: tuberías, uniones, accesorios, aparatos sanitarios y equipos. "
                 "Sigue las conexiones del modelo, así que lo que no está conectado no se cuenta.")
        + outs([
            ("PLANTILLA", "Plantilla ALF", "Prepara la plantilla o completa el proyecto, sin borrar ni cambiar lo que ya existe.",
             ["Sistemas AF, AC, DS, VE, DP, ANP y ACI con color y línea",
              "PVC-U C-10, CPVC y PVC SAL con diámetros comerciales",
              "Filtros por red y tablas de IISS listas"]),
            ("METRADOS", "Metrados por salidas", "Según la Norma Técnica de Metrados, OE.4 Instalaciones sanitarias.",
             ["Salidas (pto) de AF, AC, desagüe y ventilación",
              "Redes en metros por red, material y diámetro",
              "Accesorios, válvulas, aparatos y equipos por unidad"]),
            ("EXCEL Y S10", "Sustento por elemento", "Un Excel con la hoja Resumen, una hoja por grupo y una hoja S10.",
             ["Nivel, ambiente e Id de Revit de cada elemento",
              "Hoja S10 numerada 03.xx.yy.zz",
              "Partida, unidad y material editables con ALF_Partida"]),
            ("IS.010", "Verificar IS.010", "Recorre cada red de desagüe como un árbol desde su salida.",
             ["Pendiente mínima y sentido del flujo (6.2 c)",
              "Unidades de descarga de los Anexos 8 y 9",
              "Distancia a la ventilación (6.5 c) y extremos sin conectar"]),
            ("ISOMÉTRICO", "Isométricos de agua", "Agua fría, agua caliente o las dos, de toda la red o de lo que selecciones.",
             ["Diámetro de cada tramo y su caudal",
              "Altura de salida de cada aparato y nivel de cada piso",
              "Escala automática de 1:20 a 1:200"]),
            ("ALF-17", "Cálculo hidráulico", "Exporta las redes a RedesInterioresALF y trae los resultados al modelo.",
             ["Hunter y Hazen-Williams para el agua; UD para el desagüe",
              "Escribe caudal, velocidad, presión y estado en cada tubería",
              "Opcional: cambia los diámetros en el modelo"]),
        ], cls="outs outs-3"),
        "funciones", first=True)

    ejemplo = section(
        sec_head("El resultado", "Así sale el modelo de prueba",
                 "Una vivienda de 2 pisos con baño y terma por piso, cocina, lavandería y sumidero: 85 tuberías, 50 codos y 29 tees. "
                 "El colector de desagüe del 2.º piso está a 0.8 % a propósito, para que la verificación lo encuentre. "
                 "Salieron 34 partidas de metrados y 54 elementos verificados: 30 cumplen, 14 por revisar y 10 no cumplen.")
        + shots([
            (img + "revit_vista_verificacion.jpg", 480, 480,
             "Vista 3D «ALF IISS - Verificación IS.010» de la vivienda de prueba con las tuberías coloreadas según cumplen o no la norma.",
             "Revit: vista de verificación coloreada (rojo, naranja y verde)"),
            (img + "revit_resultados_alf17.jpg", 756, 775,
             "Ventana de resultados de RedesInterioresALF en Revit: agua fría y caliente cumplen, el desagüe no cumple, 176 elementos escritos y 33 diámetros cambiados, con la lista de observaciones de la IS.010.",
             "Revit: resultados del cálculo hidráulico de RedesInterioresALF"),
        ], style="margin-top:.5rem")
        + shots([
            (img + "xls_verificacion.jpg", 1500, 567,
             "Hoja Desagüe del informe de verificación: Id de Revit, nivel, tipo, diámetro, longitud, pendiente, pendiente mínima, unidades de descarga, referencia, estado y observaciones de cada tubo.",
             "Excel: informe de verificación IS.010, tubo por tubo", "wide"),
        ], cls="shots shots-ui"),
        "ejemplo")

    verificacion = section(
        sec_head("Verificar IS.010", "Qué revisa en el desagüe",
                 "Escribe en cada elemento ALF_Estado (CUMPLE, REVISAR o NO CUMPLE) y sus observaciones, colorea la vista 3D y guarda el informe en Excel.")
        + outs([
            ("6.2 c)", "Pendiente", "Al menos 1 % desde 100 mm y 1.5 % hasta 75 mm, a favor del flujo.", [], " out-hl"),
            ("6.2 d)", "Diámetro con inodoro", "Todo tubo aguas abajo de un inodoro debe tener 100 mm o más."),
            ("ANEXO 6", "Trampa mínima", "El diámetro del desagüe de cada aparato."),
            ("ANEXOS 8 Y 9", "Unidades de descarga", "Ramales, montantes de hasta 3 pisos o de más, y colectores."),
            ("6.5 c)", "Distancia a la ventilación", "1.10, 1.50, 1.80 y 3.00 m para 40, 50, 75 y 100 mm, medida por la tubería."),
            ("MODELO", "Extremos sin conectar", "En desagüe, agua y ventilación: así aparecen las uniones que faltan."),
        ], cls="outs outs-3")
        + '<p class="fine">El botón «Diagnóstico» guarda en un .txt todo lo que SanitariasALF lee del modelo: tramos por red y diámetro, '
          'pendientes, extremos libres y aparatos con sus salidas. Es lo primero que conviene revisar si un resultado no es el esperado.</p>',
        "verificacion")

    pasos = section(
        sec_head("Cómo funciona", "Tres pasos dentro de Revit")
        + steps([
            ("Prepara el modelo", "Con «Plantilla ALF» quedan los sistemas, tipos de tubería, parámetros y vistas. Modela los aparatos con sus "
             "conectores y une las tuberías con codos y tees: SanitariasALF sigue las conexiones."),
            ("Metra y verifica", "«Metrados» genera el Excel con sustento y hoja S10. «Verificar IS.010» colorea la vista 3D y lista lo que "
             "no cumple, con el Id de cada elemento."),
            ("Dibuja y calcula", "«Isométrico» crea la vista de dibujo lista para la lámina. «A ALF-17» y «De ALF-17» llevan las redes al "
             "cálculo hidráulico y traen los resultados."),
        ])
        + shots([
            (img + "xls_salidas.jpg", 1500, 758,
             "Hoja Salidas del Excel de metrados con el sustento de cada salida: partida, nivel, aparato, red e Id de Revit.",
             "Excel: sustento de cada salida con su Id de Revit"),
            (img + "xls_metrados.jpg", 1253, 1124,
             "Hoja Resumen del Excel de metrados: aparatos sanitarios, sistema de agua fría, agua caliente y desagüe y ventilación con ítem, descripción, unidad, metrado y referencia de la Norma Técnica de Metrados.",
             "Excel: resumen de metrados con la referencia OE.4"),
        ]),
        "")

    faq_items = [
        ("¿Qué versiones de Revit soporta?", "Revit 2023, 2024, 2025, 2026 y 2027 en Windows. El instalador detecta las versiones instaladas; también puedes elegirlas a mano."),
        ("¿Cómo funciona la prueba gratis?", "En el botón «Licencia» escribes tu correo y pulsas «Enviarme el código». Con el código de 6 dígitos que llega al correo se activan 14 días con todas las funciones. Hay una prueba por persona y por PC."),
        ("¿Trae plantilla?", "Sí. El instalador deja en el menú Inicio la plantilla ALF_BIM_INSTALACIONES_SANITARIAS.rte, con los sistemas, tuberías, filtros y tablas de IISS. En un proyecto que ya tienes, «Plantilla ALF» solo completa lo que falta."),
        ("Un aparato no aparece en los metrados.", "No está conectado a ninguna tubería o su familia no se reconoce. Revisa el Diagnóstico y escribe la clave IS.010 del aparato en el parámetro ALF_Aparato (inodoro_tanque, lavatorio, ducha…)."),
        ("¿Necesito RedesInterioresALF?", "Solo para el cálculo hidráulico (Hunter, Hazen-Williams y UD tramo por tramo). Los metrados, la verificación IS.010 y los isométricos funcionan sin él."),
        ("¿Sirve mi clave de AceroALF?", "No. Cada programa tiene su propia clave, ligada al Id de máquina que muestra su botón «Licencia»."),
        ("¿Hay licencia para estudiantes?", "Sí: 3 meses gratis, de uso no comercial. Los metrados, informes e isométricos llevan la marca «VERSIÓN ESTUDIANTE»."),
        ("¿Reemplaza la revisión del proyectista?", "No. Es una herramienta de apoyo: los resultados dependen del modelo y de los datos que ingresas, y el profesional responsable los revisa con la norma vigente."),
    ]

    jsonld = '<script type="application/ld+json">' + json.dumps({
        "@context": "https://schema.org", "@type": "SoftwareApplication", "name": "SanitariasALF",
        "applicationCategory": "DesignApplication", "operatingSystem": "Windows 10, Windows 11",
        "softwareVersion": ins["version"], "url": "https://www.alfbim.com/sanitariasalf",
        "description": "Complemento de Revit para instalaciones sanitarias: metrados por salidas, verificación IS.010 e isométricos.",
        "offers": {"@type": "Offer", "price": str(P["sanitariasalf"]["precio"]["mensual"]), "priceCurrency": "PEN"},
        "author": {"@type": "Person", "name": "Anderson Irigoín Colunche"}}, ensure_ascii=False) + "</script>"

    return {
        "id": "sanitariasalf",
        "title": "SanitariasALF · Instalaciones sanitarias en Revit con la IS.010",
        "og_title": "SanitariasALF · Metrados, IS.010 e isométricos de IISS en Revit",
        "desc": "Complemento de Revit 2023–2027 para instalaciones sanitarias: metrados por salidas según la Norma Técnica de Metrados, "
                "verificación del desagüe con la IS.010, isométricos de agua y enlace con RedesInterioresALF. Prueba gratis 14 días.",
        "nav": [("#funciones", "Funciones"), ("#ejemplo", "Ejemplo"), ("#verificacion", "IS.010"),
                ("#precios", "Precios"), ("#preguntas", "Preguntas")],
        "hero": {
            "crumb": "SanitariasALF para Revit",
            "h1": "Metrados e IS.010",
            "h1em": "desde Revit",
            "lede": "SanitariasALF saca de tu modelo de Revit MEP los metrados de instalaciones sanitarias por salidas y partidas, "
                    "verifica el desagüe con la IS.010, dibuja los isométricos de agua y lleva las redes a RedesInterioresALF para el cálculo hidráulico.",
            "cta2": ("#ejemplo", "Ver el modelo de prueba"),
            "trial": 'Prueba gratis 14 días con todas las funciones · <a href="%s" target="_blank" rel="noopener">Manual (PDF)</a>' % P["sanitariasalf"]["manual"],
            "meta": ["Revit 2023–2027", "Norma Técnica de Metrados OE.4", "IS.010"],
            "img": {"src": img + "revit_isometrico.jpg", "w": 550, "h": 510,
                    "alt": "Isométrico de agua fría y agua caliente generado por SanitariasALF en Revit para la vivienda de prueba, con diámetros, caudales, aparatos y niveles.",
                    "cap": "Isométrico · vivienda de prueba",
                    "legend": ["Agua fría, línea continua", "Agua caliente, a trazos"]},
        },
        "tiles": [
            ("#descargar", "down", "Prueba gratis 14 días", "Instalador para Revit 2023–2027"),
            ("#ejemplo", "table", "Metrados con hoja S10", "Sustento por elemento con su Id"),
            ("#verificacion", "check", "Verifica la IS.010", "Pendientes, UD y ventilación"),
        ],
        "secciones": [funciones, ejemplo, verificacion, pasos],
        "faq": faq_items,
        "dl_titulo": "Descarga SanitariasALF y pruébalo 14 días",
        "dl_texto": "Instalador para Revit 2023–2027 en Windows 10 y 11. Trae la plantilla ALF_BIM_INSTALACIONES_SANITARIAS y el manual. "
                    "Al terminar, abre Revit y busca la pestaña SanitariasALF.",
        "plataforma": "Revit 2023–2027",
        "tm": "Autodesk y Revit son marcas registradas de Autodesk, Inc. Excel es marca de Microsoft. S10 es marca de S10 Software. "
              "SanitariasALF es un desarrollo independiente de ALF_BIM y no está afiliado a ellas.",
        "jsonld": jsonld,
    }
