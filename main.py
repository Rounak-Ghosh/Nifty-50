import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ohlc_data = pd.read_csv('nifty-50\SBIN.csv',index_col=0 , parse_dates=True)

daily = np.array(ohlc_data)

money = 10000
bull = 0
bear = 0

def ohlc_plot(Data, window, name):
    Chosen = Data[-window:, ]

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


def signal(Data):

    for i in range(len(Data)):

        # Bullish Doji
        if abs(Data[i, 3] - Data[i, 0])<5 and Data[i, 3] < Data[i - 1, 3] and Data[i, 3] < Data[i - 2, 3]:
            #Data[i, 6] = 1
            print('Bullish Doji at ', i)

            # Bearish Doji
        if abs(Data[i, 3] - Data[i, 0])<5 and Data[i, 3] > Data[i - 1, 3] and Data[i, 3] > Data[i - 2, 3]:
            #Data[i, 7] = -1
            print('Bearish Doji at ', i)


# Using the function
signal(daily)
ohlc_plot(daily, 50, '')
