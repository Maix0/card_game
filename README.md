# nsi_project
### What is this repo ?
Its a repo for me, I use it to get the code from my computer to the school's computer

### What is the project ?
We had only one guideline, make a card game, many of the others chose simple card game, but our group chose an Heart Stone like game because why not.
We need to code this game in a 4 week span with 2 hours at school per week, only in python and using tkinter.
Our project is quite ambitious for that time span , so I am coding during my freetime , thus this repo existance (and because it is nice to have it stored somewere)

# How to play
You can customise the deck, by modifing `deck_generator.py` and then execute that file to create your deck.

To run the game, run `main.py`, it will create the window and you can play directly
 
## Rules

The only way to win is to get your opponent to 0hp, in order to do that , you need play your cards.
The cards cost mana, you have a mana pool, capped to a certain number, that increase each turn until it reach 10.

Each card have an illustration (currently all are patchouli), attack stat, health stat and mana cost.
You can click on a card from your hand, and if you have enough mana and your battlefield have less than 8 card on it.
When your card join the battlefield, it will be unable to attack, thus having a red border.
If the card have taunt, il will have an additional grey border.

You can only attack with a card whose border is green. To attack , you need to click on the card ,
and then click on the card you wan to attack or the button dedicated to the other player.
If the other player have a card with taunt, You won't be able to target a card (or the player) without taunt

When a player's health is equal to 0 (or less), the other player win

