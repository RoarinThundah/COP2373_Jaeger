import random

class Card:
    # Represents a card
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        # Prints a label for the card
        return f"{self.rank} of {self.suit}"

class Deck:
    # Represents the deck
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    def __init__(self):
        # Builds the deck
        self.cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        #Shuffles deck
        random.shuffle(self.cards)
        print("Deck has been shuffled.")

    def deal_card(self):
        # Deals a card returns none if no cards left in deck
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None

def get_cards_to_replace(hand_size):
    #Prompt user on which card to replace
    indices_to_replace = []

    while True:
        # Prompt the user for input
        response = input(
            f"\nEnter card numbers to replace (1-{hand_size}), separated by commas (e.g., 1, 3, 5). Press 0 for none: ")

        response = response.strip()

        # Check if user wants to replace no cards
        if response == "0":
            return []  # Return an empty list

        # Reset list for each new attempt
        indices_to_replace = []
        is_valid = True

        parts = response.split(',')

        if not parts:
            print("Invalid input. Please try again.")
            continue

        for part in parts:
            try:
                # Clean up whitespace and convert to a number
                num_str = part.strip()
                if not num_str:
                    continue  # Ignore empty strings from double commas

                card_num = int(num_str)

                # Check if the number is in the valid range
                if 1 <= card_num <= hand_size:
                    index = card_num - 1  # Convert to 0-based index
                    if index not in indices_to_replace:
                        indices_to_replace.append(index)
                    else:
                        print(f"Note: You already selected card {card_num}.")
                else:
                    print(f"Error: Card number '{card_num}' is out of range (must be 1-{hand_size}).")
                    is_valid = False
                    break  # Exit the for-loop, prompt user again

            except ValueError:
                print(f"Error: '{part}' is not a valid number.")
                is_valid = False
                break  # Exit the for-loop, prompt user again

        if is_valid:
            return sorted(indices_to_replace)  # Return the list of 0-based indices

def play_poker_draw():
   #Main function
    print("--- Welcome to 5-Card Draw ---")

    # Create and shuffle the deck
    game_deck = Deck()
    game_deck.shuffle()

    # Deal the initial hand
    hand_size = 5
    hand = []
    for _ in range(hand_size):
        card = game_deck.deal_card()
        if card:
            hand.append(card)

    if len(hand) != hand_size:
        print("Error: Could not deal a full hand.")
        return

    print("\nYour initial 5-card hand:")
    for i, card in enumerate(hand):
        print(f"  {i + 1}: {card}")

    # Prompt user for cards to replace
    indices = get_cards_to_replace(hand_size)

    # Draw new cards
    if not indices:
        print("\nYou chose to keep all your cards.")
    else:
        print(f"\nReplacing {len(indices)} card(s)...")

        # Replace cards one by one
        for index in indices:
            old_card = hand[index]
            new_card = game_deck.deal_card()

            if new_card:
                hand[index] = new_card
                print(f"  Replaced {old_card}  ->  {new_card}")
            else:
                print("  The deck is out of cards! Cannot replace.")
                break  # Stop trying to replace if deck is empty

    # Print the final hand
    print("\nYour final hand:")
    for i, card in enumerate(hand):
        print(f"  {i + 1}: {card}")

    print("\n--- Game Over. Good luck! ---")

# Main execution block
if __name__ == "__main__":
    play_poker_draw()