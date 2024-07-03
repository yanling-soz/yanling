"""Module creating User and Auction class"""
import numpy as np

class User:
    '''Class to represent a user with a secret probability of clicking an ad.'''
    def __init__(self):
        '''Generating a probability between 0 and 1 from a uniform distribution'''
        self.__probability = np.random.uniform(0, 1)

    def __repr__(self):
        '''User object with secret probability'''
        return "User with secret probability " + str(self.__probability)

    def __str__(self):
        '''User object with a secret likelihood of clicking on an ad'''
        return "User with a secret likelihood " + str(self.__probability) + " of clicking on an ad"

    def show_ad(self):
        '''Returns True to represent the user clicking on an ad or False otherwise'''
        return np.random.choice([True, False], p = [self.__probability, 1 - self.__probability])

class Auction:
    '''Class to represent an online second-price ad auction'''
    def __init__(self, users, bidders):
        '''Initializing users, bidders, and dictionary
        to store balances for each bidder in the auction'''
        self.users = users
        self.bidders = bidders
        self.balances = {b:0 for b in bidders}

    def __repr__(self):
        '''Return auction object with users and qualified bidders'''
        return f"Auction object with users {self.users} and bidders {self.bidders}"

    def __str__(self):
        '''Return auction object with users and qualified bidders'''
        return self.__repr__()

    def execute_round(self):
        '''Executes a single round of an auction, completing the following steps:
        - random user selection
        - bids from every qualified bidder in the auction
        - selection of winning bidder based on maximum bid
        - selection of actual price (second-highest bid)
        - showing ad to user and finding out whether or not they click
        - notifying winning bidder of price and user outcome and updating balance
        - notifying losing bidders of price'''
        # Select random user with uniform probability
        selected_user = np.random.choice(self.users)

        # Return bidders' bid amount
        bids = {}
        for bidder in self.bidders:
            if self.balances[bidder] < -1000:
                raise Exception("Bidder can no logger bid due to insufficient balance.")
            bids[bidder] = bidder.bid(selected_user)

        # Find the winner of the auction
        winning_bidders = list(filter(lambda x: bids[x] == max(bids.values()), bids))
        if len(winning_bidders) == 0:
            winning_bidder = winning_bidders[0]
        else:
            winning_bidder = np.random.choice(winning_bidders)

        # Select the winning price by selecting the second-highest bid
        winning_prices = -1*np.sort(-1*np.unique([*bids.values()]))
        if len(winning_prices) == 1:
            winning_price = winning_prices[0]
        else:
            winning_price = winning_prices[1]

        # Return if user clicked on the ad
        user_clicked = selected_user.show_ad()

        # Results for each bidder
        for bidder in self.bidders:
            if bidder == winning_bidder:
                bidder.notify(True, winning_price, user_clicked)
                self.balances[bidder] -= winning_price
                if user_clicked:
                    self.balances[bidder] += 1
            else:
                bidder.notify(False, winning_price, None)

    def plot_history(self):
        '''Creates a visual representation of how the auction has proceeded'''
        pass
    
