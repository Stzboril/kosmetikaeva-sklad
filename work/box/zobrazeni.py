import re
PRESKOCIT = {'EAU DE PARFUM', 'EAU DE PARFUM II', 'BODY', 'FOR HER', 'POUR FEMME', 'Woman', 'BLEU DE CHANEL'}
RUCNE = {
    'JOY BY DIOR': 'Joy', 'BOSS Bottled': 'Bottled', 'THE NARCOTICS GOOD GIRL GONE BAD': 'Good Girl Gone Bad',
    'BECAUSE IT ́S': "Because It's", 'L. 12. 12 WHITE BLANC': 'L.12.12 Blanc', 'MOLECULE01+MANDARIN': 'Molecule 01 + Mandarin',
    'ANGE OU DEMON LE SECRET': 'Ange ou Démon Le Secret', 'LA VIE EST BELLE': 'La Vie est Belle',
    'LA NUIT TRESOR NUDE': 'La Nuit Trésor Nude', 'ECLAT D`ARPEGE': "Éclat d'Arpège", 'J`ADORE': "J'adore",
    'L´INTERDIT': "L'Interdit", 'L`IMPERATRICE 3': "L'Impératrice 3", 'BAL D’AFRIQUE': "Bal d'Afrique",
    'BOIS D‘ARGENT': "Bois d'Argent", 'DEVIL’S INTRIGUE': "Devil's Intrigue", 'MYSLF': 'MYSLF', 'NO. 5': 'No. 5',
    'Y for men': 'Y for Men', 'THE ONE FOR MEN': 'The One for Men', 'EARL GREY & CUCUMBER': 'Earl Grey & Cucumber',
    'LIME BASIL & MANDARIN': 'Lime Basil & Mandarin', 'WOOD SAGE & SEA SALT': 'Wood Sage & Sea Salt',
    'LIGHT BLUE POUR HOMME': 'Light Blue pour Homme', 'STRONGER WITH YOU': 'Stronger with You',
    'A LA ROSE': 'À la Rose', 'ACQUA DI GIOIA': 'Acqua di Gioia', 'ACQUA DI GIÒ': 'Acqua di Giò',
    'SÌ': 'Sì', 'PINK MOLECULE 090.09': 'Pink Molecule 090.09', 'MOLECULE 02': 'Molecule 02',
    'CHANCE EAU FRAÎCHE': 'Chance Eau Fraîche', 'CHANCE EAU TENDRE': 'Chance Eau Tendre', 'MAN EAU FRAÎCHE': 'Man Eau Fraîche',
    'STARS LA CAPITALE': 'Stars La Capitale', 'Scandal Pour Homme': 'Scandal pour Homme',
}
MALA = {'in', 'a', 'di', 'de', 'la', 'le', 'du', 'des', 'et', 'en', 'pour', 'for', 'with', 'of', 'ou', 'est', 'by'}
def zobraz(v):
    v = (v or '').strip()
    if not v or v in PRESKOCIT:
        return None
    if v in RUCNE:
        return RUCNE[v]
    if v != v.upper():
        return v  # už má velká/malá písmena
    slova = []
    for i, w in enumerate(v.split()):
        lw = w.lower()
        slova.append(lw if (i > 0 and lw in MALA) else lw[:1].upper() + lw[1:])
    return ' '.join(slova)
if __name__ == '__main__':
    import json
    z = json.load(open('/home/claude/work/essens_zam.json'))
    for v in sorted({x[0] for x in z.values() if x[0]}):
        print(repr(v), '->', zobraz(v))
