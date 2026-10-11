#!/bin/bash
# záloha pracovních souborů (jen veřejné texty, žádné nákupní ceny) do větve prace
set -e
cd /home/claude/prace-wt
rm -rf work && mkdir work
(cd /home/claude/work && tar --exclude='eshop_kody.tsv' --exclude='__pycache__' --exclude='export_texty.json' -cf - .) | (cd work && tar -xf -)
git add -A
git commit -qm "Záloha práce $(date -u +%H:%M)" || exit 0
git push -q -u origin prace 2>&1 | tail -1
