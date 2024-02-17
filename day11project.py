import random
from art import logo

print(logo)

def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    
    if 11 in cards and sum(cards)>21:
        cards.append(1)
        cards.remove(11)

    return sum(cards)


def compare(user_score,computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤 \n"
    
    if user_score == computer_score:
        return "Draw 🙃 \n"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱 \n"
    elif user_score == 0:
        return "Win with a Blackjack 😎 \n"
    elif user_score > 21:
        return "You went over. You lose 😭 \n"
    elif computer_score > 21:
        return "Opponent went over. You win 😁 \n"
    elif user_score > computer_score:
        return "You win 😃 \n"
    else:
        return "You lose 😤 \n"
    
def play_game():
    user_cards=[]
    computer_cards=[]
    game_completed=False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    while not game_completed:
        user_score=calculate_score(user_cards)  
        computer_score=calculate_score(computer_cards)

        print(f"Your cards : {user_cards} , Your score : {user_score} \n")
        print(f"Computer's First Card : {computer_cards[0]} \n")

        if computer_score==0 or user_score==0 or user_score>21:
            game_completed=True
        else:
            user_should_deal=input("Type 'y' to get another card and 'n' to pass : ").lower()
            if user_should_deal=="y":
                user_cards.append(deal_card())
                
            else:
                game_completed=True  


    while computer_score<17 and computer_score!=0:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)


    print(f"Your final hand : {user_cards} , Your score : {user_score}. \n")
    print(f"Computer's final hand : {computer_cards} , Computer's score : {computer_score}. \n")
    print(compare(user_score,computer_score)) 


while input("Do you want to play a game of BlackJack? Type 'y' or 'n' ").lower()=="y":
    play_game()
    





