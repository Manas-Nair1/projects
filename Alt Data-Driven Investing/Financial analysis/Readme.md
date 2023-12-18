# Analysis on financial reports
The scripts here either aquire and clean various financial reports such as 10-K's and 10-Q's

# company.idx
It is imperative that this is a relatively recent version as otherwise it may not have up to date information on the latest SEC filings

# usingEDGAR.py 
This script can be manipulated to gather various financial reports from the SEC archives

# SA on 10K
was initially written to work with 10-K's. Uses the FinBERT transformers model to conduct sentiment analysis on the text sentence by sentence. 

# Collaborators.py
This is for another project that builds a social network graph between all biotech companies on the nasdaq and uses the centrality score as a feature in a regression model. 
Looks through the filing from a given company(AbbVie inc currently) and finds any entities with which this company has collaboration agreements.
