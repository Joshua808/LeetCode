# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 19:45:02 2021
Function to conver between the american, fractional, and decimal odds
@author: Joshua
"""


def american_to_decimal_odds_conversion(american_odds):
    
    if american_odds < 0:
        decimal_odds = -(100/american_odds) + 1
    else:
        decimal_odds = (american_odds/100) + 1
    
    return decimal_odds
 
    
# =============================================================================
#  takes american odds, percent edge, and total bankroll
# =============================================================================
    
def kelly_bet_size(odds, edge, bankroll):
    
# =============================================================================
#     Convert american odds to decimal for kelly bet sizing
# =============================================================================
    decimal = american_to_decimal_odds_conversion(odds)
    
# =============================================================================
#     find kelly betsize
# =============================================================================
    kelly_bet = round(bankroll * (edge / (decimal - 1)), 2)
    
    return kelly_bet