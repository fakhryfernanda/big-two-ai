from utils.hand_helper import HandHelper
from brain.play_selector import PlaySelector 

if __name__ == "__main__":
    helper = HandHelper()
    # hand = helper.generate_hand_from_list(['3C', '3D', '3H', '3S', '6S', '7D', '8C', '9C', '9H', '0C', 'QC', '2D', '2H'])
    hand = helper.generate_random_hand()
    helper.print_hand(hand)

    last_played = ['5H','5S','5C','2S','2D']
    last_played = helper.generate_hand_from_list(last_played)
    print("Last played:", last_played)
    print()
    
    play_selector = PlaySelector(hand)
    print(play_selector.find_playable_cards(last_played))