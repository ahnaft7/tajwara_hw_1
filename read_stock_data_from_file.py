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

except Exception as e:
    print(e)
    print('failed to read stock data for ticker: ', ticker)












