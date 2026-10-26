"""Página de CadRevitALF (ALF-21). Fuentes: Manual_CadRevitALF_1.0.pdf, VENTA/16_CadRevitALF/LEEME.txt,
claude/ALF-21_CadRevitALF_estado.md. Se publica como «Próximamente» mientras dure la pausa de la web (24-oct-2026)."""
import json


def pagina(g):
    section, sec_head, outs, steps = g["section"], g["sec_head"], g["outs"], g["steps"]
    P = g["P"]
    ins = P["cadrevitalf"]["instalador"]

    funciones = section(
        sec_head("Qué hace", "Del plano CAD al modelo de Revit, con tus plantillas",
                 "Cuatro botones en la pestaña CadRevitALF de Revit: Arquitectura, Estructuras, Sanitarias y Eléctricas. Cada uno lee el DWG "
                 "vinculado, te muestra lo reconocido en colores y crea el modelo nativo con los tipos, familias y sistemas de tu plantilla ALF_BIM.")
        + outs([
            ("ARQUITECTURA", "Muros, vanos y habitaciones", "Muros por pares de líneas (rectos, diagonales y curvos) con su tipo por espesor.",
             ["Columnas, puertas (con su sentido de apertura) y ventanas",
              "Medidas del cuadro de vanos; tipos duplicados a la medida exacta",
              "Habitaciones con nombre y N.P.T., y un piso por ambiente"]),
            ("ESTRUCTURAS", "Cimentación y techos", "Desde los planos de cimentación y aligerados, leídos juntos y alineados.",
             ["Zapatas, cimientos corridos y sobrecimientos",
              "Columnas, placas y vigas con su rótulo V-101 (25x40)",
              "Losas aligeradas con viguetas cada 40 cm y ladrillos de techo"]),
            ("SANITARIAS", "Aparatos y tuberías", "Agua fría, agua caliente, desagüe y ventilación desde los planos de agua y desagüe.",
             ["Aparatos con el respaldo contra el muro; sumideros y registros",
              "Diámetros de los rótulos; desagüe con pendiente hacia la caja de registro",
              "Montantes, salidas a cada aparato, codos y tees de la plantilla"]),
            ("ELÉCTRICAS", "Salidas y tubos de los circuitos", "Leyenda del plano, bloques y etiquetas S, 2S, 3S.",
             ["Interruptores y tomacorrientes en la cara del muro, a su altura",
              "Luminarias bajo la losa; tableros y cajas de paso",
              "Tubos por techo y por piso con la bajada a cada aparato"]),
            ("VISTA PREVIA", "Nada se crea sin que lo veas", "Verde reconocido, naranja dudoso, rojo no reconocido.",
             ["Clic en un elemento: su ficha y por qué es dudoso",
              "Un clic cambia la clase de todos los símbolos iguales",
              "Perfiles por proyectista: el mapeo se guarda para el próximo plano"]),
            ("REPORTE", "Lo pendiente, en Excel", "Todo en una sola operación: un Ctrl+Z la deshace.",
             ["Pendientes con coordenadas del CAD, ejes y handle",
              "Dudosos con su motivo y creados con su Id de Revit",
              "Metros de tubería por red, diámetro y planta"]),
        ], cls="outs outs-3"),
        "funciones", first=True)

    lectura = section(
        sec_head("Cómo lee el plano", "Lo que el proyectista ya dibujó",
                 "No hace falta limpiar ni redibujar el CAD: CadRevitALF usa las capas, los bloques (también explotados o anónimos), los textos, "
                 "la leyenda y los rótulos del propio plano. Lo que no entiende lo marca y lo deja en el reporte para terminarlo a mano.")
        + outs([
            ("PLANTAS", "Plantas dibujadas juntas", "Separa cada planta por su título («PLANTA 1° PISO», «AZOTEA») y la alinea con la primera por ejes, columnas o muros.", [], " out-hl"),
            ("LEYENDA", "La leyenda del plano", "Cada símbolo y cada tipo de línea de la leyenda dice qué es: tomacorriente, agua fría, circuito por piso…"),
            ("RÓTULOS", "Diámetros y pendientes", "«Ø3/4\"», «PVC Ø4\" S=1%», «20mmØ» a lo largo del tubo; si falta, el del tramo vecino."),
            ("VÍNCULO", "Arquitectura desalineada", "Si los muros vinculados no coinciden con el plano, estima cuánto mover el vínculo y lo mueve por ti."),
            ("TIPOS", "Tu plantilla manda", "Usa tus tipos y familias; si falta una medida, duplica un tipo de la misma familia con la medida del plano."),
            ("REVIT", "Calibrado al milímetro", "Coordenadas tomadas de las líneas del propio DWG vinculado (error 0 mm en las pruebas)."),
        ], cls="outs outs-3"),
        "lectura")

    pasos = section(
        sec_head("Cómo funciona", "Cuatro pasos dentro de Revit")
        + steps([
            ("Vincula el DWG", "Crea el proyecto con la plantilla ALF_BIM de la especialidad y vincula el plano (origen a origen). "
             "En instalaciones, vincula también el Revit de arquitectura."),
            ("Revisa el mapeo", "Plantas → niveles, capas, tipos de muro, familias de aparatos y tipos de tubería. Lo que elijas queda en tu perfil."),
            ("Mira la vista previa", "Corrige lo naranja, cambia la clase de un símbolo o descarta lo que no quieras crear."),
            ("Crea y revisa el reporte", "«Crear en Revit» hace todo en una operación y guarda el Excel con lo pendiente y lo dudoso."),
        ]),
        "")

    faq_items = [
        ("¿Qué versiones de Revit soporta?", "Revit 2023, 2024, 2025, 2026 y 2027 en Windows. El instalador detecta las versiones instaladas; también puedes elegirlas a mano."),
        ("¿Necesito mis planos en un formato especial?", "No. Lee el DWG como lo dibujó el proyectista: capas, bloques, leyenda, textos y rótulos. Mientras más ordenado esté (títulos de planta, leyenda, capas con nombre), menos queda dudoso."),
        ("¿Qué plantillas usa?", "Las plantillas ALF_BIM de arquitectura, estructuras e instalaciones (gratis en esta web). Usa sus tipos, familias y sistemas y no inventa tipos: si falta una medida, duplica uno de la misma familia."),
        ("¿Crea las tuberías y los circuitos?", "Sí: tuberías de agua fría, agua caliente, desagüe (con pendiente) y ventilación con sus montantes, codos y tees, y los tubos de los circuitos por techo y por piso con la bajada a cada aparato. Los conductores no."),
        ("¿Y si se equivoca?", "Todo se crea en una sola operación: un Ctrl+Z la deshace completa. Lo dudoso queda marcado en Comentarios y en el reporte, para revisarlo."),
        ("¿Cómo funciona la prueba gratis?", "En el botón «Licencia» escribes tu correo y pulsas «Enviarme el código». Con el código de 6 dígitos se activan 14 días con todas las funciones. Hay una prueba por persona y por PC."),
        ("¿Sirve mi clave de otro programa ALF?", "No. Cada programa tiene su propia clave, ligada al Id de máquina que muestra su botón «Licencia»."),
        ("¿Reemplaza la revisión del modelo?", "No. Es una herramienta de apoyo: el reconocimiento depende de cómo está dibujado el plano, y el profesional responsable revisa lo creado."),
    ]

    jsonld = '<script type="application/ld+json">' + json.dumps({
        "@context": "https://schema.org", "@type": "SoftwareApplication", "name": "CadRevitALF",
        "applicationCategory": "DesignApplication", "operatingSystem": "Windows 10, Windows 11",
        "softwareVersion": ins["version"], "url": "https://www.alfbim.com/cadrevitalf",
        "description": "Complemento de Revit que lee planos CAD (DWG) y crea el modelo BIM nativo de arquitectura, estructuras e instalaciones con las plantillas ALF_BIM.",
        "offers": {"@type": "Offer", "price": str(P["cadrevitalf"]["precio"]["mensual"]), "priceCurrency": "PEN"},
        "author": {"@type": "Person", "name": "Anderson Irigoín Colunche"}}, ensure_ascii=False) + "</script>"

    return {
        "id": "cadrevitalf",
        "title": "CadRevitALF · De planos CAD a modelo BIM en Revit",
        "og_title": "CadRevitALF · Del DWG al modelo de Revit con tus plantillas",
        "desc": "Complemento de Revit 2023–2027 que lee planos CAD (DWG) y crea el modelo BIM nativo: muros, puertas, ventanas, habitaciones, "
                "zapatas, columnas, vigas, aligerados, aparatos sanitarios y eléctricos, tuberías y tubos de los circuitos, con vista previa y reporte Excel. Prueba gratis 14 días.",
        "nav": [("#funciones", "Funciones"), ("#lectura", "Cómo lee el plano"),
                ("#precios", "Precios"), ("#preguntas", "Preguntas")],
        "hero": {
            "crumb": "CadRevitALF para Revit",
            "h1": "Del plano CAD",
            "h1em": "al modelo BIM",
            "lede": "CadRevitALF lee tus planos DWG de arquitectura, estructuras e instalaciones y crea el modelo nativo de Revit con tus plantillas: "
                    "te muestra lo reconocido en colores antes de crear nada y te entrega en Excel lo que queda pendiente.",
            "cta2": ("#lectura", "Ver cómo lee el plano"),
            "trial": 'Prueba gratis 14 días con todas las funciones · <a href="%s" target="_blank" rel="noopener">Manual (PDF)</a>' % P["cadrevitalf"]["manual"],
            "meta": ["Revit 2023–2027", "Plantillas ALF_BIM", "Vista previa y reporte"],
            "img": {"cap": "Cuatro botones · un solo Ctrl+Z", "panel": '<ul class="hpanel">'
                    '<li><span class="hc">01</span><b>Arquitectura</b><span class="hu">muros · vanos</span><small>Muros, columnas, puertas, ventanas, habitaciones y pisos.</small></li>'
                    '<li><span class="hc">02</span><b>Estructuras</b><span class="hu">cimentación · techos</span><small>Zapatas, cimientos, columnas, vigas y aligerados con viguetas.</small></li>'
                    '<li><span class="hc">03</span><b>Sanitarias</b><span class="hu">aparatos · tuberías</span><small>Agua fría y caliente, desagüe con pendiente, ventilación y montantes.</small></li>'
                    '<li><span class="hc">04</span><b>Eléctricas</b><span class="hu">salidas · tubos</span><small>Interruptores, tomacorrientes, luminarias y tubos de los circuitos.</small></li>'
                    '<li><span class="hc">XLS</span><b>Reporte</b><span class="hu">pendientes</span><small>Lo dudoso y lo no convertido, con su ubicación en el CAD.</small></li>'
                    '</ul>'},
        },
        "tiles": [
            ("#descargar", "down", "Prueba gratis 14 días", "Instalador para Revit 2023–2027"),
            ("#funciones", "layers", "Cuatro especialidades", "Arquitectura, estructuras e instalaciones"),
            ("#lectura", "check", "Vista previa en colores", "Nada se crea sin que lo veas"),
        ],
        "secciones": [funciones, lectura, pasos],
        "faq": faq_items,
        "dl_titulo": "Descarga CadRevitALF y pruébalo 14 días",
        "dl_texto": "Instalador para Revit 2023–2027 en Windows 10 y 11, con el manual. Al terminar, abre Revit y busca la pestaña CadRevitALF.",
        "plataforma": "Revit 2023–2027",
        "tm": "Autodesk, AutoCAD y Revit son marcas registradas de Autodesk, Inc. Excel es marca de Microsoft. "
              "CadRevitALF es un desarrollo independiente de ALF_BIM y no está afiliado a ellas. Lector de DWG: ACadSharp (MIT).",
        "jsonld": jsonld,
    }
