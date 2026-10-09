# 🔨 Secret Auction — Python CLI

**A beginner-friendly, interactive command-line auction simulator built with Python.**

Collect bids from multiple participants, validate their entries, and announce the highest bidder when the auction ends. This project demonstrates how functions, dictionaries, loops, conditionals, and input validation work together in a practical Python program.

> **Educational project:** This is a local, terminal-based auction simulation. It does **not** accept payments, send real bids, or securely conceal entries. Previous inputs may remain visible in terminal scrollback.

## ✨ Features

- **Multiple bidders:** Keep collecting names and bid amounts until there are no more bidders.
- **Automatic winner selection:** Find the highest bid using Python's `max()` function.
- **Input validation:** Reject empty names, repeated bidder names, non-numeric bids, and bids of $0 or less.
- **Flexible answers:** Accept `yes` and `no` regardless of capitalization or surrounding whitespace.
- **Visual separation:** Print blank lines between bidders so the next participant starts with a clear-looking screen.
- **Predictable ties:** If two people bid the same highest amount, the **first bidder** wins.
- **Clean exit:** Handle `Ctrl+C` and end-of-file input without a Python traceback.
- **Automated tests:** Test validation, winner selection, and complete bidding sessions with `unittest`.
- **Zero third-party dependencies:** Uses the Python standard library only.

## 📂 Project structure

```text
secret-auction-python/
├── auction.py          # Main application and auction logic
├── art2.py             # Local ASCII banner (included, no extra install)
├── test_auction.py     # Automated unit and flow tests
├── README.md           # Project documentation
└── .gitignore          # Files to exclude from Git
```

## 🚀 Getting started

### Requirements

- Python **3.8 or newer**
- A terminal (Windows PowerShell, Command Prompt, macOS Terminal, or Linux shell)

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/secret-auction-python.git
cd secret-auction-python
```

Or download the project ZIP and extract it. Replace `Fafali1234557` with your GitHub username if you use the clone command.

### 2. Run the auction

```bash
python auction.py
```

If `python` is not recognized, try `py auction.py` on Windows or `python3 auction.py` on Linux/macOS.

**No `pip install` is required.** The `art2.py` file is included with the project.

## 💻 Example session

```text
Welcome to the Secret Auction!

What is your name?
> Ama
What is your bid?
$ 100
Are there any other bidders? Type 'yes' or 'no':
> yes

[The screen is visually separated for the next bidder.]

What is your name?
> Kofi
What is your bid?
$ 150
Are there any other bidders? Type 'yes' or 'no':
> no

The winner is Kofi with a bid of $150.
```

### Auction rules

| Situation | Program behavior |
|---|---|
| A name is blank | Ask again |
| A bidder name is already used | Ask for another name (case-insensitive) |
| A bid contains letters or decimals | Ask for a whole-number bid |
| A bid is $0 or negative | Ask for a positive bid |
| `yes` / `no` has extra spaces or uppercase | Accept it |
| Another response is entered for `yes` / `no` | Ask again |
| Two bids tie for the highest | Earlier bidder wins |

**Currency:** `$` is used as an example in the console. No real financial transaction occurs.

## 🧠 How it works

**1. Collect a bidder's name.** `get_bidder_name()` checks that the name is not empty and hasn't already been entered.

**2. Read a positive bid.** `get_bid_amount()` uses `int()` inside `try/except` to reject invalid numbers safely.

**3. Store the bid.** The `bids` dictionary keeps names as keys and amounts as values:

```python
bids = {
    "Ama": 100,
    "Kofi": 150,
    "Esi": 125,
}
```

**4. Repeat for the next person.** `has_more_bidders()` keeps the auction running while new participants are available.

**5. Find the winner.** `find_highest_bidder()` selects the largest amount:

```python
winner, winning_bid = max(bids.items(), key=lambda entry: entry[1])
```

Python dictionaries preserve insertion order, so when the highest amounts tie, the first recorded bidder wins.

**6. Show the result.** The winner's name and bid amount are announced after the final entry.

## 🧪 Running the tests

From the project directory, run:

```bash
python -m unittest -v
```

The test suite covers winner selection, tie behavior, invalid and repeated names, invalid bids, yes/no validation, multi-bidder sessions, and cancellation.

## 📚 Concepts practiced

- Functions, parameters, and return values
- Dictionaries and key-value pairs
- Loops (`while`)
- Conditional statements (`if` / `elif` / `else`)
- Comparison operators
- String methods: `.strip()`, `.lower()`, `.casefold()`
- Exception handling (`try` / `except`)
- Built-in functions: `int()`, `max()`, `any()`
- Separating program logic into reusable functions
- Testing with Python's `unittest` and `unittest.mock`

## 🛠️ Potential future improvements

- [ ] Let bidders use a secret bidder ID instead of entering names in public.
- [ ] Add an administrator-only results screen.
- [ ] Support decimal currency amounts using `decimal.Decimal`.
- [ ] Save bids and auction results to a file or database.
- [ ] Build a graphical interface (Tkinter) or web application.
- [ ] Introduce meaningful authentication and secure storage if adapting this to real auctions.

## 🎯 Why I built this

I built this project to turn Python fundamentals into a small interactive application. It helped me practice problem-solving, dictionaries, loops, functions, validation, and choosing a result from user-provided data.

**Feedback and suggestions are welcome. If you find the project useful, consider giving the repository a star!** ⭐
