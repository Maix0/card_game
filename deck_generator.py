import json

# Carte 1 :
tank = {"name":"Tank","atk":1,"vie":1,"cout":1,"path":"./assets/tank.gif","qte":4, "taunt":False}
# Carte 2 :
panda_roux = {"name":"Panda roux","atk":1,"vie":2,"cout":2,"path":"./assets/panda.gif",
              "qte":3,"taunt":False}
# Carte 3 :
canard_en_plastique = {"name":"Canard en \
plastique","atk":3,"vie":2,"cout":3,"path":"./assets/canard.gif","qte":1, "taunt":True}
# Carte 4 :
palpatine = {"name":"Palpatine","atk":4,"vie":2,"cout":4,
             "path":"./assets/palpatine.gif","qte":1, "taunt":False}
# Carte 5 :
terminator = {"name":"Terminator","atk":2,"vie":3,"cout":3,
              "path":"./assets/terminator.gif","qte":1,"taunt":False}
# Carte 6 :
sid = {"name":"Sid","atk":3,"vie":3,"cout":3,
       "path":"./assets/sid.gif","qte":1,"taunt":False}
# Carte 7 :
patchouli = {"name":"Patchouli","atk":2,"vie":1,"cout":1,
             "path":"./assets/patchouli.gif","qte":3,"taunt":False}
# Carte 8 :
moussa = {"name":"Moussa","atk":2,"vie":3,"cout":3,
          "path":"./assets/moussa.gif","qte":1,"taunt":True}
# Carte 9 :
projecteur = {"name":"Projecteur Epson","atk":4,"vie":4,"cout":4,
              "path":"./assets/proj.gif","qte":1,"taunt":True}
# Carte 10 :
quenouille = {"name":"Quenouille","atk":2,"vie":2,"cout":2,
              "path":"./assets/quenouille.gif","qte":2,"taunt":False}
# Carte 11 :v
devoir_maison = {"name":"Devoir Maison","atk":7,"vie":5,"cout":7,
                 "path":"./assets/dmmaths.gif","qte":1,"taunt":True}
# Carte 12 :
ronald = {"name":"Ronald McDonald","atk":9,"vie":1,"cout":5,
          "path":"./assets/ronald.gif","qte":1,"taunt":False}

"""
    END OF CARDS DEF
    CONST DEF
"""

FORMAT = {"name":"name","atk":"attack","vie":"health","cout":"mana","path":"image", "taunt":"taunt"}
FORMAT_BL = ["qte"]
OUT_FILE = "./deck.json"
CARDS = [tank,panda_roux,canard_en_plastique,palpatine,terminator,sid,patchouli,moussa,projecteur,quenouille,devoir_maison,ronald]

"""
    END OF CONST DEF
    START GENERATOR
"""

deck = []

for definition in CARDS:
    card = {}
    for key in definition:
        if key in FORMAT:
            card[FORMAT[key]] = definition[key] if definition[key] != "placeholder"\
                                                else "./assets/patchouli.gif"
            if definition[key] == "placeholder" :
                print("def placeholder")
        else:
            if key not in FORMAT_BL:
                print("KEY `{}` not in FORMAT && FORMAT_BL for card : {}".format(key,card))
    deck += [card] * definition["qte"]

f = open(OUT_FILE,"w")
json.dump(deck,f)
f.close()
