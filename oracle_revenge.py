"""
Ahnaf Tajwar
Class: CS 677
Date: 3/16/23
Homework Problem # 6
Description of Problem (just a 1-2 line summary!): This problem is to calculate the total ending balance after 5 years similar to problem 4,
    but also missing the highest 10 days, taking the lowest 10 days, or missing the highest 5 days and taking the lowest 5 days.
"""

import os

tickers = ['TSLA', 'SPY']

for ticker in tickers:
    here = os.path.abspath(__file__)
    input_dir = os.path.abspath(os.path.join(here, os.pardir))
    ticker_file = os.path.join(input_dir, ticker + '.csv')

    start_amount = 100
    current_amount_exclude_best_10 = start_amount
    current_amount_include_worst_10 = start_amount
    current_amount_best_worst_5 = start_amount
    excluded_days = []
    included_days = []

    try:
        with open(ticker_file) as f:
            lines = f.read().splitlines()
        print('opened file for ticker: ', ticker)

        returns = []

        for row in lines[1:]:
            fields = row.split(',')
            return_value = float(fields[13])
            returns.append(return_value)

        # Sort returns in descending/ascending order
        sorted_returns_desc = sorted(returns, reverse=True)
        sorted_returns_asc = sorted(returns)

        # Exclude the top 10 days with the highest return
        excluded_days = sorted_returns_desc[:10]
        included_days = sorted_returns_asc[:10]

        for row in lines[1:]:
            fields = row.split(',')
            return_value = float(fields[13])
            
            # Only trade on days with positive return and not in the excluded days
            if return_value > 0 and return_value not in excluded_days:
                current_amount_exclude_best_10 *= (1 + return_value)
            
            # Only trade on days with positive return and in the included days
            if return_value > 0 or return_value in included_days:
                current_amount_include_worst_10 *= (1 + return_value)

            # Only trade on days with positive return and not in the top 5 excluded days and in the top 5 included days
            if return_value > 0 and return_value not in excluded_days[:5]:
                current_amount_best_worst_5 *= (1 + return_value)
            elif return_value in included_days[:5]:
                current_amount_best_worst_5 *= (1 + return_value)

        print(f"Total amount at the end date (excluding top 10 days with highest return): ${current_amount_exclude_best_10:.2f}")
        print(f"Total amount at the end date (including top 10 days with lowest return): ${current_amount_include_worst_10:.2f}")
        print(f"Total amount at the end date (excluding top 5 days with highest return and including top 5 days with lowest return): ${current_amount_best_worst_5:.2f}")

    except Exception as e:
        print(e)
        print('failed to read stock data for ticker: ', ticker)