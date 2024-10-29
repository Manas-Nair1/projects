**work in progress** (currently contains a lot of napkin math) 

- project investigating effects of momentum in directional movements in price of highly volatile assets.    
- inspired by https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4322637   
- assmumptions: discretize the GBM for the ease of obtaining data such as volume of assets traded. I also assume volatility and volume of assets traded correlate. This assumption may not hold in all market conditions as the presence of a large ATM buy order could discredit the effects of a large ATM sell order as it would cause no effect on volatility. 
- trading thesis: price can be modeled using a random walk. The random walk rules govern that at each timestep, Prob(Price(x+1)>Price(x)) = Prob(Price(x+1)< Price(x)). This symmetery may not be reflected in highly volatile crypto markets, as the paper suggests. **My strategy models price as a random walk with a directional bias dependent on volume. this directional bias represents momentum and should decay over time**  
 We could model the continous case using the general form of an SDE: change in price is given by a step in the random walk scaled by volume + Momentum (dependent on volume) * - dM/dt

- dP = V \cdot \Delta W + \text{Momentum} \cdot \left( - \frac{dM}{dt} \right)
- P is price, V is volume, dW represents a step in weiner process, M is a momentum value depending on volume(is multiplied by its negative derivative to imply that momentum decays)

- Currently working on estimating params for Momentum and rate of momentum Decay given volume of assets traded. 