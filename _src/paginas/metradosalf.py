"""Página de MetradosALF (ALF-01). Fuentes: Manual_MetradosALF_1.0.pdf, VENTA/10_MetradosALF/LEEME.txt,
claude/ALF-01_MetradosALF_estado.md (edificio de prueba Edificio_prueba_metrados, comprobado a mano)."""
import json


def pagina(g):
    section, sec_head, outs, shots, steps = g["section"], g["sec_head"], g["outs"], g["shots"], g["steps"]
    P = g["P"]
    ins = P["metradosalf"]["instalador"]
    img = "img/metradosalf/"

    funciones = section(
        sec_head("Qué hace", "La planilla de metrados del expediente, sacada del modelo",
                 "Dos botones en la pestaña MetradosALF de Revit: Estructuras y Arquitectura. Cada partida sale con su sustento fila por fila "
                 "(veces × largo × ancho × alto), por nivel y por ejes, con la regla de la Norma Técnica de Metrados (R.D. 073-2010-VIVIENDA) que aplica.")
        + outs([
            ("OE.2.1", "Movimiento de tierras", "Desde la cimentación del modelo y la cota del terreno natural.",
             ["Excavación de zanjas sin repetir lo ya excavado",
              "Refine, relleno compactado y nivelación interior",
              "Eliminación con el esponjamiento del suelo (tabla de la Norma)"]),
            ("OE.2.2 · OE.2.3", "Concreto y encofrado", "Cada volumen va a un solo elemento, como manda la Norma, sin depender de las uniones de Revit.",
             ["Zapatas, cimientos, vigas de cimentación, columnas, placas, vigas, losas y escaleras",
              "Encofrado por área efectiva de contacto",
              "Solado, falso piso y ladrillo de techo del aligerado"]),
            ("ACERO", "Acero de refuerzo", "Longitud real de cada barra del modelo por su peso nominal (NTP 341.031).",
             ["Lee el acero de AceroALF con su uso",
              "Resumen por diámetro en varillas de 9 m",
              "Opcional: acero estimado por cuantía (kg/m³), marcado como referencial"]),
            ("OE.3.1 · OE.3.2", "Muros y tarrajeos", "Áreas netas, descontando el vano real de cada puerta y ventana.",
             ["Muros y tabiques por tipo de muro",
              "Tarrajeo interior y exterior según las habitaciones",
              "Columnas, vigas, placas y vestidura de derrames"]),
            ("OE.3.3 · OE.3.6", "Cielorrasos, pisos y coberturas", "Sin descontar columnas ni huecos pequeños, como dice la Norma.",
             ["Cielorraso con mezcla y falsos cielorrasos",
              "Contrapiso y pisos por acabado",
              "Zócalos y contrazócalos desde los acabados de las habitaciones"]),
            ("OE.3.7 · OE.3.11", "Carpintería, vidrios y pintura", "Puertas y ventanas por unidades iguales; pintura vinculada a los tarrajeos.",
             ["Carpintería de madera y metálica (und)",
              "Vidrios en m²",
              "Pintura de muros, concreto, cielorrasos y puertas (dos caras)"]),
        ], cls="outs outs-3"),
        "funciones", first=True)

    ejemplo = section(
        sec_head("El resultado", "Así sale el edificio de prueba",
                 "Un edificio de 2 pisos con zapatas, vigas de cimentación, columnas, una placa, vigas, aligerado y losa maciza, muros de soga, un tabique, "
                 "puertas, ventanas, baño y sala con acabados, falso cielorraso y cobertura. Cada partida se comprobó a mano y los dos Excel se recalcularon "
                 "sin una sola diferencia: muro de soga 48.25 m², piso cerámico 37.61 m², excavación de zapatas 21.60 m³, eliminación 14.63 m³.")
        + shots([
            (img + "xls_planilla_estructuras.jpg", 1434, 568,
             "Planilla de metrados de estructuras: excavación de zanjas para zapatas y vigas de cimentación con ubicación por ejes, veces, largo, ancho, alto, parcial, total, regla de la Norma e Id de Revit; los descuentos en rojo.",
             "Excel: planilla de estructuras con fórmulas, por ejes y con el Id de Revit", "wide"),
        ], cls="shots shots-ui", style="margin-top:.5rem")
        + shots([
            (img + "revit_modelo_prueba.jpg", 1190, 580,
             "Vista 3D en Revit del edificio de prueba de dos pisos: zapatas, columnas, vigas, losas, muros con puertas y ventanas.",
             "Revit: el edificio de prueba"),
            (img + "revit_resultado_arquitectura.jpg", 856, 869,
             "Ventana de resultados de MetradosALF con el resumen de arquitectura: muros, tarrajeos, cielorrasos, pisos, zócalos, coberturas, carpintería, vidrios y pintura.",
             "Revit: resumen de arquitectura antes de guardar el Excel"),
        ])
        + shots([
            (img + "xls_planilla_arquitectura.jpg", 1383, 612,
             "Planilla de metrados de arquitectura: muro de soga por tramos con el descuento de cada vano, tabique con su ajuste por forma del modelo y tarrajeo interior por cara y por ambiente.",
             "Excel: muros por tramos con el vano real de cada puerta y ventana", "wide"),
        ], cls="shots shots-ui"),
        "ejemplo")

    norma = section(
        sec_head("Cómo mide", "Las reglas de la Norma, no el orden del modelo",
                 "MetradosALF lee la geometría sin las uniones de Revit y reparte cada cruce como lo pide la Norma Técnica de Metrados. "
                 "Si las medidas del sustento no explican todo el volumen del modelo, una fila «Ajuste por forma del modelo» lo deja a la vista.")
        + outs([
            ("OE.2.3.7", "Columnas", "Van de la cara superior de la cimentación a la cara superior del techo: el nudo con vigas y losas es de la columna.", [], " out-hl"),
            ("OE.2.3.8", "Vigas", "Entre caras de columnas o placas, con su peralte total; en el cruce de vigas se mide una sola vez."),
            ("OE.2.3.9.2", "Losa aligerada", "Volumen como losa maciza menos los ladrillos, con la cantidad neta de ladrillos de techo."),
            ("OE.2.1.6", "Esponjamiento", "Eliminación = (excavación − relleno) × factor del suelo elegido, con fórmula viva en el Excel."),
            ("OE.3.1", "Vanos", "En muros se descuentan todos los vanos, medidos en el muro y no solo con la medida nominal de la puerta."),
            ("OE.3.11", "Pintura", "Concordante con los tarrajeos: la fórmula del Excel está vinculada a su total, menos los zócalos."),
        ], cls="outs outs-3")
        + '<p class="fine">El botón «Diagnóstico» guarda en un .txt cómo clasifica MetradosALF cada elemento del modelo (categoría, tipo, material, f\'c, nivel). '
          'Es lo primero que conviene revisar si un elemento no aparece en la planilla.</p>',
        "norma")

    excel = section(
        sec_head("El Excel", "Listo para el expediente y para el S10",
                 "Times New Roman, A4 horizontal ajustado al ancho y con los títulos repetidos al imprimir. Como la planilla tiene fórmulas, "
                 "puedes corregir una medida o agregar una fila y el Resumen y el S10 se actualizan solos.")
        + outs([
            ("HOJA 1", "Resumen", "Índice tipo S10 con los totales vinculados a la planilla e indicadores m³/m² y kg/m³."),
            ("HOJA 2", "Planilla de metrados", "Ítem, descripción, ejes, unidad, veces, medidas, parcial, total, regla de la Norma e Id de Revit."),
            ("HOJA 3", "Acero", "Barras por diámetro y elemento, y el resumen por diámetro con varillas comerciales."),
            ("HOJA 4", "S10", "Ítem, descripción, unidad y metrado para copiar al presupuesto (ítem base 01 y 02)."),
            ("HOJA 5", "Criterios", "Reglas aplicadas, avisos y elementos omitidos con el motivo."),
            ("PRESUPUESTO", "Con PresupuestoALF", "Los metrados pasan al presupuesto con análisis de precios unitarios y de ahí al S10."),
        ], cls="outs outs-3")
        + shots([
            (img + "xls_acero.jpg", 1409, 574,
             "Hoja Acero: barras de 5/8 y 1/2 pulgada con forma, piezas, longitud y peso, y acero estimado por cuantía en los elementos sin barras.",
             "Excel: hoja de acero por elemento y diámetro", "wide"),
        ], cls="shots shots-ui", style="margin-top:1rem"),
        "excel")

    pasos = section(
        sec_head("Cómo funciona", "Tres pasos dentro de Revit")
        + steps([
            ("Modela como siempre", "Cada elemento en su categoría y con un tipo que diga lo que es (aligerado, maciza, falso piso, tabique). En arquitectura, "
             "coloca habitaciones y escribe sus acabados de base y de muro: de ahí salen los zócalos y contrazócalos."),
            ("Elige el alcance y los criterios", "Todo el modelo, lo seleccionado o lo visible en una vista. Marca las partidas y ajusta los criterios: "
             "cota del terreno y tipo de suelo, f'c por defecto, NPT, pesos del acero y cuantías. Se guardan en el modelo."),
            ("Calcula y guarda el Excel", "La ventana muestra el resumen; «Guardar Excel» genera el libro con las cinco hojas y lo abre."),
        ])
        + shots([
            (img + "revit_ventana_estructuras.jpg", 1091, 1022,
             "Ventana de metrados de estructuras: alcance, partidas, criterios de metrado, f'c por defecto, ítem base S10 y movimiento de tierras con la cota del terreno y el tipo de suelo.",
             "Revit: ventana de estructuras"),
            (img + "revit_ventana_arquitectura.jpg", 968, 869,
             "Ventana de metrados de arquitectura: alcance, partidas, cielorraso de losas, cota del piso terminado y contrazócalo por derrame de puerta.",
             "Revit: ventana de arquitectura"),
        ]),
        "")

    faq_items = [
        ("¿Qué versiones de Revit soporta?", "Revit 2023, 2024, 2025, 2026 y 2027 en Windows. El instalador detecta las versiones instaladas; también puedes elegirlas a mano."),
        ("¿Cómo funciona la prueba gratis?", "En el botón «Licencia» escribes tu correo y pulsas «Enviarme el código». Con el código de 6 dígitos que llega al correo se activan 14 días con todas las funciones. Hay una prueba por persona y por PC."),
        ("¿Necesito una plantilla especial?", "No. MetradosALF reconoce los elementos por su categoría, su tipo y su material. Si un elemento no se reconoce, escribe su clase en el parámetro ALF_Metrado (por ejemplo Viga o LosaMaciza) o «No» para excluirlo."),
        ("¿Puedo metrar solo un bloque o un nivel?", "Sí: selecciona los elementos o abre una vista que muestre solo eso y elige «Elementos visibles en la vista activa». Los elementos de alrededor siguen contando para los cruces."),
        ("¿Y si no modelé el acero?", "Marca «Estimar el acero por cuantía»: usa los kg/m³ que definas por tipo de elemento y lo marca como referencial en el Excel. Con AceroALF el acero sale de las barras reales."),
        ("¿Sirve mi clave de AceroALF o SanitariasALF?", "No. Cada programa tiene su propia clave, ligada al Id de máquina que muestra su botón «Licencia»."),
        ("¿Hay licencia para estudiantes?", "Sí: 3 meses gratis, de uso no comercial. Las planillas llevan la marca «VERSIÓN ESTUDIANTE»."),
        ("¿Reemplaza la revisión del metrado?", "No. Es una herramienta de apoyo: los metrados dependen del modelo y de los criterios que eliges, y el profesional responsable los revisa con la Norma y los planos."),
    ]

    jsonld = '<script type="application/ld+json">' + json.dumps({
        "@context": "https://schema.org", "@type": "SoftwareApplication", "name": "MetradosALF",
        "applicationCategory": "DesignApplication", "operatingSystem": "Windows 10, Windows 11",
        "softwareVersion": ins["version"], "url": "https://www.alfbim.com/metradosalf",
        "description": "Complemento de Revit para metrados de estructuras y arquitectura con la Norma Técnica de Metrados, con Excel sustentado y hoja S10.",
        "offers": {"@type": "Offer", "price": str(P["metradosalf"]["precio"]["mensual"]), "priceCurrency": "PEN"},
        "author": {"@type": "Person", "name": "Anderson Irigoín Colunche"}}, ensure_ascii=False) + "</script>"

    return {
        "id": "metradosalf",
        "title": "MetradosALF · Metrados de estructuras y arquitectura en Revit",
        "og_title": "MetradosALF · Planilla de metrados sustentada desde Revit",
        "desc": "Complemento de Revit 2023–2027: metrados de estructuras (movimiento de tierras, concreto, encofrado, acero) y de arquitectura "
                "(muros, tarrajeos, pisos, zócalos, carpintería, pintura) con la Norma Técnica de Metrados, en Excel con sustento por ejes y hoja S10. Prueba gratis 14 días.",
        "nav": [("#funciones", "Funciones"), ("#ejemplo", "Ejemplo"), ("#norma", "Cómo mide"), ("#excel", "Excel"),
                ("#precios", "Precios"), ("#preguntas", "Preguntas")],
        "hero": {
            "crumb": "MetradosALF para Revit",
            "h1": "Metrados sustentados",
            "h1em": "desde Revit",
            "lede": "MetradosALF saca de tu modelo la planilla de metrados de estructuras y arquitectura con la Norma Técnica de Metrados: "
                    "cada partida con su sustento por ejes y por nivel, en un Excel con fórmulas, listo para el expediente y para el S10.",
            "cta2": ("#ejemplo", "Ver el edificio de prueba"),
            "trial": 'Prueba gratis 14 días con todas las funciones · <a href="%s" target="_blank" rel="noopener">Manual (PDF)</a>' % P["metradosalf"]["manual"],
            "meta": ["Revit 2023–2027", "Norma Técnica de Metrados", "Excel y S10"],
            "img": {"src": img + "xls_resumen.jpg", "w": 966, "h": 690,
                    "alt": "Hoja Resumen del Excel de MetradosALF para el edificio de prueba: movimiento de tierras, concreto simple y concreto armado con ítem, descripción, unidad, metrado y regla de la Norma.",
                    "cap": "Resumen · edificio de prueba"},
        },
        "tiles": [
            ("#descargar", "down", "Prueba gratis 14 días", "Instalador para Revit 2023–2027"),
            ("#ejemplo", "table", "Planilla con fórmulas", "Por ejes, por nivel y con el Id"),
            ("#norma", "check", "Norma Técnica de Metrados", "Estructuras y arquitectura"),
        ],
        "secciones": [funciones, ejemplo, norma, excel, pasos],
        "faq": faq_items,
        "dl_titulo": "Descarga MetradosALF y pruébalo 14 días",
        "dl_texto": "Instalador para Revit 2023–2027 en Windows 10 y 11, con el manual. Al terminar, abre Revit y busca la pestaña MetradosALF.",
        "plataforma": "Revit 2023–2027",
        "tm": "Autodesk y Revit son marcas registradas de Autodesk, Inc. Excel es marca de Microsoft. S10 es marca de S10 Software. "
              "MetradosALF es un desarrollo independiente de ALF_BIM y no está afiliado a ellas.",
        "jsonld": jsonld,
    }
