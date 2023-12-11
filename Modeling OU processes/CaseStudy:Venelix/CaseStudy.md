## Cointegration relationship between AbbVie and Genentech between 2016 and 2021
# Background
- AbbVie and Genentech Announce Collaboration to Develop and Commercialize Venelex for Alzheimer's Disease (press release), AbbVie, June 14, 2016.
- AbbVie and Genentech Expand Collaboration on Venelex for Alzheimer's Disease (press release), AbbVie, October 24, 2017.
- AbbVie and Genentech Discontinue Phase 3 Clinical Trial for Venelex in Alzheimer's Disease (press release), AbbVie, July 6, 2021.
# Hypothesis

As both companies had stake in the clinical trial, their stock prices may display a cointegration relationship due to both of their stock prices being driven by atleast one common factor, in addition to other common market factors affecting the pharmaceutical industry.

# Cointegration testing: 
Goal is to construct a portfolio that displays stationary properties from assets whose stock price individually does not possess stationary properties. 
We will first look for visual confirmation regarding a linear relationship between the prices of the 2 assets, we will then apply regression to model the price of one asset as y = beta * x + epsilon. We apply OLS to find beta and then conduct the ADF test on the residuals to confirm that they are stationary. 

# Results
The scatter plot shows a linear relationship for about the first half of the data but diverges into 2 clusters. We should not apply a linear regression as we would be introducing look ahead bias when deciding where to truncate the data. 
The biotech industry may not be the best fit for this strategy as it's constituent stocks may be less correlated to the industry and better modeled using charecteristics of the company itself(such as financials, drug portfolio, and upcoming catalyst dates).