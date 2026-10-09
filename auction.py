"""A beginner-friendly, terminal-based secret auction game.

Bidders enter their names and whole-dollar bids one at a time.
The application announces the highest bidder after the last entry.
"""

from art2 import logo


def get_bidder_name(existing_bids):
    """Ask for a non-empty name that has not already been used."""
    while True:
        name = input("What is your name?\n> ").strip()

        if not name:
            print("Name cannot be empty. Please try again.")
        elif any(name.casefold() == bidder.casefold() for bidder in existing_bids):
            print("This bidder name has already been used. Try another name.")
        else:
            return name


def get_bid_amount():
    """Ask for a positive, whole-dollar bid."""
    while True:
        raw_bid = input("What is your bid?\n$ ").strip()

        try:
            bid = int(raw_bid)
        except ValueError:
            print("Invalid bid. Please enter a whole number, such as 50.")
            continue

        if bid <= 0:
            print("Your bid must be greater than $0.")
            continue

        return bid


def has_more_bidders():
    """Return True for 'yes' and False for 'no'; retry invalid answers."""
    while True:
        answer = input(
            "Are there any other bidders? Type 'yes' or 'no':\n> "
        ).strip().lower()

        if answer == "yes":
            return True
        if answer == "no":
            return False

        print("Please type 'yes' or 'no'.")


def clear_screen():
    """Visually separate bidders by moving earlier entries out of view.

    This does not securely erase terminal history or hide the screen
    from other people.
    """
    print("\n" * 50, end="")


def find_highest_bidder(bids):
    """Return (name, amount); the earliest bidder wins any tie."""
    if not bids:
        raise ValueError("Cannot find a winner without any bids.")

    return max(bids.items(), key=lambda entry: entry[1])


def run_auction():
    """Collect bids until the user says there are no more bidders."""
    print(logo)
    print("Welcome to the Secret Auction!\n")
    bids = {}

    while True:
        name = get_bidder_name(bids)
        amount = get_bid_amount()
        bids[name] = amount

        more_bidders = has_more_bidders()
        clear_screen()
        if not more_bidders:
            break

    winner, winning_bid = find_highest_bidder(bids)
    print(f"The winner is {winner} with a bid of ${winning_bid:,}.")


def main():
    try:
        run_auction()
    except (KeyboardInterrupt, EOFError):
        print("\nAuction cancelled before a winner was announced.")


if __name__ == "__main__":
    main()
