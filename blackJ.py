import random

class BlackJack():

    def __init__(self,bet_amount): # pass in bet amount as a parameter

        self.cards = ["Ace",2,3,4,5,6,7,8,9,10,"Joker","Queen","King","Ace",2,3,4,5,6,7,8,9,10,"Joker","Queen","King",
                    "Ace",2,3,4,5,6,7,8,9,10,"Joker","Queen","King","Ace",2,3,4,5,6,7,8,9,10,"Joker","Queen","King"]
        self.bet_amount = bet_amount
        random.shuffle(self.cards) # shuffle cards  
        self.players_hand = []
        self.dealers_hand = []       

    def hit(self,hand):

        hand.append(self.cards.pop())        

    def sum_cards(self,given_hand):
        """Takes in the total amount of cards, sums up the value"""

        sum1 = 0
        sum2 = 0
        # loop through players / dealers cards 
        for val in given_hand:
            if type(val) == str:
                if (val == "Ace"):
                    sum1 += 11
                    sum2 += 1
                else:
                    sum1 += 10
                    sum2 += 10
            else:
                sum1 += val
                sum2 += val
        
        possible_sums = [sum1,sum2] # multiple possibilities when an Ace is in hand
        return possible_sums

    def win_draw(self):
        
        
        player_score = 0
        dealer_score = 0
        if max(self.sum_cards(self.players_hand)) >= 21:
            player_score = min(self.sum_cards(self.players_hand))
        else:
            player_score = max(self.sum_cards(self.players_hand))

        if max(self.sum_cards(self.dealers_hand)) >= 21:
            dealer_score = min(self.sum_cards(self.dealers_hand))
        else:
            dealer_score = max(self.sum_cards(self.dealers_hand))

        return [player_score,dealer_score]        

