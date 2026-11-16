"""Página de CheckerALF (ALF-03). Fuentes: Manual_CheckerALF_1.0.pdf, docs/NORMATIVA.md, VENTA/18_CheckerALF/LEEME.txt,
claude/ALF-03_CheckerALF_estado.md."""
import json


def pagina(g):
    section, sec_head, outs, steps = g["section"], g["sec_head"], g["outs"], g["steps"]
    P = g["P"]
    ins = P["checkeralf"]["instalador"]

    funciones = section(
        sec_head("Qué hace", "Revisa el modelo antes de entregarlo",
                 "CheckerALF revisa tu modelo de Revit, o el IFC que te entregaron, con las guías del Plan BIM Perú (MEF) y el EIR de la "
                 "Entidad. Te dice qué falta, en qué elemento y qué numeral de la guía lo pide.")
        + outs([
            ("GESTIÓN", "Nombre, información y coordenadas", "Lo que pide la Guía Nacional BIM para el archivo.",
             ["Nomenclatura del archivo: campos, códigos y revisión",
              "Información del proyecto, unidades y georreferencia",
              "Vínculos y subproyectos"]),
            ("ESTRUCTURA", "Niveles, ejes y elementos", "Un modelo ordenado que otros puedan usar.",
             ["Elementos sin nivel, en el nivel equivocado o flotantes",
              "Duplicados, superposiciones y advertencias",
              "CAD importados y contenido sin uso"]),
            ("INFORMACIÓN", "Parámetros, materiales y clasificación", "Lo que la Entidad exige a cada elemento.",
             ["Parámetros obligatorios por categoría",
              "Material, código de clasificación y clase IFC",
              "Nombres de tipos legibles"]),
            ("ESPECIALIDAD", "Arquitectura, estructuras e instalaciones", "Reglas propias de cada modelo.",
             ["Habitaciones cerradas, puertas y ventanas en muros",
              "Analítico, uso estructural y f'c del concreto",
              "Tuberías con sistema, redes sin extremos abiertos"]),
            ("IFC", "Sin Revit", "CheckerALF IFC revisa el archivo IFC con las mismas reglas.",
             ["Para la Entidad o el supervisor que recibe el modelo",
              "IFC4 e IFC2x3",
              "Lo que el IFC no trae queda «No aplica» y no resta"]),
            ("ENTREGABLES", "Reportes, BCF e historial", "Listos para el expediente y la coordinación.",
             ["Reporte Excel y PDF en Times New Roman",
              "Incidencias BCF 2.1 para Navisworks, BIMcollab o el CDE",
              "Comparación con la revisión anterior"]),
        ], cls="outs outs-3"),
        "funciones", first=True)

    lectura = section(
        sec_head("Cómo lo hace", "Cada observación con su fuente",
                 "43 reglas configurables. Cada una cita el documento, el numeral y la página de la guía del MEF que la pide, o explica "
                 "por qué es una buena práctica.")
        + outs([
            ("PUNTAJE", "General y por grupo", "Pesos por gravedad; APROBADO u OBSERVADO según la meta del EIR (95 % por defecto).", [], " out-hl"),
            ("PERFIL", "El EIR de la Entidad", "Códigos, parámetros obligatorios, sistema de clasificación y meta, en un archivo."),
            ("CONJUNTO", "Las reglas en Excel", "Activa, desactiva o cambia la gravedad de cada regla y vuelve a cargarlo."),
            ("EN REVIT", "Ve a cada elemento", "Selecciona los observados, vista 3D coloreada y estado escrito en parámetros."),
            ("BCF", "Incidencias abiertas", "Una incidencia por observación, con el elemento marcado y la cámara en su sitio."),
            ("VALIDADO", "Revit e IFC comparados", "14 IFC de modelos reales y de prueba, regla por regla contra Revit; las diferencias que quedan vienen del exportador y están en el manual."),
        ], cls="outs outs-3"),
        "lectura")

    pasos = section(
        sec_head("Cómo funciona", "Tres pasos")
        + steps([
            ("Abre el modelo", "En Revit, la pestaña CheckerALF; sin Revit, CheckerALF IFC con el archivo .ifc."),
            ("Elige las reglas y el perfil", "Las guías del MEF de fábrica y, si la Entidad te dio uno, su EIR."),
            ("Revisa y corrige", "Puntaje, observaciones con su fuente, reportes y BCF; vuelve a revisar y compara."),
        ]),
        "")

    faq_items = [
        ("¿Qué necesito?", "Windows 10 u 11. Para el complemento, Revit 2023, 2024, 2025, 2026 o 2027. CheckerALF IFC no necesita Revit."),
        ("¿En qué se basan las reglas?", "En la RD 0007-2025-EF/63.01, la Guía Nacional BIM 2023, la Guía técnica BIM, la Guía openBIM y el EIR de ejemplo del MEF. Cada observación cita su documento, numeral y página."),
        ("¿Puedo usar el EIR de mi Entidad?", "Sí. El perfil del proyecto fija los códigos, los parámetros obligatorios, el sistema de clasificación y la meta de aprobación. El conjunto de reglas se edita en Excel."),
        ("¿Revisa archivos IFC?", "Sí, con CheckerALF IFC y sin Revit. Lo que un IFC no trae (vínculos, subproyectos, advertencias de Revit) queda como «No aplica» y no resta puntaje."),
        ("¿Qué es el BCF?", "El formato abierto de incidencias de buildingSMART. CheckerALF guarda cada observación con su elemento marcado, para abrirla en Navisworks, BIMcollab, Solibri o el CDE de la Entidad."),
        ("¿Hay licencia para Entidades?", "Sí, la licencia institucional de 12 meses. La misma clave sirve para Revit y para CheckerALF IFC en la misma computadora."),
        ("¿Cómo funciona la prueba gratis?", "En el botón «Licencia» escribes tu correo y pulsas «Enviarme el código». Con el código de 6 dígitos se activan 14 días con todas las funciones. Hay una prueba por persona y por PC."),
        ("¿Reemplaza la revisión del especialista?", "No. Revisa lo que se puede comprobar en el modelo; el coordinador BIM y la Entidad dan la conformidad."),
    ]

    jsonld = '<script type="application/ld+json">' + json.dumps({
        "@context": "https://schema.org", "@type": "SoftwareApplication", "name": "CheckerALF",
        "applicationCategory": "DesignApplication", "operatingSystem": "Windows 10, Windows 11",
        "softwareVersion": ins["version"], "url": "https://www.alfbim.com/checkeralf",
        "description": "Verificador de modelos BIM de Revit e IFC con las guías del Plan BIM Perú (MEF) y el EIR de la Entidad: puntaje, observaciones con fuente normativa, reportes Excel y PDF, BCF y comparación de revisiones.",
        "offers": {"@type": "Offer", "price": str(P["checkeralf"]["precio"]["mensual"]), "priceCurrency": "PEN"},
        "author": {"@type": "Person", "name": "Anderson Irigoín Colunche"}}, ensure_ascii=False) + "</script>"

    return {
        "id": "checkeralf",
        "title": "CheckerALF · Revisa tu modelo BIM con las guías del MEF",
        "og_title": "CheckerALF · Verificador de modelos BIM para el Perú",
        "desc": "Revisa el modelo de Revit o el IFC con las guías del Plan BIM Perú (MEF) y el EIR de la Entidad: puntaje, observaciones con su fuente "
                "normativa, reportes Excel y PDF, incidencias BCF y comparación de revisiones. Revit 2023–2027 e IFC. Prueba gratis 14 días.",
        "nav": [("#funciones", "Funciones"), ("#lectura", "Cómo lo hace"),
                ("#precios", "Precios"), ("#preguntas", "Preguntas")],
        "hero": {
            "crumb": "CheckerALF para Revit e IFC",
            "h1": "Revisa tu modelo BIM",
            "h1em": "con las guías del MEF",
            "lede": "CheckerALF revisa el modelo de Revit o el IFC con las guías del Plan BIM Perú y el EIR de la Entidad. Te da un puntaje, "
                    "cada observación con su elemento y su fuente, reportes para el expediente e incidencias BCF.",
            "cta2": ("#lectura", "Ver cómo lo hace"),
            "trial": 'Prueba gratis 14 días con todas las funciones · <a href="%s" target="_blank" rel="noopener">Manual (PDF)</a>' % P["checkeralf"]["manual"],
            "meta": ["Revit 2023–2027", "IFC4 e IFC2x3", "Plan BIM Perú"],
            "img": {"cap": "Revisión BIM", "panel": '<ul class="hpanel">'
                    '<li><span class="hc">G</span><b>Gestión</b><span class="hu">13 reglas</span><small>Nombre, información, coordenadas y vínculos.</small></li>'
                    '<li><span class="hc">E</span><b>Estructura</b><span class="hu">12 reglas</span><small>Niveles, ejes, duplicados y advertencias.</small></li>'
                    '<li><span class="hc">I</span><b>Información</b><span class="hu">6 reglas</span><small>Parámetros, materiales y clasificación.</small></li>'
                    '<li><span class="hc">A·S·M</span><b>Especialidad</b><span class="hu">9 reglas</span><small>Arquitectura, estructuras e instalaciones.</small></li>'
                    '<li><span class="hc">L</span><b>Línea ALF</b><span class="hu">3 reglas</span><small>Listo para MetradosALF y EtabsRevitALF.</small></li>'
                    '</ul>'},
        },
        "tiles": [
            ("#descargar", "down", "Prueba gratis 14 días", "Revit 2023–2027 e IFC"),
            ("#funciones", "layers", "43 reglas con su fuente", "Guías del Plan BIM Perú"),
            ("#lectura", "check", "APROBADO u OBSERVADO", "Con la meta del EIR"),
        ],
        "secciones": [funciones, lectura, pasos],
        "faq": faq_items,
        "dl_titulo": "Descarga CheckerALF y pruébalo 14 días",
        "dl_texto": "Un instalador para Windows 10 y 11: el complemento para Revit 2023–2027 y CheckerALF IFC, con el manual. Al terminar, abre Revit y busca la pestaña CheckerALF, o abre CheckerALF IFC desde el menú Inicio.",
        "plataforma": "Revit 2023–2027 · IFC",
        "tm": "Autodesk y Revit son marcas registradas de Autodesk, Inc. IFC y BCF son estándares de buildingSMART International. Excel es marca de Microsoft. "
              "CheckerALF es un desarrollo independiente de ALF_BIM y no está afiliado a ellas ni al Ministerio de Economía y Finanzas.",
        "jsonld": jsonld,
    }
