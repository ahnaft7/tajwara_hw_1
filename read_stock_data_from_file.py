# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 14:37:29 2018

@author: epinsky
this scripts reads your ticker file (e.g. MSFT.csv) and
constructs a list of lines
"""
import os
from collections import defaultdict

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

    weekday_returns_2016 = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}
    weekday_returns_2017 = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}
    weekday_returns_2018 = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}
    weekday_returns_2019 = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}
    weekday_returns_2020 = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}
    day_year_returns = defaultdict(lambda: defaultdict(list))

    for row in lines[1:]:
        fields = row.split(',')
        year = int(fields[1])
        # weekday = fields[4]
        # if year == '2016':
        #     weekday = fields[4]
        #     return_value = float(fields[13])
        #     weekday_returns_2016[weekday].append(return_value)
        # if year == '2017':
        #     weekday = fields[4]
        #     return_value = float(fields[13])
        #     weekday_returns_2017[weekday].append(return_value)
        # if year == '2018':
        #     weekday = fields[4]
        #     return_value = float(fields[13])
        #     weekday_returns_2018[weekday].append(return_value)
        # if year == '2019':
        #     weekday = fields[4]
        #     return_value = float(fields[13])
        #     weekday_returns_2019[weekday].append(return_value)
        # if year == '2020':
        #     weekday = fields[4]
        #     return_value = float(fields[13])
        #     weekday_returns_2020[weekday].append(return_value)
        if 2016 <= year <= 2020:  # Filter for years 2016-2020
            weekday = fields[4]
            return_value = float(fields[13])  # Assuming Return is the 14th field
            day_year_returns[year][weekday].append(return_value)
        
    # Calculate the mean return for each day in each year
    mean_returns = {}
    for year, days_data in day_year_returns.items():
        mean_returns[year] = {}
        for weekday, returns in days_data.items():
            mean_returns[year][weekday] = sum(returns) / len(returns)

    # Print the mean return for each day in each year
    for year, days_data in mean_returns.items():
        print(f"Mean return for each day in {year}:")
        for weekday, mean_return in days_data.items():
            print(f"   {weekday}: {mean_return}")
    
    # mean_returns_2016 = {}
    # mean_returns_2017 = {}
    # mean_returns_2018 = {}
    # mean_returns_2019 = {}
    # mean_returns_2020 = {}

    # for weekday, returns in weekday_returns_2016.items():
    #     mean_returns_2016[weekday] = sum(returns) / len(returns)

    
    # for weekday, returns in weekday_returns_2017.items():
    #     mean_returns_2017[weekday] = sum(returns) / len(returns)
    
    # for weekday, returns in weekday_returns_2018.items():
    #     mean_returns_2018[weekday] = sum(returns) / len(returns)
    
    # for weekday, returns in weekday_returns_2019.items():
    #     mean_returns_2019[weekday] = sum(returns) / len(returns)
    
    # for weekday, returns in weekday_returns_2020.items():
    #     mean_returns_2020[weekday] = sum(returns) / len(returns)

    # # Print the mean return for each weekday
    # for weekday, mean_return in mean_returns_2016.items():
    #     print(f"Mean return for {weekday} in 2016: {mean_return}")
    
    # for weekday, mean_return in mean_returns_2017.items():
    #     print(f"Mean return for {weekday} in 2017: {mean_return}")
    
    # for weekday, mean_return in mean_returns_2018.items():
    #     print(f"Mean return for {weekday} in 2018: {mean_return}")
    
    # for weekday, mean_return in mean_returns_2019.items():
    #     print(f"Mean return for {weekday} in 2019: {mean_return}")
    
    # for weekday, mean_return in mean_returns_2020.items():
    #     print(f"Mean return for {weekday} in 2020: {mean_return}")

    
except Exception as e:
    print(e)
    print('failed to read stock data for ticker: ', ticker)












