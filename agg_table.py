"""
Ahnaf Tajwar
Class: CS 677
Date: 3/16/23
Homework Problem # 3
Description of Problem (just a 1-2 line summary!): This problem is to do the same as problem 1, but this time do it for each day for all 5 years together as well as SPY.
"""

import os
import csv
from collections import defaultdict
import statistics
from tabulate import tabulate

tickers = ['TSLA', 'SPY']

for ticker in tickers:
    here = os.path.abspath(__file__)
    input_dir = os.path.abspath(os.path.join(here, os.pardir))
    ticker_file = os.path.join(input_dir, ticker + '.csv')

    try:
        with open(ticker_file) as f:
            lines = f.read().splitlines()
        print('opened file for ticker: ', ticker)

        weekday_returns = defaultdict(list)

        # Get returns for each day and append to dictionary
        for row in lines[1:]:
            fields = row.split(',')
            weekday = fields[4]
            return_value = float(fields[13])
            weekday_returns[weekday].append(return_value)

        # Calculate the mean return and standard deviation for each weekday
        weekday_statistics = defaultdict(tuple)
        for weekday, returns in weekday_returns.items():
            mean_returns = sum(returns) / len(returns)
            std_dev = statistics.stdev(returns)
            neg_returns = [val for val in returns if val < 0]
            pos_returns = [val for val in returns if val >= 0]
            neg_mean = sum(neg_returns) / len(neg_returns) if neg_returns else 0
            pos_mean = sum(pos_returns) / len(pos_returns) if pos_returns else 0
            neg_std_dev = statistics.stdev(neg_returns) if len(neg_returns) > 1 else 0
            pos_std_dev = statistics.stdev(pos_returns) if len(pos_returns) > 1 else 0
            weekday_statistics[weekday] = (round(mean_returns, 4), round(std_dev, 4), len(neg_returns), round(neg_mean, 4), round(neg_std_dev, 4), len(pos_returns), round(pos_mean, 4), round(pos_std_dev, 4))

        # Prepare table data
        table_data = []
        for weekday, stats in weekday_statistics.items():
            mean_return, std_dev, neg_returns_count, neg_mean, neg_std_dev, pos_returns_count, pos_mean, pos_std_dev = stats
            table_data.append([weekday, mean_return, std_dev, neg_returns_count, neg_mean, neg_std_dev, pos_returns_count, pos_mean, pos_std_dev])

        headers = ["Weekday", "Mean Return", "Std Dev", "Neg Returns", "Neg Mean", "Neg Std Dev", "Pos Returns", "Pos Mean", "Pos Std Dev"]

        # Output the table
        print(tabulate(table_data, headers=headers, tablefmt="grid"))

    except Exception as e:
        print(e)
        print('failed to read stock data for ticker: ', ticker)