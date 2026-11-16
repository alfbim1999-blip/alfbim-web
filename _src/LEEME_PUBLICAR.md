# Web de ALF_BIM (www.alfbim.com): cómo funciona (actualizado el 15-nov-2026, lanzamiento)

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

- Precio de un programa: `productos → <programa> → precio`. Revit: `mensual`, `m6` y `anual`; escritorio y calculadoras: `mensual` y `anual`.
  La tabla aprobada está en `precios_lanzamiento` (15-nov-2026). Ya no hay plan de 3 meses ni «primer mes a mitad de precio».
- Packs: `packs → obra / completo → anual` (Pack Obra S/ 349, Pack ALF_BIM S/ 599). El «por separado» se calcula con el precio anual de cada programa.
- AceroALF (página hecha a mano) tiene su propia tabla con Todo en uno y Empresa: los montos están en `aceroalf.html` (botones `data-term` 1, 6 y 12 y el objeto `const P`).
- Programa nuevo o que pasa de «Próximamente» a «Disponible»: cambiar `estado`, completar `instalador` (archivo, versión, bytes, SHA-256) y crear su página en `_src/paginas/<id>.py`.

## Publicar una versión nueva de un instalador

1. En GitHub → Releases → **descargas** → Edit: arrastra el .exe nuevo (puedes dejar el viejo). Guarda.
2. En `_src/config.json` actualiza `archivo`, `version`, `bytes` y `sha` del programa (el SHA-256 está en el archivo SHA256 de la carpeta de venta del programa).
3. `python3 _src/verificar_release.py --guardar`: comprueba que cada .exe esté en la release con el mismo tamaño y SHA-256, y marca `en_release`.
4. `python3 _src/build.py` y subir a GitHub. La tabla de instaladores de `instalacion.html` se arma sola.

## Calendario de PlazosALF

`datos/plazosalf_calendario.json` (mismo formato de siempre). PlazosALF lo descarga de `https://www.alfbim.com/datos/plazosalf_calendario.json`.

## Archivos de la web

- `index.html`: portada con el catálogo por especialidad, packs y descargas gratuitas (la arma `_src/index_contenido.py`).
- Páginas de producto generadas (fuente en `_src/paginas/`): `metradosalf`, `cadrevitalf`, `etabsrevitalf`, `memoriaestructuralalf`, `checkeralf`, `planosalf`,
  `plantilla-excel-estructuras`, `sanitariasalf`, `redesinterioresalf`, `dotacionalf`, `electricasalf`, `maximademandaalf`, `plantilla-excel-iiee`, `plazosalf`,
  `valorizacionesalf`, `simulacion4dalf`.
- Páginas hechas a mano (el generador actualiza sus precios, descargas, versión, tamaño y manual): `aceroalf`, `presupuestoalf`, `cronogramaalf`, `informemensualalf`, `saneamientoruralalf`.
- Legales: `terminos`, `reembolsos`, `privacidad`, `reclamaciones`, `reclamo-enviado`.

## Diseño (desde el 27-oct-2026)

- Estilo inspirado en autodesk.com (no copia): barra negra, portada negra, secciones blanco y piedra, un solo color de acción (azul ALF), tipografía Archivo alojada en `assets/fonts/` (licencia OFL).
- Hoja única: `assets/alf.css`. Comportamiento común: `assets/alf.js`. Visor 3D del acero: `assets/rebar3d.js`.
- Barra superior, pie y `<head>` comunes: `_src/chrome.py`; `build.py` los vuelve a poner en todas las páginas en cada ejecución (bloques `<!--ALF:gh-->`, `<!--ALF:gf-->`, `<!--ALF:head-->`).
- La pausa terminó el 15-nov-2026: todas las páginas tienen el diseño nuevo (las cuatro hechas a mano se pasaron con `python3 _src/migrar_diseno.py --productos`).
- `build.py` todavía sabe armar páginas «Próximamente» (estado `proximamente`) por si hace falta pausar un programa.
