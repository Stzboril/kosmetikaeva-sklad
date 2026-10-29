# ke-ozivi-v10.js (29. 10. 2026) – NA WEBU

Majitel (screenshot, výrobek 1 179 Kč × 5 ks): „toto taky neodpovídá, text je že je výdejní místo zdarma, když by měla být zdarma celá doprava.“

- Příčina (v9, msHTML): při prázdném košíku a výrobku, který pokryje 1. hranici (2 500 Kč), vždy text msEmptyOk „S tímto výrobkem máte výdejní místo zdarma.“ – i když cena × množství pokryje i 3 500 Kč (kurýr zdarma). Stejně u neprázdného košíku („… Tento výrobek to dorovná.“ jen k výdejnímu místu).
- Oprava: nové texty CZ msEmptyAll „S tímto výrobkem máte dopravu zdarma – na výdejní místo i kurýrem.“ a msCoverAll „S tímto výrobkem budete mít dopravu zdarma – na výdejní místo i kurýrem.“; v msHTML: `else if (tr.m.length > 1 && f.tot + f.add >= max) t = f.tot <= 0 ? T.msEmptyAll : T.msCoverAll;`. SK (jedna hranice 120 €) beze změny.
- Soubor /user/documents/upload/CSS/ke-ozivi-v10.js (35 123 B, SHA-256 4453ef59c53ed0b7dd72b42208cb10019320f1b49b6e7d047faafd6d0482710c), zápatí HTML kódů v9 → v10 (komentář doplněn). Záloha zápatí: localStorage keHtmlKodyBackup_20261029_ozivi10. Návrat = ke-ozivi-v9.js.
- Ověřeno živě (očni krém 599 Kč): 1 ks „Ještě 2 331 Kč a výdejní místo máte zdarma.“, 6 ks „S tímto výrobkem budete mít dopravu zdarma – na výdejní místo i kurýrem.“; s prázdným košíkem (test) 5 ks „… výdejní místo zdarma.“, 6 ks „… máte dopravu zdarma – na výdejní místo i kurýrem.“
- Další verze = ke-ozivi-v11.js.
