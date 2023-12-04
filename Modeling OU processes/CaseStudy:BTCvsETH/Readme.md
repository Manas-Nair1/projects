# Cointegration
As it is accepted that any single tradable asset follows GBM and is not mean-reverting, we will build a portfolio of 2 separate assets in a manner commonly refered to as a 'pairs trade.' The general idea is that the 2 assets should be chosen such that they are susceptible to similar market factors. Occasionally, their relative stock prices diverge due to certain events, but will revert to the long-term mean.

# Plot BTC:USDT vs ETH:USDT to look for a cointegration relationship
We will first look at BTC vs ETH over 2022-2023 to look for a cointegration relationship.
The scatterplot.png shows a linear relationship between the 2 assets. We will now apply OLS to find an optimal beta hedge ratio and test the residuals using the CADF test. The output is:
CADF:(-2.4309702743229167, 0.1331853612834536, 0, 364, {'1%': -3.4484434475193777, '5%': -2.869513170510808, '10%': -2.571017574266393}, 5287.853020691161).
This result suggests that there may not be a cointegrating relationship between these 2 assets over this time period. 

Lets now investigate the relationship over a longer period of time. 
Running the analysis over 1-1-2018 -> 10-1-2023 outputs:
CADF:(-2.755845582962943, 0.0648629501207425, 24, 1475, {'1%': -3.434791163965702, '5%': -2.8635014840083945, '10%': -2.5678142741740877}, 23667.734903608045)

# Trading strategy:
We will model the residuals as an Ornstein-Uhnlenbeck process as we expect the residuals to display mean reverting properties. Although the CADF test does not suggest a particularly strong cointegration relationship, as the p-value is > 0.05 and the CADF result is also > the 5% critical value, we will backtest a trading strategy that takes opposite positions in these 2 assets if their residuals diverge from the modelled mean.
