# Web de ALF_BIM (www.alfbim.com): cómo funciona desde el 24-oct-2026

## Dónde está todo

| Pieza | Dónde |
|---|---|
| Código de la web (fuente única) | GitHub: `alfbim1999-blip/alfbim-web`, rama `main` |
| Publicación | GitHub Pages (gratis). Cada cambio que se sube a `main` se publica solo en 1–2 minutos |
| Instaladores (.exe) | GitHub → release **descargas** del mismo repositorio (sin límite de descargas) |
| Dominio | Spaceship: `A @` → 185.199.108.153 / .109 / .110 / .111 y `CNAME www` → `alfbim1999-blip.github.io` |
| Libro de Reclamaciones | FormSubmit → llega a alfbim1999@gmail.com (la primera vez pide activar por correo) |
| Plantilla de Revit (ZIP 26.6 MB) | Google Drive (enlace en `index.html` y `aceroalf.html`) |

Netlify ya no se usa. La carpeta `WEB\01_web_alfbim` de la PC queda como copia antigua: **los cambios se hacen en GitHub** (desde el chat de Claude del proyecto, que administra la web).

## Cambiar precios, contacto, redes o instaladores

Todo está en un solo archivo: `_src/config.json`. Después se ejecuta `python3 _src/build.py`, que regenera las páginas, y se sube a GitHub.

- Precio de un programa: `productos → <programa> → precio` (`mensual`, `anual`, o `m3`/`m6` en los de Revit).
- Packs: `packs → obra / completo → anual`.
- Programa nuevo o que pasa de «Próximamente» a «Disponible»: cambiar `estado`, completar `instalador` (archivo, versión, bytes, SHA-256) y crear su página en `_src/paginas/<id>.py`.

## Publicar una versión nueva de un instalador

1. En GitHub → Releases → **descargas** → Edit: borra el .exe viejo y arrastra el nuevo. Guarda.
2. En `_src/config.json` actualiza `archivo`, `version`, `bytes` y `sha` del programa (el SHA-256 está en `VENTA\<programa>\1_PARA_CLIENTES`).
3. `python3 _src/build.py` y subir a GitHub.

## Calendario de PlazosALF

`datos/plazosalf_calendario.json` (mismo formato de siempre). PlazosALF lo descarga de `https://www.alfbim.com/datos/plazosalf_calendario.json`.

## Archivos de la web

- `index.html`: portada con el catálogo por especialidad, packs y descargas gratuitas (la arma `_src/index_contenido.py`).
- Páginas de producto generadas: `sanitariasalf`, `dotacionalf`, `plazosalf`, `planosalf`, `plantilla-excel-estructuras`, `plantilla-excel-iiee` (fuente en `_src/paginas/`).
- Páginas hechas a mano (el generador solo actualiza sus precios y descargas): `aceroalf`, `presupuestoalf`, `cronogramaalf`, `informemensualalf`, `saneamientoruralalf`.
- Legales: `terminos`, `reembolsos`, `privacidad`, `reclamaciones`, `reclamo-enviado`.

## Diseño (desde el 27-oct-2026)

- Estilo inspirado en autodesk.com (no copia): barra negra, portada negra, secciones blanco y piedra, un solo color de acción (azul ALF), tipografía Archivo alojada en `assets/fonts/` (licencia OFL).
- Hoja única: `assets/alf.css`. Comportamiento común: `assets/alf.js`. Visor 3D del acero: `assets/rebar3d.js`.
- Barra superior, pie y `<head>` comunes: `_src/chrome.py`; `build.py` los vuelve a poner en todas las páginas en cada ejecución (bloques `<!--ALF:gh-->`, `<!--ALF:gf-->`, `<!--ALF:head-->`).
- Las páginas guardadas en `_src/pausadas/` todavía tienen el diseño anterior: al reactivarlas, pasarlas por `_src/migrar_diseno.py` (o rehacer su portada como la de AceroALF).
