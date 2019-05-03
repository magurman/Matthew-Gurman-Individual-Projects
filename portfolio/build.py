import pandas as pd 
import classes as cl
import scrape_data as sd

def display_menu():
    print("Stock Return Calculator")
    
def read_data(file):
    #read csv
    trans = pd.read_csv(file)
    #trans = trans.dropna()
    return trans

#Read in csv of transactions and create list of Transaction objects
def list_of_tr(df):
   
    #create empty transaction list 
    transactions = []
   
    #append transaction objects to list of transactions -- will have list of unique transaction objects
    for index, row in df.iterrows():
        transactions.append(cl.Transaction(row['symbol'], row['company'], row['date'],
                                    row['quantity'], row['price'], row['order_type'],
                                    row['commission']))
    return transactions

def list_of_eq(df):
    
    eq = []
    equities = []
     
    #unique list of stock symbols from dataframe
    eq = df.symbol.unique().tolist()
    
    #list of equity objects 
    for i in eq:
        equities.append(cl.Equity(i, 0, 0, 0, 0, 0))
    return equities

def populate_equities(tr, eq):
    #loop through equity objects
    for i in eq:
        #for each transaction
        for j in tr:
            if i.symbol == j.symbol and j.order_type == 'buy':
                i.total_shares += j.quantity
                i.total_buys += j.price * j.quantity
            elif i.symbol == j.symbol and j.order_type == 'sell':
                i.total_shares -= j.quantity
                i.total_sells += j.price * j.quantity
    return eq
    
def calculate_indiv_return(eq):
    
    equity = str(input("Which equity do you want to calculate a return for (stock symbol): "))
    
    #gets string of outputs from scrape_data method, locates index of closing price 
    #locates index of beginning of next entry and then grabs the string between those indexes 
    string = sd.load_csv_data(equity)[1]
    index = find_nth(string, ",",4)
    length = find_nth(string, ",",5) - find_nth(string, ",",4) - 1
    price = string[(index + 1):(index + length + 1)]
    #conditional if web scraber messes up
    if price == '    "finance": ':
        px_last = float(input("What is the current price of the stock?: "))
    else:
        px_last = float(price)

    rtrn = 0
    for i in eq:
        if i.symbol == equity:
            mkt_value = px_last * i.total_shares
            rtrn = ((mkt_value + i.total_sells) - i.total_buys) / i.total_buys
    return rtrn


#unsued function that was causing me difficulty
'''def calculate_return_all(eq):
    prices = []
    for i in eq:
        i.symbol = str(i.symbol)
        #print(i.symbol)
        string = sd.load_csv_data(i.symbol)
        #print(string)
        prices.append(string)
    for i in prices:
        string2 = i[1]
        print(string2)
        index = find_nth(string2, ",",4)
        length = find_nth(string2, ",",5) - find_nth(string2, ",",4) - 1
        price = string2[(index + 1):(index + length + 1)]
        print(price)'''

def find_nth(text, character, n):
    start = text.find(character)
    while start >= 0 and n > 1:
        start = text.find(character, start+len(character))
        n -= 1
    return start
    
def main():
    display_menu()
    file = str(input("Enter a file path for your list of transactions file: "))
    df = read_data(file)
    eq = populate_equities(list_of_tr(df), list_of_eq(df))
    #stock_return = calculate_return_all(eq)
    cont = 'y'
    while cont == 'y':
        
        stock_return = calculate_indiv_return(eq)
        stock_return = "{:.1%}".format(stock_return)
        
        print("Your return on this equity is: ", stock_return)
        cont = input("Do you want to calculate the return of another stock? (y/n)")
    print()
    print("Thank you! Bye!")
    
if __name__ == "__main__":
   main()

#FilePath: /Users/mattgurman/Projects/python/portfolio/portfolio.csv