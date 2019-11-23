from tkinter import *

IMG_FSIZE= (135,150)
IMG_BSIZE= (200,300)

FONT_SIZE = 20
class Game:
    def __init__(self):
        self.current_player = 1;
        self.end_of_game = False
        self.window = Tk()
        self.window.title("DwellingRock")
        self.width = 900
        self.height = 450
        self.canv = Canvas(self.window, width = self.width, height =self.height, bg ='Grey')
        self.canv.pack(padx =0, pady =0)
        self.player1 = Player(self.canv)
        self.player2 = Player(self.canv)
        self.player1.test()
        self.player2.test()
        for i in range(5):
            self.player1.draw_card()
            self.player2.draw_card()
        self.canv.bind("<Button-1>", self.click_handler)
        self.atk_card = (None,None)
        self.info_text = self.canv.create_text(0,0)
        self.canv.itemconfig(self.info_text,\
                             text= "Player {} is playing".format(self.current_player),\
                             fill= "black",\
                             anchor= NW,\
                             font= ("",int(FONT_SIZE * 0.95))\
                             )
        self.canv.coords(self.info_text,350,2)
        self.canv.create_rectangle(56,345,56+80,345+80,fill="red")
        self.canv.create_rectangle(770,345,770+80,345+80,fill="red")
    def start(self):
        self.canv.after(1000//15,self.new_frame)
        self.window.mainloop()
    def new_frame(self):
        if self.player1.health <= 0:
            self.end_of_game = True
        if self.player2.health <= 0:
            self.end_of_game = True
        if self.end_of_game:
            self.w_rect = self.canv.create_rectangle(0,0,\
                                                     self.canv.winfo_width(),self.canv.winfo_height(),\
                                                     fill="grey",\
                                                     )
            self.w_id = self.canv.create_text(50,50,text="{} Won The Game".format(\
                                              "Player1" if self.player2.health <= 0 else "Player2"),\
                                              font=("",FONT_SIZE * 2),\
                                              anchor=NW)
        self.canv.itemconfig(self.info_text,\
                             text= "Player {} is playing".format(self.current_player))
        self.player1.clear_dead()
        self.player2.clear_dead()
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
        self.canv.after(1000//15,self.new_frame)
        return
    def click_handler(self,e):
        print(e.x,e.y)
        current_player = self.player1 if self.current_player == 1 \
                                     else self.player2;
        if 56 <= e.x <= 56 + 80 and 345 <= e.y <= 345 + 80:
            return self.finish_turn()
        for index, card in enumerate(current_player.hand):
            if card.is_clicked((e.x,e.y)) and len(current_player.battlefield) <= 8:
                if current_player.mana - card.cost >= 0:
                    current_player.battlefield.append(\
                                    current_player.hand.pop(index).remove_attack())
                    current_player.mana -= card.cost
                    return
        for index,card in enumerate(current_player.battlefield):
            if card.is_clicked((e.x,e.y)) and card.can_attack:
                self.atk_card = (card,index)
                return
        if self.atk_card != (None,None):
            if 770 <= e.x <= 770 + 80 and 345 <= e.y <= 345 + 80:
                (self.player1 if self.current_player == 2 \
                                         else self.player2).health -= self.atk_card[0].attack
                self.atk_card[0].can_attack = False
                current_player.battlefield[self.atk_card[1]] = self.atk_card[0]
                self.atk_card = (None,None)
                return
            for index,card in enumerate((self.player1 if self.current_player == 2 \
                                         else self.player2).battlefield):
                if card.is_clicked((e.x,e.y)):
                    cards = self.atk_card[0].battle(card)
                    current_player.battlefield[self.atk_card[1]] = cards[0]
                    (self.player1 if self.current_player == 2 \
                                         else self.player2).battlefield[index] = cards[1]
                    self.atk_card = (None,None)
    def finish_turn(self):
        self.current_player = 2 if self.current_player == 1 else 1
        current_player = self.player1 if self.current_player == 1 \
                                     else self.player2;
        old_player = self.player1 if self.current_player == 2 \
                                     else self.player2;
        for card in current_player.battlefield:
            card.can_attack = True
            card.custom()
        current_player.mana_max += 1 if current_player.mana_max < 10 else 0
        current_player.mana = current_player.mana_max
        if len(current_player.hand) < 6:
            current_player.draw_card()
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
        if len(self.deck) >= 1:
            self.hand.append(self.deck.pop())
        return
    def test(self):
        for i in range(20):
            self.deck.append(Card({"image": "./patchouli.gif",
                               "attack": 8,
                               "health": 7,
                               "mana":i +  1,
                            "name": "patchouli"},
                              self.canv))
        for i in range(0):
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
            self.hand[1].draw(463,320)
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
        elif len(self.hand) == 0:
            pass
        else:
            #raise "player hand not valid"
            print(len(self.hand))
        return
    def draw_ally_bf(self):
        offset = 52 if len(self.battlefield) % 2 == 0 else 106
        for i in range(len(self.battlefield)):
            c_offset = 50 * ((8 if len(self.battlefield) % 2 == 0 else 7)\
                             - len(self.battlefield))
            self.battlefield[i].draw(100*i + offset + c_offset\
                    , 183)
        return
    def draw_ally_info(self):
        self.canv.itemconfig(self.h_id, text=self.health, anchor=NW)
        self.canv.itemconfig(self.m_id, text="{}/{}".format(self.mana,self.mana_max),\
                             anchor=NW)
        self.canv.coords(self.h_id,0, self.canv.winfo_height() * 0.95)
        self.canv.coords(self.m_id, self.canv.winfo_width() * 0.92,\
                         self.canv.winfo_height() * 0.95)
        return
    def draw_en_bf(self):
        offset = 52 if len(self.battlefield) % 2 == 0 else 106
        for i in range(len(self.battlefield)):
            c_offset = 50 * ((8 if len(self.battlefield) % 2 == 0 else 7)\
                             - len(self.battlefield))
            self.battlefield[i].draw(100*i + offset + c_offset\
                    , 46)
    def draw_en_info(self):
        self.canv.itemconfig(self.h_id, text=self.health, anchor=NW)
        self.canv.itemconfig(self.m_id, text="{}/{}".format(self.mana,self.mana_max),\
                             anchor=NW)
        self.canv.coords(self.h_id,0, 0)
        self.canv.coords(self.m_id, self.canv.winfo_width() * 0.92,0)
    def clear_dead(self):
        for index,card in enumerate(self.battlefield):
            if card.health <= 0:
                card.hide()
                self.battlefield.pop(index)


class Card:
    def __init__(self, card, canv):
        self.image = PhotoImage(file=card["image"])
        self.name = card["name"]
        self.scale()
        self.attack = int(card["attack"])
        self.health = int(card["health"])
        self.cost = int(card["mana"])
        self.coords = (-1000,-1000)
        self.can_attack = False
        self.id = canv.create_image(self.coords[0],self.coords[1], anchor=NW, \
                                    image = self.image)
        self.a_id = canv.create_text(-1000,-1000, anchor=NW)
        canv.itemconfig(self.a_id, text = self.attack,font = ("", FONT_SIZE), fill="orange")
        self.h_id = canv.create_text(-1000,-1000, anchor=NW)
        canv.itemconfig(self.h_id, text = self.health,font = ("", FONT_SIZE), fill="green")
        self.c_id = canv.create_text(-1000,-1000, anchor=NW)
        canv.itemconfig(self.c_id, text = self.cost,font = ("", FONT_SIZE), fill="blue")
        self.atk_id = canv.create_rectangle(self.coords[0],self.coords[1],\
                                            self.coords[0] + self.image.width(),\
                                            self.coords[1] + self.image.height(),\
                                            )
        self.canv = canv
    def remove_attack(self):
        self.can_attack = False
        return self

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
        self.canv.coords(self.atk_id, self.coords[0],self.coords[1],\
                         self.coords[0] + self.image.width(),\
                         self.coords[1] + self.image.height())
        self.canv.itemconfig(self.atk_id,width=2,outline= "green" if self.can_attack else "red")
    def hide(self):
        self.coords = (-1000,-1000)
        self.canv.coords(self.id, self.coords[0], self.coords[1])
        self.canv.coords(self.a_id, self.coords[0], self.coords[1])
        self.canv.coords(self.h_id, self.coords[0], self.coords[1])
        self.canv.coords(self.c_id, self.coords[0],self.coords[1])
        self.canv.coords(self.atk_id, self.coords[0],self.coords[1],\
                         self.coords[0] + self.image.width(),\
                         self.coords[1] + self.image.height())
        self.canv.itemconfig(self.atk_id,width=2,outline= "green" if self.can_attack else "red")
    def is_clicked(self,coords):
        if self.coords[0] < coords[0] < self.coords[0] + self.image.width():
            if self.coords[1] < coords[1] < self.coords[1] + self.image.height():
                return True
        return False

    def battle(self,card):
        self.health -= card.attack;
        card.health -= self.attack;
        card.can_attack = False
        self.can_attack = False
        return (self,card)

    def scale(self):
        self.image = self.image.zoom(IMG_FSIZE[0] // 10)
        self.image = self.image.subsample(IMG_BSIZE[1] // 10)
    def custom(self):
        pass


game = Game()
game.start()

