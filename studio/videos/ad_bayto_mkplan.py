import json, sys
A='assets/ad/'
ZOOM = sys.argv[1] if len(sys.argv) > 1 else '@0,5'
def C(at,text,x,y,kind='dark',icon=None):
    d={'at':at,'text':text,'x':x,'y':y,'kind':kind}
    if icon: d['icon']=icon
    return d
plan={
 'name':'ad_bayto','engine':'engine2.html','series':'LOCATION COURTE DURÉE','epLabel':"· L'ASTUCE ULTIME",'duration':'auto',
 'chapters':['@sais-0.3','@mais-0.1','@donnes-0.45','@trois-0.25'],
 'emph':["l'astuce",'ultime','booster','fond','pro','galère','photographe','dispo','place','retouches','téléphone','0,5','coin','clic','transforme','draps','table','cuisine','télé','prêtes','airbnb','trois','offertes','abonne-toi'],
 'coral':['ultime','bayto','clic','offertes','bayto.tech'],
 'beats':[
  {'type':'hero','at':0,'kicker':'JE TE DONNE','l1':"L'ASTUCE",'l2':'ULTIME','l2At':'@ultime','burstAt':'@ultime+0.1','sub':'pour booster ton logement','subAt':'@booster',
   'chips':[C('@fond','À fond',660,835,'coral','bolt')]},
  {'type':'ba','at':'@des','before':A+'chambre_avant.jpg','after':A+'chambre_apres.jpg','revealAt':'@pro','label':'Des photos de pro'},
  {'type':'list','at':'@sais-0.3','title':'Un photographe pro ?','items':[
     {'at':'@trouver','text':'Le trouver','mark':'no','markAt':'@photographe/e'},
     {'at':'@attendre','text':"Attendre qu'il soit dispo",'mark':'no','markAt':'@dispo/e'},
     {'at':'@tout','text':'Tout mettre en place','mark':'no','markAt':'@place/e'},
     {'at':'@attendre','text':'Attendre les retouches','mark':'no','markAt':'@retouches/e'}],
   'chips':[C('@galère','Galère',700,95,'coral','x')]},
  {'type':'hero','at':'@mais-0.1','kicker':'MAIS VOILÀ','l1':"L'ASTUCE",'l2':'ULTIME','l2At':'@ultime','burstAt':'@ultime+0.1'},
  {'type':'logo','at':'@une','logoAt':'@bayto','tagAt':'@bayto+0.45','tag':'Le studio photo de ta location'},
  {'type':'cam','at':'@prends-0.3','img':A+'salon_avant.jpg','zoomAt':ZOOM,'shootAt':'@pièce','s0':1.9,
   'chips':[C(ZOOM+'+0.35','Mode 0,5 : toute la pièce',215,120,'coral','camera'),C('@coin','Depuis un coin',370,830,'dark','check')]},
  {'type':'upload','at':'@donnes-0.45','dropAt':'@donnes','thumbs':[A+'chambre_avant.jpg',A+'table_avant.jpg',A+'cuisine_avant.jpg',A+'salon_avant.jpg'],
   'clickAt':'@clic','barDur':1.3,'status':'Bayto transforme tes photos…'},
  {'type':'ba','at':'@tend-0.25','before':A+'chambre_avant.jpg','after':A+'chambre_apres.jpg','revealAt':'@draps','label':'Draps tendus'},
  {'type':'ba','at':'@dresse-0.2','before':A+'table_avant.jpg','after':A+'table_apres.jpg','revealAt':'@table','label':'Table dressée'},
  {'type':'ba','at':'@range-0.2','before':A+'cuisine_avant.jpg','after':A+'cuisine_apres.jpg','revealAt':'@cuisine','label':'Cuisine rangée'},
  {'type':'ba','at':'@allume-0.2','before':A+'salon_avant.jpg','after':A+'salon_apres.jpg','revealAt':'@télé','label':'Télé allumée'},
  {'type':'grid6','at':'@tes-0.15','imgs':[A+'chambre_apres.jpg',A+'table_apres.jpg',A+'cuisine_apres.jpg',A+'salon_apres.jpg',A+'bain_apres.jpg'],'endAt':'@airbnb','endText':'Prêtes pour Airbnb'},
  {'type':'offer','at':'@trois-0.25','num':'3','l1':'photos','l2':'offertes','tags':[{'text':'Sans carte bancaire','icon':'check','kind':'dark','at':'@offertes'}],'url':'bayto.tech','urlAt':'@offertes+0.35'},
  {'type':'brand','at':"@n'oublie-0.25",'clickAt':'@abonne+0.5','brandAt':'@utilise','logo':'bayto','tag':'Booste ton logement'}
 ]}
json.dump(plan,open('videos/ad_bayto_plan.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('plan ok')
