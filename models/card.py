
"""Define the cards."""

SUITS = ("diamonds", "coeurs", "piques", "carreaux")
RANKS = (
    "deux",
    "trois",
    "quatre",
    "cinq",
    "six",
    "sept",
    "huit",
    "neuf",
    "dix",
    "valet",
    "reine",
    "roi",
    "ace",
)

class Card:
    """Init objet carte"""
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.is_face_up = False

        self._rank_score = RANKS.index(self.rank)
        self._suit_score = SUITS.index(self.suit)

    """Retourne une forme lisible de la carte"""
    def __str__(self):
        # Affichage "élégant"
        return f"{self.rank} de {self.suit}"

    def __repr__(self):
        # But d'affichage information précise de l'objet
        return str(self)

    """Méthode comparaison sur l'infériorité:
    permet de faire des comparaison entre objet
    mais comme si c'é'tait des nombres"""
    def __lt__(self, other= "Card"):
        if self._rank_score != other._rank_score:
            return self._rank_score < other._rank_score

        return self._suit_score < other._suit_score


card1 = Card("diamonds", "cinq")
card2 = Card("coeurs", "cinq")
card3 = Card("coeurs", "valet")
print(card1 < card2)
print(card3 > card2)