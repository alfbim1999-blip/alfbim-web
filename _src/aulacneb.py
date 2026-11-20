"""Página de AulaCNEB (www.alfbim.com/aulacneb), el programa para docentes de EBR.

No es de la línea de ingeniería: tiene su propio diseño (papel claro y verde), no entra en el catálogo, los packs ni la
tabla de instalación, y solo la enlaza el pie. Datos: _src/config.json → otros_productos.aulacneb.
Fuentes del contenido: manual de AulaCNEB 1.0 (herramientas/manual_pdf.py), docs/INFORME_BASE_CURRICULAR.md,
docs/COSTOS_IA_Y_PRECIO.md (precio de lanzamiento aprobado el 20-11-2026) y las capturas del programa.
"""
import json

PID = "aulacneb"

CSS = """<style>/*AulaCNEB*/
.aula{--ac:#0E6B55;--ac-ink:#0A4F3F;--ac-soft:#E2F1EA;--ac-cream:#FBF6EC;--ac-sun:#E3A33A;--ac-line:#E4DCCB;
  --accent:#0E6B55;--accent-ink:#0A4F3F;--accent-soft:#E2F1EA;--stone:#F6F1E6}
.aula .eyebrow{color:var(--ac)}
.pbar.ac-bar{background:#0A2E26;border-bottom-color:#14453a}
.pbar.ac-bar .btn-primary{background:#E3A33A;color:#1d1606}
.pbar.ac-bar .btn-primary:hover{background:#f0b552}
.ac-hero{background:var(--ac-cream);color:#14201c;padding:clamp(2.2rem,5vw,4.5rem) 0 clamp(2.6rem,6vw,5rem);position:relative;overflow:hidden;border-bottom:1px solid var(--ac-line)}
.ac-hero::before{content:"";position:absolute;inset:auto -10% -55% 40%;height:120%;background:radial-gradient(closest-side,rgba(14,107,85,.14),transparent);pointer-events:none}
.ac-grid{display:grid;grid-template-columns:minmax(0,1fr);gap:clamp(2rem,5vw,4rem);align-items:center;position:relative}
@media (min-width:980px){.ac-grid{grid-template-columns:minmax(0,1.05fr) minmax(0,1fr)}}
.ac-hero .crumb,.ac-hero .crumb a{color:#5b5a50}
.ac-hero .crumb b{color:#14201c}
.ac-tag{display:inline-flex;align-items:center;gap:.6rem;font-weight:700;font-size:1.02rem;color:#14201c}
.ac-tag img{width:36px;height:36px;border-radius:8px}
.ac-hero h1{color:#0f1a17;font-size:clamp(2.3rem,4.6vw,3.7rem);line-height:1.04;letter-spacing:-.02em;margin:.9rem 0 0}
.ac-hero h1 em{font-style:normal;color:var(--ac)}
.ac-hero .lede{color:#3c4642;font-size:clamp(1.05rem,1.5vw,1.2rem);margin-top:1.1rem;max-width:56ch}
.ac-price{margin-top:1.1rem;font-size:1.02rem;color:#3c4642}
.ac-price b{color:#0f1a17}
.ac-cta{display:flex;flex-wrap:wrap;gap:.75rem;margin-top:1.4rem}
.ac-hero .btn-ghost{background:transparent;color:#14201c;border:1.5px solid #14201c}
.ac-hero .btn-ghost:hover{background:#14201c;color:#fff}
.ac-note{margin-top:1rem;font-size:.92rem;color:#5b5a50}
.ac-note a{color:#14201c}
.ac-chips{display:flex;flex-wrap:wrap;gap:.45rem;margin-top:1.4rem}
.ac-chips span{font-size:.86rem;font-weight:600;padding:.35rem .7rem;border-radius:999px;background:#fff;border:1px solid var(--ac-line);color:#2b3531}
.ac-stack{position:relative;aspect-ratio:1/1;max-width:640px;width:100%;margin:0 auto}
.ac-stack .pg{position:absolute;background:#fff;border-radius:4px;box-shadow:0 18px 50px -18px rgba(20,32,28,.45),0 2px 6px rgba(20,32,28,.08);overflow:hidden;border:1px solid #e9e3d6}
.ac-stack .pg img{display:block;width:100%;height:auto}
.ac-stack .p1{width:78%;left:0;top:2%;transform:rotate(-3.5deg)}
.ac-stack .p3{width:78%;right:0;top:45%;transform:rotate(3deg);z-index:1}
.ac-stack .p2{width:52%;left:25%;top:7%;transform:rotate(1deg);z-index:2}
.ac-stack figcaption{position:absolute;left:0;right:0;bottom:0;display:flex;justify-content:center;gap:.5rem;z-index:3}
.ac-stack figcaption span{font-size:.82rem;font-weight:700;padding:.35rem .75rem;border-radius:999px;background:#0f1a17;color:#fff}
.ac-stack figcaption span.w{background:#fff;color:#0f1a17;border:1px solid var(--ac-line)}
.ac-band{background:#0A2E26;color:#fff}
.ac-band .wrap{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:1rem;padding-top:1.4rem;padding-bottom:1.4rem}
.ac-band div b{display:block;font-size:1.45rem;font-weight:800;letter-spacing:-.01em}
.ac-band div small{color:rgba(255,255,255,.74);font-size:.9rem}
.aula .out .code{color:var(--ac)}
.ac-docs{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:1.4rem;margin-top:.6rem}
.ac-doc{display:flex;flex-direction:column;gap:.8rem;text-decoration:none;color:inherit}
.ac-doc .pg{background:#fff;border:1px solid var(--ac-line);border-radius:6px;overflow:hidden;box-shadow:0 12px 30px -18px rgba(20,32,28,.5);transition:transform .25s var(--ease),box-shadow .25s}
.ac-doc:hover .pg{transform:translateY(-4px);box-shadow:0 22px 40px -20px rgba(20,32,28,.55)}
.ac-doc img{display:block;width:100%;aspect-ratio:1275/902;height:auto;object-fit:cover;object-position:top}
.ac-doc b{font-size:1.05rem}
.ac-doc small{display:block;color:var(--muted);font-size:.9rem}
.ac-doc .lnk{font-size:.9rem;font-weight:600;color:var(--ac)}
.ac-doc .lnk::after{content:" ↗"}
.ac-src{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:.8rem;margin-top:.4rem}
.ac-src div{background:#fff;border:1px solid var(--ac-line);border-radius:10px;padding:1rem 1.1rem}
.ac-src b{display:block;font-size:.98rem}
.ac-src small{color:var(--muted);font-size:.88rem}
.ac-ia{margin-top:1.4rem;display:grid;grid-template-columns:auto minmax(0,1fr);gap:1rem;align-items:start;background:var(--ac-soft);border-radius:12px;padding:1.2rem 1.3rem}
.ac-ia svg{width:28px;height:28px;color:var(--ac)}
.ac-ia p{margin:0;color:#24302c}
.aula .pricing{background:var(--stone)}
.aula .plan.feat{border-color:var(--ac)}
.aula .plan.feat .ribbon{background:var(--ac)}
.ac-soon{margin-top:1.2rem;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:1rem;border:1.5px dashed #c9bfa8;border-radius:12px;padding:1rem 1.2rem;background:#fff}
.ac-soon p{margin:0;color:#3c4642;max-width:70ch}
.ac-soon b{color:#0f1a17}
.ac-end{background:#0A2E26}
.endcta.ac-end .btn:not(.btn-ghost):not(.btn-primary){background:#E3A33A;color:#1d1606}
.endcta.ac-end .btn:not(.btn-ghost):not(.btn-primary):hover{background:#f0b552}
.ac-end code{word-break:break-all}
</style>"""

