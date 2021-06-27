import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ohlc_data = pd.read_csv('nifty-50\SBIN.csv', index_col=0, parse_dates=True)

daily = np.array(ohlc_data)

money = int(input('Enter amount you want to invest : '))
risk = int(input('Enter no of shares you want to buy/sell in each transaction : '))

def doji_detection(data, cash, risk):
    initial_amount = cash
    transactions = 0
    stocks = 0
    for i in range(len(data)):

        invest = stocks * data[i, 3]

        # Bullish Doji
        if abs(data[i, 3] - data[i, 0]) < 5 and data[i, 3] < data[i - 1, 3] and cash >= 5 * data[i, 3] and risk * data[i, 3] < cash:
            # Buying shares at close
            cash -= risk * data[i, 3]
            invest += risk * data[i, 3]
            stocks += risk
            print('\n', i, ') BULL: Bought ', risk, ' at ', data[i, 3], '|| Cash Left = ', cash, '|| Invested = ', invest)
            transactions += 1

        # Bearish Doji
        if abs(data[i, 3] - data[i, 0]) < 5 and data[i, 3] > data[i - 1, 3] and transactions > 0 and stocks > 0:
            # Selling shares at closing
            cash += risk * data[i, 3]
            invest -= risk * data[i, 3]
            stocks -= risk
            print('\n', i, ') BEAR: Sold ', risk, ' at ', data[i, 3], '|| Cash Left = ', cash, '|| Invested = ', invest)
            transactions += 1
        if i == 79:
            gross = data[i, 3] * stocks + cash
            print("\n\n\n\tTotal Amount   : Rs. ", gross)
            print("\tInitial Amount : Rs. ", initial_amount)
            print("\tProfit / Loss  : Rs. ", gross - initial_amount)
    print('\n\tThanks for using Trading Bot !!!')



"""
def ohlc_plot(data, window, name):
    Chosen = data[-window:, ]

    for i in range(len(Chosen)):

        plt.vlines(x=i, ymin=Chosen[i, 2], ymax=Chosen[i, 1], color='black', linewidth=1)

        if Chosen[i, 3] > Chosen[i, 0]:
            color_chosen = 'green'
            plt.vlines(x=i, ymin=Chosen[i, 0], ymax=Chosen[i, 3], color=color_chosen, linewidth=4)
        if Chosen[i, 3] < Chosen[i, 0]:
            color_chosen = 'red'
            plt.vlines(x=i, ymin=Chosen[i, 3], ymax=Chosen[i, 0], color=color_chosen, linewidth=4)

        if Chosen[i, 3] == Chosen[i, 0]:
            color_chosen = 'black'
            plt.vlines(x=i, ymin=Chosen[i, 3], ymax=Chosen[i, 0], color=color_chosen, linewidth=4)

    plt.grid()
    plt.title('SBIN (2000-21)')
    plt.show()
"""

# Using the function
list = doji_detection(daily, money, risk)
# print(list)
# ohlc_plot(daily, 40, '')
