"""Portada de www.alfbim.com (diseño de oct-2026, inspirado en autodesk.com; lanzamiento del 15-nov-2026).

Portada negra con los programas por especialidad (íconos), catálogo completo por especialidad,
precios de lanzamiento y packs, descargas gratis, plantilla de Revit gratis, confianza y contacto. Los datos salen de _src/config.json.
"""
import re, html

E = html.escape

MOTIVOS = {
    # planta de arquitectura: muros, puerta con su giro y ventana
    "arquitectura": '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="10" width="48" height="44" rx="1"/><path d="M8 32h20M36 32h20M30 10v12"/><path d="M28 32a8 8 0 0 1 8-8"/><path d="M28 32v-8"/><path d="M40 7v6M50 7v6M40 10h10"/></svg>',
    # columna con su acero: sección, barras y estribo
    "estructuras": '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="10" y="10" width="44" height="44" rx="1"/><rect x="17" y="17" width="30" height="30" rx="3"/><circle cx="21" cy="21" r="2.4" fill="currentColor"/><circle cx="43" cy="21" r="2.4" fill="currentColor"/><circle cx="21" cy="43" r="2.4" fill="currentColor"/><circle cx="43" cy="43" r="2.4" fill="currentColor"/><circle cx="32" cy="21" r="2.4" fill="currentColor"/><circle cx="32" cy="43" r="2.4" fill="currentColor"/><path d="M17 23l5-6"/></svg>',
    # tubería con codo, tee y gota
    "sanitarias": '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M6 20h30a8 8 0 0 1 8 8v30"/><path d="M6 28h26a4 4 0 0 1 4 4v26"/><path d="M14 16v16M28 16v16M38 40h10M38 50h10"/><path d="M54 8s5 6 5 9a5 5 0 0 1-10 0c0-3 5-9 5-9Z"/></svg>',
    # diagrama unifilar: barra, interruptores y circuitos
    "electricas": '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M32 4v12M12 16h40M12 16v10M26 16v10M40 16v10M52 16v10"/><path d="M12 26l4 8M26 26l4 8M40 26l4 8M52 26l4 8"/><path d="M12 36v22M26 36v22M40 36v22M52 36v22"/><circle cx="32" cy="4" r="2" fill="currentColor"/></svg>',
    # cronograma: barras de Gantt y ruta crítica
    "obra": '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M6 8v50h52"/><rect x="10" y="14" width="18" height="6" rx="1"/><rect x="22" y="25" width="22" height="6" rx="1" fill="currentColor" fill-opacity=".25"/><rect x="34" y="36" width="14" height="6" rx="1"/><rect x="44" y="47" width="12" height="6" rx="1" fill="currentColor" fill-opacity=".25"/><path d="M28 17h0M28 20v5M44 31v5M48 42v5"/></svg>',
}

CONFIANZA = [
    ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="4" y="5" width="16" height="15" rx="2"/><path d="M4 10h16M9 3v4M15 3v4M9 15l2 2 4-4"/></svg>',
     "Pruébalo antes de pagar", "Los complementos de Revit traen 14 días de prueba con todas las funciones; los de escritorio, una versión gratuita."),
    ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M4 19V5h16v14l-4-3H4"/><path d="M8 9h8M8 12h5"/></svg>',
     "Hablas con quien lo programa", "El soporte lo da el ingeniero que desarrolla cada programa, por WhatsApp o correo."),
    ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M12 3 4 6v6c0 4.5 3.4 8 8 9 4.6-1 8-4.5 8-9V6l-8-3Z"/><path d="m9 12 2 2 4-4"/></svg>',
     "Licencias firmadas", "Cada clave va ligada a tu PC y se verifica sin enviar tus modelos a ningún servidor."),
    ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M3 12h4l3-7 4 14 3-7h4"/></svg>',
     "Norma peruana de verdad", "E.060, Norma Técnica de Metrados, IS.010, CNE y Ley 32069, leídas página por página."),
]


