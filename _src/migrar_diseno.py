"""Migración única al diseño de oct-2026 (inspirado en autodesk.com): AceroALF y páginas legales.
Uso: python3 _src/migrar_diseno.py   (es idempotente: si la página ya tiene marcadores, solo refresca encabezado y pie)."""
import re, json, pathlib, importlib.util

RAIZ = pathlib.Path(__file__).resolve().parent.parent
SRC = RAIZ / "_src"
spec = importlib.util.spec_from_file_location("chrome", SRC / "chrome.py"); chrome = importlib.util.module_from_spec(spec); spec.loader.exec_module(chrome)
spec = importlib.util.spec_from_file_location("build", SRC / "build.py"); build = importlib.util.module_from_spec(spec); spec.loader.exec_module(build)
CFG = build.CFG
SOCIAL = build.social_html()

PBAR = '''<div class="pbar" id="pbar"><div class="wrap">
  <a class="pname" href="#inicio"><img src="img/iconos/aceroalf.png" alt="" width="30" height="30">AceroALF</a>
  <nav aria-label="Secciones de AceroALF"><a href="#acero">Elementos</a><a href="#entregables">Entregables</a><a href="#tutoriales">Descarga</a><a href="#precios">Precios</a><a href="#preguntas">Preguntas</a></nav>
  <div class="pend"><span class="pprice">Desde <b>S/ 29</b> al mes</span><a class="btn btn-ghost" href="#precios">Ver precios</a><a class="btn btn-primary" href="#descargar">Descargar</a></div>
</div></div>
'''

HERO = '''  <section class="hero">
    <div class="wrap hero-grid">
      <div>
        <p class="crumb"><a href="index.html">Inicio</a><span aria-hidden="true">/</span><a href="index.html#productos">Productos</a><span aria-hidden="true">/</span><b>AceroALF</b></p>
        <p class="badge"><img src="img/iconos/aceroalf.png" alt="" width="36" height="36">AceroALF para Revit</p>
        <h1>Del modelo al plano de acero, en minutos</h1>
        <p class="lede">AceroALF coloca el refuerzo de zapatas, columnas, vigas, placas, escaleras y losas directamente en tu modelo de Revit, y genera las vistas, la lámina y el metrado de acero, concreto y encofrado.</p>
        <p class="price-line">Desde <b>S/ 29</b> al mes. El primer mes cuesta S/ 15.</p>
        <div class="cta">
          <a class="btn btn-primary" href="#descargar">Descargar y probar 14 días</a>
          <a class="btn btn-ghost" href="#precios">Ver precios</a>
        </div>
        <div class="hero-meta"><span>Revit 2023 a 2027</span><span>Español e inglés</span><span>Configurable por país</span></div>
      </div>
      <figure class="sheet">
        <div class="sheet-head"><span><b>Vista 3D de la armadura</b></span><span>Zapata Z-1, columna C-1 y vigas V-101 y V-102</span></div>
        <div class="stage"><canvas id="rebar3d" role="img" aria-label="Vista 3D del acero de una zapata, una columna y dos vigas que llegan a ella, con el concreto transparente: barras longitudinales, estribos de confinamiento y la malla de la zapata."></canvas><span class="hint">Arrastra para girar</span></div>
        <div class="legend"><span><i class="sw sw-l"></i>Barras longitudinales</span><span><i class="sw sw-s"></i>Estribos</span><span><i class="sw sw-c"></i>Concreto transparente</span></div>
      </figure>
    </div>
  </section>
'''

TONOS = {"acero": "", "entregables": "tone-stone", "pasos": "", "internacional": "tone-stone", "plantilla": "", "tutoriales": "",
         "precios": "", "estudiantes": "", "preguntas": "tone-stone", "contacto": "", "final": ""}


def migrar_acero():
    f = RAIZ / "aceroalf.html"
    s = f.read_text(encoding="utf-8")
    if "<!--ALF:gh-->" in s:
        f.write_text(chrome.aplicar(s, CFG, SOCIAL, "aceroalf"), encoding="utf-8")
        return "aceroalf (refrescada)"
    s = chrome.migrar(s, CFG, SOCIAL, "aceroalf")
    s = s.replace("<!--/ALF:gh-->", "<!--/ALF:gh-->\n" + PBAR, 1)
    # portada y accesos rápidos
    i = s.index('<section class="hero">')
    j = s.index('</div>\n  </div>', s.index('<div class="tiles">')) + len('</div>\n  </div>')
    s = s[:i].rstrip(" ") + HERO.lstrip(" ") + s[j:]
    # ids y tonos de las secciones sin id
    secs = list(re.finditer(r'<section class="block( pricing)?"([^>]*)>', s))
    nombres = ["acero", "entregables", "pasos", "internacional", "plantilla", "tutoriales", "precios", "estudiantes", "preguntas", "contacto", "final"]
    out, last = [], 0
    for m, nom in zip(secs, nombres):
        attrs = re.sub(r'\s*style="padding-top:0"', "", m.group(2))
        if 'id="' not in attrs:
            attrs += ' id="%s"' % nom
        cls = "block" + (m.group(1) or "") + ((" " + TONOS[nom]) if TONOS[nom] else "")
        out.append(s[last:m.start()]); out.append('<section class="%s"%s>' % (cls, attrs)); last = m.end()
    out.append(s[last:]); s = "".join(out)
    # scripts: sin animaciones de aparición; visor 3D como archivo común; menú en assets/alf.js
    scripts = list(re.finditer(r"<script>(.*?)</script>", s, re.S))
    for m in reversed(scripts):
        body = m.group(1)
        if "Rediseño 2: apariciones" in body:
            s = s[:m.start()] + s[m.end():]
        elif "Vista 3D de armadura" in body:
            s = s[:m.start()] + '<script src="assets/rebar3d.js" defer></script>' + s[m.end():]
    s = re.sub(r"const mb=document\.getElementById\('menuBtn'\),ln=document\.getElementById\('links'\);\s*"
               r"mb\.addEventListener\([^\n]*\n\s*ln\.addEventListener\([^\n]*\n", "", s)
    s = s.replace("var(--accent)';setTi", "var(--accent)';setTi")
    f.write_text(s, encoding="utf-8")
    return "aceroalf"


def migrar_legal(nombre):
    f = RAIZ / nombre
    s = f.read_text(encoding="utf-8")
    ya = "<!--ALF:gh-->" in s
    s = chrome.migrar(s, CFG, SOCIAL, "")
    if not ya:
        s = re.sub(r"<main>", '<main class="legal-page" id="inicio"><div class="wrap">', s, count=1)
        s = s.replace("</main>", "</div></main>", 1)
    f.write_text(s, encoding="utf-8")
    return nombre


if __name__ == "__main__":
    hechas = [migrar_acero()]
    for n in ["terminos.html", "privacidad.html", "reembolsos.html", "reclamaciones.html", "reclamo-enviado.html", "instalacion.html"]:
        hechas.append(migrar_legal(n))
    print("Migradas:", ", ".join(hechas))
