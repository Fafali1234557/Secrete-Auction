"""Automated tests for the Secret Auction project.

Run from the project folder:
    python -m unittest -v
"""

import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

import auction


class TestFindHighestBidder(unittest.TestCase):
    def test_single_bidder(self):
        self.assertEqual(auction.find_highest_bidder({"Ama": 50}), ("Ama", 50))

    def test_highest_bidder_in_middle(self):
        bids = {"Ama": 20, "Kofi": 100, "Akosua": 60}
        self.assertEqual(auction.find_highest_bidder(bids), ("Kofi", 100))

    def test_first_bidder_wins_tie(self):
        bids = {"Ama": 90, "Kofi": 90, "Akosua": 70}
        self.assertEqual(auction.find_highest_bidder(bids), ("Ama", 90))

    def test_empty_bids_raise_value_error(self):
        with self.assertRaises(ValueError):
            auction.find_highest_bidder({})


class TestInputValidation(unittest.TestCase):
    def test_name_trims_whitespace(self):
        with patch("builtins.input", return_value="  Ama  "):
            self.assertEqual(auction.get_bidder_name({}), "Ama")

    def test_empty_name_is_reprompted(self):
        with patch("builtins.input", side_effect=["   ", "Ama"]):
            with redirect_stdout(io.StringIO()):
                self.assertEqual(auction.get_bidder_name({}), "Ama")

    def test_duplicate_name_is_reprompted_case_insensitively(self):
        with patch("builtins.input", side_effect=["  ama ", "Kofi"]):
            with redirect_stdout(io.StringIO()):
                self.assertEqual(auction.get_bidder_name({"Ama": 10}), "Kofi")

    def test_positive_bid_is_accepted(self):
        with patch("builtins.input", return_value=" 42 "):
            self.assertEqual(auction.get_bid_amount(), 42)

    def test_invalid_text_bid_is_reprompted(self):
        with patch("builtins.input", side_effect=["twenty", "45"]):
            with redirect_stdout(io.StringIO()):
                self.assertEqual(auction.get_bid_amount(), 45)

    def test_decimal_bid_is_reprompted(self):
        with patch("builtins.input", side_effect=["12.50", "13"]):
            with redirect_stdout(io.StringIO()):
                self.assertEqual(auction.get_bid_amount(), 13)

    def test_negative_bid_is_reprompted(self):
        with patch("builtins.input", side_effect=["-10", "10"]):
            with redirect_stdout(io.StringIO()):
                self.assertEqual(auction.get_bid_amount(), 10)

    def test_zero_bid_is_reprompted(self):
        with patch("builtins.input", side_effect=["0", "5"]):
            with redirect_stdout(io.StringIO()):
                self.assertEqual(auction.get_bid_amount(), 5)

    def test_yes_with_capitals_and_spaces(self):
        with patch("builtins.input", return_value=" YES "):
            self.assertTrue(auction.has_more_bidders())

    def test_no_with_capitals_and_spaces(self):
        with patch("builtins.input", return_value=" No "):
            self.assertFalse(auction.has_more_bidders())

    def test_invalid_yes_no_reprompts(self):
        with patch("builtins.input", side_effect=["maybe", "no"]):
            with redirect_stdout(io.StringIO()):
                self.assertFalse(auction.has_more_bidders())


class TestAuctionFlow(unittest.TestCase):
    def test_single_bidder_receives_win(self):
        output = io.StringIO()
        with patch("builtins.input", side_effect=["Ama", "15", "no"]):
            with patch("auction.clear_screen") as mock_clear:
                with redirect_stdout(output):
                    auction.run_auction()
        mock_clear.assert_called_once()
        self.assertIn("The winner is Ama with a bid of $15.", output.getvalue())

    def test_multiple_bidders_find_maximum(self):
        output = io.StringIO()
        answers = ["Ama", "50", "yes", "Kofi", "120", "yes", "Yaw", "95", "no"]
        with patch("builtins.input", side_effect=answers):
            with patch("auction.clear_screen") as mock_clear:
                with redirect_stdout(output):
                    auction.run_auction()
        self.assertEqual(mock_clear.call_count, 3)
        self.assertIn("The winner is Kofi with a bid of $120.", output.getvalue())

    def test_run_auction_handles_invalid_entries(self):
        output = io.StringIO()
        answers = [" ", "Ama", "hi", "0", "1000", "maybe", "YES",
                   "ama", "Esi", "999", "no"]
        with patch("builtins.input", side_effect=answers):
            with patch("auction.clear_screen"):
                with redirect_stdout(output):
                    auction.run_auction()
        self.assertIn("The winner is Ama with a bid of $1,000.", output.getvalue())

    def test_main_handles_interrupted_input(self):
        output = io.StringIO()
        with patch("builtins.input", side_effect=KeyboardInterrupt):
            with redirect_stdout(output):
                auction.main()
        self.assertIn("Auction cancelled", output.getvalue())

    def test_main_handles_closed_input(self):
        output = io.StringIO()
        with patch("builtins.input", side_effect=EOFError):
            with redirect_stdout(output):
                auction.main()
        self.assertIn("Auction cancelled", output.getvalue())


if __name__ == "__main__":
    unittest.main()
