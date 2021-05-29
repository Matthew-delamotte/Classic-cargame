from models import *
from controller import *


class PlayerView:

    def prompt_for_player(self):
        name = input("Tapez le nom du joueur: ")
        if not name:
            return None
        return name

    def show_player_hand(self, name, hand):
        print(f'[Joueur {name}]')
        for card in hand:
            if card.is_face_up:
                print(card)
            else:
                print("(carte face cachée)")

    def prompt_for_flip_cards(self):
        print()
        input("Prêt à retourner les cartes ?")
        return True

    def show_winner(self, name):
        print(f"Bravo {name}")

    def prompt_for_new_game(self):
        print("Souhaitez vous refaire une partie ?")
        choice = input("Y/n: ")
        if choice == "n":
            return False
        return True


class BroadcastView:
    def prompt_for_player(self):
        return None

    def show_player_hand(self, name, hand):
        pass
        # Implémentation possible

    def prompt_for_flip_cards(self):
        return True

    def show_winner(self, name):
        pass
        # Implémentation possible

    def prompt_for_new_game(self):
        return True


class InternetStreamingView:
    def prompt_for_player(self):
        return None

    def show_player_hand(self, name, hand):
        pass
        # Implémentation possible

    def prompt_for_flip_cards(self):
        return True

    def show_winner(self, name):
        pass
        # Implémentation possible

    def prompt_for_new_game(self):
        return True
