import random 
import os
def clear_console():
    """
    Clears the console screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
def play_game():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
   
    def calculate_scores(cards):
        if sum(cards)==21 and len(cards)==2:
            return 0
        if 11 in cards and sum(cards)>21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    def compare(user_score,computer_score):
        if user_score== computer_score:
            return"Draw"
        elif user_score==0:
            return"you win"
        elif computer_score==0:
            return"computer win"
        elif user_score>21:
            return"You loose"
        elif computer_score >21:
            return "you win"
        elif user_score>computer_score:
            return "you win"
        else:
            return "you loose"       

    def deal_cards(cards):
        return random.choice(cards)
    while True:
        user_card=[]
        computer_card=[]

        for i in range(2):
            user_card.append(deal_cards(cards))
            computer_card.append(deal_cards(cards))

        while True:   
            user_score=calculate_scores(user_card)
            computer_score=calculate_scores(computer_card)

            print(f"user card= {user_card} and score={user_score}")
            print(f"computer first card={computer_card[0]}")

            if user_score==0 or computer_score==0 or user_score>21:
                break
            else:
                user_prompt=input("Another card: 'y' and 'n' to pass ").lower()
                if user_prompt=='y':
                    user_card.append(deal_cards(cards))
                else: 
                    break
                    
        while computer_score!=0  and computer_score<17:
            computer_card.append(deal_cards(cards))
            computer_score=calculate_scores(computer_card)
            
        print(f"computer score is {computer_score}")
        print(compare(user_score,computer_score))

        play_again=input("you want to play again yes:'y' and no 'n': ")
        if play_again!='y':
            exit(0)
        else:
            clear_console()

play_game()