def construir(g):
    CFG, P, RAIZ = g["CFG"], g["P"], g["RAIZ"]
    wa, soles, svg, E_ = g["wa"], g["soles"], g["svg"], g["E"]
    CH = g["CHROME"]
    base = (g["SRC"] / "base_index.html").read_text(encoding="utf-8")
    favicon = re.search(r'<link rel="icon"[^>]+>', base).group(0)

    acero = P["aceroalf"]
    pagos = [k for k, p in P.items() if p.get("precio")]
    gratis = [k for k, p in P.items() if not p.get("precio")]
    total = len(P)

    def icono(pid, size=44):
        f = RAIZ / "img" / "iconos" / (pid + ".png")
        if f.exists():
            return '<img src="img/iconos/%s.png" width="%d" height="%d" alt="" loading="lazy">' % (pid, size, size)
        ic = {"estructuras": "layers", "sanitarias": "drop", "electricas": "bolt", "obra": "cal"}[P[pid]["linea"]]
        if P[pid]["tipo"] == "excel":
            ic = "table"
        return '<span class="ph">%s</span>' % svg(ic)

    def plataforma(p):
        return {"revit": "Complemento de Revit", "escritorio": "Windows", "excel": "Excel"}[p["tipo"]]

    def precio_corto(p):
        if not p.get("precio"):
            return "<b>Gratis</b>"
        return "Desde <b>%s</b> al mes" % soles(p["precio"]["mensual"])

    # ---------- portada: título y los programas por especialidad
    CORTO = {"aceroalf": "Acero", "metradosalf": "Metrados", "cadrevitalf": "CAD a Revit", "etabsrevitalf": "Revit a ETABS",
             "memoriaestructuralalf": "Memoria E.030", "checkeralf": "Revisión BIM", "planosalf": "Planos",
             "plantilla-excel-estructuras": "Excel Estructuras", "sanitariasalf": "IISS en Revit", "redesinterioresalf": "Redes interiores",
             "dotacionalf": "Dotación", "saneamientoruralalf": "Saneamiento rural", "electricasalf": "IIEE en Revit",
             "maximademandaalf": "Máxima demanda", "plantilla-excel-iiee": "Excel IIEE", "presupuestoalf": "Presupuesto",
             "cronogramaalf": "Cronograma", "valorizacionesalf": "Valorizaciones", "plazosalf": "Plazos",
             "informemensualalf": "Informe mensual", "simulacion4dalf": "Simulación 4D"}
    filas = []
    for ln in CFG["lineas"]:
        ids = [k for k, p in P.items() if p["linea"] == ln["id"]]
        apps = "".join('<a class="app" href="%s.html" title="%s">%s<span>%s</span></a>' % (k, E(P[k]["nombre"]), icono(k, 40), E(CORTO.get(k, P[k]["nombre"]))) for k in ids)
        filas.append('<div class="apps-row"><a class="apps-head" href="#linea-%s">%s<b>%s</b><small>%d</small></a><div class="apps">%s</div></div>' % (
            ln["id"], MOTIVOS[ln["id"]], E(ln["nombre"]), len(ids), apps))
    hero = f"""<section class="home-hero">
  <div class="wrap home-grid">
    <div>
      <h1>Software para la ingeniería civil</h1>
      <p class="lede">{total} programas para Revit, el expediente técnico y la obra, hechos con la norma peruana: estructuras, instalaciones sanitarias y eléctricas, costos y gestión de obra.</p>
      <p class="price-line">Desde <b>{soles(min(P[k]['precio']['mensual'] for k in pagos))}</b> al mes. Pruébalos gratis antes de pagar.</p>
      <div class="cta">
        <a class="btn btn-primary" href="#productos">Ver los programas</a>
        <a class="btn btn-ghost" href="#precios">Precios y packs</a>
      </div>
    </div>
    <nav class="apps-card" aria-label="Programas por especialidad">{''.join(filas)}</nav>
  </div>
</section>
"""

    # ---------- catálogo completo por especialidad
    tabs = ['<button type="button" data-f="todos" aria-pressed="true">Todos <small>%d</small></button>' % total]
    grupos = []
    for ln in CFG["lineas"]:
        ids = [k for k, p in P.items() if p["linea"] == ln["id"]]
        if not ids:
            continue
        tabs.append('<button type="button" data-f="%s" aria-pressed="false">%s <small>%d</small></button>' % (ln["id"], E(ln["nombre"]), len(ids)))
        cards = "".join(
            '<a class="ccard" href="%s.html" data-linea="%s"><div class="ccard-top">%s<div><span class="ctag %s">%s</span><h4>%s</h4></div></div>'
            '<p>%s</p><div class="cmeta"><span>%s</span><span>%s</span></div></a>' % (
                k, ln["id"], icono(k), "live" if P[k].get("precio") else "free", "Prueba 14 días" if P[k]["tipo"] == "revit" and P[k].get("precio")
                else ("Gratis" if not P[k].get("precio") else "Versión gratuita"),
                E(P[k]["nombre"] + (" " + P[k]["marca"] if P[k].get("marca") else "")), E(P[k]["resumen"]),
                plataforma(P[k]), precio_corto(P[k]))
            for k in ids)
        grupos.append('<div class="cat-line" id="linea-%s" data-linea="%s"><div class="cat-line-head"><h3>%s</h3><p>%s</p></div><div class="cgrid">%s</div></div>' % (
            ln["id"], ln["id"], E(ln["nombre"]), E(ln["desc"]), cards))

    # ---------- precios de lanzamiento por grupo
    PL = CFG["precios_lanzamiento"]["grupos"]
    def lista(g):
        return [k for k in pagos if P[k].get("grupo_precio") == g]
    def plan(nombre, g, quien, promo, otros, feat=False):
        pr = PL[g]
        return ('<article class="plan%s">%s<span class="pn">%s</span><p class="who">%s</p>'
                '<div class="price"><span class="amt mono">%s</span><span class="per">/ mes</span></div><p class="ps">%s</p><p class="promo">%s</p>'
                '<ul>%s</ul></article>') % (
            " feat" if feat else "", '<span class="ribbon">Más programas</span>' if feat else "", nombre, quien, soles(pr["mensual"]), otros, promo,
            "".join('<li><a href="%s.html">%s</a></li>' % (k, E(P[k]["nombre"])) for k in lista(g)))
    rv, es, ca = PL["revit"], PL["escritorio"], PL["calculadora"]
    tarifas = "".join([
        plan("Complementos de Revit", "revit", "Trabajan dentro de tu modelo de Revit 2023 a 2027.", "Prueba gratis 14 días con todas las funciones",
             "%s por 6 meses · %s al año" % (soles(rv["m6"]), soles(rv["anual"]))),
        plan("Programas de escritorio", "escritorio", "Para el expediente y la obra, en Windows 10 y 11.", "Versión gratuita con marca de agua",
             "%s al año" % soles(es["anual"])),
        plan("Calculadoras", "calculadora", "Cálculo de instalaciones con su memoria.", "Versión gratuita con marca de agua",
             "%s al año" % soles(ca["anual"])),
    ])
    precios = f"""<section class="block pricing" id="precios">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Precios de lanzamiento</p>
      <h2>Un precio por programa, o todos en un pack</h2>
      <p class="lede">Cada licencia es por computadora y tiene todas las funciones. Pagas con {E(CFG['pagos'])}; te mandamos la clave apenas se acredite el pago.</p>
    </div>
    <div class="plans">{tarifas}</div>
    <div id="packs">{g['packs_html']()}</div>
    <p class="fine">Precios de lanzamiento en soles; se mantienen mientras renueves sin interrupción. PlanosALF y las plantillas de Excel son gratis.
      Revisa la <a href="reembolsos.html">política de reembolso</a> y los <a href="terminos.html">términos y condiciones</a>.</p>
  </div>
</section>
"""

    # ---------- descargas gratis
    gcards = "".join(
        '<a class="ccard" href="%s.html"><div class="ccard-top">%s<div><span class="ctag free">Gratis</span><h4>%s</h4></div></div><p>%s</p>'
        '<div class="cmeta"><span>%s</span><span><b>Descargar</b></span></div></a>' % (
            k, icono(k), E(P[k]["nombre"]), E(P[k]["resumen"]), plataforma(P[k]))
        for k in gratis)

    productos = f"""<section class="block" id="productos">
  <div class="wrap">
    <div class="sec-head">
      <h2>Productos</h2>
      <p class="lede">Cada programa resuelve una parte del expediente o de la obra. Los complementos de Revit traen 14 días de prueba; los programas de escritorio, una versión gratuita con marca de agua. Entra a cada uno para ver sus capturas y sus resultados.</p>
    </div>
    <div class="cat-tabs" role="group" aria-label="Filtrar por especialidad">{''.join(tabs)}</div>
    {''.join(grupos)}
  </div>
</section>

{precios}
<section class="block tone-stone" id="gratis" aria-labelledby="t-gratis">
  <div class="wrap">
    <div class="sec-head">
      <h2 id="t-gratis">Descargas gratis</h2>
      <p class="lede">Sin licencia y sin fecha de vencimiento.</p>
    </div>
    <div class="cgrid">{gcards}</div>
  </div>
</section>
"""

    # ---------- plantillas de Revit gratis (config.json → plantillas_revit)
    PR = CFG["plantillas_revit"]
    tcards = "".join(
        '<article class="ccard tplcard"><div class="ccard-top"><span class="ph">%s</span><div><span class="ctag free">Gratis</span><h4>%s</h4></div></div>'
        '<p>%s</p><ul>%s</ul><p class="tpl-para">Para %s.</p>'
        '<div class="cmeta"><span>ZIP · %s · %s</span><a class="btn btn-primary" href="descargas/%s" download>Descargar</a></div></article>' % (
            MOTIVOS[t["id"]], E(t["nombre"]).replace("_", "_<wbr>"), E(t["desc"]), "".join("<li>%s</li>" % E(x) for x in t["incluye"]),
            E(t["para"]), g["mb"](t["bytes"]), E(PR["revit"]), t["archivo"])
        for t in PR["lista"])
    plantilla = f"""<section class="block" id="plantilla" aria-labelledby="t-tpl">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Descarga gratuita</p>
      <h2 id="t-tpl">Plantillas de Revit ALF_BIM</h2>
      <p class="lede">Las plantillas con las que trabajamos, limpias y en Times New Roman, con el rótulo ALF_BIM de A0 a A3. Funcionan con o sin nuestros programas.</p>
    </div>
    <div class="cgrid tplgrid">{tcards}</div>
    <p class="fine">Descomprime el ZIP y abre el archivo .rte desde Revit (Nuevo → Proyecto → Examinar). Para usarla siempre, agrégala en Revit → Opciones → Ubicaciones de archivos.</p>
  </div>
</section>
"""

    confianza = """<section class="block" aria-labelledby="t-conf">
  <div class="wrap">
    <div class="sec-head"><h2 id="t-conf">Hecho por ingenieros, para ingenieros</h2>
      <p class="lede">ALF_BIM nace en Chota, Cajamarca, de la experiencia en obra y en modelado BIM. Hacemos las herramientas que nos hubiera gustado tener.</p></div>
    <div class="trust">%s</div>
  </div>
</section>
""" % "".join('<div>%s<b>%s</b><p>%s</p></div>' % c for c in CONFIANZA)

    con = CFG["contacto"]
    contacto = f"""<section class="block" id="contacto">
  <div class="wrap">
    <div class="endcta">
      <div>
        <h2>¿Tienes una consulta o una idea?</h2>
        <p>Escríbenos por WhatsApp al {con['whatsapp_txt']} o al correo {con['correo']}. Respondemos el mismo día hábil.</p>
      </div>
      <div class="endcta-side">
        <a class="btn btn-primary" href="{E(wa('Hola ALF_BIM, quiero hacer una consulta.'))}" target="_blank" rel="noopener">Escribir por WhatsApp</a>
        <a class="btn btn-ghost" href="mailto:{con['correo']}">Enviar un correo</a>
      </div>
    </div>
  </div>
</section>
"""

    script = """<script>
(function(){
  var bs=[].slice.call(document.querySelectorAll('.cat-tabs button'));
  var lines=[].slice.call(document.querySelectorAll('#productos .cat-line'));
  function aplicar(f){
    bs.forEach(function(b){b.setAttribute('aria-pressed',b.dataset.f===f)});
    lines.forEach(function(l){l.hidden=!(f==='todos'||l.dataset.linea===f)});
  }
  bs.forEach(function(b){b.addEventListener('click',function(){aplicar(b.dataset.f)})});
  [].slice.call(document.querySelectorAll('.line-card[data-ir]')).forEach(function(a){
    if(a.getAttribute('href').charAt(0)==='#')a.addEventListener('click',function(){aplicar(a.dataset.ir)});
  });
})();
</script>"""

    desc = ("ALF_BIM: software para la ingeniería civil. Programas para Revit, el expediente técnico y la obra: acero, metrados, ETABS, "
            "memoria E.030, instalaciones sanitarias y eléctricas, presupuesto 5D, cronograma, valorizaciones y plazos. Desde S/ 25 al mes.")
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="description" content="{E(desc)}">
<meta name="theme-color" content="#000000">
<meta property="og:type" content="website">
<meta property="og:site_name" content="ALF_BIM">
<meta property="og:title" content="ALF_BIM · Software para la ingeniería civil">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="https://www.alfbim.com/">
<meta property="og:image" content="https://www.alfbim.com/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="https://www.alfbim.com/">
{favicon}
<title>ALF_BIM · Software para la ingeniería civil</title>
{CH.HEAD}
</head>
<body>
<a class="skip" href="#inicio">Saltar al contenido</a>
{CH.header(CFG, "")}
<main id="inicio">
{hero}
{productos}
{plantilla}
{confianza}
{contacto}
</main>
{CH.footer(CFG, g['social_html']())}
{script}
</body>
</html>
"""
