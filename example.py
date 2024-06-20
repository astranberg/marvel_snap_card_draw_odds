import simulations.py as sim

# Define the cards
cards_without_domino = [
    Card("Infinaut", tags=["big"]),
    Card("Magneto", tags=["big"]),
    Card("RedHulk", tags=["big"]),
    Card("Blade", tags=["discard"]),
    Card("LadySif", tags=["discard"]),
    Card("GhostRider", tags=["revive"]),
    Card("Jeff"),
    Card("BlackKnight"),
    Card("RedGuardian"),
    Card("MsMarvel"),
    Card("Blink"),
    Card("Sandman")
]
cards_with_domino = [
    Card("Infinaut", tags=["big"]),
    Card("Magneto", tags=["big"]),
    Card("RedHulk", tags=["big"]),
    Card("Blade", tags=["discard"]),
    Card("LadySif", tags=["discard"]),
    Card("GhostRider", tags=["revive"]),
    Card("Domino", tags=["2"]),  # Always drawn on turn 2
    Card("BlackKnight"),
    Card("RedGuardian"),
    Card("MsMarvel"),
    Card("Blink"),
    Card("Sandman")
]

deck_without_domino = Deck(cards_without_domino)
deck_with_domino = Deck(cards_with_domino)

# Define tag queries
tag_queries = {
    "big": 3,
    "discard": 3,
    "revive": 5
}

odds_without_domino = calculate_odds(deck_without_domino, tag_queries)
odds_with_domino = calculate_odds(deck_with_domino, tag_queries)

print("odds_without_domino", odds_without_domino)
print("odds_with_domino", odds_with_domino)
