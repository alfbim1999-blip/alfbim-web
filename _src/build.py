#!/usr/bin/env python3
"""Generador de www.alfbim.com.

Uso:  python3 _src/build.py

- Lee _src/config.json (precios, contacto, redes, instaladores).
- Genera las páginas de producto descritas en _src/paginas/*.py con el diseño de _src/base_producto.html.
- Genera index.html (catálogo por especialidad) desde _src/base_index.html.
- Actualiza en las páginas hechas a mano (aceroalf, presupuestoalf, ...) los bloques de precios y descarga.
"""
import math, html, json, re, importlib.util, pathlib, urllib.parse

RAIZ = pathlib.Path(__file__).resolve().parent.parent
SRC = RAIZ / "_src"
CFG = json.loads((SRC / "config.json").read_text(encoding="utf-8"))
P = CFG["productos"]
E = html.escape

# ---------------------------------------------------------------- utilidades
def wa(msg):
    return "https://wa.me/%s?text=%s" % (CFG["contacto"]["whatsapp"], urllib.parse.quote(msg, safe=""))

def soles(x):
    return ("S/ %d" % x) if float(x).is_integer() else ("S/ %.2f" % x)

def usd(x):
    return "≈ US$ %.2f" % (x / CFG["tipo_cambio"])

def mb(b):
    if b < 1024 * 1024:
        return "%d KB" % round(b / 1024)
    return "%.1f MB" % (b / 1048576) if b < 10 * 1048576 else "%d MB" % round(b / 1048576)

def nombre_html(pid):
    """AceroALF -> Acero<em>ALF</em> (para el estilo de marca)."""
    n = P[pid]["nombre"]
    if P[pid].get("marca"):
        return E(n) + ' <em>' + E(P[pid]["marca"]) + '</em>'
    if n.endswith("ALF"):
        return E(n[:-3]) + "<em>ALF</em>"
    return E(n)

def url_descarga(pid):
    ins = P[pid]["instalador"]
    if ins["archivo"].lower().endswith(".exe") and CFG.get("descargas_base_github"):
        return CFG["descargas_base_github"] + ins["archivo"]
    return CFG["descargas_base"] + ins["archivo"]

def pagina(pid):
    return pid + ".html"

ICON = {
    "down": '<path d="M12 4v11M7.5 10.5 12 15l4.5-4.5M5 19h14"/>',
    "table": '<rect x="4" y="4" width="16" height="16" rx="2"/><path d="M4 9h16M4 14h16M9 9v11"/>',
    "cube": '<path d="M12 3 4 7.5v9L12 21l8-4.5v-9L12 3Z"/><path d="M4 7.5 12 12l8-4.5M12 12v9"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "doc": '<path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5M10 13h6M10 17h6"/>',
    "drop": '<path d="M12 3s6 6.4 6 11a6 6 0 0 1-12 0c0-4.6 6-11 6-11Z"/>',
    "bolt": '<path d="M13 3 5 14h6l-1 7 8-11h-6l1-7Z"/>',
    "cal": '<rect x="4" y="5" width="16" height="15" rx="2"/><path d="M4 10h16M9 3v4M15 3v4"/>',
    "bell": '<path d="M6 16V11a6 6 0 1 1 12 0v5l2 2H4l2-2Z"/><path d="M10 20a2 2 0 0 0 4 0"/>',
    "layers": '<path d="m12 3 9 5-9 5-9-5 9-5Z"/><path d="m3 13 9 5 9-5"/>',
    "pump": '<circle cx="12" cy="12" r="7"/><path d="M12 5v7l4 3"/>',
    "gift": '<rect x="4" y="9" width="16" height="11" rx="1"/><path d="M4 13h16M12 9v11M12 9S10 4 7.5 5.5 9 9 12 9Zm0 0s2-5 4.5-3.5S15 9 12 9Z"/>',
}
def svg(name, size=24):
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" '
            'stroke-linejoin="round" aria-hidden="true">%s</svg>' % ICON[name])

ARROW_DOWN = '<span class="ic" aria-hidden="true"><svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M8 3v9M4.5 8.5 8 12l3.5-3.5"/></svg></span>'
ARROW_OUT = '<span class="ic" aria-hidden="true"><svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 11 11 5M6 5h5v5"/></svg></span>'

