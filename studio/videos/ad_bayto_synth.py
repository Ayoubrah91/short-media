# Provisional word timings for the Bayto ad (replaced by the real transcript later)
import json, re
script = ("Je vais te donner l'astuce ultime pour booster ton logement à fond : des photos de pro. "
 "Je sais, c'est galère. Il faut trouver un photographe, attendre qu'il soit dispo, tout mettre en place… et attendre les retouches. "
 "Mais voilà l'astuce ultime : une appli qui s'appelle Bayto. Tu prends tes photos avec ton téléphone, en mode 0,5, depuis un coin de la pièce. Tu les donnes à Bayto… "
 "et en un seul clic, il transforme tout : il tend les draps, dresse la table, range la cuisine, allume la télé. Tes photos sont prêtes pour Airbnb. Et tes trois premières photos sont offertes ! "
 "Et n'oublie pas : abonne-toi, et utilise Bayto.tech pour booster ton logement !")
toks = script.split()
t = 0.15; out = []
for w in toks:
    if w in (':', '!', '?'):
        if out: out[-1]['text'] += ' ' + w
        t += 0.25; continue
    d = 0.11 + 0.042 * len(w)
    out.append({'text': w, 'start': round(t, 3), 'end': round(t + d, 3), 'type': 'word'})
    t += d + 0.06
    if w.endswith(','): t += 0.16
    if w.endswith('.') or w.endswith('!'): t += 0.38
    if w.endswith('…'): t += 0.35
json.dump({'words': out}, open('videos/ad_bayto_words.json', 'w', encoding='utf-8'), ensure_ascii=False)
print('synthetic words', len(out), 'end', round(t, 2))
