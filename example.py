import simulation as sim

# Define the cards of the decks
cards_without_domino = [
    sim.Card("Infinaut", tags=["big"]),
    sim.Card("Magneto", tags=["big"]),
    sim.Card("RedHulk", tags=["big"]),
    sim.Card("Blade", tags=["discard"]),
    sim.Card("LadySif", tags=["discard"]),
    sim.Card("GhostRider", tags=["revive"]),
    sim.Card("Jeff"),
    sim.Card("BlackKnight"),
    sim.Card("RedGuardian"),
    sim.Card("MsMarvel"),
    sim.Card("Blink"),
    sim.Card("Sandman")
]
cards_with_domino = [
    sim.Card("Infinaut", tags=["big"]),
    sim.Card("Magneto", tags=["big"]),
    sim.Card("RedHulk", tags=["big"]),
    sim.Card("Blade", tags=["discard"]),
    sim.Card("LadySif", tags=["discard"]),
    sim.Card("GhostRider", tags=["revive"]),
    sim.Card("Domino", tags=["2"]),  # Always drawn on turn 2
    sim.Card("BlackKnight"),
    sim.Card("RedGuardian"),
    sim.Card("MsMarvel"),
    sim.Card("Blink"),
    sim.Card("Sandman")
]

deck_without_domino = sim.Deck(cards_without_domino)
deck_with_domino = sim.Deck(cards_with_domino)

# Define tag queries, which are essentially saying:
#    What are the odds of drawing a card tagged "big" by turn 3, tagged "discard" by turn 3, and "revive" by turn 5?
tag_queries = {
    "big": 3,
    "discard": 3,
    "revive": 5
}

# Perform the monte-carlos simulation
odds_without_domino = sim.calculate_odds(deck_without_domino, tag_queries)
odds_with_domino = sim.calculate_odds(deck_with_domino, tag_queries)

# Print the results!
print("odds_without_domino", odds_without_domino)
print("odds_with_domino", odds_with_domino)
