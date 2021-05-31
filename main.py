# """Entry point."""
#
# from models.deck import Deck
# from controllers.base import Controller
# from controllers.evaluate import CheckerRankAndSuitIndex
# from views.base import PlayerView
# from views.broadcast import BroadcastView
# from views.internet import InternetStreamingView
#
#
# def main():
#     deck = Deck()
#     views = (PlayerView(), BroadcastView(), InternetStreamingView())
#     checker = CheckerRankAndSuitIndex()
#     game = Controller(deck, views, checker)
#     game.run()
#
#
# if __name__ == "__main__":
#     main()

class PersonException(Exception):
    pass


class InvalidDOBPersonException(PersonException):
    pass


try:
    raise InvalidDOBPersonException("Invalid Date of Birth")
except PersonException:
    print("PersonException caught")
except InvalidDOBPersonException("Invalid Date of Birth"):
    print("InvalidDOBPersonException caught")
except Exception:
    print("Exception caught.")