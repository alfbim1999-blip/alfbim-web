"""Portada de www.alfbim.com: catálogo por especialidad, packs y descargas gratuitas.

Se arma sobre _src/base_index.html (conserva su CSS, la sección de la plantilla de Revit,
Nosotros, Contacto, el pie y los scripts) y reemplaza el encabezado, el hero y el catálogo.
"""
import re, html, pathlib

E = html.escape

def construir(g):
    CFG, P = g["CFG"], g["P"]
    RAIZ = g["RAIZ"]
    base = (g["SRC"] / "base_index.html").read_text(encoding="utf-8")
    svg, wa, soles, nombre_html, packs_html = g["svg"], g["wa"], g["soles"], g["nombre_html"], g["packs_html"]
    ARROW_OUT = g["ARROW_OUT"]

    disp = [k for k, p in P.items() if p["estado"] == "disponible"]
    grat = [k for k, p in P.items() if p["estado"] == "gratis"]
    prox = [k for k, p in P.items() if p["estado"] == "proximamente"]
    total = len(P)

    def icono(pid):
        f = RAIZ / "img" / "iconos" / (pid + ".png")
        if f.exists():
            return '<img src="img/iconos/%s.png" width="44" height="44" alt="" loading="lazy">' % pid
        ic = {"estructuras": "layers", "sanitarias": "drop", "electricas": "bolt", "obra": "cal"}[P[pid]["linea"]]
        if P[pid]["tipo"] == "excel":
            ic = "table"
        return '<span class="ph">%s</span>' % svg(ic)

    def precio_corto(p):
        pr = p.get("precio")
        if p["estado"] == "gratis":
            return "<b>Gratis</b>"
        if not pr:
            return ""
        return "desde <b>%s</b> / mes" % soles(pr["mensual"])

    def plataforma(p):
        return {"revit": "Revit 2023–2027", "escritorio": "Windows 10 / 11", "excel": "Excel, sin macros"}[p["tipo"]]

    def tarjeta(pid):
        p = P[pid]
        est = p["estado"]
        tag = {"disponible": ('<span class="ctag live">Disponible</span>'), "gratis": '<span class="ctag free">Gratis</span>',
               "proximamente": '<span class="ctag soon">Próximamente</span>'}[est]
        top = '<div class="ccard-top">%s<div>%s<h4>%s</h4></div></div>' % (icono(pid), tag, nombre_html(pid))
        attrs = 'data-linea="%s" data-estado="%s"' % (p["linea"], est)
        if est == "proximamente":
            return ('<div class="ccard ccard-soon" %s>%s<p>%s</p><a class="btn btn-ghost" href="%s" target="_blank" rel="noopener">Avísame cuando salga</a></div>' % (
                attrs, top, E(p["resumen"]), E(wa("Hola ALF_BIM, avísame cuando salga %s." % p["nombre"]))))
        return ('<a class="ccard" href="%s.html" %s>%s<p>%s</p><div class="cmeta"><span>%s</span><span>%s</span></div></a>' % (
            pid, attrs, top, E(p["resumen"]), plataforma(p), precio_corto(p)))

    # ---------- hero
    fam = []
    for ln in CFG["lineas"]:
        ids = [k for k, p in P.items() if p["linea"] == ln["id"] and p["estado"] != "proximamente"]
        n_prox = len([k for k, p in P.items() if p["linea"] == ln["id"] and p["estado"] == "proximamente"])
        nombres = " · ".join(P[k]["nombre"] + (" " + P[k]["marca"] if P[k].get("marca") else "") for k in ids)
        cnt = ("%d listos" % len(ids) if len(ids) != 1 else "1 listo") if ids else ""
        if n_prox:
            cnt += (" · " if cnt else "") + "%d en camino" % n_prox
        if not ids:
            nombres = " · ".join(P[k]["nombre"] for k, q in P.items() if q["linea"] == ln["id"])
        fam.append('<a href="#linea-%s" data-ir="%s"><span class="fn">%s</span><b>%s</b><small>%s</small><span class="fc">%s</span></a>' % (
            ln["id"], ln["id"], E(ln["nombre"]), E(ln["corto"]), E(nombres or "Primeros programas en camino"), cnt))
    if grat:
        fam.append('<a class="fam-wide" href="#gratis"><span class="fn">Descargas gratuitas</span><b>%d herramientas gratis para empezar hoy</b>'
                   '<small>PlanosALF, la Plantilla Excel de Estructuras, la Plantilla Excel IIEE y la plantilla de Revit</small></a>' % (len(grat) + 1))
    else:
        fam.append('<a class="fam-wide" href="aceroalf.html"><span class="fn">Disponible hoy</span><b>AceroALF y la plantilla de Revit gratis</b>'
                   '<small>Acero de refuerzo automático en Revit, con prueba gratis de 14 días. El resto de la línea sale en las próximas semanas.</small></a>')

    hero = f"""  <section class="hero">
    <div class="wrap hero-grid">
      <div>
        <p class="crumb"><a href="#nosotros">ALF_BIM</a> <b>Ingeniería civil · BIM</b></p>
        <h1>Software que automatiza <em>la ingeniería civil</em></h1>
        <p class="lede">Programas para Revit, para el expediente técnico y para la obra, hechos con la normativa peruana: estructuras, instalaciones sanitarias y eléctricas, presupuesto, cronograma y plazos. Menos trabajo repetitivo, más tiempo para la ingeniería.</p>
        <div class="cta">
          <a class="btn btn-primary" href="#productos">Ver los programas{ARROW_OUT}</a>
          <a class="btn btn-ghost" href="aceroalf.html">Conocer AceroALF</a>
        </div>
        <div class="hero-meta"><span>{(str(len(disp)) + " programas disponibles") if len(disp) != 1 else "AceroALF disponible"}</span><span>{len(prox)} programas en camino</span><span>Soporte por WhatsApp</span></div>
      </div>
      <div class="fam" aria-label="Líneas de programas de ALF_BIM">
        {''.join(fam)}
      </div>
    </div>
  </section>
"""

    # ---------- catálogo
    tabs = ['<button type="button" data-f="todos" aria-pressed="true">Todos <small>%d</small></button>' % total]
    for ln in CFG["lineas"]:
        n = len([1 for p in P.values() if p["linea"] == ln["id"]])
        tabs.append('<button type="button" data-f="%s" aria-pressed="false">%s <small>%d</small></button>' % (ln["id"], E(ln["nombre"]), n))
    if grat:
        tabs.append('<button type="button" data-f="gratis" aria-pressed="false">Gratis <small>%d</small></button>' % len(grat))
    orden = {"disponible": 0, "gratis": 1, "proximamente": 2}
    lineas = []
    for ln in CFG["lineas"]:
        ids = sorted([k for k, p in P.items() if p["linea"] == ln["id"]], key=lambda k: orden[P[k]["estado"]])
        lineas.append('<div class="cat-line" id="linea-%s" data-linea="%s"><div class="cat-line-head"><h3>%s</h3><p>%s</p></div>'
                      '<div class="cgrid">%s</div></div>' % (ln["id"], ln["id"], E(ln["nombre"]), E(ln["desc"]), "".join(tarjeta(k) for k in ids)))
    catalogo = f"""  <section class="block" id="productos">
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow">Programas</p>
        <h2>Una familia de herramientas ALF</h2>
        <p class="lede">Cada programa resuelve una parte del expediente o de la obra, y se conectan entre sí: los metrados de Revit van al presupuesto, el presupuesto al cronograma y a la valorización, y todo al informe mensual.</p>
      </div>
      <div class="cat-tabs" role="group" aria-label="Filtrar programas">{''.join(tabs)}</div>
      {''.join(lineas)}
    </div>
  </section>

  <section class="block pricing" id="packs" style="padding-top:0">
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow">Packs de lanzamiento</p>
        <h2>Llévalos juntos y paga menos</h2>
        <p class="lede">Cada programa se puede usar gratis o en prueba con todas las funciones. Si trabajas con varios, un pack anual sale bastante más barato que las licencias por separado. Pagas con {CFG['pagos']}.</p>
      </div>
      {packs_html()}
      <p class="fine">Licencia por computadora, válida por 12 meses desde la activación. Precios en soles. Cada programa tiene su propia página con sus precios mensuales y anuales.</p>
    </div>
  </section>
"""

    pausa = CFG.get("pausa", {}).get("activa")
    if pausa:  # en pausa: sin packs (incluyen programas que aún no salen)
        i = catalogo.index('  <section class="block pricing" id="packs"')
        catalogo = catalogo[:i]
    gratis = ['<section class="block" id="gratis" style="padding-top:0"><div class="wrap">',
              '<div class="sec-head"><p class="eyebrow">Descargas gratuitas</p><h2>Empieza sin pagar nada</h2>'
              '<p class="lede">Herramientas completas y gratuitas, sin registro ni fecha de vencimiento.</p></div>',
              '<div class="cgrid">' + "".join(tarjeta(k) for k in grat) +
              '<a class="ccard" href="#plantilla" data-linea="estructuras" data-estado="gratis"><div class="ccard-top"><span class="ph">%s</span><div>'
              '<span class="ctag free">Gratis</span><h4>Plantilla Revit <em>ALF_BIM</em></h4></div></div><p>La plantilla estructural con la que trabajamos: 15 diámetros, '
              'filtros por diámetro, planilla de acero y lámina E-00.</p><div class="cmeta"><span>Revit 2027</span><span><b>Gratis</b></span></div></a>' % svg("cube") +
              "</div></div></section>"]
    if not grat:
        gratis = []

    # ---------- ensamblar sobre la base
    s = base
    s = re.sub(r'<meta name="description" content="[^"]*">',
               '<meta name="description" content="ALF_BIM: programas de automatización para ingeniería civil con normativa peruana. '
               'Acero, metrados y láminas en Revit; instalaciones sanitarias y eléctricas; presupuesto 5D y S10, cronograma, plazos de la Ley 32069 e informe mensual de obra. Descargas gratis.">', s, count=1)
    nav = """<nav class="links" id="links">
      <a href="#productos">Programas</a>
      <a href="#packs">Packs</a>
      <a href="#gratis">Gratis</a>
      <a href="#nosotros">Nosotros</a>
      <a href="#contacto">Contacto</a>
      <a class="btn btn-primary" href="#productos">Ver programas</a>
    </nav>"""
    if pausa:
        nav = """<nav class="links" id="links">
      <a href="#productos">Programas</a>
      <a href="aceroalf.html">AceroALF</a>
      <a href="#plantilla">Plantilla gratis</a>
      <a href="#nosotros">Nosotros</a>
      <a href="#contacto">Contacto</a>
      <a class="btn btn-primary" href="aceroalf.html#descargar">Descargar AceroALF</a>
    </nav>"""
    s = re.sub(r'<nav class="links" id="links">.*?</nav>', lambda m: nav, s, count=1, flags=re.S)
    i0 = s.index('  <section class="hero">')
    i1 = s.index('  <section class="block" id="plantilla"')
    s = s[:i0] + hero + "\n" + catalogo + "\n  " + "".join(gratis) + "\n\n" + s[i1:]
    s = s.replace("Software BIM para ingeniería estructural", "Software para ingeniería civil y gestión de obras")
    prods = " · ".join(P[k]["nombre"] for k in disp)
    s = re.sub(r'(<div class="cell"><small>Productos</small><b>)[^<]*(</b>)', lambda m: m.group(1) + E(prods) + m.group(2), s, count=1)
    s = s.replace("AceroALF es un desarrollo independiente, no afiliado a Autodesk.",
                  "Excel es marca de Microsoft y S10 de S10 Software. Los programas ALF son desarrollos independientes de ALF_BIM, no afiliados a esas empresas.")
    # Nosotros: los programas de escritorio no tienen "prueba", tienen versión gratuita
    s = s.replace("Nuestros productos tienen prueba gratis con todas las funciones.",
                  "Los complementos de Revit traen 14 días de prueba y los programas de escritorio se usan gratis con todas las funciones.")
    css_extra = "<style>/*ALF:extra*/\n" + g["EXTRA_CSS"] + "\n</style>\n</head>"
    s = s.replace("</head>", css_extra, 1)
    tabs_js = """<script>
(function(){
  var bs=[].slice.call(document.querySelectorAll('.cat-tabs button'));
  var lines=[].slice.call(document.querySelectorAll('#productos .cat-line'));
  function aplicar(f){
    bs.forEach(function(b){b.setAttribute('aria-pressed',b.dataset.f===f)});
    lines.forEach(function(l){
      var vis=0;
      [].slice.call(l.querySelectorAll('.ccard')).forEach(function(c){
        var ok=f==='todos'||c.dataset.linea===f||(f==='gratis'&&c.dataset.estado==='gratis');
        c.hidden=!ok; if(ok)vis++;
      });
      l.hidden=!vis;
    });
  }
  bs.forEach(function(b){b.addEventListener('click',function(){aplicar(b.dataset.f)})});
  [].slice.call(document.querySelectorAll('.fam a[data-ir]')).forEach(function(a){a.addEventListener('click',function(){aplicar(a.dataset.ir)})});
})();
</script>
</body>"""
    s = s.replace("</body>", tabs_js, 1)
    # el script de aparición también anima las tarjetas nuevas
    s = s.replace("var sel='.sec-head,.prod,", "var sel='.sec-head,.ccard,.pack,.prod,")
    return s
