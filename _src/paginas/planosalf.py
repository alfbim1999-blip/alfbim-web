"""Página de PlanosALF (gratuito)."""
import json


def pagina(g):
    section, sec_head, outs, shots, steps = g["section"], g["sec_head"], g["outs"], g["shots"], g["steps"]
    P = g["P"]
    p = P["planosalf"]
    ins = p["instalador"]

    jsonld = '<script type="application/ld+json">' + json.dumps({
        "@context": "https://schema.org", "@type": "SoftwareApplication",
        "name": "PlanosALF", "softwareVersion": ins["version"],
        "operatingSystem": "Windows 10, Windows 11", "applicationCategory": "DesignApplication",
        "description": "Extensión gratuita de pyRevit para Revit 2023–2027: crea láminas desde Excel, llena rótulos, "
                       "renumera por especialidad y exporta en lote a PDF y DWG con índice de planos.",
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "PEN"},
        "url": "https://www.alfbim.com/planosalf",
        "publisher": {"@type": "Organization", "name": "ALF_BIM"},
    }, ensure_ascii=False) + "</script>"

    funciones = section(
        sec_head("Qué hace", "Todo el juego de planos, desde una lista en Excel",
                 "Armar las láminas de un expediente lleva días: crear decenas de hojas por especialidad, llenar el rótulo "
                 "con el formato de la Entidad, numerarlas y exportarlas una por una. PlanosALF lo hace en minutos y "
                 "cada cambio se ve antes en una vista previa.")
        + outs([
            ("EXCEL", "Crea láminas desde Excel", "Una fila por lámina: especialidad, número, nombre, rótulo y vistas.",
             ["Crea las nuevas y actualiza las existentes", "Numera solas las filas sin número", "Al volver a leer el Excel no duplica nada"]),
            ("RÓTULO", "Llena el rótulo", "Cada columna verde se escribe en el parámetro del mismo nombre.",
             ["Parámetros de la lámina y de su rótulo", "Información del proyecto desde la hoja PROYECTO", "Revit en español o en inglés"]),
            ("VISTAS", "Coloca vistas y tablas", "Las ordena en filas dentro del rótulo, dejando libre la franja del cajetín.",
             ["Plantas, cortes, leyendas y tablas", "Cuadros de carga de tableros", "Avisa si una vista no entra"]),
            ("IDA Y VUELTA", "Láminas a Excel", "Exporta las láminas del modelo para editarlas en Excel y volver a leerlas.",
             ["Con sus parámetros y vistas", "Columna Id Revit para cambiar números", "Si nada cambió, todo sale «Sin cambios»"]),
            ("NUMERACIÓN", "Renumera por especialidad", "E-01, IE-01, IS-01… cada especialidad por separado, o con un prefijo fijo.",
             ["Inicio, incremento, dígitos y separador", "Intercambia números sin choques", "Total de láminas en el rótulo (opcional)"]),
            ("EXPORTAR", "PDF y DWG en lote", "Una subcarpeta por especialidad y nombres de archivo con patrón.",
             ["PDF por lámina, por especialidad o uno solo", "300, 600 o 1200 ppp", "DWG con la versión de AutoCAD que elijas"]),
            ("ÍNDICE", "Índice de planos", "Excel agrupado por especialidad, con la revisión y su fecha.",
             ["En el orden de tus especialidades", "Se guarda junto a los PDF", "Omite las láminas fuera de la lista"]),
            ("SEGURO", "Vista previa y un solo Deshacer", "Ves qué se crea, qué se actualiza y por qué antes de aplicar.",
             ["Todo queda en un solo Ctrl+Z", "Si cancelas, el modelo no cambia", "Trabaja solo en tu PC, sin internet"]),
        ]),
        "funciones", first=True)

    ejemplo = section(
        sec_head("En Revit", "Así se ve PlanosALF",
                 "Capturas de las pruebas en Revit 2027.3 con un juego de láminas de estructuras, sanitarias y eléctricas.")
        + shots([
            ("img/planosalf/vista_previa.jpg", 1387, 580,
             "Ventana Crear láminas desde Excel con la vista previa: filas para crear, actualizar, sin cambios y con error, y el detalle de cada cambio.",
             "Crear desde Excel: vista previa con lo que cambia en cada lámina", "wide"),
            ("img/planosalf/renumerar.jpg", 1036, 570,
             "Ventana Renumerar con las láminas marcadas, la columna Nuevo con el número resultante y las opciones de prefijo y numeración.",
             "Renumerar: la columna «Nuevo» muestra el resultado antes de aplicarlo"),
            ("img/planosalf/configuracion.jpg", 1110, 765,
             "Ventana Configuración con la lista de especialidades del Perú, la numeración, el rótulo por defecto y la colocación de vistas.",
             "Configuración: especialidades usuales de los expedientes en el Perú"),
            ("img/planosalf/lamina.jpg", 725, 515,
             "Lámina creada por PlanosALF con una planta de cimentación, una leyenda de detalle y una tabla dentro del rótulo.",
             "Lámina creada con una planta, una leyenda y una tabla"),
            ("img/planosalf/informe.jpg", 874, 400,
             "Informe de resultados con cada lámina creada o actualizada, un enlace para abrirla y las observaciones.",
             "Informe de resultados con un enlace a cada lámina"),
        ], style="margin-top:.5rem"),
        "ejemplo")

    como = section(
        sec_head("Cómo funciona", "Del Excel al juego de planos en tres pasos")
        + steps([
            ("Prepara el Excel", "Carga el rótulo de tu Entidad y pulsa «Plantilla Excel». Llena la hoja LÁMINAS, una fila por lámina, y la hoja PROYECTO con los datos comunes del cajetín."),
            ("Crea las láminas", "Pulsa «Crear desde Excel», revisa la vista previa y aplica. Si luego cambias un nombre o una fecha, cámbialo en el Excel y vuelve a leerlo: solo se actualiza lo que cambió."),
            ("Exporta", "Pulsa «Exportar PDF / DWG»: una subcarpeta por especialidad, nombres estandarizados como E-01.pdf y el índice de planos en Excel."),
        ])
        + shots([
            ("img/planosalf/exportar.jpg", 1377, 868,
             "Ventana Exportar PDF y DWG con la lista de láminas, el destino, el patrón de nombre y las opciones de PDF y DWG.",
             "Exportar: láminas, formatos, nombres de archivo y opciones de PDF y DWG", "wide"),
        ]),
        "como")

    requisitos = section(
        sec_head("Requisitos", "Qué necesitas para usarlo",
                 "PlanosALF es una extensión de pyRevit, un complemento gratuito y de código abierto para Revit. "
                 "Si no lo tienes, el instalador te ofrece abrir la página de descarga.")
        + outs([
            ("REVIT", "Revit 2023 a 2027", "Probado en Revit 2027.3. Se instala para tu usuario de Windows, sin permisos de administrador.", [], " out-hl"),
            ("PYREVIT", "pyRevit, gratis", 'Versión 6.4 o superior para Revit 2027. Se descarga de <a href="https://github.com/pyrevitlabs/pyRevit/releases" target="_blank" rel="noopener">github.com/pyrevitlabs/pyRevit</a>.', []),
            ("EXCEL", "Un programa que guarde .xlsx", "Microsoft Excel, LibreOffice o Google Sheets para preparar la lista de láminas.", []),
        ], "outs outs-3")
        + '<p class="fine">¿Prefieres no usar el instalador? Descarga el ZIP, copia la carpeta PlanosALF.extension en '
          '<code style="overflow-wrap:anywhere">%APPDATA%\\pyRevit\\Extensions</code> y pulsa pyRevit → Recargar. Para desinstalar, borra esa carpeta.</p>'
        + '<div class="sec-head" style="margin-top:3.5rem;margin-bottom:1.5rem"><p class="eyebrow">Del mismo equipo</p>'
          '<h2>Lleva el modelo más lejos</h2></div>'
        + outs([
            ("DE PAGO", '<a href="aceroalf.html">AceroALF</a>', "Coloca el acero de refuerzo en Revit y genera las vistas, la planilla y las láminas de acero que luego ordenas con PlanosALF.",
             ['<a href="aceroalf.html">Conocer AceroALF →</a>']),
            ("DE PAGO", '<a href="metradosalf.html">MetradosALF</a>', "Metrados de estructuras y arquitectura desde el mismo modelo, con la Norma Técnica de Metrados y hoja para el S10.",
             ['<a href="metradosalf.html">Conocer MetradosALF →</a>']),
            ("GRATIS", '<a href="plantilla-excel-estructuras.html">Plantilla Excel Estructuras</a>', "Diseño en concreto armado con la E.060 en 15 hojas de Excel, sin macros.",
             ['<a href="plantilla-excel-estructuras.html">Ver la plantilla →</a>']),
        ], "outs outs-3"),
        "requisitos")

    zip_sha = "03EF3C82FAD7CCE9C75EC33A068021EB0784C388DD6F2A52BFFCB47F9C7E16E0"
    return {
        "id": "planosalf",
        "title": "PlanosALF · Láminas en lote para Revit, gratis",
        "desc": "PlanosALF es una extensión gratuita de pyRevit para Revit 2023–2027: crea láminas desde Excel, llena los "
                "rótulos, renumera por especialidad (E-, IE-, IS-) y exporta en lote a PDF y DWG con el índice de planos.",
        "og_title": "PlanosALF · Láminas en lote para Revit, gratis",
        "jsonld": jsonld,
        "nav": [("#funciones", "Funciones"), ("#ejemplo", "En Revit"), ("#requisitos", "Requisitos"), ("#preguntas", "Preguntas")],
        "hero": {
            "crumb": "PlanosALF para Revit",
            "h1": "Láminas en lote", "h1em": "para Revit, gratis",
            "lede": "PlanosALF crea las láminas del expediente desde un Excel, llena los rótulos, las renumera por especialidad "
                    "y las exporta en lote a PDF y DWG con el índice de planos. Lo que antes tomaba días, ahora toma minutos.",
            "cta2": ("#ejemplo", "Ver cómo se ve en Revit"),
            "trial": 'Gratis para uso personal, académico y comercial · <a href="tutoriales/Manual_PlanosALF_1.0.pdf" target="_blank" rel="noopener">Manual (PDF)</a>',
            "meta": ["Revit 2023–2027", "Requiere pyRevit (gratis)", "Sin licencia ni registro"],
            "img": {"src": "img/planosalf/exportar.jpg", "w": 1377, "h": 868,
                    "alt": "Ventana Exportar PDF y DWG de PlanosALF con nueve láminas marcadas y las opciones de formato, nombre de archivo, PDF y DWG.",
                    "cap": "Exportar PDF / DWG · láminas de prueba",
                    "legend": ["Una subcarpeta por especialidad", "PDF hasta 1200 ppp y DWG"]},
        },
        "tiles": [
            ("#descargar", "down", "Descargar gratis", "Instalador para Revit 2023–2027"),
            ("#funciones", "table", "Láminas desde Excel", "Crear, actualizar y volver a leer"),
            ("tutoriales/Manual_PlanosALF_1.0.pdf", "doc", "Manual en PDF", "Instalación y uso, paso a paso"),
        ],
        "secciones": [funciones, ejemplo, como, requisitos],
        "faq": [
            ("¿Es gratis de verdad?", "Sí. PlanosALF es gratuito para uso personal, académico y comercial. No tiene licencia, servidor ni registro."),
            ("No aparece la pestaña PlanosALF", "Verifica que pyRevit cargue (pestaña «pyRevit») y pulsa pyRevit → Recargar. La extensión debe estar en %APPDATA%\\pyRevit\\Extensions\\PlanosALF.extension."),
            ("¿Funciona con el rótulo de mi Entidad?", "Sí. Cargas tu rótulo en el modelo y cada columna verde del Excel se escribe en el parámetro del mismo nombre. Si el dato es un parámetro de tipo en la familia del rótulo, cámbialo a parámetro de ejemplar."),
            ("¿Puedo deshacer lo que hizo?", "Sí. Cada comando es un solo paso de Deshacer (Ctrl+Z). Si cancelas «Crear desde Excel» a mitad de camino, el modelo no cambia. La exportación no modifica el modelo."),
            ("¿Coloca cuadros de carga y tablas?", "Sí. Las tablas de planificación, los cuadros de carga de tableros eléctricos y las leyendas se colocan igual que las vistas y pueden repetirse en varias láminas."),
            ("¿Envía mis datos a internet?", "No. PlanosALF trabaja solo en tu PC."),
        ],
        "dl_titulo": "Descarga PlanosALF gratis",
        "dl_texto": "Instalador por usuario para Revit 2023–2027: no pide permisos de administrador y detecta pyRevit. "
                    "También puedes bajar el ZIP para instalarlo a mano (SHA-256 <code style='overflow-wrap:anywhere;word-break:break-all'>%s</code>) y el Excel de ejemplo "
                    "con el expediente de una institución educativa." % zip_sha,
        "dl_extra": '<a class="btn btn-ghost" href="descargas/PlanosALF_1.0.0_instalacion_manual.zip" download>ZIP sin instalador</a>'
                    '<a class="btn btn-ghost" href="descargas/Ejemplo_Laminas_PlanosALF.xlsx" download>Excel de ejemplo</a>',
        "plataforma": "Revit 2023–2027 · pyRevit",
        "tm": "Autodesk y Revit son marcas registradas de Autodesk, Inc. pyRevit es de pyRevitLabs. Excel es marca de Microsoft. "
              "PlanosALF es un desarrollo independiente de ALF_BIM y no está afiliado a ellas.",
    }
