from tkinter import *

IMG_FSIZE= (135,150)
IMG_BSIZE= (200,300)

FONT_SIZE = 20
class Game:
    def __init__(self):
        self.current_player = 1;
        self.window = Tk()
        self.window.title("Card Game")
        self.width = 900
        self.height = 450
        self.canv = Canvas(self.window, width = self.width, height =self.height, bg ='Grey')
        self.canv.pack(padx =0, pady =0)
        self.player1 = Player(self.canv)
        self.player2 = Player(self.canv)
        self.player1.test()
        self.player2.test()
        self.canv.bind("<Button-1>", self.click_handler)
        self.s_card = (None,None)
    def start(self):
        self.canv.after(1000//15,self.new_frame)
        self.window.mainloop()
    def new_frame(self):
        self.canv.after(1000//15,self.new_frame)
        #self.player1.battlefield[0].draw( 0,75)
        #self.player1.battlefield[1].draw( 200,75)
        if self.current_player == 1:
            self.player1.draw_ally_info()
            self.player1.draw_hand()
            self.player1.draw_ally_bf()
            self.player2.draw_en_bf()
            self.player2.hide_hand()
            self.player2.draw_en_info()
        elif self.current_player == 2:
            self.player2.draw_ally_info()
            self.player2.draw_hand()
            self.player2.draw_ally_bf()
            self.player1.draw_en_bf()
            self.player1.hide_hand()
            self.player1.draw_en_info()
        return
    def click_handler(self,e):
        for index,card in enumerate(self.player1.battlefield):
            if card.is_clicked((e.x,e.y)) and self.s_card == (None,None):
                self.s_card = (card, index)
            elif card.is_clicked((e.x,e.y)):
                cards = self.s_card[0].battle(card)
                self.player1.battlefield[self.s_card[1]] = cards[0]
                self.player1.battlefield[index] = cards[1]
                self.s_card = (None, None)
        return


class Player:
    def __init__(self,canv):
        self.canv = canv
        self.deck = []
        self.base_deck = []
        self.health = 15
        self.mana_max = 1
        self.mana =  1
        self.hand = []
        self.battlefield = []
        self.h_id = self.canv.create_text(-1000,-1000,anchor=NW)
        self.m_id = self.canv.create_text(-1000,-1000,anchor=NW)
        self.canv.itemconfig(self.h_id,text="{}".format(self.health), font= ("",FONT_SIZE),\
                             fill="red")
        self.canv.itemconfig(self.m_id,text="{}/{}".format(self.mana,self.mana_max),\
                             font=("",FONT_SIZE),fill="blue")
    def draw_card(self):
        return
    def test(self):
        for i in range(5):
            self.hand.append(Card({"image": "./patchouli.gif",
                               "attack": 8,
                               "health": 7,
                               "mana":i,
                            "name": "patchouli"},
                              self.canv))
        for i in range(8):
            self.battlefield.append(Card({"image": "./patchouli.gif",
                               "attack": i,
                               "health": i,
                               "mana":i,
                                          "name":"patchouli"},
                              self.canv))
    def hide_hand(self):
        for card in self.hand:
            card.hide()
        return

    def draw_hand(self):
        if len(self.hand) == 1:
            self.hand[0].draw(406,320)
        elif len(self.hand) == 2:
            self.hand[0].draw(350,320)
            self.hand[1].draw(363,320)
        elif len(self.hand) == 3:
            self.hand[0].draw(306,320)
            self.hand[1].draw(406,320)
            self.hand[2].draw(506,320)
        elif len(self.hand) == 4:
            self.hand[0].draw(256,320)
            self.hand[1].draw(356,320)
            self.hand[2].draw(456,320)
            self.hand[3].draw(556,320)
        elif len(self.hand) == 5:
            self.hand[0].draw(206,320)
            self.hand[1].draw(306,320)
            self.hand[2].draw(406,320)
            self.hand[3].draw(506,320)
            self.hand[4].draw(606,320)
        elif len(self.hand) == 6:
            self.hand[0].draw(156,320)
            self.hand[1].draw(256,320)
            self.hand[2].draw(356,320)
            self.hand[3].draw(456,320)
            self.hand[4].draw(556,320)
            self.hand[5].draw(656,320)
        else:
            print(len(self.hand))
        return
    def draw_ally_bf(self):
        for i in range(len(self.battlefield)):
                       self.battlefield[i].draw(100*i + 56, 183)
        return
    def draw_ally_info(self):
        self.canv.itemconfig(self.h_id, text=self.health, anchor=NW)
        self.canv.itemconfig(self.m_id, text="{}/{}".format(self.mana,self.mana_max),\
                             anchor=NW)
        self.canv.coords(self.h_id,0, self.canv.winfo_height() * 0.95)
        self.canv.coords(self.m_id, self.canv.winfo_width() * 0.95,\
                         self.canv.winfo_height() * 0.95)
        return
    def draw_en_bf(self):
        for i in range(len(self.battlefield)):
                       self.battlefield[i].draw(100*i + 56, 46)
        return
    def draw_en_info(self):
        self.canv.itemconfig(self.h_id, text=self.health, anchor=NW)
        self.canv.itemconfig(self.m_id, text="{}/{}".format(self.mana,self.mana_max),\
                             anchor=NW)
        self.canv.coords(self.h_id,0, 0)
        self.canv.coords(self.m_id, self.canv.winfo_width() * 0.95,0)
        return


class Card:
    def __init__(self, card, canv):
        self.image = PhotoImage(file=card["image"])
        self.name = card["name"]
        self.scale()
        self.attack = int(card["attack"])
        self.health = int(card["health"])
        self.cost = int(card["mana"])
        self.coords = (-1000,-1000)
        self.id = canv.create_image(self.coords[0],self.coords[1], anchor=NW, \
                                    image = self.image)
        self.a_id = canv.create_text(0,0, anchor=NW)
        canv.itemconfig(self.a_id, text = self.attack,font = ("", FONT_SIZE), fill="orange")
        self.h_id = canv.create_text(0,0, anchor=NW)
        canv.itemconfig(self.h_id, text = self.health,font = ("", FONT_SIZE), fill="green")
        self.c_id = canv.create_text(0,0, anchor=NW)
        canv.itemconfig(self.c_id, text = self.cost,font = ("", FONT_SIZE), fill="blue")
        self.canv = canv

    def draw(self,x,y):
        self.coords = (x,y)
        self.canv.itemconfig(self.h_id, text = self.health, fill="green")
        self.canv.itemconfig(self.a_id, text = self.attack, fill="orange")
        self.canv.itemconfig(self.c_id, text = self.cost, fill="blue")
        self.canv.coords(self.id, x,y)
        self.canv.coords(self.a_id, self.coords[0], self.coords[1])
        self.canv.coords(self.h_id, int(self.coords[0] + self.image.width() * 0.80), \
                         int(self.coords[1]))
        self.canv.coords(self.c_id, int(self.coords[0] + self.image.width() * 0.40 ),\
                         int(self.coords[1] + self.image.height() * 0.80))
    def hide(self):
        self.coords = (-1000,-1000)
        self.canv.coords(self.id, self.coords[0], self.coords[1])
        self.canv.coords(self.a_id, self.coords[0], self.coords[1])
        self.canv.coords(self.h_id, self.coords[0], self.coords[1])
        self.canv.coords(self.c_id, self.coords[0],self.coords[1])
    def is_clicked(self,coords):
        if self.coords[0] < coords[0] < self.coords[0] + self.image.width():
            if self.coords[1] < coords[1] < self.coords[1] + self.image.height():
                return True
        return False

    def battle(self,card):
        self.health -= card.attack;
        card.health -= self.attack;
        return (self,card)

    def scale(self):
        self.image = self.image.zoom(IMG_FSIZE[0] // 10)
        self.image = self.image.subsample(IMG_BSIZE[1] // 10)



game = Game()
game.start()
