from models import *
from view import *


class CheckerRankAndSuitIndex:
    def check(self, players):
        """Evalue la meilleur carte"""
        last_player = self.players[0]
        best_candidate = self.players[0]

        for player in self.players[1:]:
            player_card = player.hand[0]
            last_player_card = last_player.hand[0]

            score = (RANKS.index(player_card.rank), SUITS.index(player_card.suit))
            last_score = (
                RANKS.index(last_player_card.rank),
                SUITS.index(last_player_card.suit),
            )

            if score[0] == last_score[0]:
                if score[1] > last_score[1]:
                    best_candidate = player
            elif score[0] > last_score[0]:
                best_candidate = player

            last_player = player

        return best_candidate.name


class Controller:
    """Définie le controleur"""
    def __init__(self, deck, views, checker_strategy):
        # models
        self.players = []
        self.deck = deck

        # view
        self.views = views

        self.checker_strategy = checker_strategy()

    def get_players(self):
        while len(self.players) < 5:  # nombre magique
            choices = []
            for view in self.views:
                name = view.prompt_for_player()
                choices.append(name)
                if not any(choices):
                    return
            for choice in choices:
                if choice:
                    name = choice
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
        self.checker_strategy.check()

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

                for view in self.views:
                    view.show_player_hand(player.name, player.hand)

            for view in self.views:
                view.prompt_for_flip_cards()
            print()

            for player in self.players:
                for card in player.hand:
                    card.is_face_up = True
                for view in self.views:
                    view.show_player_hand(player.name, player.hand)
            print()

            for view in self.views:
                view.show_winner(self.evaluate_game())

            for view in self.views:
                running = view.prompt_for_new_game()
                if not running:
                    return

            self.rebuild_deck()