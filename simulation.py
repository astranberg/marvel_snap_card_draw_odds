import random
from collections import defaultdict

class Card:
    def __init__(self, name, tags=None):
        self.name = name
        self.tags = tags if tags else []
        self.tags.append(name)

    def __repr__(self):
        return f"Card(name={self.name}, tags={self.tags})"

class Deck:
    def __init__(self, cards):
        self.original_deck = cards[:]
        self.deck = cards[:]
        random.shuffle(self.deck)

    def draw(self, num, turn):
        # Draw cards that match the current turn number in their tags
        drawn_cards = [card for card in self.deck if str(turn) in card.tags][:num]
        remaining = num - len(drawn_cards)
        
        # Draw remaining cards from the deck if needed, excluding those with numeric tags
        if remaining > 0:
            non_numeric_tag_cards = [card for card in self.deck if not any(tag.isdigit() for tag in card.tags)]
            drawn_cards.extend(non_numeric_tag_cards[:remaining])
            self.deck = [card for card in self.deck if card not in drawn_cards]
        
        # Remove drawn cards from the deck
        self.deck = [card for card in self.deck if card not in drawn_cards]
        
        return drawn_cards
        
    def reset(self):
        self.deck = self.original_deck[:]
        random.shuffle(self.deck)
        
    def __repr__(self):
        return ', '.join(repr(card) for card in self.deck)

def calculate_odds(deck, tag_queries, simulations=10000, turns=6):
    results = defaultdict(lambda: defaultdict(int))
    all_queries_met_count = 0
        
    for tag, turn in tag_queries.items():
        results[tag][turn] = 0

    for _ in range(simulations):
        deck.reset()
        hand = []
        turn_results = defaultdict(list)
        
        for turn in range(turns + 1):  # Including turn 0 for initial draw
            if turn == 0:
                drawn = deck.draw(3, turn)  # Initial draw of 3 cards
            elif turn == 1:
                drawn = deck.draw(1, turn)  # Draw the fourth card on turn 1
            else:
                drawn = deck.draw(1, turn)
            
            for card in drawn:
                if card not in hand:  # Avoid duplicate adding
                    hand.append(card)
                    turn_results[turn].append(card)

                    if 'draw_another' in card.tags:
                        extra_card = deck.draw(1, turn)
                        hand.append(extra_card)
                        turn_results[turn].append(extra_card)

            always_drawn_cards = [card for card in deck.original_deck if 'always_drawn' in card.tags and card not in hand]
            for card in always_drawn_cards:
                hand.append(card)
                turn_results[turn].append(card)

        all_queries_met = True
        for tag, turn in tag_queries.items():
            found_tag = any(tag in card.tags for t in range(turn + 1) for card in turn_results[t])
            if found_tag:
                results[tag][turn] += 1
            else:
                all_queries_met = False

        if all_queries_met:
            all_queries_met_count += 1

    odds = {tag: {turn: count / simulations for turn, count in turn_data.items()}
            for tag, turn_data in results.items()}
    
    odds["all_queries_met"] = all_queries_met_count / simulations

    return odds
