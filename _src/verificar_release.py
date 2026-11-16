#!/usr/bin/env python3
"""Compara los instaladores de _src/config.json con los archivos subidos a la release «descargas» de GitHub.

Uso:  python3 _src/verificar_release.py            (solo revisa)
      python3 _src/verificar_release.py --guardar  (además pone en config.json los bytes de la release y en_release = true)

Para cada programa revisa que el .exe exista en la release, que su tamaño coincida y que su SHA-256 (el «digest» que da GitHub)
sea igual al de config.json. Si algo no coincide, no lo marca como subido.
"""
import json, sys, pathlib, urllib.request

RAIZ = pathlib.Path(__file__).resolve().parent.parent
CFG_F = RAIZ / "_src" / "config.json"
API = "https://api.github.com/repos/alfbim1999-blip/alfbim-web/releases/tags/descargas"


def assets():
    req = urllib.request.Request(API, headers={"Accept": "application/vnd.github+json", "User-Agent": "alfbim-web"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    return {a["name"]: a for a in data["assets"]}


def main():
    guardar = "--guardar" in sys.argv
    cfg = json.loads(CFG_F.read_text(encoding="utf-8"))
    rel = assets()
    pendientes, ok = [], []
    for pid, p in cfg["productos"].items():
        ins = p.get("instalador") or {}
        if not ins.get("archivo", "").endswith(".exe"):
            continue
        a = rel.get(ins["archivo"])
        if not a:
            pendientes.append("%-24s %s  NO ESTÁ en la release" % (p["nombre"], ins["archivo"]))
            ins["en_release"] = False
            continue
        dig = (a.get("digest") or "").split(":")[-1].upper()
        problemas = []
        if dig and dig != ins["sha"].upper():
            problemas.append("SHA-256 distinto (release %s…)" % dig[:12])
        if a["size"] != ins["bytes"]:
            problemas.append("tamaño %d en la release, %d en config" % (a["size"], ins["bytes"]))
        if problemas and not (len(problemas) == 1 and problemas[0].startswith("tamaño") and dig == ins["sha"].upper()):
            pendientes.append("%-24s %s  %s" % (p["nombre"], ins["archivo"], "; ".join(problemas)))
            ins["en_release"] = False
            continue
        ins["bytes"] = a["size"]
        ins["en_release"] = True
        ok.append("%-24s %s  %d bytes  ok" % (p["nombre"], ins["archivo"], a["size"]))
    print("\n".join(ok))
    if pendientes:
        print("\nPENDIENTES:")
        print("\n".join(pendientes))
    print("\n%d de %d instaladores verificados." % (len(ok), len(ok) + len(pendientes)))
    if guardar:
        CFG_F.write_text(json.dumps(cfg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print("config.json actualizado.")
    return 1 if pendientes else 0


if __name__ == "__main__":
    sys.exit(main())
