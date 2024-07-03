"""Module creating Bidder class."""

class Bidder:
    '''Class to represent a bidder in an online second-price ad auction'''
    def __init__(self, num_users, num_rounds):
        '''Setting number of users and number of rounds'''
        #self.balance = 0
        self.num_users = num_users
        self.num_rounds = num_rounds

    def __repr__(self):
        '''Return Bidder object with balance'''
        return "Bidder object with " + self.num_rounds + "left in the game."

    def __str__(self):
        '''Return Bidder object with balance'''
        return self.__repr__()

    def bid(self, user_id):
        '''Returns a non-negative bid amount'''
        return 500

    def notify(self, auction_winner, price, clicked):
        '''Updates bidder attributes based on results from an auction round'''
        if auction_winner:
            if clicked:
                return "User clicked your ad."
            return "User did not click your ad."
        return "You did not win the round. The winning price is " + str(price) + "."
            