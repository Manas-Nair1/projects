# Select projects
#WIP : project is still under active development

Key projects included:
- (WIP)Value investing principles:
    * Applying principles of value investing to find good long term investments with high upside. 
- Trading engine: connects to exchanges and executes trades systematically
    * Use API calls to get data and place trades with varying parameters.
    * Query OHCLV data to be used in custom backtesting framework
- Statistical testing and time series analysis
    * Applying statistical testing to trades executed data as provided by kucoin exchange.
    * Using "pairs trading" to build a portfolio with stationary properties from assets that individually follow GBM
- Ornstein-Uhlenbeck process to model mean reverting stochastic processes
    * Modeling residuals between cointegrated pairs of assets as mean reverting and using continous and discritized versions of the OU process to model dynamics. 
- (WIP)Data driven investment thesis using mix of analysis algorithms on BioTech/Pharmaceutical stocks (Focuses on NLP)
    * Sentiment analysis using BERT models on News 
    * Analyzing 10-K's and 10-Q's
    * (From value investing) Using comps trading strategies comparing EV/EBITDA multiple to identify undervalued/overvalued companies. 
- Backtesting a systematic trading strategy to evaluate risk and efficacy
    * Using Backtrader library to setup data feeds, generate signals, and evaluate strategies.
    * Developing a custom backtesting framework to deal with limitations of open-source libraries. 

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
