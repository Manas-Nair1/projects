# Select projects
#WIP : project is still under active development

Key projects included:

- Statistical testing and time series analysis
    * Applying statistical testing to trades executed data as provided by kucoin's crypto Futures exchange.
    * Using "pairs trading" to build a portfolio with stationary properties from assets that individually follow GBM
- Trading engine: connects to exchanges and executes trades systematically
    * Use API calls to get data and place trades with varying parameters.
    * Query OHCLV data to be used in custom backtesting framework
- Ornstein-Uhlenbeck process to model mean reverting stochastic processes
    * Modeling residuals between cointegrated pairs of assets as mean reverting and using continous and discritized versions of the OU process to model dynamics. 
- (WIP)Data driven investment thesis using mix of analysis algorithms on BioTech/Pharmaceutical stocks (Focuses on NLP)
    * Sentiment analysis using BERT models on News/ Announcements 
    * Analyzing 10-K's and 10-Q's
- Backtesting a systematic trading strategy to evaluate risk and efficacy
    * Using Backtrader library to setup data feeds, generate signals, and evaluate strategies.
    * Developing a custom backtesting framework to deal with limitations of open-source libraries. 
- Screener:
    * Applying principles of value investing to identify "undervalued" or "overvalued" companies. 
    * These list of companies should then be investigated to find out what causes them to trade above(or below) companies in the same sector. 

Key mathematical methods used:
- Solving Stochastic partial differential equations. 
    * Deriving Black-Sholes-Merton PDE using Ito Calc and applying no-arbitrage pricing
    * Solving the OU and Vasicek SDE model to model mean reverting processes
    * Finite difference method/ Monte-Carlo Simulations usage when analytical solutions are not possible
- Statistical testing 
    * Testing for Cointegration 
    * Using ADF and KPSS tests as well as Hurst exponents to identify appropriate methods of modeling
- Regression analysis
    * Using MLE to estimate parameters for the discretized OU processes
