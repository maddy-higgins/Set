from graphics import *
import random
from itertools import product #for making a cartesian product.
import math
import itertools
from itertools import combinations

#size of cards
card_width = 160
card_height = 100

S = ['squiggle','diamond','pill']
F = ['striped','filled','empty']
C = ['red','green','purple']
N = [0,1,2,3]

class card:
    # we keep card location with the card so we can click on them
    def __init__(self, shape=0, fill=0, color=0, number=0,x=0,y=0):
        self.shape = shape
        self.fill = fill
        self.color = color
        self.number = number
        self.x=x
        self.y=y      
    
    def __str__(self):
        end="\n"
        if  N[self.number]>1: #add an s if there is more than one.
            end="s\n"
        return str(N[self.number]) + " " + C[self.color] +" "+ F[self.fill] + " " + S[self.shape] + end 
    
    def __repr__(self):
        return str(self)
    
    def __eq__(self,other):
        return self.shape == other.shape and self.fill == other.fill and self.color == other.color and self.number == other.number
    
    def __ne__(self,other):
        return not (self == other)
    
    def __hash__(self): #the x,y location isn'tincluded in the hash
        return hash((self.shape,self.fill,self.color,self.number))
 
    def draw_diamond(self,center,win,color,pat):
        diamond = Polygon(Point(center.x,center.y+40),Point(center.x+17,center.y),Point(center.x,center.y-40),Point(center.x-17,center.y))
        diamond.setOutline(color)
        diamond.draw(win)
        if pat==1:
            diamond.setFill(color)
        if pat==0:
            for x in range(0,17,2):
                stripe = Line(Point(x+center.x-17,center.y+((40*x)/17)),Point(x+center.x-17,center.y-((40*x)/17)))
                stripe.setOutline(color)
                stripe.draw(win)
            for x in range(1,17,2):
                stripe = Line(Point(x+center.x,center.y+(17-x)*40/17),Point(x+center.x,center.y-(17-x)*40/17))
                stripe.setOutline(color)
                stripe.draw(win)
   

    def draw_oval(self,center,win,color,pat):
        p1 = Point(center.x-17,center.y-40)
        p2 = Point(center.x+17,center.y+40)
        o = Oval(p1,p2)
        o.setOutline(color)
        o.draw(win)
        if pat==1:
            o.setFill(color)
        if pat==0:
            for k in range(-16,17,2):
                num = math.sqrt(((289*1600)-1600*(k**2))/289)
                l = Line(Point(center.x+k, center.y+num),Point(center.x+k,center.y-num))
                l.setOutline(color)
                l.draw(win)
        #for x in range(0,17):


    def draw_wave(self,center,win,color,pat):
        p = Polygon(Point(center.x,center.y+40),Point(center.x-17,center.y+40/3),Point(center.x,center.y-40/3),Point(center.x-17,center.y-40),Point(center.x,center.y-40),Point(center.x+17,center.y-40/3),Point(center.x,center.y+40/3),Point(center.x+17,center.y+40))
        p.setOutline(color)
        p.draw(win)
        if pat==1:
            p.setFill(color)
        if pat==0:
            for x in range(-17,0,2):
                l = Line(Point(center.x+x,center.y+(80/51)*x+40),Point(center.x+x,center.y-80*(x+17)/51+40/3))
                l.setOutline(color)
                l.draw(win)
                l2 = Line(Point(center.x+x,center.y-40),Point(center.x+x,center.y+(80*(x+17)/51)-40))
                l2.setOutline(color)
                l2.draw(win)
            for x in range(1,17,2):
                l = Line(Point(center.x+x,center.y+40),Point(center.x+x,center.y+(80*(x-17)/51)+40))
                l.setOutline(color)
                l.draw(win)
                l2 = Line(Point(center.x+x,center.y-(80*x/51)+40/3),Point(center.x+x,center.y+(80*(x-17)/51)-40/3))
                l2.setOutline(color)
                l2.draw(win)

    # 'draw' as in make a graphic
    # win is the graphics.py drawing window
    
    def draw_one(self,win):
        #one shape will be centered
        center=Point(self.x+card_width/2,self.y+card_height/2)
        if self.shape==0: #squiggle           
            self.draw_wave(center,win,C[self.color],self.fill)
        if self.shape==1: #diamond            
            self.draw_diamond(center,win,C[self.color],self.fill)           
        if self.shape==2: #pill           
            self.draw_oval(center,win,C[self.color],self.fill)
            
    def draw_two(self,win):
        center1=Point(self.x+card_width/3,self.y+card_height/2)
        center2=Point(self.x+2*card_width/3,self.y+card_height/2)
        if self.shape==0: #squiggle           
            self.draw_wave(center1,win,C[self.color],self.fill)
            self.draw_wave(center2,win,C[self.color],self.fill)
        if self.shape==1: #diamond            
            self.draw_diamond(center1,win,C[self.color],self.fill)
            self.draw_diamond(center2,win,C[self.color],self.fill)
        if self.shape==2: #pill           
            self.draw_oval(center1,win,C[self.color],self.fill)
            self.draw_oval(center2,win,C[self.color],self.fill)

    def draw_three(self,win):
        center1=Point(self.x+card_width/4,self.y+card_height/2)
        center2=Point(self.x+2*card_width/4,self.y+card_height/2)
        center3=Point(self.x+3*card_width/4,self.y+card_height/2)
        if self.shape==0: #squiggle           
            self.draw_wave(center1,win,C[self.color],self.fill)
            self.draw_wave(center2,win,C[self.color],self.fill)
            self.draw_wave(center3,win,C[self.color],self.fill)
        if self.shape==1: #diamond            
            self.draw_diamond(center1,win,C[self.color],self.fill)
            self.draw_diamond(center2,win,C[self.color],self.fill)
            self.draw_diamond(center3,win,C[self.color],self.fill)
        if self.shape==2: #pill           
            self.draw_oval(center1,win,C[self.color],self.fill)
            self.draw_oval(center2,win,C[self.color],self.fill)
            self.draw_oval(center3,win,C[self.color],self.fill)
        
        
    
    
    def draw_card(self,win,bgcolor="white"):
        #if bgcolor=="white":
        #    bgcolor=C[self.color]
        c=Rectangle(Point(self.x,self.y),Point(self.x+card_width,self.y+card_height))
        c.setFill(bgcolor)
        t = Text(Point(self.x+card_width/2,self.y+card_height/2), str(self))
        c.draw(win)
        if self.number==1:
            self.draw_one(win)
        if self.number==2:
            self.draw_two(win)
        if self.number==3:
            self.draw_three(win)
              
        


class deck:
    # make a deck with one of each card
    
    def __init__(self, card_list = []):
        self.card_list = []
        for i in product([0,1,2],[0,1,2],[0,1,2],[1,2,3]): #cartesian product of sets
            self.card_list.append(card(i[0],i[1],i[2],i[3]))
            
    def __str__(self):
        r=""
        for i in self.card_list:
            r+=str(i) + "\n"
            
        return r
    def __repr__(self):
        return str(self)
                        
    def shuffle(self):
        random.shuffle(self.card_list)