# ---------------------------------------------------------------- bloques de contenido
def sec_head(eyebrow, h2, lede=""):
    s = '<div class="sec-head"><p class="eyebrow">%s</p><h2>%s</h2>' % (eyebrow, h2)
    if lede:
        s += '<p class="lede">%s</p>' % lede
    return s + "</div>"

def outs(items, cls="outs"):
    h = '<div class="%s">' % cls
    for it in items:
        code, h3, p = it[0], it[1], it[2]
        lis = it[3] if len(it) > 3 else []
        extra = it[4] if len(it) > 4 else ""
        h += '<div class="out%s"><span class="code">%s</span><h3>%s</h3><p>%s</p>' % (extra, code, h3, p)
        if lis:
            h += "<ul>" + "".join("<li>%s</li>" % li for li in lis) + "</ul>"
        h += "</div>"
    return h + "</div>"

def shots(items, cls="shots shots-ui", style=""):
    h = '<div class="%s"%s>' % (cls, (' style="%s"' % style) if style else "")
    for it in items:
        src, w, hh, alt, cap = it[:5]
        st = ' style="grid-column:1/-1"' if len(it) > 5 and it[5] == "wide" else ""
        h += ('<figure class="shot"%s><img src="%s" width="%d" height="%d" loading="lazy" alt="%s">'
              '<figcaption>%s</figcaption></figure>') % (st, src, w, hh, E(alt), cap)
    return h + "</div>"

def steps(items):
    return '<div class="steps">' + "".join('<div class="step"><h3>%s</h3><p>%s</p></div>' % s for s in items) + "</div>"

def faq(items):
    return '<div class="faq">' + "".join("<details><summary>%s</summary><p>%s</p></details>" % q for q in items) + "</div>"

def section(inner, id_="", first=False):
    st = 'padding-top:clamp(3rem,6vw,5rem)' if first else 'padding-top:0'
    return '<section class="block"%s style="%s"><div class="wrap">%s</div></section>' % (
        (' id="%s"' % id_) if id_ else "", st, inner)

