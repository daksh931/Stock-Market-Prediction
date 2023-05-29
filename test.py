from yahoo_fin.stock_info import *
import yahoo_fin.stock_info as si


# def tabledata():
#     # Stocklist = ['TSLA','AAPL','BAC','MARA','AMZN','NVDA','NIO','RIOT','GOOGL','INFY','PLUG','APE','SOFI','META','MSFT','SNAP','USB','NYCB','DNA','UBER','AFRM','PYPL','PARA','MS','DELL','HPQ','HPE','DIS']
#     Stocklist = ['TSLA','AAPL','BAC']
#     # temp = si.get_quote_data('TSLA')
#     # stock_data = []
#     for i in Stocklist:
        
#         temp = (si.get_quote_data(i))
#         print(temp)
#     print(temp['price']['symbol'])

# tabledata()

def topLoseData():   
    top_gainers = 	si.get_day_gainers(3)
    stockcode = list(top_gainers['Symbol'])

    top_stock_data = []
    # print(top_gain_stocksCode)


    for i in stockcode:
        temp = (si.get_quote_data(i))
        temp = temp['price']
      
        top_stock_data.append([temp['symbol'],
                    temp['regularMarketPrice']['raw'],
                    temp['regularMarketDayHigh']['raw'],
                    temp['regularMarketDayLow']['raw']])
    print(top_stock_data)
topLoseData()
