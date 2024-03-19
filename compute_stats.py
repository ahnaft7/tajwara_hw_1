"""
Ahnaf Tajwar
Class: CS 677
Date: 3/16/23
Homework Problem # 1-2
Description of Problem (just a 1-2 line summary!): This problem is to compute the mean and standard deviation for all, positive, and negative returns for each day in each year. The results are added to a table.
"""

import os
import csv
from collections import defaultdict
import statistics
from tabulate import tabulate
from math import sqrt

ticker='TSLA'
here = os.path.abspath(__file__)
input_dir =os.path.abspath(os.path.join(here,os.pardir))
ticker_file = os.path.join(input_dir, ticker + '.csv')

try:   
    with open(ticker_file) as f:
        lines = f.read().splitlines()
    print('opened file for ticker: ', ticker)
    """    your code for assignment 1 goes here
    """

    day_year_returns = defaultdict(lambda: defaultdict(list))

    # Get returns for each day in each year and append to dictionary
    for row in lines[1:]:
        fields = row.split(',')
        year = int(fields[1])

        if 2016 <= year <= 2020:  # Filter for years 2016-2020
            weekday = fields[4]
            return_value = float(fields[13])
            day_year_returns[year][weekday].append(return_value)
        
    # Calculate the mean return and standard deviation for each day in each year
    day_year_statistics = {}
    for year, days_data in day_year_returns.items():
        day_year_statistics[year] = {}
        for weekday, returns in days_data.items():
            mean_returns = sum(returns) / len(returns)

            # Calculate the sum of squares
            # sum_squares = sum((val - mean_returns) ** 2 for val in returns)

            # Calculate the population standard deviation
            # std_dev = sqrt(sum_squares / len(returns))

            # Calculating std_dev using statistics library
            std_dev = statistics.stdev(returns)
            neg_returns = [] 
            pos_returns = []
            for val in returns:
                if val >= 0:
                    pos_returns.append(val)
                else:
                    neg_returns.append(val)
            neg_mean = sum(neg_returns) / len(neg_returns)
            pos_mean = sum(pos_returns) / len(pos_returns)
            neg_std_dev = statistics.stdev(neg_returns)
            pos_std_dev = statistics.stdev(pos_returns)

            # sum_squares_neg = sum((val - neg_mean) ** 2 for val in neg_returns)
            # sum_squares_pos = sum((val - pos_mean) ** 2 for val in pos_returns)
            # neg_std_dev = sqrt(sum_squares_neg / len(neg_returns))
            # pos_std_dev = sqrt(sum_squares_pos / len(pos_returns))

            day_year_statistics[year][weekday] = (mean_returns, std_dev, len(neg_returns), neg_mean, neg_std_dev, len(pos_returns), pos_mean, pos_std_dev)

    # Print the mean return and standard deviation for each day in each year
    table_data = []
    for year, days_data in day_year_statistics.items():
        for weekday, stats in days_data.items():
            mean_return, std_dev, neg_returns_count, neg_mean, neg_std_dev, pos_returns_count, pos_mean, pos_std_dev = stats
            table_data.append([year, weekday, round(mean_return, 4), round(std_dev, 4), neg_returns_count, round(neg_mean, 4), round(neg_std_dev, 4), pos_returns_count, round(pos_mean, 4), round(pos_std_dev, 4)])
    
    headers = ["Year", "Weekday", "Mean Return", "Std Dev", "Neg Returns", "Neg Mean", "Neg Std Dev", "Pos Returns", "Pos Mean", "Pos Std Dev"]

    # Output the table
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
    
except Exception as e:
    print(e)
    print('failed to read stock data for ticker: ', ticker)
