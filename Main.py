from graphics import *
from card import *
import time
import random
#size of game window
win_x=1200
win_y=800

pad=2 #padding for title bar and card mat

win = GraphWin(": : S E T : :", win_x, win_y)
win.setCoords(0,0,win_x,win_y)

#Title bar
titlebar_y=40
score=0

def draw_titlebar(title_text, bg_color="white"):
    #this is where we tell the user the score, and if they found a set
    t_box = Rectangle(Point(pad,win_y-pad),Point(win_x-pad,win_y+pad-titlebar_y))
    t_box.setFill(bg_color)
    t_box.draw(win)
    t = Text(Point(win_x/2,win_y-titlebar_y/2), title_text)
    t.draw(win)

#draw start-up title bar
draw_titlebar("Can You Spot A SET?")

mat_x=win_x-pad
mat_y=win_y-pad-titlebar_y

name_tag = Text(Point(win_x-120,20), "Creative commons Madeleine Higgins 2024")
name_tag.draw(win)
#row and col numbers for card array
col = 4 
row = 4

rowpad = (mat_y -row*card_height)/(row+1)
colpad = (mat_x - col*card_width)/(col+1)

card_mat = Rectangle(Point(pad,mat_y), Point(mat_x,pad))
card_mat.draw(win)

#make a new deck, shuffle it
d=deck()
d.shuffle()

displayed_cards=[]

hint_height = 40
hint_wid = 80
hint_x = win_x/25
hint_y = win_y-90
hint = Polygon(Point(hint_x,hint_y),Point(hint_x+hint_wid,hint_y),Point(hint_x+hint_wid,hint_y+hint_height),Point(hint_x,hint_y+hint_height))
hint.setFill("light blue")
hint.draw(win)
t = Text(Point(hint_x+hint_wid/2,hint_y+hint_height/2), "NO SETS?")
t.draw(win)
#pop cards off of the top of the deck and assign coordinates
#put them in the displayed_cards array
for j in range(0,row):
    for i in range(0,col):
        card_i=d.card_list.pop(0)
        card_i.x=(i+1)*colpad + i*card_width
        card_i.y=(j+1)*rowpad + j*card_height
        displayed_cards.append(card_i)

#draw all the cards in the displayed_cards
#since location is a attribute of card() this is
#all we need
for c in displayed_cards:
    c.draw_card(win)
    
def is_a_set(lis): #takes list of card objects
    # three cards are a set only if there are not exactly 2 of any attribute:
    if len(lis)!=3:
        return False
    if len(set([x.number for x in lis]))==2:
        return False
    if len(set([x.color for x in lis]))==2:
        return False
    if len(set([x.fill for x in lis]))==2:
        return False
    if len(set([x.shape for x in lis]))==2:
        return False
    return True

def are_there_sets(lis):
    sets = combinations(lis,3)
    for s in sets:
        if is_a_set(s):
            return s
    return False
# check if a point selected by mouse is inside a card
def check_click(win,cards_Selected):
    p1=win.getMouse()
    for crd in displayed_cards:       
        if p1.x>crd.x and p1.x<crd.x+card_width and p1.y>crd.y and p1.y<crd.y+card_height:
            crd.draw_card(win,"gray")
            return crd
        if p1.x>hint_x and p1.x<hint_x+hint_wid and p1.y>hint_y and p1.y<hint_y+hint_height:
            if are_there_sets(displayed_cards):
                hinted_card = are_there_sets(displayed_cards)[0]
                hinted_card.draw_card(win,"gray")
                return hinted_card
            else:
                for x in cards_Selected:
                    x.draw_card(win,"white")
                cards_Selected = []
                n = random.randint(1,len(displayed_cards))
                remove_card = displayed_cards[n]
                displayed_cards.remove(remove_card)
                drawcard=d.card_list.pop(0)
                drawcard.x=remove_card.x
                displayed_cards.append(drawcard)
                drawcard.draw_card(win)
    return card() #returns an invalid card with self.number=0 for function consistency
    #(functional consistency means that the function always has the same type when called)



def pick_three_cards(): #user highlights three cards
    while len(cards_Selected)<3:
        card_clicked=check_click(win,cards_Selected) #get next click
        if card_clicked not in cards_Selected: #if it's not on the list
            if card_clicked.number>0: #if they clicked a real card not self.number=0
                #the invalid placeholder card
                cards_Selected.append(card_clicked)
        else:
            cards_Selected.remove(card_clicked)
            card_clicked.draw_card(win,"white")
cards_Selected=[]
while len(d.card_list)>2: #if there are still more cards in the deck
    
    pick_three_cards() #add three cards to cards_Selected
    
    #if those three are not a set
    if not is_a_set(cards_Selected):
        draw_titlebar("NOT A SET (try again)", "red")
        for p in cards_Selected:
            #make selected cards white again
            p.draw_card(win,"white")
        #empty the selected cards list
        cards_Selected=[]   
    
    elif is_a_set(cards_Selected):
        score+=1
        draw_titlebar("SETS FOUND: " + str(score))
        displayed_cards= list(set(displayed_cards) - set(cards_Selected))
            
        for card_i in cards_Selected:
            #replace the set in displayed_cards with new cards from the deck.
            drawcard=d.card_list.pop(0)
            drawcard.x=card_i.x
            drawcard.y=card_i.y
            displayed_cards.append(drawcard)
            drawcard.draw_card(win)
        #empty the selected cards list
        cards_Selected=[]

print("no more cards")
# pip install auto-py-to-exe