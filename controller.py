from models import RANKS, SUITS, Card, Deck, Player
import view


class Controller:
    """Définie le controleur"""
    def __init__(self, deck, view):
        # models
        self.players = []
        self.deck = deck

        # view
        self.view = view

    def get_players(self):
        """Création de la liste de joueur"""
        while len(self.players) < 5: #nombre magique
            name = self.view.prompt_for_player()
            if not name:
                return
            player = Player(name)
            self.players.append(player)

    def start_game(self):
        """Distribution des cartes"""
        self.deck.shuffle()
        for player in self.players:
            card = self.deck.draw_card()
            if card:
                player.hand.append(card)

    def evaluate_game(self):
        last_player = self.players[0]
        best_player = self.players[0]

        for player in self.players[1:]:
            player_card = player.hand[0]
            last_player_card = last_player.hand[0]

            if player_card > last_player_card:
                best_candidate = player

            last_player = player
        return best_candidate.name

    def rebuilt_deck(self):
        for player in self.players:
            while player.hand:
                card = player.hand.pop()
                card.is_face_up = False
                self.deck.append(card)
        self.deck.shuffle()


    def run(self):
        self.get_players()

        running = True
        while running:
            self.start_game()

            for player in self.players:
                self.view.show_player_hand(player.name, player.hand) # appelle une view

            self.view.prompt_for_flip_cards()

            for player in self.players:
                for card in player.hand:
                    card.is_face_up = True

            self.view.show_player_hand(player.name, player.hand)

            self.view.show_winner(self.evaluate_game())

            running = self.view.prompt_for_new_game()
            self.rebuilt_deck()
