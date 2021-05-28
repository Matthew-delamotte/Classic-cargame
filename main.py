from controller import Controller, CheckerRankAndSuitIndex
from view import PlayerView, BroadcastView, InternetStreamingView
from models import Deck


def main():
    deck = Deck()
    views = (PlayerView(), BroadcastView(), InternetStreamingView())
    checker = CheckerRankAndSuitIndex
    game = Controller(deck, views, checker)
    game.run()


if __name__ == "__main__":
    main()