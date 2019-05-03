
#Define Transaction class
class Transaction: 
    
    def __init__(self, symbol, company, date, quantity, price, order_type, commission):
        self.symbol = symbol 
        self.company = company
        self.date = date
        self.quantity = quantity
        self.price = float(price)
        self.order_type = order_type
        self.commission = commission 
        
#Define Equity class        
class Equity:
    #initializer 
    def __init__(self, symbol, total_shares, total_buys, total_sells, market_value, rtrn):
        self.symbol = symbol
        self.total_shares = total_shares 
        self.total_buys = total_buys
        self.total_sells = total_sells
        self.market_value = market_value
        self.rtrn = rtrn
        
