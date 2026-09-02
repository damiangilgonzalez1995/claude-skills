"""Instala las skills de este repo en ~/.claude/skills.

Por que hace falta un instalador
--------------------------------
Claude Code descubre las skills personales en ~/.claude/skills/<nombre>/SKILL.md,
a UN SOLO NIVEL. Una skill dentro de una subcarpeta de categoria no se descubre
(comprobado: "Unknown skill").

Este repo esta organizado en carpetas de categoria para que se entienda. El
instalador lo aplana al copiarlo al directorio donde Claude Code mira.

    repo                                  ->  instalado
    3-frontend/animar/SKILL.md            ->  ~/.claude/skills/animar/SKILL.md

Uso
---
    python instalar.py            # instala
    python instalar.py --dry-run  # dice que haria, sin tocar nada
    python instalar.py --limpiar  # ademas borra del destino lo que ya no esta en el repo
"""

import argparse
import os
import shutil
import sys

CATEGORIAS = [
    "1-planificar",
    "2-backend",
    "3-frontend",
    "4-revisar-y-cerrar",
    "9-otras",
]

# El directorio donde Claude Code busca las skills personales.
DESTINO = os.path.expanduser("~/.claude/skills")

# Reservado por Claude Code para las skills sincronizadas desde claude.ai.
RESERVADOS = {"synced"}

RAIZ = os.path.dirname(os.path.abspath(__file__))


def skills_del_repo():
    """Devuelve [(nombre, ruta_origen)] recorriendo las carpetas de categoria."""
    encontradas = []
    for categoria in CATEGORIAS:
        ruta_cat = os.path.join(RAIZ, categoria)
        if not os.path.isdir(ruta_cat):
            continue
        for nombre in sorted(os.listdir(ruta_cat)):
            ruta = os.path.join(ruta_cat, nombre)
            if not os.path.isdir(ruta):
                continue
            if not os.path.isfile(os.path.join(ruta, "SKILL.md")):
                print("  AVISO  %s/%s no tiene SKILL.md, se salta" % (categoria, nombre))
                continue
            encontradas.append((nombre, ruta))
    return encontradas


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="no toca nada, solo informa")
    parser.add_argument("--limpiar", action="store_true",
                        help="borra del destino las skills que ya no estan en el repo")
    args = parser.parse_args()

    skills = skills_del_repo()
    if not skills:
        print("No se encontro ninguna skill. Estas ejecutando esto desde el repo?")
        return 1

    # Un mismo nombre en dos categorias se instalaria dos veces sobre si mismo.
    vistos = {}
    duplicados = []
    for nombre, ruta in skills:
        if nombre in vistos:
            duplicados.append((nombre, vistos[nombre], ruta))
        vistos[nombre] = ruta
    if duplicados:
        print("ERROR: hay nombres repetidos en categorias distintas:")
        for nombre, a, b in duplicados:
            print("  %s: %s  y  %s" % (nombre, a, b))
        return 1

    if not args.dry_run:
        os.makedirs(DESTINO, exist_ok=True)

    for nombre, origen in skills:
        destino = os.path.join(DESTINO, nombre)
        if args.dry_run:
            print("  instalaria  %s" % nombre)
            continue
        if os.path.isdir(destino):
            shutil.rmtree(destino)
        shutil.copytree(origen, destino)
        print("  %s" % nombre)

    print("\n%d skills en %s" % (len(skills), DESTINO))

    # Lo que hay en el destino y no viene del repo: puede ser una skill que
    # borraste, o algo instalado por otra via. No se toca salvo que lo pidas.
    if os.path.isdir(DESTINO):
        del_repo = set(n for n, _ in skills)
        sobrantes = []
        for nombre in sorted(os.listdir(DESTINO)):
            ruta = os.path.join(DESTINO, nombre)
            if not os.path.isdir(ruta) or nombre in RESERVADOS or nombre in del_repo:
                continue
            if os.path.isfile(os.path.join(ruta, "SKILL.md")):
                sobrantes.append(nombre)
        if sobrantes:
            print("\nEn el destino hay skills que no vienen de este repo:")
            for nombre in sobrantes:
                print("  %s" % nombre)
            if args.limpiar and not args.dry_run:
                for nombre in sobrantes:
                    shutil.rmtree(os.path.join(DESTINO, nombre))
                    print("  borrada %s" % nombre)
            elif not args.limpiar:
                print("  (se dejan tal cual; usa --limpiar para borrarlas)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