ICONS = {
    "spark": '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M6 18l2.5-2.5M15.5 8.5 18 6"/>',
}


def _svg(path):
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" '
            'stroke-linejoin="round" aria-hidden="true">%s</svg>' % path)


def pagina(g):
    CFG, E, wa, soles, mb = g["CFG"], g["E"], g["wa"], g["soles"], g["mb"]
    section, sec_head, outs, shots, steps, faq = g["section"], g["sec_head"], g["outs"], g["shots"], g["steps"], g["faq"]
    ARROW_DOWN, ARROW_OUT = g["ARROW_DOWN"], g["ARROW_OUT"]
    p = CFG["otros_productos"][PID]
    pr, ins = p["precio"], p["instalador"]
    gratis, anual, inst, n_inst = pr["gratis_sesiones_mes"], pr["anual"], pr["institucion"], pr["institucion_docentes"]
    img = "img/aulacneb/"
    url_exe = (CFG["descargas_base_github"] if ins.get("en_release") else CFG["descargas_base"]) + ins["archivo"]
    msg_anual = "Hola ALF_BIM, quiero la licencia anual de AulaCNEB (%s). Mi ID de equipo es: " % soles(anual)
    msg_inst = "Hola ALF_BIM, quiero la licencia de AulaCNEB para una institución (%d docentes, %s al año)." % (n_inst, soles(inst))
    msg_ia = "Hola ALF_BIM, avísenme cuando AulaCNEB tenga la IA incluida."

    hero = f"""  <section class="ac-hero">
    <div class="wrap ac-grid">
      <div>
        <p class="crumb"><a href="index.html">Inicio</a><span aria-hidden="true">/</span><b>AulaCNEB</b></p>
        <p class="ac-tag" style="margin-top:1rem"><img src="img/iconos/aulacneb.png" alt="" width="36" height="36">AulaCNEB · para docentes de EBR</p>
        <h1>Tu planificación curricular, <em>lista en Word y PDF</em></h1>
        <p class="lede">Planificación anual, unidades, sesiones, instrumentos de evaluación y registro auxiliar según el Currículo
          Nacional, con las competencias y los desempeños oficiales de tu grado y situaciones pensadas para tu comunidad.</p>
        <p class="ac-price"><b>Gratis</b>, con {gratis} sesiones al mes. Licencia anual de <b>{soles(anual)}</b> para sesiones sin límite.</p>
        <div class="ac-cta">
          <a class="btn btn-primary" href="#descargar">Descargar gratis</a>
          <a class="btn btn-ghost" href="#muestras">Ver documentos de ejemplo</a>
        </div>
        <p class="ac-note">Para Windows 10 y 11 · funciona sin internet · <a href="{p['guia']}" target="_blank" rel="noopener">Tu primera sesión en 5 minutos (PDF)</a></p>
        <div class="ac-chips"><span>Inicial</span><span>Primaria</span><span>Secundaria</span><span>Multigrado</span><span>Contexto rural y EIB</span></div>
      </div>
      <figure class="ac-stack" aria-label="Tres documentos hechos con AulaCNEB">
        <div class="pg p1"><img src="{img}doc_registro.jpg" width="1275" height="902" alt="Registro auxiliar del primer periodo con el nivel de logro de cada estudiante por competencia." fetchpriority="high"></div>
        <div class="pg p2"><img src="{img}doc_sesion.jpg" width="902" height="1275" alt="Primera página de una sesión de aprendizaje multigrado de Matemática para 3.° y 4.° grado de Primaria."></div>
        <div class="pg p3"><img src="{img}doc_unidad.jpg" width="1275" height="902" alt="Primera página de una unidad de aprendizaje de 2.° de Secundaria con su situación significativa."></div>
        <figcaption><span>Word editable</span><span class="w">PDF para imprimir</span></figcaption>
      </figure>
    </div>
  </section>
"""

    banda = ('  <div class="ac-band"><div class="wrap">'
             '<div><b>31</b><small>competencias del CNEB, con capacidades y estándares</small></div>'
             '<div><b>1 997</b><small>desempeños oficiales, grado por grado</small></div>'
             '<div><b>36</b><small>semanas lectivas del año escolar 2026</small></div>'
             '<div><b>5 min</b><small>para tu primera sesión</small></div>'
             '</div></div>\n')

    prepara = section(
        sec_head("Qué prepara", "Todo lo que pide la planificación, en un solo programa",
                 "Eliges nivel, grado y áreas, escribes los datos de tu institución y de tu comunidad, y AulaCNEB arma los documentos "
                 "del año. Todo sale en Word para que lo ajustes y en PDF listo para imprimir o entregar.")
        + outs([
            ("PLAN ANUAL", "Planificación anual", "Las unidades del año en las semanas lectivas, por bimestre o trimestre.",
             ["Todas las competencias de cada área en cada periodo",
              "Los siete enfoques transversales a lo largo del año",
              "Calendario comunal y fechas de tu región"]),
            ("UNIDAD", "Unidades de aprendizaje", "Situación significativa con preguntas retadoras y el producto de la unidad.",
             ["Competencias, capacidades y desempeños del grado",
              "Criterios de evaluación y evidencias",
              "En Inicial, una actividad por día con su calendario"]),
            ("SESIÓN", "Sesiones de aprendizaje", "Inicio, desarrollo y cierre con tiempos que suman la duración de la sesión.",
             ["Propósito, criterios, evidencia y enfoque",
              "Ficha para los estudiantes y materiales",
              "Multigrado: un tema, actividades por grado"]),
            ("INSTRUMENTOS", "Instrumentos de evaluación", "Lista de cotejo, escala de valoración o rúbrica con los criterios de cada sesión.",
             ["Con la lista de tus estudiantes",
              "Listos para imprimir",
              "Van como anexo de la sesión"]),
            ("REGISTRO", "Registro auxiliar", "Niveles AD, A, B y C por competencia, como pide la R.V.M. N.° 094-2020-MINEDU.",
             ["Importa la nómina del SIAGIE desde Excel",
              "Sugiere el nivel del periodo; tú lo confirmas",
              "Conclusiones descriptivas para el nivel C"]),
            ("REVISIÓN", "Revisión antes de entregar", "El programa revisa la coherencia de todo lo que vas a presentar.",
             ["Desempeños del grado correcto",
              "Criterios con su desempeño y su evidencia",
              "Tiempos que suman y competencias que faltan"]),
        ], cls="outs outs-3"),
        "prepara")

    docs = "".join(
        '<a class="ac-doc" href="%s" target="_blank" rel="noopener"><div class="pg"><img src="%s" width="1275" height="902" loading="lazy" alt="%s"></div>'
        '<div><b>%s</b><small>%s</small></div><span class="lnk">Abrir el PDF completo</span></a>' % (
            f, img + im, E(alt), E(t), E(s))
        for (f, t, s), im, alt in zip(p["muestras"], ["doc_sesion.jpg", "doc_unidad.jpg", "doc_registro.jpg"], [
            "Sesión de aprendizaje multigrado de Matemática para 3.° y 4.° de Primaria, con propósito, criterios por grado y secuencia didáctica.",
            "Unidad de aprendizaje de 2.° de Secundaria con situación significativa, propósitos de aprendizaje y secuencia de sesiones.",
            "Registro auxiliar de Inicial 5 años con el nivel de logro de cada estudiante en cada competencia del primer bimestre."]))
    muestras = section(
        sec_head("Documentos de ejemplo", "Así quedan tus documentos",
                 "Hechos con AulaCNEB para instituciones y estudiantes ficticios, sin cambiar nada a mano. Times New Roman, "
                 "con el encabezado de tu institución y tu logo.")
        + '<div class="ac-docs">' + docs + "</div>",
        "muestras", tono="alt")

    como = section(
        sec_head("Cómo funciona", "Siete pasos, en el orden en que planificas",
                 "Un asistente te lleva de tus datos a los documentos. Puedes volver a cualquier paso y corregir títulos, situaciones o productos.")
        + shots([
            (img + "app_datos.jpg", 1366, 728,
             "Paso 1 de AulaCNEB: nivel, grados, áreas, datos de la institución y contexto de la comunidad.",
             "Paso 1 · Tus datos y tu aula: nivel, grado, áreas y comunidad"),
            (img + "app_plan.jpg", 1366, 728,
             "Paso 3: planificación anual con las unidades del año y la matriz de competencias por unidad.",
             "Paso 3 · Planificación anual con su matriz de competencias"),
            (img + "app_sesion.jpg", 1366, 728,
             "Paso 5: sesión de aprendizaje generada, con propósito, criterios, inicio, desarrollo y cierre.",
             "Paso 5 · La sesión, con sus tiempos y su ficha"),
            (img + "app_evaluacion.jpg", 1366, 728,
             "Paso 6: registro de niveles de logro por estudiante y evidencia, con el nivel sugerido del periodo.",
             "Paso 6 · Evaluación y registro auxiliar"),
        ], style="margin-top:.5rem")
        + steps([
            ("Pasos 1 y 2 · Tus datos y tus estudiantes", "Nivel, grado (dos grados = multigrado), áreas, institución y contexto: zona, EIB, "
             "actividades productivas, fiestas y problemática. Importa la nómina del SIAGIE o escribe los nombres."),
            ("Pasos 3 a 5 · Plan, unidad y sesión", "Generas la planificación anual, luego cada unidad y cada sesión. Sin internet y sin "
             "inteligencia artificial, con las plantillas del programa; o con IA, si la activas."),
            ("Pasos 6 y 7 · Evalúas y exportas", "Registras los niveles de logro, revisas la coherencia y exportas todo a Word y PDF con "
             "nombres claros, por ejemplo «3B_Comunicacion_Sesion05»."),
        ]),
        "como")

    oficial = section(
        sec_head("Datos oficiales", "Con los documentos del MINEDU, página por página",
                 "Las áreas, competencias, capacidades, estándares y desempeños por grado salen de una base construida con los "
                 "documentos oficiales. Cada dato guarda su documento y su página, para que puedas comprobarlo.")
        + '<div class="ac-src">'
        + "".join('<div><b>%s</b><small>%s</small></div>' % x for x in [
            ("Currículo Nacional de la Educación Básica", "R.M. N.° 281-2016-MINEDU, modificada por la R.M. N.° 159-2017-MINEDU"),
            ("Programas curriculares de Inicial, Primaria y Secundaria", "R.M. N.° 649-2016-MINEDU"),
            ("Evaluación de las competencias", "R.V.M. N.° 094-2020-MINEDU: niveles AD, A, B, C y conclusiones descriptivas"),
            ("Año escolar 2026", "R.M. N.° 501-2025-MINEDU: 36 semanas lectivas y 8 de gestión"),
        ])
        + "</div>"
        + '<div class="ac-ia">%s<p><b>La inteligencia artificial no inventa el currículo.</b> Si la activas, solo redacta lo creativo '
          '(situaciones, actividades, fichas y conclusiones) y elige entre los desempeños que le entrega el programa. Si nombra una '
          'competencia o un desempeño que no está en la base oficial, el programa la rechaza y usa sus plantillas.</p></div>' % _svg(ICONS["spark"]),
        "oficial")

    planes = [
        dict(n="Gratis", amt="S/ 0", per="para siempre", ps="Sin tarjeta y sin registro", promo="%d sesiones al mes" % gratis, feat=False,
             li=["Planificación anual, unidades, instrumentos y registro sin límite", "%d sesiones de aprendizaje cada mes" % gratis,
                 "Word editable y PDF", "Todas las funciones del programa"],
             btn=('<a class="btn btn-ghost" href="#descargar">Descargar gratis</a>')),
        dict(n="Licencia anual", amt=soles(anual), per="/ año", ps="Equivale a %s al mes" % soles(round(anual / 12, 2)),
             promo="Precio de lanzamiento", feat=True,
             li=["Sesiones sin límite", "1 computadora", "Soporte por WhatsApp", "Actualizaciones de la base curricular",
                 "IA opcional con tu propia clave"],
             btn='<a class="btn btn-primary" href="%s" target="_blank" rel="noopener">Comprar por WhatsApp%s</a>' % (E(wa(msg_anual)), ARROW_OUT)),
        dict(n="Institución", amt=soles(inst), per="/ año", ps="%s por docente" % soles(round(inst / n_inst, 2)),
             promo="%d licencias anuales" % n_inst, feat=False,
             li=["%d docentes, una computadora cada uno" % n_inst, "Para tu IE, tu red educativa o tu UGEL",
                 "Activación de todas las licencias por WhatsApp", "Soporte por WhatsApp"],
             btn='<a class="btn btn-ghost" href="%s" target="_blank" rel="noopener">Pedir por WhatsApp</a>' % E(wa(msg_inst))),
    ]
    h = ['<section class="block pricing" id="precios"><div class="wrap">',
         sec_head("Precios de lanzamiento", "Empieza gratis; paga solo si lo usas todo el año",
                  "La versión gratuita no vence. La licencia quita el límite de sesiones. Pagas con %s." % CFG["pagos"]),
         '<div class="plans">']
    for pl in planes:
        h.append('<article class="plan%s">' % (" feat" if pl["feat"] else ""))
        if pl["feat"]:
            h.append('<span class="ribbon">Recomendado</span>')
        h.append('<span class="pn">%s</span>' % pl["n"])
        h.append('<div class="price"><span class="amt mono">%s</span><span class="per">%s</span></div>' % (pl["amt"], pl["per"]))
        h.append('<p class="ps">%s</p><p class="promo">%s</p>' % (pl["ps"], pl["promo"]))
        h.append("<ul>" + "".join("<li>%s</li>" % x for x in pl["li"]) + "</ul>")
        h.append(pl["btn"])
        h.append("</article>")
    h.append("</div>")
    h.append('<div class="ac-soon"><p><b>Próximamente: IA incluida.</b> La redacción con inteligencia artificial sin configurar nada '
             'ni tener una clave propia. Hoy puedes usar la IA con tu propia clave de Anthropic o trabajar sin IA, con las plantillas.</p>'
             '<a class="btn btn-ghost" href="%s" target="_blank" rel="noopener">Avísame%s</a></div>' % (E(wa(msg_ia)), ARROW_OUT))
    h.append('<p class="fine">Precios de lanzamiento en soles. La licencia es por computadora: abre <b>Ayuda → Licencia</b>, copia el ID de '
             'tu equipo y envíalo por WhatsApp (%s) con el comprobante de pago; te mandamos la clave apenas se acredite el pago. '
             'Revisa la <a href="reembolsos.html">política de reembolso</a> y los <a href="terminos.html">términos y condiciones</a>.</p>'
             % E(CFG["contacto"]["whatsapp_txt"]))
    h.append("</div></section>")
    precios = "".join(h)

    preguntas = section(sec_head("Preguntas frecuentes", "Antes de instalar") + faq([
        ("¿Necesito internet?", "No. AulaCNEB funciona sin internet y la licencia se valida en tu computadora. Solo la inteligencia "
         "artificial, si la activas, usa internet."),
        ("¿Sirve para aulas multigrado?", "Sí. Si marcas dos o más grados, el programa trabaja un mismo tema para todos, con los "
         "desempeños y los criterios de cada grado y actividades diferenciadas por grado."),
        ("¿Puedo cambiar lo que genera?", "Sí. Puedes corregir títulos, situaciones y productos en el programa, y todo se exporta en "
         "Word editable. La planificación es tuya: revísala y adáptala a tu aula antes de presentarla."),
        ("¿De dónde salen las competencias y los desempeños?", "De los documentos oficiales del MINEDU: el CNEB y los programas "
         "curriculares de cada nivel. Cada dato guarda su documento y su página. En Secundaria, el documento oficial es un PDF "
         "escaneado: los pocos desempeños que no se pudieron leer con total certeza salen marcados para que los revises."),
        ("¿Necesito Word?", "Para los documentos en Word, no. Para guardar el PDF, el programa usa Microsoft Word o, si no lo tienes, "
         "LibreOffice, que es gratuito."),
        ("¿Qué pasa con los datos de mis estudiantes?", "La nómina se guarda solo en tu computadora, dentro de tu proyecto; no se "
         "envía a ALF_BIM. Si usas la IA, se envían a Anthropic los datos de la clase y de las evidencias, nunca los nombres ni el DNI "
         "de tus estudiantes."),
        ("¿Cuánto cuesta la IA con mi propia clave?", "La pagas directamente a Anthropic según tu uso: alrededor de US$ 0.04 por "
         "sesión con el modelo recomendado. Sin IA, el programa usa sus plantillas y no cuesta nada."),
        ("¿Cuántas sesiones tengo gratis?", "%d sesiones de aprendizaje cada mes, para siempre. La planificación anual, las unidades, "
         "los instrumentos y el registro auxiliar no tienen límite." % gratis),
        ("¿Cómo compro la licencia?", "Abre Ayuda → Licencia en el programa, copia el ID de tu equipo y envíalo por WhatsApp con "
         "el comprobante de pago por %s. Te enviamos la clave apenas se acredite el pago." % CFG["pagos"]),
    ]), "preguntas")

    sha = ""
    if ins.get("sha"):
        sha = ('<p class="sha">Versión <span class="ver">%s</span> · <span class="tam">%s</span> · SHA-256 <code id="sha">%s</code></p>'
               % (ins["version"], mb(ins["bytes"]), ins["sha"]))
    descarga = ('<section class="block" id="descargar"><div class="wrap"><div class="endcta ac-end"><div>'
                '<h2>Descarga AulaCNEB gratis</h2><p>Instalador para Windows 10 y 11 (64 bits). Al terminar se abre con tres proyectos '
                'de ejemplo: Inicial, Primaria multigrado y Secundaria. Empieza por la guía «Tu primera sesión en 5 minutos».</p>%s'
                '<p class="dl-note">Si Windows muestra «Windows protegió su PC», pulsa «Más información» y luego «Ejecutar de todas formas».</p>'
                '</div><div class="endcta-side">'
                '<a class="btn" id="dlBtn" href="%s" download>Descargar instalador%s</a>'
                '<a class="btn btn-ghost" href="%s" target="_blank" rel="noopener">Manual en PDF</a>'
                '<a class="btn btn-ghost" href="%s" target="_blank" rel="noopener">Guía de 5 minutos</a>'
                '<a class="btn btn-ghost" href="%s" target="_blank" rel="noopener">Consultas por WhatsApp</a>'
                '</div></div></div></section>') % (
        sha, url_exe, ARROW_DOWN, p["manual"], p["guia"], E(wa("Hola ALF_BIM, tengo una consulta sobre AulaCNEB.")))

    main = ('<div class="aula">\n' + hero + banda + "\n".join([prepara, muestras, como, oficial, precios, preguntas, descarga]) + "\n</div>")

    jsonld = CSS + '\n<script type="application/ld+json">' + json.dumps({
        "@context": "https://schema.org", "@type": "SoftwareApplication", "name": "AulaCNEB",
        "applicationCategory": "EducationalApplication", "operatingSystem": "Windows 10, Windows 11",
        "softwareVersion": ins["version"], "url": "https://www.alfbim.com/aulacneb",
        "description": "Planificación curricular para docentes de Educación Básica Regular del Perú según el CNEB: planificación anual, "
                       "unidades, sesiones, instrumentos de evaluación y registro auxiliar en Word y PDF.",
        "offers": [{"@type": "Offer", "name": "Gratis", "price": "0", "priceCurrency": "PEN"},
                   {"@type": "Offer", "name": "Licencia anual", "price": str(anual), "priceCurrency": "PEN"}],
        "author": {"@type": "Person", "name": "Anderson Irigoín Colunche"}}, ensure_ascii=False) + "</script>"

    pend = ('<span class="pprice">Gratis · anual <b>%s</b></span><a class="btn btn-ghost" href="#precios">Ver precios</a>' % soles(anual))
    return {
        "id": PID,
        "title": "AulaCNEB · Sesiones, unidades y planificación anual según el CNEB",
        "og_title": "AulaCNEB · Planificación curricular CNEB en Word y PDF",
        "desc": "Programa para docentes de Inicial, Primaria y Secundaria: planificación anual, unidades, sesiones de aprendizaje, "
                "instrumentos de evaluación y registro auxiliar según el CNEB, con desempeños oficiales y multigrado. Gratis para Windows.",
        "nav": [("#prepara", "Qué prepara"), ("#muestras", "Ejemplos"), ("#como", "Cómo funciona"), ("#oficial", "Datos oficiales"),
                ("#precios", "Precios"), ("#preguntas", "Preguntas")],
        "prod": p, "pend": pend, "pbar_cls": "ac-bar",
        "jsonld": jsonld,
        "main": main,
    }
