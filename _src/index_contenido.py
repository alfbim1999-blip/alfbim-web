"""Portada de www.alfbim.com (diseño de oct-2026, inspirado en autodesk.com).

Portada negra con AceroALF y su visor 3D, «Explora por especialidad», producto destacado,
catálogo de los próximos programas, plantilla gratis, confianza y contacto.
Los datos salen de _src/config.json: un programa con estado «disponible» aparece como destacado.
"""
import re, html

E = html.escape

MOTIVOS = {
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
     "Pruébalo antes de pagar", "AceroALF trae 14 días de prueba con todas las funciones, sin tarjeta."),
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

    disp = [k for k, p in P.items() if p["estado"] == "disponible"]
    prox = [k for k, p in P.items() if p["estado"] == "proximamente"]
    acero = P["aceroalf"]

    def icono(pid, size=44):
        f = RAIZ / "img" / "iconos" / (pid + ".png")
        if f.exists():
            return '<img src="img/iconos/%s.png" width="%d" height="%d" alt="" loading="lazy">' % (pid, size, size)
        ic = {"estructuras": "layers", "sanitarias": "drop", "electricas": "bolt", "obra": "cal"}[P[pid]["linea"]]
        if P[pid]["tipo"] == "excel":
            ic = "table"
        return '<span class="ph">%s</span>' % svg(ic)

    def plataforma(p):
        return {"revit": "Revit", "escritorio": "Windows", "excel": "Excel"}[p["tipo"]]

    # ---------- portada
    hero = f"""<section class="home-hero">
  <div class="wrap home-grid">
    <div>
      <h1>Software para la ingeniería civil peruana</h1>
      <p class="lede">Programas para Revit, el expediente técnico y la obra, hechos con la norma peruana. Empezamos con AceroALF: el acero de refuerzo de tu modelo con sus vistas, láminas y metrados.</p>
      <div class="cta">
        <a class="btn btn-primary" href="aceroalf.html">Conocer AceroALF</a>
        <a class="btn btn-ghost" href="#productos">Ver todos los programas</a>
      </div>
    </div>
    <figure class="feature-card" style="margin:0">
      <div class="stage"><canvas id="rebar3d" role="img" aria-label="Vista 3D del acero de una zapata, una columna y dos vigas modelados con AceroALF."></canvas><span class="hint">Arrastra para girar</span></div>
      <div class="fc-body">
        <div class="fc-name"><img src="img/iconos/aceroalf.png" alt="" width="40" height="40"><div><b>AceroALF</b><small>Acero de refuerzo en Revit, desde {soles(acero['precio']['mensual'])} al mes</small></div></div>
        <a class="btn btn-primary" href="aceroalf.html#descargar">Probar 14 días gratis</a>
      </div>
    </figure>
  </div>
</section>
"""

    # ---------- explora por especialidad
    tarjetas = []
    for ln in CFG["lineas"]:
        ids = [k for k, p in P.items() if p["linea"] == ln["id"]]
        live = [k for k in ids if P[k]["estado"] == "disponible"]
        if live:
            st, cls, sub = "Disponible", "st live", " y ".join(P[k]["nombre"] for k in live) + " ya está disponible"
            href = "aceroalf.html" if "aceroalf" in live else "#linea-" + ln["id"]
        else:
            st, cls, sub = "Próximamente", "st", "%d programas en camino" % len(ids)
            href = "#linea-" + ln["id"]
        tarjetas.append('<a class="line-card" href="%s" data-ir="%s"><span class="%s">%s</span>%s<span><b>%s</b><small>%s</small></span></a>' % (
            href, ln["id"], cls, st, MOTIVOS[ln["id"]], E(ln["nombre"]), E(sub)))
    lineas = """<section class="lines" aria-labelledby="t-esp">
  <div class="wrap">
    <h2 id="t-esp">Explora por especialidad</h2>
    <div class="lines-grid">%s</div>
  </div>
</section>
""" % "".join(tarjetas)

    # ---------- producto destacado
    destacado = f"""<article class="featured">
        <div class="f-media">
          <img src="img/salidas/grupos.jpg" width="800" height="360" alt="Modelo 3D de Revit con el acero de zapatas, columnas, vigas, placas y escalera colocado por AceroALF.">
          <img src="img/salidas/laminas.jpg" width="760" height="470" alt="Sección de una columna en T generada por AceroALF: 8 barras de 3/4 de pulgada y 2 de 5/8, con sus cotas." loading="lazy">
          <img src="img/salidas/cuadro.jpg" width="800" height="360" alt="Cuadro de columnas por nivel generado por AceroALF a partir del acero modelado." loading="lazy">
        </div>
        <div class="f-body">
          <p class="badge"><img src="img/iconos/aceroalf.png" alt="" width="36" height="36">AceroALF</p>
          <h3>El acero de tu modelo de Revit, listo para el plano</h3>
          <p>Seleccionas el elemento, revisas el armado en su ventana y aplicas. Las barras quedan como armadura nativa de Revit, con sus vistas, la lámina y la planilla de metrados.</p>
          <ul><li>Zapatas y columnas</li><li>Vigas continuas</li><li>Placas y muros</li><li>Escaleras</li><li>Losas en una y dos direcciones</li><li>Planilla y láminas</li></ul>
          <p class="price-line">Desde <b>{soles(acero['precio']['mensual'])}</b> al mes. Primer mes a {soles(-(-acero['precio']['mensual'] // 2))}.</p>
          <div class="cta"><a class="btn btn-primary" href="aceroalf.html#descargar">Probar 14 días gratis</a><a class="btn btn-ghost" href="aceroalf.html">Ver AceroALF</a></div>
        </div>
      </article>"""

    # ---------- próximos programas
    tabs = ['<button type="button" data-f="todos" aria-pressed="true">Todos <small>%d</small></button>' % len(prox)]
    grupos = []
    for ln in CFG["lineas"]:
        ids = [k for k in prox if P[k]["linea"] == ln["id"]]
        if not ids:
            continue
        tabs.append('<button type="button" data-f="%s" aria-pressed="false">%s <small>%d</small></button>' % (ln["id"], E(ln["nombre"]), len(ids)))
        cards = "".join(
            '<div class="ccard ccard-soon" data-linea="%s"><div class="ccard-top">%s<div><span class="ctag soon">Próximamente</span><h4>%s</h4></div></div>'
            '<p>%s</p><a class="btn btn-ghost" href="%s" target="_blank" rel="noopener">Avísame cuando salga</a></div>' % (
                ln["id"], icono(k), E(P[k]["nombre"] + (" " + P[k]["marca"] if P[k].get("marca") else "")), E(P[k]["resumen"]),
                E(wa("Hola ALF_BIM, avísame cuando salga %s." % P[k]["nombre"])))
            for k in ids)
        grupos.append('<div class="cat-line" id="linea-%s" data-linea="%s"><div class="cat-line-head"><h3>%s</h3><p>%s</p></div><div class="cgrid">%s</div></div>' % (
            ln["id"], ln["id"], E(ln["nombre"]), E(ln["desc"]), cards))

    productos = f"""<section class="block" id="productos">
  <div class="wrap">
    <div class="sec-head">
      <h2>Productos</h2>
      <p class="lede">Cada programa resuelve una parte del expediente o de la obra. AceroALF ya está disponible; los demás los estamos validando con proyectos reales antes de publicarlos.</p>
    </div>
    {destacado}
  </div>
</section>

<section class="block tone-stone" id="proximos" aria-labelledby="t-prox">
  <div class="wrap">
    <div class="sec-head">
      <h2 id="t-prox">Lo que viene</h2>
      <p class="lede">{len(prox)} programas para estructuras, instalaciones y gestión de obra. Escríbenos por WhatsApp y te avisamos cuando salga el que necesitas.</p>
    </div>
    <div class="cat-tabs" role="group" aria-label="Filtrar por especialidad">{''.join(tabs)}</div>
    {''.join(grupos)}
  </div>
</section>
"""

    # ---------- plantilla gratis (contenido de la portada anterior)
    m = re.search(r'<section class="block" id="plantilla".*?</section>', base, re.S)
    plantilla = re.sub(r'\s*style="padding-top:0"', "", m.group(0)) if m else ""

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
  var lines=[].slice.call(document.querySelectorAll('#proximos .cat-line'));
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

    desc = ("ALF_BIM: software para la ingeniería civil peruana. AceroALF arma el acero de refuerzo en Revit con sus vistas, láminas y metrados. "
            "Pronto: metrados, instalaciones sanitarias y eléctricas, presupuesto 5D, cronograma y plazos de obra.")
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="description" content="{E(desc)}">
<meta name="theme-color" content="#000000">
<meta property="og:type" content="website">
<meta property="og:site_name" content="ALF_BIM">
<meta property="og:title" content="ALF_BIM · Software para la ingeniería civil peruana">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="https://www.alfbim.com/">
<meta property="og:image" content="https://www.alfbim.com/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="https://www.alfbim.com/">
{favicon}
<title>ALF_BIM · Software para la ingeniería civil peruana</title>
{CH.HEAD}
</head>
<body>
<a class="skip" href="#inicio">Saltar al contenido</a>
{CH.header(CFG, "")}
<main id="inicio">
{hero}
{lineas}
{productos}
{plantilla}
{confianza}
{contacto}
</main>
{CH.footer(CFG, g['social_html']())}
<script src="assets/rebar3d.js" defer></script>
{script}
</body>
</html>
"""
