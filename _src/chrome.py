"""Encabezado, pie y <head> comunes de www.alfbim.com (diseño de oct-2026).

Cada página lleva bloques marcados que build.py reemplaza en cada ejecución:
  <!--ALF:head--> ... <!--/ALF:head-->   fuentes y hoja de estilos
  <!--ALF:gh--> ... <!--/ALF:gh-->       barra global negra
  <!--ALF:gf--> ... <!--/ALF:gf-->       pie
"""
import re, html, urllib.parse

E = html.escape

ICON_WA = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.7 14.9L2 22l5.2-1.3A10 10 0 1 0 12 2Zm0 18.2'
           'a8.2 8.2 0 0 1-4.2-1.1l-.3-.2-3.1.8.8-3-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9'
           'c-.3-.4.3-.4.8-1.4a.5.5 0 0 0 0-.5l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4 5.2 5.2 0 0 0 3.2.7'
           ' 2.7 2.7 0 0 0 1.8-1.3 2.2 2.2 0 0 0 .2-1.3c-.1-.1-.3-.2-.5-.3Z"/></svg>')

HEAD = ('<!--ALF:head-->\n'
        '<link rel="preload" href="assets/fonts/archivo-var.woff" as="font" type="font/woff" crossorigin>\n'
        '<link rel="stylesheet" href="assets/alf.css">\n'
        '<script src="assets/alf.js" defer></script>\n'
        '<!--/ALF:head-->')


def wa(cfg, msg):
    return "https://wa.me/%s?text=%s" % (cfg["contacto"]["whatsapp"], urllib.parse.quote(msg, safe=""))


def header(cfg, activo=""):
    def a(href, txt, key):
        cur = ' aria-current="page"' if key == activo else ""
        return '<a href="%s"%s>%s</a>' % (href, cur, txt)
    nav = "".join([
        a("index.html#productos", "Productos", "productos"),
        a("aceroalf.html", "AceroALF", "aceroalf"),
        a("aceroalf.html#tutoriales", "Tutoriales", "tutoriales"),
        a("index.html#plantilla", "Plantilla gratis", "plantilla"),
        a("index.html#contacto", "Contacto", "contacto"),
    ])
    con = cfg["contacto"]
    return ('<!--ALF:gh-->\n<header class="gh" id="gh"><div class="wrap">'
            '<a class="brand" href="index.html" aria-label="ALF_BIM, inicio"><img src="assets/logo-d.png" alt="" width="34" height="29"><b>ALF<span>_</span>BIM</b></a>'
            '<button class="menu-btn" id="menuBtn" type="button" aria-expanded="false" aria-controls="ghNav">Menú</button>'
            '<nav class="gh-nav" id="ghNav" aria-label="Principal">%s</nav>'
            '<div class="gh-end"><a class="gh-wa" href="%s" target="_blank" rel="noopener">%s<span>%s</span></a>'
            '<a class="btn btn-primary" href="aceroalf.html#descargar">Prueba gratis</a></div>'
            '</div></header>\n<!--/ALF:gh-->') % (nav, E(wa(cfg, "Hola ALF_BIM, quiero hacer una consulta.")), ICON_WA, E(con["whatsapp_txt"]))


def footer(cfg, social_html):
    neg, con = cfg["negocio"], cfg["contacto"]
    legal = ('<li><a href="privacidad.html">Privacidad y cookies</a></li><li><a href="terminos.html">Términos y condiciones</a></li>'
             '<li><a href="reembolsos.html">Política de reembolso</a></li><li><a class="lr" href="reclamaciones.html">Libro de Reclamaciones</a></li>')
    return ('<!--ALF:gf-->\n<footer class="gf"><div class="wrap">'
            '<div class="gf-top">'
            '<div class="gf-about"><a class="brand" href="index.html"><img src="assets/logo-d.png" alt="" width="34" height="29"><b>ALF<span>_</span>BIM</b></a>'
            '<p>Software para la ingeniería civil peruana: Revit, expediente técnico y obra. Hecho por ingenieros en Chota, Cajamarca.</p>%s</div>'
            '<div><h4>Productos</h4><ul><li><a href="aceroalf.html">AceroALF</a></li><li><a href="aceroalf.html#precios">Precios de AceroALF</a></li>'
            '<li><a href="index.html#productos">Próximos programas</a></li><li><a href="index.html#plantilla">Plantilla de Revit gratis</a></li></ul></div>'
            '<div><h4>Soporte</h4><ul><li><a href="aceroalf.html#tutoriales">Tutoriales en video</a></li><li><a href="instalacion.html">Guía de instalación</a></li>'
            '<li><a href="%s" target="_blank" rel="noopener">WhatsApp %s</a></li><li><a href="mailto:%s">%s</a></li></ul></div>'
            '<div><h4>Legal</h4><ul>%s</ul></div>'
            '</div>'
            '<div class="gf-bottom"><span>© 2026 ALF_BIM. Titular: %s, RUC %s. %s.</span>'
            '<p class="tm">Autodesk y Revit son marcas registradas de Autodesk, Inc. Excel es marca de Microsoft. AceroALF y los programas ALF son desarrollos '
            'independientes de ALF_BIM y no están afiliados a esas empresas.</p></div>'
            '</div></footer>\n<!--/ALF:gf-->') % (
        social_html, E(wa(cfg, "Hola ALF_BIM, necesito soporte.")), E(con["whatsapp_txt"]), con["correo"], con["correo"],
        legal, neg["titular"], neg["ruc"], neg["lugar"])


def _sub_block(s, tag, new):
    pat = re.compile(r"<!--ALF:%s-->.*?<!--/ALF:%s-->" % (tag, tag), re.S)
    if pat.search(s):
        return pat.sub(lambda m: new, s, count=1), True
    return s, False


def aplicar(s, cfg, social_html, activo=""):
    """Pone el <head>, la barra y el pie comunes en una página ya migrada (con marcadores)."""
    s, _ = _sub_block(s, "head", HEAD)
    s, _ = _sub_block(s, "gh", header(cfg, activo))
    s, _ = _sub_block(s, "gf", footer(cfg, social_html))
    return s


def migrar(s, cfg, social_html, activo=""):
    """Convierte una página con el diseño anterior: quita los <style>, cambia encabezado y pie y agrega los marcadores."""
    if "<!--ALF:gh-->" in s:
        return aplicar(s, cfg, social_html, activo)
    s = re.sub(r"<style[^>]*>.*?</style>\s*", "", s, flags=re.S)
    s = re.sub(r'<link rel="preconnect"[^>]*>\s*', "", s)
    s = re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com[^>]*>\s*', "", s)
    s = s.replace("</head>", HEAD + "\n</head>", 1)
    s = re.sub(r'<meta name="theme-color" content="[^"]*">', '<meta name="theme-color" content="#000000">', s)
    s = re.sub(r"<header\b.*?</header>", lambda m: header(cfg, activo), s, count=1, flags=re.S)
    i = s.rfind("<footer")
    j = s.find("</footer>", i)
    if i >= 0 and j >= 0:
        s = s[:i] + footer(cfg, social_html) + s[j + len("</footer>"):]
    return s
