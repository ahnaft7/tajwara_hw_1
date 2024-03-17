# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 14:37:29 2018

@author: epinsky
this scripts reads your ticker file (e.g. MSFT.csv) and
constructs a list of lines
"""
import os
from collections import defaultdict
import statistics

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
            day_year_statistics[year][weekday] = (mean_returns, std_dev, len(neg_returns), neg_mean, neg_std_dev, len(pos_returns), pos_mean, pos_std_dev)

    # Print the mean return and standard deviation for each day in each year
    for year, days_data in day_year_statistics.items():
        print(f"Stats for each day in {year}:")
        for weekday, stats in days_data.items():
            mean_return, std_dev, neg_returns_count, neg_mean, neg_std_dev, pos_returns_count, pos_mean, pos_std_dev = stats
            print(f"   {weekday}: Mean return: {mean_return}, Standard Deviation: {std_dev}, Negative Returns: {neg_returns_count},"
                   f" Negative Mean: {neg_mean}, Negative Standard Deviation: {neg_std_dev}, Positive Returns: {pos_returns_count},"
                    f" Positive Mean: {pos_mean}, Positive Standard Deviation: {pos_std_dev}")
    
except Exception as e:
    print(e)
    print('failed to read stock data for ticker: ', ticker)












