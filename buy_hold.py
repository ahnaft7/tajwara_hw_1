"""
Ahnaf Tajwar
Class: CS 677
Date: 3/16/23
Homework Problem # 5
Description of Problem (just a 1-2 line summary!): This problem is to calculate the total ending balance after 5 years if everyday is traded on starting with $100.
"""

import os

tickers = ['TSLA', 'SPY']

for ticker in tickers:
    here = os.path.abspath(__file__)
    input_dir = os.path.abspath(os.path.join(here, os.pardir))
    ticker_file = os.path.join(input_dir, ticker + '.csv')

    start_amount = 100
    current_amount = start_amount

    try:
        with open(ticker_file) as f:
            lines = f.read().splitlines()
        print('opened file for ticker: ', ticker)

        # Get returns
        for row in lines[1:]:
            fields = row.split(',')
            return_value = float(fields[13])
            
            # Make the trade everyday
            current_amount *= (1 + return_value)

        print(f"Total amount at the end date: ${current_amount:.2f}")


    except Exception as e:
        print(e)
        print('failed to read stock data for ticker: ', ticker)