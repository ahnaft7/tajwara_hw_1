# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 14:37:29 2018

@author: epinsky
this scripts reads your ticker file (e.g. MSFT.csv) and
constructs a list of lines
"""
import os

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

    for row in lines[1:]:
        fields = row.split(',')
        year = fields[1]
        weekday = fields[4]
        if year == '2016':
            weekday = fields[4]
            return_value = float(fields[13])
            weekday_returns_2016[weekday].append(return_value)
        if year == '2017':
            weekday = fields[4]
            return_value = float(fields[13])
            weekday_returns_2017[weekday].append(return_value)
        if year == '2018':
            weekday = fields[4]
            return_value = float(fields[13])
            weekday_returns_2018[weekday].append(return_value)
        if year == '2019':
            weekday = fields[4]
            return_value = float(fields[13])
            weekday_returns_2019[weekday].append(return_value)
        if year == '2020':
            weekday = fields[4]
            return_value = float(fields[13])
            weekday_returns_2020[weekday].append(return_value)
    
    mean_returns_2016 = {}
    mean_returns_2017 = {}
    mean_returns_2018 = {}
    mean_returns_2019 = {}
    mean_returns_2020 = {}

    for weekday, returns in weekday_returns_2016.items():
        mean_returns_2016[weekday] = sum(returns) / len(returns)
    
    for weekday, returns in weekday_returns_2017.items():
        mean_returns_2017[weekday] = sum(returns) / len(returns)
    
    for weekday, returns in weekday_returns_2018.items():
        mean_returns_2018[weekday] = sum(returns) / len(returns)
    
    for weekday, returns in weekday_returns_2019.items():
        mean_returns_2019[weekday] = sum(returns) / len(returns)
    
    for weekday, returns in weekday_returns_2020.items():
        mean_returns_2020[weekday] = sum(returns) / len(returns)

    # Print the mean return for each weekday
    for weekday, mean_return in mean_returns_2016.items():
        print(f"Mean return for {weekday} in 2016: {mean_return}")
    
    for weekday, mean_return in mean_returns_2017.items():
        print(f"Mean return for {weekday} in 2017: {mean_return}")
    
    for weekday, mean_return in mean_returns_2018.items():
        print(f"Mean return for {weekday} in 2018: {mean_return}")
    
    for weekday, mean_return in mean_returns_2019.items():
        print(f"Mean return for {weekday} in 2019: {mean_return}")
    
    for weekday, mean_return in mean_returns_2020.items():
        print(f"Mean return for {weekday} in 2020: {mean_return}")

    
except Exception as e:
    print(e)
    print('failed to read stock data for ticker: ', ticker)












