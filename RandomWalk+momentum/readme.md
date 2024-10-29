**work in progress** (currently contains a lot of napkin math) 

- project investigating effects of momentum in directional movements in price of highly volatile assets.    
- inspired by https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4322637   
- We will discretize the GBM for the ease of obtaining data such as volume of assets traded. I also assume volatility and volume of assets traded correlate. This assumption may not hold in all market conditions as the presence of a large ATM buy order could discredit the effects of a large ATM sell order as it would cause no effect on volatility. 
- trading thesis: price can be modeled using a discretized random walk. We could model the continous case using the general form of an SDE: change in price is given by a step in the random walk scaled by volume + Momentum (dependent on volume) * - dM/dt

- dP = V \cdot \Delta W + \text{Momentum} \cdot \left( - \frac{dM}{dt} \right)
- P is price, V is volume, dW represents a step in weiner process, M is a momentum value depending on volume(is multiplied by its negative derivative to imply that momentum decays)
