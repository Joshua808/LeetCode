# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 19:45:02 2021
Library of functions to convert between the american odds, fractional odds, decimal odds

TODO:
    ADD PROBABILITY CONVERSIONS
"""


def american_to_decimal_odds_conversion(american_odds):
    
    if american_odds < 0:
        decimal_odds = -(100/american_odds) + 1
    else:
        decimal_odds = (american_odds/100) + 1
    
    return decimal_odds
    
def american_to_fractional_odds_conversion(american_odds):
    
    if american_odds < 0:
        fractional_odds = -100/american_odds
    else:
        fractional_odds = american_odds/100
    
    return fractional_odds 

def fractional_to_decimal_odds_conversion(fractional_odds):
    S
    decimal_odds = fractional_odds + 1
    
    return decimal_odds 

def fractional_to_american_odds_conversion(fractional_odds):
    
    if fractional_odds < 0:
       american_odds = -100 / fractional_odds    
    else:
        american_odds = fractional_odds *100
    
    return american_odds 
    
def decimal_to_fractional_odds_conversion(decimal_odds):
    
    fractional_odds = decimal_odds - 1
    
    return fractional_odds

def decimal_to_american_odds_conversion(decimal_odds):
    
    if decimal_odds < 2:
       american_odds = -100 / (decimal_odds -1)     
    else:
        american_odds = (decimal_odds - 1) * 100
    
    return american_odds

