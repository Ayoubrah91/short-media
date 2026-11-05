# BRIEF COMPLET — Studio vidéo « Location courte durée » × Bayto

> **À lire en entier avant toute action.** Ce document contient tout le contexte accumulé (décisions, outils, identifiants, pipeline, état du planning, tâches en cours). Il remplace la session cloud précédente : tu reprends exactement là où elle s'est arrêtée, le 5 novembre 2026 vers 17h10 (heure de Casablanca).

---

## 0. Règles absolues (non négociables)

1. **Toujours parler en français à Ayoub. Jamais en anglais.** Même pour les résumés et les erreurs.
2. **Autonomie maximale.** Ayoub veut que tout soit automatisé : il parle, tu fais tout (script → voix → montage → vérification → mise en ligne → programmation). Ne lui demande quelque chose que si c'est vraiment une décision à lui (argent, publication d'une pub sponsorisée, changement de ligne éditoriale).
3. **Minimum 3 posts par jour** (Instagram + TikTok ensemble, plus une version LinkedIn). Ayoub l'a exigé explicitement : « Minimum 3 posts par jour ».
4. **Chaque vidéo se termine par la phrase signature** (validée par Ayoub, « Parfait ») :
   > « Et n'oublie pas : abonne-toi, et utilise Bayto.tech pour booster ton logement ! »
   + la carte de fin animée (bouton « S'abonner » → « Abonné », puis carte bayto.tech « Booste ton logement »).
5. **Exactitude.** Les conseils doivent être vrais et vérifiables (centre d'aide Airbnb/Booking, sources officielles). Jamais de chiffre inventé présenté comme un fait. Exemples = exemples, présentés comme tels.
6. **Honnêteté Bayto :** pour les avant/après, n'utiliser QUE les vraies photos fournies par Ayoub (voir §12). Jamais de photo « avant » simulée/dégradée, jamais de faux résultat.
7. **Pas de contrefaçon de marque :** pas de logo Airbnb, pas d'imitation d'Airbnb. Les couleurs corail sont « inspirées », la mascotte/les icônes sont originales.
8. **Vérifier visuellement avant de publier** : générer des images fixes (stills) aux moments clés et les regarder (chevauchements, textes coupés, sous-titres).
9. Contenu **universel** (« Oublie la France… oublie le Maroc ») : conseils valables partout, pas de lois locales spécifiques sauf actu Airbnb mondiale.
10. Déclarer l'IA : `isAiGenerated: true` (Instagram), `isAigc: true` (TikTok). Pour une **pub Bayto**, TikTok `commercialContentOwnBrand: true`.

---

## 1. Qui, quoi, pourquoi

- **Ayoub** : hôte en location courte durée (gère un logement au Maroc), fondateur de **Bayto** (https://bayto.tech), le « studio photo IA de ta location » : on dépose ses photos de logement, l'IA les optimise pour Airbnb/Booking.
- **Objectif des réseaux** : faire grandir une audience d'hôtes Airbnb/Booking francophones avec des conseils utiles, et amener du trafic vers Bayto.
- **Comptes** (tous connectés dans Metricool, marque `7690346`) : Instagram, TikTok (**@bayto.tech**), LinkedIn.
- **Voix** : la voix clonée d'Ayoub, en français, tutoiement, ton dynamique.

## 2. Historique et décisions (chronologie)

1. Départ sur des vidéos « IA en darija » → **abandonné**. Puis : « on doit rester que sur du Airbnb… on oublie le reste ».
2. Passage au **français**, contenu **universel** (pas France, pas Maroc).
3. 1er style (moteur `engine.html`) : thème corail type Airbnb + mascotte maison pixel originale → séries f1–f8 (déjà publiées les 4–5 nov.).
4. Ayoub envoie une vidéo de référence plus animée → **nouveau style « épisodes » (moteur `engine2.html`)**, validé : « C'est bon, c'est parfait ». **C'est le style standard maintenant.**
5. Organisation : d'abord 1 post/jour → refusé → **minimum 3 posts/jour**.
6. Ajout de la **fin Bayto.tech** sur toutes les vidéos (validée).
7. Demande d'une **pub sponsorisée Bayto** « l'astuce ultime » (photos optimisées, mode 0,5, Bayto transforme tout en un clic), avec **uniquement ses 5 paires avant/après** (fournies dans un zip). Montage prêt (§13), voix à générer avec VoiceStudio.
8. Ayoub a installé **VoiceStudio** (voix clonée gratuite, serveur MCP local `http://127.0.0.1:3900/mcp/`, en-tête `X-OmniVoice-Client-Id: claude-code`). La session cloud ne pouvait pas l'atteindre → **décision : tout faire dans UNE session locale sur son ordinateur** (celle-ci).

## 3. Ligne éditoriale et formats

### Série « Location courte durée · Ép. N » (format standard)
- Durée 40–50 s, vertical 1080×1920, 30 i/s.
- Structure du script :
  1. **Accroche** (problème/question choc, 1–2 phrases).
  2. **Contexte** (pourquoi ça compte, 1–2 phrases).
  3. **2 à 4 points** (« Premier critère… », « Option un… », « Règle un… ») — chaque point = une scène.
  4. **Conclusion / réflexe** (1 phrase).
  5. **CTA épisode** : « Abonne-toi : dans le prochain épisode, <sujet suivant>. »
  6. **Phrase signature** : « Et n'oublie pas : abonne-toi, et utilise Bayto.tech pour booster ton logement ! »
- Ton : tutoiement, phrases courtes, chiffres concrets (exemples clairement présentés comme exemples).
- Légende Instagram/TikTok (modèle) :
  ```
  Ép. N — <accroche courte + emoji>
  <1 ligne de promesse>

  Commente MOTCLÉ et je t'envoie <la checklist/le guide/…> 👇 (ou lien en bio)

  #airbnb #locationcourteduree #hoteairbnb #<thème> #<thème>
  ```
- Titre TikTok (obligatoire) : « <Sujet> (Ép. N) ».
- Version **LinkedIn** : même vidéo, texte professionnel (3 paragraphes : constat → méthode → lien), lien vers la page ressources `https://ressources-hote.vercel.app/#<ancre>`, hashtags pro (#LocationCourteDurée #Airbnb #RevenueManagement #ExpérienceClient #Hospitalité…).

### Mots-clés déjà utilisés (une section existe pour chacun sur la page ressources)
RÈGLES (#regles), ANNONCE (#annonce), AVIS (#avis), CALENDRIER (#calendrier), SAISON (#saison), LIVRET (#livret), SYNCHRO (#synchro), SUPERHOST (#superhost), BADGE (#badge), MENAGE (#menage), REVENUS (#revenus), ARRIVEE (#arrivee), PHOTOS (#photos), REPONSE (#reponse), EQUIPEMENTS (#equipements).
**Chaque nouveau mot-clé = ajouter sa section sur la page ressources (§10) avant publication.**

## 4. Identité visuelle (moteur `engine2.html`)

- Fond clair (#F6F6F6 + halos corail), cartes blanches arrondies, ombres douces.
- Couleurs : corail `#FF385C`, encre `#1F1F1F`, gris `#8E8E8E`, vert validation `#00A699`, rouge refus `#E5484D`. Bayto : ambre `#FFB547`, nuit `#0B0C10`, crème `#F7F2EA`.
- En-tête : pastille « LOCATION COURTE DURÉE · ÉP. N » + barre de progression segmentée (chapitres).
- Sous-titres karaoké en haut de la zone basse (top 1230 px), mots importants en noir gras (`emph`), mots-clés en corail (`coral`).
- Police : Inter Tight (fichiers locaux dans `fonts/`).
- Logo Bayto (officiel, repris du code du site) : carré arrondi ambre avec un « b » noir + mot « bayto. » avec point ambre. Constante `LOGO` dans `engine2.html`.

## 5. Outils, accès et identifiants

| Outil | Usage | Détails |
|---|---|---|
| **VoiceStudio** (MCP local) | Voix off gratuite avec la voix clonée d'Ayoub | `http://127.0.0.1:3900/mcp/`, en-tête `X-OmniVoice-Client-Id: claude-code`. L'app VoiceStudio doit être ouverte. Liste ses outils au démarrage et utilise la voix d'Ayoub. Pas de balises type [excited] : écris le texte naturellement (ponctuation = rythme). |
| **ElevenLabs** (connecteur claude.ai) | Secours voix + **transcription mot à mot** (Scribe) | Voix « Ayoub » `voice_id = Pc7QntN6aDxotShA2wOF`, modèle `eleven_v4`, balises [excited]/[serious]/[curious]. Coût ≈ 1 crédit/caractère/prise ; **il reste ~410 crédits** (quota 38 576/mois) → réserver ElevenLabs à la transcription. Transcription : `creative_attach_reference_file(url=…, flow_id)` puis `creative_transcribe_audio(model_id="eleven_scribe_v1", connect_from=[node_id])`, puis `creative_get_flow_run_status` → `words_download_url`. |
| **Metricool** (connecteur) | Programmation IG + TikTok + LinkedIn | Marque `blogId = 7690346`, fuseau `Africa/Casablanca`. Voir §9. |
| **GitHub** | Hébergement public des MP4 + ce studio | Dépôt public `Ayoubrah91/short-media`. Vidéos dans `videos/`, URL publique : `https://raw.githubusercontent.com/Ayoubrah91/short-media/main/videos/<fichier>.mp4` (Metricool copie ensuite le fichier chez lui). |
| **Vercel** (connecteur) | Page ressources (lien en bio / réponses aux mots-clés) | Équipe `team_HdqTdaewV03dMtU6UzINwx1P`, projet `ressources-hote`, URL https://ressources-hote.vercel.app. Source : `studio/hub/index.html`. |
| **Windsor.ai** (connecteur) | Lecture stats + actions Instagram (répondre/masquer un commentaire) | Le connecteur Instagram est lié au compte **bayto.tech**. Pas d'envoi de DM via API. |
| vidIQ | Recherche de tendances | Peu de crédits ; le scraping TikTok/Instagram ne marche pas, utiliser la recherche web. |

## 6. Installation (une seule fois, sur cet ordinateur)

```bash
git clone https://github.com/Ayoubrah91/short-media.git   # ou git pull s'il existe déjà
cd short-media/studio
npm install                 # installe playwright
npx playwright install chromium
# ffmpeg doit être dans le PATH : macOS → brew install ffmpeg ; Windows → winget install Gyan.FFmpeg ; Linux → apt install ffmpeg
python3 -m pip install numpy   # pour admix.py (effets sonores)
node --version && ffmpeg -version && python3 -c "import numpy"
```
Test : `node render.mjs videos/ep6_photos.json stills/test --stills 5,20` doit produire 2 PNG.
Conseil : crée dans le dossier du projet (VIDEO BAYTO) un `CLAUDE.md` qui dit « Lis short-media/studio/BRIEF.md en entier au début de chaque session et parle toujours en français. »

## 7. Pipeline de production (pas à pas)

1. **Sujet** : recherche web (centre d'aide Airbnb, actus hôtes, tendances TikTok/IG via recherche web). Vérifie les faits.
2. **Script** (§3), inclure la phrase signature à la fin. ~110–130 mots pour 45 s.
3. **Voix** : VoiceStudio → `audio/<nom>.mp3` (ou .wav).
4. **Timings mot à mot** : transcription ElevenLabs Scribe (voir §5) → enregistrer au format :
   `videos/<nom>_words.json` = `{"words":[{"text":"Bonjour","start":0.12,"end":0.48,"type":"word"}, …]}`
   (Si l'audio est sur GitHub, l'URL raw sert directement à `creative_attach_reference_file`.)
   Secours sans ElevenLabs : `pip install faster-whisper` puis transcription avec `word_timestamps=True` (langue `fr`), même format.
5. **Plan** `videos/<nom>_plan.json` : liste de scènes (« beats ») avec des **ancres** sur les mots (§8). S'inspirer des plans existants (`ep1…ep8_*_plan.json`, `ad_bayto_plan.json`).
6. **Spec** : `python3 build_spec.py videos/<nom>_plan.json videos/<nom>_words.json videos/<nom>.json`
7. **Contrôle visuel** : `node render.mjs videos/<nom>.json stills/<nom> --stills 2,8,15,22,30,38` puis regarder les PNG (ou une planche : `ffmpeg -pattern_type glob -i 'stills/<nom>/*.png' -vf "scale=270:480,tile=6x2" -frames:v 1 stills/<nom>_sheet.png`).
8. **(Option) effets sonores** : `python3 admix.py videos/<nom>.json audio/<nom>.mp3 audio/<nom>_mix.wav` (clics, déclencheur photo, scintillements, discrets sous la voix).
9. **Rendu** : `node render.mjs videos/<nom>.json out/<nom>.mp4 --audio audio/<nom>.mp3` (ou le `_mix.wav`). ~2 min pour 45 s.
10. **Contrôle** : `ffprobe` (durée, piste audio), extraire 2–3 images du MP4 final.
11. **Mise en ligne** : copier dans `short-media/videos/`, `git add/commit/push`, vérifier que l'URL raw répond 200.
12. **Programmation** Metricool (§9) : IG+TikTok ensemble + LinkedIn séparé, au même horaire.
13. **Page ressources** : ajouter la section du mot-clé et redéployer (§10).

### Ajouter la fin Bayto.tech à une vidéo qui ne l'a pas (cas particulier)
Avec VoiceStudio, mets simplement la phrase signature à la fin du script (même voix, recommandé). Pour une vidéo déjà rendue sans la fin :
`./outro_concat.sh videos/outro/<nom>.json out/<nom>.mp4 <secondes_à_garder> out/<nom>_bt.mp4`
(spec de fin = carte « S'abonner » + carte bayto.tech, voix `audio/outro_bayto.mp3` ; `<secondes_à_garder>` = fin du dernier mot + 0,6 s).

## 8. Référence du moteur `engine2.html`

### Spec / plan (clés de premier niveau)
`name`, `engine: "engine2.html"`, `series: "LOCATION COURTE DURÉE"`, `ep: N` (ou `epLabel: "· L'ASTUCE ULTIME"`, ou `ep: 0` = pas de numéro), `chapters: [ancres]` (segments de la barre de progression), `emph: [mots]`, `coral: [mots]`, `beats: [...]`, `duration: "auto"` (= fin du dernier mot + 1,3 s).

### Ancres (résolues par `build_spec.py`)
- `"@mot"` = début du premier mot égal à (ou commençant par) `mot`, **après la position de l'ancre précédente** (on suit l'ordre du script).
- `"@mot#2"` = 2ᵉ occurrence dans tout le texte ; `"@mot/e"` = fin du mot ; `"@mot+0.3"` / `"@mot-0.2"` = décalage en secondes.
- Les clés `end`, `happy`, `chapters` ne font pas avancer le curseur ; **`chapters` est résolu depuis le début du texte → utiliser `#N` ou des mots uniques.**
- Pièges connus : la correspondance par préfixe fait que `@règle` attrape aussi « règles » (décaler les `#N`) ; les élisions sont un seul mot (`@d'ancienneté`, `@l'astuce`, `@n'oublie`, `@qu'il`) ; les nombres arrivent souvent en chiffres (`@0,5`, `@80`) — **vérifie le texte réel de la transcription**.

### Types de scènes (`type`) et paramètres
Toutes les scènes : `at` (début ; la scène dure jusqu'au `at` suivant) et `chips: [{at, text, x, y, kind:"coral"|"dark"|blanc, icon}]` (pastilles positionnées en px dans la zone 1080×1000 qui commence à y=180 de l'écran).
- `chapter` : `num`, `label` (gros numéro + étiquette).
- `icon` : `icon`, `label`, `onAt` (tuile devient corail), `coins` (pluie de « € »).
- `grid` : `items:[{icon,label,at,onAt,offAt}]` (2 colonnes).
- `gauge` : `to`, `suffix`, `label`, `countAt`, `max`, `dec`.
- `list` : `title`, `items:[{at,text,mark:"ok"|"no",markAt}]`.
- `results` : `query`, `youAt`, `riseAt` (ton annonce remonte), `badgeAt`, `badge`.
- `receipt` : `lines:[{label,value,at}]`, `total`, `totalLabel`, `totalAt`, `sub`.
- `compare` : `cols:[{k,big,s,tone:"good"|"bad",at}]` (big > 5 caractères → police réduite).
- `waterfall` : `startLabel`, `steps:[{label,cut,at}]`, `endLabel`, `endValue`, `endAt`.
- `stars` : `label`, `to` (note), `fillAt`.
- `medal` : `label` (+ confettis). `podium` : `bars:[{k,v,hgt,at,color}]`. `clock` : `time`, `sub`, `moonAt`.
- `phone` : `code`, `typeAt`, `okAt`, `okText`. `chat` : `msgs:[{me,text,at}]`, `photosAt`. `apt` : illustration salon + `caption`.
- `subscribe` : `clickAt`, `next`, `nextAt`, `nextIcon`, `nextKicker`.
- `brand` (fin Bayto.tech) : `clickAt` (S'abonner→Abonné), `brandAt`, `tag`, `logo:"bayto"` (logo officiel au lieu de la maison).
- **Pub / Bayto** : `hero` (`kicker`, `l1`, `l2`, `l2At`, `burstAt`, `sub`, `subAt`) ; `ba` avant/après (`before`, `after`, `revealAt`, `label`, `beforeLabel`, `afterLabel`) ; `cam` téléphone en mode photo (`img`, `zoomAt` = passage 1× → 0,5, `shootAt`, `s0`) ; `upload` appli Bayto (`thumbs`, `dropAt`, `clickAt`, `barDur`, `status`, `btn`, `cx0/cy0/cx1/cy1` = trajet du curseur) ; `logo` (`logoAt`, `tagAt`, `tag`) ; `grid6` (`imgs` ×5 + tuile finale `endText`, `endAt`) ; `offer` (`num`, `l1`, `l2`, `tags`, `url`, `urlAt`).
- Icônes disponibles : house, star, chat, ban, cal, badge, heart, search, broom, euro, lock, key, moon, phone, user, bell, check, x, clock, bolt, trophy, camera, wifi, car, washer, desk, snow, pot, bed, bath, trash, tag, cursor.

### Mise en page (leçons apprises)
- Dans les scènes `icon` (agrandies ×1,4), garder les pastilles à `y ≤ 800`, sinon elles touchent les sous-titres.
- Pastilles sous une carte : `y ≈ 820–880`. Au-dessus : `y ≈ 90–130`.
- Toujours vérifier les stills avant le rendu final.

## 9. Publication Metricool

- `createScheduledPost(blogId="7690346", date="2026-11-08T16:00:00+00:00", info=<JSON>)`.
- **Instagram + TikTok (même post)** :
```json
{"autoPublish":true,"descendants":[],"draft":false,"firstCommentText":"","hasNotReadNotes":false,
 "media":["https://raw.githubusercontent.com/Ayoubrah91/short-media/main/videos/<fichier>.mp4"],"mediaAltText":[],
 "providers":[{"network":"instagram"},{"network":"tiktok"}],
 "publicationDate":{"dateTime":"2026-11-08T16:00:00","timezone":"Africa/Casablanca"},
 "shortener":false,"smartLinkData":{"ids":[]},"text":"<légende>",
 "instagramData":{"type":"REEL","showReelOnFeed":true,"isAiGenerated":true},
 "tiktokData":{"privacyOption":"PUBLIC_TO_EVERYONE","title":"<Sujet> (Ép. N)","photoCoverIndex":0,"isAigc":true}}
```
- **LinkedIn (post séparé, même heure)** : `providers:[{"network":"linkedin"}]`, `linkedinData:{"previewIncluded":true,"type":"post"}`, texte pro + lien page ressources.
- **Pub Bayto** : ajouter dans `tiktokData` `"commercialContentOwnBrand": true` ; on peut fixer la couverture avec `"videoCoverMilliseconds": 2600`.
- **Modifier un post** : `updateScheduledPost(id, uuid, info complet)` — renvoyer TOUT le contenu ; **l'id change** après chaque modification (l'uuid reste).
- Ne jamais mettre 2 posts IG/TikTok à la même heure.
- **Meilleurs créneaux** (données Metricool, jeudi) : Instagram pic 10h, puis 12h et 18h ; TikTok 18h, 10h, 12h. Grille actuelle : **12h, 16h, 20h** (+ 10h/14h/18h si besoin).
- Incident connu : le 5 nov. à 12h, TikTok a échoué (« refresh token »), puis est revenu tout seul. Si les échecs se répètent → Ayoub doit reconnecter TikTok dans Metricool.

## 10. Page ressources (Vercel)

- Source : `studio/hub/index.html` (sections `<details id="…">` avec une étiquette du mot-clé, ouverture automatique via `#ancre`).
- Déploiement : `create_deployment` (teamId `team_HdqTdaewV03dMtU6UzINwx1P`), `requestBody = {"name":"ressources-hote","project":"ressources-hote","target":"production","projectSettings":{"framework":null},"files":[{"file":"index.html","encoding":"utf-8","data":"<contenu complet>"}]}`.
- Vérifier ensuite : `curl -s https://ressources-hote.vercel.app/ | grep -o 'id="[a-z]*"'`.

## 11. Commentaires et DM

- Les réponses automatiques par mot-clé (commentaire → DM avec le lien de la page ressources) se configurent **côté Ayoub** : Meta Business Suite (Instagram, gratuit) et/ou Metricool Flows (réponses publiques). TikTok : nécessite un compte TikTok Business.
- Windsor.ai permet de répondre/masquer des commentaires Instagram (compte bayto.tech) ; pas de DM.
- À rappeler à Ayoub quand un nouveau mot-clé apparaît : l'ajouter dans son automatisation.

## 12. Bayto — faits produit (pour toute pub)

Source : code et site officiels (https://bayto.tech).
- Promesse : « Des photos qui donnent envie de réserver. » — « Le studio photo de votre location ».
- **Ce que Bayto fait** : allume les lumières qui existent déjà ; corrige la balance des blancs et l'exposition ; redresse les photos mal cadrées (lignes droites, horizon, perspective) ; tend les draps et aligne les coussins ; range le désordre passager (câbles, sacs, produits) ; dresse la table avec le bon nombre de couverts ; met l'écran TV en valeur (noir, Netflix ou logo) ; recadre au format Airbnb.
- **Ce qu'il ne fera jamais** : ajouter un meuble/équipement absent, agrandir une pièce, changer la vue, modifier murs/sols/fenêtres, inventer un angle, remplacer la déco. Charte : « Sublimer, oui. Tricher, jamais. »
- Fonctionnement : déposer ses photos (même HEIC depuis l'iPhone) → diagnostic gratuit → photos prêtes en quelques minutes.
- Conseil de prise de vue (affiché dans l'appli) : depuis un coin, à hauteur de poitrine, bien droit, **en mode 0,5x (grand angle)**.
- Offre : **3 photos offertes, sans carte bancaire**, diagnostic gratuit ; puis packs (ex. 9 € les 10 photos).
- **Photos avant/après à utiliser (les SEULES autorisées pour la pub)** — `studio/assets/ad/` :
  - chambre_avant.jpg → chambre_apres.jpg (draps blancs tendus, serviettes roulées, lampes allumées)
  - table_avant.jpg → table_apres.jpg (table dressée, fleurs, lampe)
  - cuisine_avant.jpg → cuisine_apres.jpg (seau/tapis rangés, cuisine nette)
  - salon_avant.jpg → salon_apres.jpg (TV allumée Netflix, fleurs, lumière chaude)
  - bain_avant.jpg → bain_apres.jpg (savon rangé, serviettes roulées)
  (Originaux : zip envoyé par Ayoub ; « avant » = PNG 16:9, « après » = JPG 3:2 nommés 03-salon-2, 06-salon-5, 15-chambre-5, 22-cuisine-3, 28-salle-de-bain-1.)

## 13. État actuel au 5 nov. 2026, 17h10 (heure de Casablanca)

### Déjà publiés
- 5 nov. : 10h CALENDRIER, 12h SAISON (TikTok en échec ce jour-là), 14h LIVRET (avec fin Bayto), 16h SYNCHRO (avec fin Bayto) — IG + TikTok + LinkedIn.
- Séries f1–f3 (règles du 20 novembre, annonce) publiées avant.

### Programmés (ids Metricool actuels ; vidéos avec fin Bayto `*_bt.mp4`)
| Date | Heure | Vidéo | IG+TikTok id | LinkedIn id | Mot-clé |
|---|---|---|---|---|---|
| 5 nov. | 20h | Ép. 1 Superhost | 417715582 | 417715647 | SUPERHOST |
| 6 nov. | 12h | Ép. 2 Coup de cœur | 417819599 | 417820792 | BADGE |
| 6 nov. | 16h | Ép. 3 Frais de ménage | 417820875 | 417820960 | MENAGE |
| 6 nov. | 20h | Ép. 4 Revenus | 417821051 | 417821116 | REVENUS |
| 7 nov. | 12h | Ép. 5 Arrivée autonome | 417821304 | 417821406 | ARRIVEE |
| 7 nov. | 16h | Ép. 6 Photos | 417821511 | 417821848 | PHOTOS |
| 7 nov. | 20h | Ép. 7 Avis négatif | 417822111 | 417824476 | REPONSE |
| 8 nov. | 12h | Ép. 8 Équipements | 417824564 | 417824619 | EQUIPEMENTS |

### À faire, dans cet ordre
1. **Installation** (§6) et test de rendu.
2. **Pub Bayto « L'astuce ultime »** (prioritaire, Ayoub voulait 18h aujourd'hui ; si 18h est passé → **21h aujourd'hui**, sinon le meilleur créneau suivant) :
   - Voix VoiceStudio avec le **script A** (§14) → `audio/bayto_pub_voix.mp3`.
   - Transcription → `videos/ad_bayto_words.json` (remplace le fichier provisoire).
   - Regarder comment « 0,5 » est transcrit, puis `python3 videos/ad_bayto_mkplan.py "@0,5"` (ou `"@zéro"` selon la transcription).
   - `python3 build_spec.py videos/ad_bayto_plan.json videos/ad_bayto_words.json videos/ad_bayto.json` → stills → `python3 admix.py videos/ad_bayto.json audio/bayto_pub_voix.mp3 audio/ad_bayto_mix.wav` → `node render.mjs videos/ad_bayto.json out/ad_bayto.mp4 --audio audio/ad_bayto_mix.wav`.
   - Le script A contient déjà la phrase signature : **ne pas** ajouter la fin une deuxième fois.
   - Envoyer la vidéo à Ayoub, puis programmer IG+TikTok (+ `commercialContentOwnBrand: true`) + LinkedIn. Légende proposée :
     ```
     L'astuce ultime pour booster ton logement : des photos de pro… sans photographe 📸
     Mode 0,5 → Bayto → un clic : draps tendus, table dressée, cuisine rangée, télé allumée.

     👉 Tes 3 premières photos sont offertes sur bayto.tech (lien en bio)

     #airbnb #locationcourteduree #photoairbnb #hoteairbnb #bayto
     ```
     Ayoub veut ensuite la **sponsoriser** : lui demander le budget/la durée avant toute dépense publicitaire.
3. **8 nov. : il manque 2 posts** → produire Ép. 9 (script B, 16h) et Ép. 10 (script C, 20h), sections REDUCTION et CHECKLIST sur la page ressources.
4. Ensuite : **tenir 3 posts/jour en continu** (nouvelle série d'épisodes : recherche de sujets qui marchent, scripts, voix, rendu, programmation), sans attendre qu'Ayoub le demande.

## 14. Scripts prêts

### Script A — Pub Bayto « L'astuce ultime » (≈ 45 s, voix VoiceStudio, texte tel quel)
Je vais te donner l'astuce ultime pour booster ton logement à fond : des photos de pro.
Je sais, c'est galère. Il faut trouver un photographe, attendre qu'il soit dispo, tout mettre en place… et attendre les retouches.
Mais voilà l'astuce ultime : une appli qui s'appelle Bayto. Tu prends tes photos avec ton téléphone, en mode 0,5, depuis un coin de la pièce. Tu les donnes à Bayto…
et en un seul clic, il transforme tout : il tend les draps, dresse la table, range la cuisine, allume la télé. Tes photos sont prêtes pour Airbnb. Et tes trois premières photos sont offertes !
Et n'oublie pas : abonne-toi, et utilise Bayto.tech pour booster ton logement !

> Le plan `videos/ad_bayto_plan.json` (généré par `ad_bayto_mkplan.py`) est calé sur ces mots exacts : titre « L'ASTUCE ULTIME », teaser avant/après chambre, liste « Un photographe pro ? », logo Bayto, téléphone en mode 0,5, appli Bayto + bouton « Transformer mes photos », 4 avant/après (draps, table, cuisine, télé), grille « Prêtes pour Airbnb », « 3 photos offertes », carte de fin avec le logo Bayto. Un aperçu sans voix a été validé visuellement.

### Script B — Ép. 9 « Réductions semaine et mois » (mot-clé REDUCTION)
Tu veux des séjours plus longs, avec moins de ménages et moins d'arrivées à gérer ? Il y a un réglage pour ça. Sur Airbnb, tu peux activer deux réductions. La réduction à la semaine, pour les séjours de sept nuits ou plus. Et la réduction au mois, pour les séjours de vingt-huit nuits ou plus. Prenons un exemple. 80 euros la nuit, avec 10 % de réduction à la semaine. Sept nuits, c'est 560 euros… qui passent à 504 euros. Et pour toi : un seul ménage, au lieu de trois ou quatre pour des courts séjours. Le piège : une réduction trop forte. Commence petit, autour de 10 %, et regarde tes réservations. Moins de rotations, moins de fatigue. Abonne-toi : dans le prochain épisode, la checklist du ménage entre deux voyageurs. Et n'oublie pas : abonne-toi, et utilise Bayto.tech pour booster ton logement !
> Idées de scènes : `icon` cal « Séjours plus longs » (+ pastilles « Moins de ménages », « Moins d'arrivées ») → chapitre 01 « Les 2 réductions » → `compare` « À la semaine 7+ nuits » / « Au mois 28+ nuits » → chapitre 02 « L'exemple » → `receipt` 7 nuits × 80 € = 560 €, −10 % → 504 € → `compare` ménages 1 vs 3–4 → chapitre 03 « Le piège » → `gauge` 10 % « Pour commencer » → `subscribe` → `brand`.

### Script C — Ép. 10 « Checklist ménage entre deux voyageurs » (mot-clé CHECKLIST)
Un cheveu dans la salle de bain, et c'est une étoile en moins. La propreté fait partie des notes que laisse chaque voyageur. Alors voilà la checklist à suivre entre deux voyageurs, pièce par pièce. La chambre : draps propres, et un coup d'œil sous le lit. La salle de bain : cheveux, miroir, et serviettes propres. La cuisine : frigo vidé, plaques nettoyées, vaisselle propre. Et partout : poubelles vidées, sols aspirés. Enfin, le détail qui change tout : recharge les consommables. Papier toilette, savon, café. Et le réflexe pro : une photo de chaque pièce, à la fin du ménage. Si un voyageur se plaint, tu as une preuve. Abonne-toi : de nouveaux épisodes chaque semaine. Et n'oublie pas : abonne-toi, et utilise Bayto.tech pour booster ton logement !
> Idées de scènes : `stars` « Propreté » → chapitres Chambre (icône bed) / Salle de bain (bath) / Cuisine (pot) / Partout (trash) avec `list` ok → `icon` « Consommables » → `icon` camera « Une photo par pièce » + pastille « Ta preuve » → `subscribe` → `brand`.

## 15. Fichiers du studio

- `engine2.html` moteur actuel (épisodes + scènes pub) ; `engine.html` ancien moteur (f1–f8).
- `render.mjs` rendu (Playwright → JPEG → ffmpeg, 30 i/s, audio aac).
- `build_spec.py` résolution des ancres ; `admix.py` mixage voix + effets ; `outro_concat.sh` ajout de la fin Bayto.
- `videos/` plans, specs et mots (ép. 1–8, f1–f8, pub) ; `videos/outro/` specs des fins.
- `audio/` voix des épisodes + `outro_bayto.mp3` (fin Bayto, voix ElevenLabs).
- `assets/ad/` les 5 paires avant/après d'Ayoub ; `hub/index.html` page ressources ; `fonts/` polices.
- Vidéos publiées : `../videos/` (ep1–ep8, `*_bt.mp4` = avec fin Bayto, f1–f8).