# ---------------------------------------------------------------- precios
def precios_html(pid):
    p = P[pid]
    pr = p.get("precio")
    if not pr:
        return ""
    nom = p["nombre"]
    lic = "licencia por PC"
    planes = []
    if p["tipo"] == "revit":
        m = pr["mensual"]
        planes.append(dict(n="Mensual", amt=soles(m), per="/ mes", ps=usd(m) + " al mes",
                           promo="Primer mes a %s" % soles(-(-m // 2)), feat=False,
                           li=["Todas las funciones de " + nom, "1 PC", "Soporte por correo en 48 h", "Actualizaciones incluidas"],
                           msg="la licencia mensual"))
        planes.append(dict(n="3 meses", amt=soles(pr["m3"]), per="por 3 meses", ps="Equivale a %s al mes" % soles(round(pr["m3"] / 3, 2)),
                           promo="Ahorras %d %%" % round(100 - pr["m3"] / (3 * m) * 100), feat=False,
                           li=["Todas las funciones de " + nom, "1 PC", "1 cambio de PC al año", "Actualizaciones incluidas"],
                           msg="la licencia de 3 meses"))
        planes.append(dict(n="6 meses", amt=soles(pr["m6"]), per="por 6 meses", ps="Equivale a %s al mes" % soles(round(pr["m6"] / 6, 2)),
                           promo="Ahorras %d %%" % round(100 - pr["m6"] / (6 * m) * 100), feat=True,
                           li=["Todas las funciones de " + nom, "1 PC", "1 cambio de PC al año", "Soporte por WhatsApp"],
                           msg="la licencia de 6 meses"))
        intro = "Prueba gratis 14 días con todas las funciones. Luego eliges el periodo; todos los planes tienen el programa completo."
    else:
        m, a = pr["mensual"], pr["anual"]
        planes.append(dict(n="Gratis", amt="S/ 0", per="para siempre", ps="Todas las funciones", promo="Las salidas llevan «VERSIÓN DE EVALUACIÓN»",
                           feat=False, li=["Cálculo completo en pantalla", "Ejemplos incluidos", "Sin fecha de vencimiento"], msg=None))
        planes.append(dict(n="Mensual", amt=soles(m), per="/ mes", ps=usd(m) + " al mes", promo="Primer mes a %s" % soles(-(-m // 2)),
                           feat=False, li=["Salidas sin marca de agua", "1 PC", "Soporte por correo en 48 h", "Actualizaciones incluidas"],
                           msg="la licencia mensual"))
        planes.append(dict(n="Anual", amt=soles(a), per="/ año", ps="Equivale a %s al mes" % soles(round(a / 12, 2)),
                           promo="Ahorras %d %% frente al mensual" % round(100 - a / (12 * m) * 100), feat=True,
                           li=["Salidas sin marca de agua", "1 PC · 1 cambio de PC al año", "Soporte por WhatsApp", "Actualizaciones incluidas"],
                           msg="la licencia anual"))
        intro = "Descárgalo gratis y usa todas las funciones. Con la licencia, la memoria, el PDF y el Excel salen sin marca de agua."
    h = ['<section class="block pricing" id="precios" style="padding-top:0"><div class="wrap">',
         sec_head("Precios de lanzamiento", "Todas las funciones en todos los planes", intro + " Pagas con " + CFG["pagos"] + "."),
         '<div class="plans">']
    for pl in planes:
        h.append('<article class="plan%s">' % (" feat" if pl["feat"] else ""))
        if pl["feat"]:
            h.append('<span class="ribbon">Recomendado</span>')
        h.append('<span class="pn">%s</span>' % pl["n"])
        h.append('<div class="price"><span class="amt mono">%s</span><span class="per">%s</span></div>' % (pl["amt"], pl["per"]))
        h.append('<p class="ps">%s</p><p class="promo">%s</p>' % (pl["ps"], pl["promo"]))
        h.append("<ul>" + "".join("<li>%s</li>" % x for x in pl["li"]) + "</ul>")
        if pl["msg"]:
            cls = "btn btn-primary" if pl["feat"] else "btn btn-ghost"
            h.append('<a class="%s" href="%s" target="_blank" rel="noopener">Comprar por WhatsApp%s</a>' % (
                cls, E(wa("Hola ALF_BIM, quiero %s de %s." % (pl["msg"], nom))), ARROW_OUT if pl["feat"] else ""))
        else:
            h.append('<a class="btn btn-ghost" href="#descargar">Descargar gratis</a>')
        h.append("</article>")
    h.append("</div>")
    h.append(packs_html(pid))
    h.append('<p class="fine">Precios en soles; los montos en dólares son referenciales (S/ %.2f por dólar). La licencia es por computadora: '
             'para activarla nos envías el ID de equipo que muestra el programa y te mandamos la clave apenas se acredite el pago. '
             'Revisa la <a href="reembolsos.html">política de reembolso</a> y los <a href="terminos.html">términos y condiciones</a>.</p>' % CFG["tipo_cambio"])
    h.append("</div></section>")
    return "".join(h)

def packs_html(pid=None):
    items = []
    for k, pk in CFG["packs"].items():
        inc = pk["incluye"]
        if pid and inc != ["*"] and pid not in inc:
            continue
        if inc == ["*"]:
            ids = [i for i, x in P.items() if x.get("precio") or (x["estado"] == "proximamente")]
        else:
            ids = inc
        separado = sum(P[i]["precio"].get("anual") or round(P[i]["precio"]["m6"] * 2) for i in ids if P[i].get("precio"))
        nombres = " · ".join(P[i]["nombre"] for i in ids if P[i].get("precio"))
        items.append(
            '<div class="pack"><div><span class="code">%s</span><h3>%s</h3><div class="pack-price"><b>%s</b><small>/ año</small></div>'
            '<p>%s</p><p class="pack-inc">%s</p></div>'
            '<div class="pack-side"><span class="pack-save">Por separado: %s al año</span>'
            '<a class="btn btn-primary" href="%s" target="_blank" rel="noopener">Quiero el %s%s</a></div></div>' % (
                "PACK", E(pk["nombre"]), soles(pk["anual"]), E(pk["nota"]), E(nombres), soles(separado),
                E(wa("Hola ALF_BIM, quiero el %s (%s al año)." % (pk["nombre"], soles(pk["anual"])))), E(pk["nombre"]), ARROW_OUT))
    if not items:
        return ""
    return '<div class="packs">' + "".join(items) + "</div>"

# ---------------------------------------------------------------- descarga
def descarga_html(pid, titulo, texto, extra_btns=""):
    p = P[pid]
    ins = p["instalador"]
    gratis = p["estado"] == "gratis"
    sha = ('<p class="sha">Versión <span class="ver">%s</span> · <span class="tam">%s</span>%s</p>' % (
        ins["version"], mb(ins["bytes"]), (' · SHA-256 <code id="sha">%s</code>' % ins["sha"]) if ins.get("sha") else ""))
    btns = ['<a class="btn" id="dlBtn" href="%s" download>%s%s</a>' % (
        url_descarga(pid), "Descargar instalador" if ins["archivo"].endswith(".exe") else "Descargar Excel", ARROW_DOWN)]
    if p.get("manual"):
        btns.append('<a class="btn btn-ghost" href="%s" target="_blank" rel="noopener">Manual en PDF</a>' % p["manual"])
    btns.append(extra_btns)
    if not gratis:
        btns.append('<a class="btn btn-ghost" href="#precios">Ver precios</a>')
    else:
        btns.append('<a class="btn btn-ghost" href="%s" target="_blank" rel="noopener">Consultas por WhatsApp</a>' % E(
            wa("Hola ALF_BIM, tengo una consulta sobre %s." % p["nombre"])))
    return ('<section class="block" id="descargar" style="padding-top:0"><div class="wrap"><div class="endcta"><div>'
            '<h2>%s</h2><p>%s</p>%s</div><div class="endcta-side">%s</div></div></div></section>') % (
        titulo, texto, sha, "".join(b for b in btns if b))

# ---------------------------------------------------------------- base de página
BASE = (SRC / "base_producto.html").read_text(encoding="utf-8")
EXTRA_CSS = (SRC / "extra.css").read_text(encoding="utf-8")

def _between(s, a, b, start=0):
    i = s.index(a, start)
    j = s.index(b, i + len(a))
    return s[i:j + len(b)]

FAVICON = re.search(r'<link rel="icon"[^>]+>', BASE).group(0)
STYLES = BASE[BASE.index("<style>"):BASE.rindex("</style>") + len("</style>")]
FOOT_BRAND = re.search(r'<div class="cell"><a class="brand".*?</div>', BASE, re.S).group(0)
FOOT_LEGAL = re.search(r'<nav class="legal".*?</nav>', BASE, re.S).group(0)
FOOT_SOCIAL = re.search(r'<div class="social" data-social>.*?</div>', BASE, re.S).group(0)

def social_html():
    """Íconos de redes ya resueltos con config.json (los vacíos se quitan)."""
    s = FOOT_SOCIAL
    for net, url in CFG["redes"].items():
        pat = r'<a data-net="%s"([^>]*)>(.*?)</a>' % net
        if url:
            s = re.sub(pat, lambda m: '<a data-net="%s" href="%s"%s>%s</a>' % (net, E(url), m.group(1), m.group(2)), s, flags=re.S)
        else:
            s = re.sub(pat, "", s, flags=re.S)
    return s

SCRIPT = """<script>
const mb=document.getElementById('menuBtn'),ln=document.getElementById('links');
mb.addEventListener('click',()=>{const o=ln.classList.toggle('open');mb.setAttribute('aria-expanded',o)});
ln.addEventListener('click',e=>{if(e.target.closest('a')){ln.classList.remove('open');mb.setAttribute('aria-expanded',false)}});
(function(){var top=document.querySelector('header.top');var f=function(){top&&top.classList.toggle('scrolled',window.scrollY>40)};window.addEventListener('scroll',f,{passive:true});f();})();
</script>"""

def shell(pg, main_html):
    pid = pg["id"]
    p = P[pid]
    nav = "".join('<a href="%s">%s</a>' % n for n in pg["nav"])
    url = "https://www.alfbim.com/" + pid
    head = f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="description" content="{E(pg['desc'])}">
<meta name="theme-color" content="#0A2457">
<meta property="og:type" content="website">
<meta property="og:site_name" content="ALF_BIM">
<meta property="og:title" content="{E(pg['og_title'])}">
<meta property="og:description" content="{E(pg['desc'])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="https://www.alfbim.com/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="{url}">
{FAVICON}
<title>{E(pg['title'])}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Geist:wght@300..800&family=Geist+Mono:wght@400..600&display=swap">
{STYLES}
<style>
{EXTRA_CSS}
</style>
{pg.get('jsonld','')}
</head>
<body>
<a class="skip" href="#inicio">Saltar al contenido</a>
<header class="top">
  <div class="wrap nav">
    <a class="brand" href="index.html" aria-label="ALF_BIM, inicio"><b>ALF<span>_</span>BIM</b></a>
    <button class="menu-btn" id="menuBtn" aria-expanded="false" aria-controls="links">Menú</button>
    <nav class="links" id="links">
      <a href="index.html#productos">Productos</a>{nav}
      <a class="btn btn-primary" href="#descargar">Descargar</a>
    </nav>
  </div>
</header>
<main id="inicio">
{main_html}
</main>
"""
    neg, con = CFG["negocio"], CFG["contacto"]
    foot = f"""<footer>
  <div class="wrap">
    <div class="rotulo">
      {FOOT_BRAND}
      <div class="cell"><small>Producto</small><b>{E(p['nombre'] + (' ' + p['marca'] if p.get('marca') else ''))}</b></div>
      <div class="cell"><small>Creador</small><b>Ing. Anderson Irigoín C.</b></div>
      <div class="cell"><small>Plataforma</small><b>{E(pg['plataforma'])}</b></div>
      <div class="cell"><small>Lámina</small><b class="mono">{p.get('lamina','WEB')}</b></div>
    </div>
    <div class="copy">
      <span>© 2026 ALF_BIM · Titular: {neg['titular']} · RUC {neg['ruc']} · {neg['lugar']}</span>
      <span>WhatsApp {con['whatsapp_txt']} · {con['correo']}</span>
    </div>
    {FOOT_LEGAL}
    {social_html()}
    <p class="tm">{pg['tm']}</p>
  </div>
</footer>
{SCRIPT}
</body>
</html>
"""
    return head + foot

def hero(pg):
    h = pg["hero"]
    meta = "".join("<span>%s</span>" % m for m in h["meta"])
    img = h["img"]
    legend = ""
    if img.get("legend"):
        legend = '<div class="legend">' + "".join(
            '<span><i class="sw %s"></i>%s</span>' % (("sw-l", "sw-s")[i % 2], t) for i, t in enumerate(img["legend"])) + "</div>"
    p = P[pg["id"]]
    cta1 = h.get("cta1") or ("Descargar y probar 14 días" if p["tipo"] == "revit" and p["estado"] == "disponible" else "Descargar gratis")
    return f"""  <section class="hero">
    <div class="wrap hero-grid">
      <div>
        <p class="crumb"><a href="index.html">ALF_BIM</a> / <b>{h['crumb']}</b></p>
        <h1>{h['h1']} <em>{h['h1em']}</em></h1>
        <p class="lede">{h['lede']}</p>
        <div class="cta">
          <a class="btn btn-primary" href="#descargar">{cta1}{ARROW_DOWN}</a>
          <a class="btn btn-ghost" href="{h['cta2'][0]}">{h['cta2'][1]}</a>
        </div>
        <p class="trial">{h['trial']}</p>
        <div class="hero-meta">{meta}</div>
      </div>
      <figure class="sheet" style="margin:0">
        <div class="sheet-head"><span><b>{E(p['nombre'])}</b></span><span>{img['cap']}</span></div>
        <img class="shot-hero" src="{img['src']}" width="{img['w']}" height="{img['h']}" alt="{E(img['alt'])}" fetchpriority="high">
        {legend}
      </figure>
    </div>
  </section>
"""

def tiles(items):
    return ('  <div class="tiles"><div class="wrap">' + "".join(
        '<a class="tile" href="%s">%s<span><b>%s</b><small>%s</small></span></a>' % (href, svg(ic), b, s)
        for href, ic, b, s in items) + "</div></div>\n")

def construir_pagina(pg):
    pid = pg["id"]
    partes = [hero(pg), tiles(pg["tiles"])]
    partes += pg["secciones"]
    if P[pid].get("precio"):
        partes.append(precios_html(pid))
    partes.append(section(sec_head("Preguntas frecuentes", "Antes de instalar") + faq(pg["faq"]), "preguntas"))
    partes.append(descarga_html(pid, pg["dl_titulo"], pg["dl_texto"], pg.get("dl_extra", "")))
    return shell(pg, "\n".join(partes))

# ---------------------------------------------------------------- páginas hechas a mano
MARK_A, MARK_B = "<!--ALF:precios-->", "<!--/ALF:precios-->"

def actualizar_existente(fname, pid):
    f = RAIZ / fname
    s = f.read_text(encoding="utf-8")
    p = P[pid]
    # 1) bloque de precios (no en AceroALF, que tiene su propia tabla)
    if pid != "aceroalf":
        bloque = MARK_A + precios_html(pid) + MARK_B
        if MARK_A in s:
            s = re.sub(re.escape(MARK_A) + ".*?" + re.escape(MARK_B), lambda m: bloque, s, flags=re.S)
        else:
            i = s.index('<section class="block" id="preguntas"')
            s = s[:i] + bloque + "\n\n  " + s[i:]
            s = s.replace('<a href="#preguntas">Preguntas</a>', '<a href="#precios">Precios</a>\n      <a href="#preguntas">Preguntas</a>', 1)
        if "<style>/*ALF:extra*/" not in s:
            s = s.replace("</head>", "<style>/*ALF:extra*/\n" + EXTRA_CSS + "\n</style>\n</head>", 1)
        else:
            s = re.sub(r"<style>/\*ALF:extra\*/.*?</style>", lambda m: "<style>/*ALF:extra*/\n" + EXTRA_CSS + "\n</style>", s, flags=re.S)
    # 2) enlace de descarga, versión, tamaño y huella
    ins = p["instalador"]
    s = re.sub(r'(<a class="btn[^"]*" id="dlBtn" href=")[^"]*(")', lambda m: m.group(1) + url_descarga(pid) + m.group(2), s)
    s = re.sub(r'href="descargas/' + re.escape(ins["archivo"]) + '"', 'href="%s"' % url_descarga(pid), s)
    s = re.sub(r'(<code id="sha">)[^<]*(</code>)', lambda m: m.group(1) + ins["sha"] + m.group(2), s)
    s = re.sub(r'(<span class="tam">)[^<]*(</span>)', lambda m: m.group(1) + mb(ins["bytes"]) + m.group(2), s)
    s = re.sub(r'(<dd class="hash">)[^<]*(</dd>)', lambda m: m.group(1) + ins["sha"].lower() + m.group(2), s)
    # 3) el instalador ya no se toma de INSTALADOR_URL (lo resuelve config.json)
    s = s.replace('const INSTALADOR_URL = "";', 'const INSTALADOR_URL = ""; // el enlace lo pone _src/build.py desde _src/config.json')
    f.write_text(s, encoding="utf-8")

# ---------------------------------------------------------------- portada
def construir_index():
    spec = importlib.util.spec_from_file_location("idx", SRC / "index_contenido.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.construir(globals())

# ---------------------------------------------------------------- principal
def main():
    hechas = []
    for f in sorted((SRC / "paginas").glob("*.py")):
        spec = importlib.util.spec_from_file_location(f.stem, f)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        pg = mod.pagina(globals())
        (RAIZ / (pg["id"] + ".html")).write_text(construir_pagina(pg), encoding="utf-8")
        hechas.append(pg["id"])
    for pid in ["aceroalf", "presupuestoalf", "cronogramaalf", "informemensualalf", "saneamientoruralalf"]:
        actualizar_existente(pid + ".html", pid)
    if (SRC / "index_contenido.py").exists():
        (RAIZ / "index.html").write_text(construir_index(), encoding="utf-8")
    print("Generadas:", ", ".join(hechas) or "-")
    print("Actualizadas: aceroalf, presupuestoalf, cronogramaalf, informemensualalf, saneamientoruralalf, index")

if __name__ == "__main__":
    main()
