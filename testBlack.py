from blackJ import BlackJack
amt = 0
while True:
    try:
        amt = int(input("Place Bet: "))
    except ValueError:
        print("Invalid value for amount")
    else:
        break

game = BlackJack(amt)

# initialize cards 
game.hit(game.players_hand)
game.hit(game.dealers_hand)
game.hit(game.players_hand)
game.hit(game.dealers_hand)


hidden = game.dealers_hand[0]
game.dealers_hand[0] = ""


if (game.win_draw()[0] == 21) or (game.win_draw()[1] == 21):
    game.dealers_hand[0] = hidden
    print(f"Player Card: {game.players_hand} {game.win_draw()[0]}") # display player card and score
    print(f"Dealer Card: {game.dealers_hand} {game.win_draw()[1]}")
    print("BLACK JACK!")

else:
    loop = True
    while loop:
        print(f"Player Card: {game.players_hand} {game.win_draw()[0]}") # displays players card and total count
        print(f"Dealers Card: {game.dealers_hand}")
        
        reply = input("\nNOTE..........\ny ==> HIT\nn ==> STAND\nHit(y/n): ").lower()

        if(reply == "y"): # Player Hits
            game.hit(game.players_hand) # add extra card to players hand
            if game.win_draw()[0] == 21:
                game.dealers_hand[0] = hidden
                print(f"Player Card: {game.players_hand} {game.win_draw()[0]}") # display player card and score
                print(f"Dealer Card: {game.dealers_hand} {game.win_draw()[1]}")
                print("YOU WIN VIA BLACK JACK!")
                loop = False
            elif game.win_draw()[0] > 21: # palyer bust
                game.dealers_hand[0] = hidden
                print(f"Player Card: {game.players_hand} {game.win_draw()[0]}") # display player card and score
                print(f"Dealer Card: {game.dealers_hand} {game.win_draw()[1]}")
                print("YOU BUST!\nDEALER WINS!")
                loop = False

        elif (reply == "n"): # player stands                
            if (game.win_draw()[0] == game.win_draw()[1]):
                game.dealers_hand[0] = hidden
                print(f"Player Card: {game.players_hand} {game.win_draw()[0]}") # display player card and score
                print(f"Dealer Card: {game.dealers_hand} {game.win_draw()[1]}")
                print("GAME ENDED IN A DRAW")
                loop = False
            else:
                mini_loop = True
                while mini_loop:

                    game.hit(game.dealers_hand)

                    if (game.win_draw()[1] < 21) and (game.win_draw()[1] > game.win_draw()[0]):
                        game.dealers_hand[0] = hidden
                        print(f"Player Card: {game.players_hand} {game.win_draw()[0]}") # display player card and score
                        print(f"Dealer Card: {game.dealers_hand} {game.win_draw()[1]}")
                        print("DEALER WINS!\nYOU LOSE!")
                        loop,mini_loop = False,False
                    elif game.win_draw()[1] == 21:
                        game.dealers_hand[0] = hidden
                        print(f"Player Card: {game.players_hand} {game.win_draw()[0]}") # display player card and score
                        print(f"Dealer Card: {game.dealers_hand} {game.win_draw()[1]}")
                        print("DEALER WINS VIA BLACK JACK!")
                        loop,mini_loop = False,False
                    elif game.win_draw()[1] > 21:
                        game.dealers_hand[0] = hidden
                        print(f"Player Card: {game.players_hand} {game.win_draw()[0]}") # display player card and score
                        print(f"Dealer Card: {game.dealers_hand} {game.win_draw()[1]}")
                        print("DEALER BUST!\nYOU WIN!n")
                        loop,mini_loop = False,False
                    
                    else:
                        continue
        else:
            print("INVALID INPUT!")

print(game.dealers_hand)