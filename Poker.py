# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 17:25:41 2019

@author: Lenovo
"""
import random
class Poker:
    num_of_game=0
    order=['2','A','K','Q','J','10','9','8','7','6','5','4','3']#手牌的排列顺序
    ranks = ['A', '2', '3', '4', '5', '6', '7','8', '9', '10', 'J', 'Q', 'K']
    suits = ['C', 'D', 'H', 'S']
    deck = []
    for s in suits:
        for r in ranks:
            deck.append(s + r)
    num_of_deck=len(deck)
    del r,s,ranks,suits
    
    def __init__(self,num_of_player):
        self.num_of_player=num_of_player
        self.deck=Poker.deck.copy()
        self.hand=[[] for i in range(num_of_player)]
        Poker.num_of_game+=1
    def shuffle(self):
        random.shuffle(self.deck)
    def draw(self,num_of_deal='all',First_player='random'):
        n=self.num_of_player
        deck=self.deck
        if num_of_deal=='all':
            num_of_deal=len(deck)#发所有的牌
        elif isinstance(num_of_deal,int):
            if num_of_deal<=len(deck):
                num_of_deal=num_of_deal#发指定个数的牌
            else:
                num_of_deal=len(deck)
        else:
            raise TypeError('num_of_deal must be int')
        r=self.choose_player(n,First_player) #选择一个玩家开始发牌
        hand=self.hand.copy()
        deck0=deck.copy()
        for i in range(r,num_of_deal+r):
            p=deck0.pop()
            hand[i%n].append(p)
        self.hand=hand.copy()
        self.deck=deck0.copy()
        return hand,deck0
    def start(self):#开始游戏
        self.shuffle()
        self.draw()
        self.sort()
    def restart(self):
        self.deck=Poker.deck
        self.hand=[]
    def sort(self):#码牌
        hand=self.hand
        n=self.num_of_player
        for i in range(n):
            hand[i]=sorted(hand[i],key=lambda x:Poker.order.index(x[1:]))
        self.hand=hand
    def show(self):#展示玩家手牌
        hand=self.hand
        n=self.num_of_player
        for i in range(n):
            print('Player'+str(i+1)+':\n',hand[i])

    def playing(self,First_player='random'):
        self.start()
        print("出牌示例：['C2','S2']")
        hand=self.hand.copy()
        n=self.num_of_player
        r=self.choose_player(n,First_player)#选择一个玩家开始出牌
        for i in range(r,Poker.num_of_deck+r):
            player=i%n
            hand[player]=self.play(hand[player],player)
            if hand[player]==[]:
                print('玩家',player+1,'获胜')
                break
            elif hand[player]==['end']:#输入end 结束游戏
                print('玩家',player+1,'已认输')
                break
    def play(self,hand,player):
        print('\n',hand)
        for i in range(3):
            if len(hand)==0:
                print('您已无牌可出')
                break
            out=input('请玩家'+str(player+1)+'出牌:').upper()
            if out=='END':
                return ['end']
            try:
                for p in eval(out):
                    hand.remove(p)
                break
            except :
                print('您出牌不合法，请重新出牌(剩余次数%g)'%(2-i))
        return hand
    def __str__(self):
        return 'Game number: '+str(Poker.num_of_game)
    def choose_player(self,n,First_player='random'):
        r=random.randint(1,n)#随机选择一个玩家开始
        if isinstance(First_player,int):
            r=First_player#从指定玩家开始
        else:
            r=random.randint(0,n-1)#随机选择一个玩家开始
        return r

if __name__=='__main__':
    Game=Poker(3)
    Game.start()
    Game.show()
    Game.playing(1)
    







