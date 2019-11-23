import json

# Carte 1 :
tank = {"name":"Tank","atk":1,"vie":1,"cout":1,"path":"path_","qte":4, "taunt":False}
# Carte 2 :
panda_roux = {"name":"Panda roux","atk":1,"vie":2,"cout":2,"path":"path_","qte":3,"taunt":False}
# Carte 3 :
canard_en_plastique = {"name":"Canard en \
plastique","atk":3,"vie":2,"cout":3,"path":"path_","qte":1, "taunt":True}
# Carte 4 :
palpatine = {"name":"Palpatine","atk":4,"vie":2,"cout":4,"path":"path_","qte":1, "taunt":False}
# Carte 5 :
terminator = {"name":"Terminator","atk":2,"vie":3,"cout":3,"path":"path_","qte":1,"taunt":False}
# Carte 6 :
sid = {"name":"Sid","atk":3,"vie":3,"cout":3,"path":"path_","qte":1,"taunt":False}
# Carte 7 :
patchouli = {"name":"Patchouli","atk":2,"vie":1,"cout":1,"path":"path_","qte":3,"taunt":False}
# Carte 8 :
moussa = {"name":"Moussa","atk":2,"vie":3,"cout":3,"path":"path_","qte":1,"taunt":True}
# Carte 9 :
projecteur = {"name":"Projecteur Epson","atk":1,"vie":1,"cout":10,"path":"path_","qte":1,"taunt":True}
# Carte 10 :
quenouille = {"name":"Quenouille","atk":2,"vie":2,"cout":2,"path":"path_","qte":2,"taunt":False}
# Carte 11 :
devoir_maison = {"name":"Devoir Maison","atk":7,"vie":5,"cout":7,"path":"path_","qte":1,"taunt":True}
# Carte 12 :
ronald = {"name":"Ronald McDonald","atk":9,"vie":1,"cout":5,"path":"path_","qte":1,"taunt":False}

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
            card[FORMAT[key]] = definition[key] if key != "path" else "patchouli.gif"
        else:
            if key not in FORMAT_BL:
                print("KEY `{}` not in FORMAT && FORMAT_BL for card : {}".format(key,card))
    deck += [card] * definition["qte"]

f = open(OUT_FILE,"w")
json.dump(deck,f)
