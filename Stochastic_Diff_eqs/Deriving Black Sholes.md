# Assumptions and general method
We are trying to model V(t,s) - which is the value of a contingent claim as a funciton of time(deterministic Process) and a underlying stock price(stochastic process). We will use no-arbitrage pricing, which states that if two "strategies" have the same payout, they must have the same price/risk associated as otherwise arbitrage opportunities would exist in the market. 
# Construction of the portfolio
We first construct a portfolio which buys some contingent claim worth V(t,s) and sells some shares against it. The amount of shares is the value denoted by delta and S represents the stock price.   
![Eqn](https://github.com/Manas-Nair1/projects/assets/138029880/b5fe9ef9-5dc1-4a88-b6f3-ca8f80d674d0)  
As we are interested in the dynamics, we take the differentials of both sides. Note, delta is some unknown constant  
![Eqn](https://github.com/Manas-Nair1/projects/assets/138029880/af48d53e-9548-4203-81d0-d85e2d71630b)  
We now have a equation in terms of dV and dS. We will now apply Ito Calculus to simplify dV. Note dS is given as the following differential, and dW is a change in the weiner process  
![Eqn](https://github.com/Manas-Nair1/projects/assets/138029880/c73f60c7-0555-4008-8429-88d1ce894b5d)  
Applying Ito's Lemma we knok  
![Eqn](https://github.com/Manas-Nair1/projects/assets/138029880/d11a8868-d2da-4d97-aa61-b35b3bdd0401)  
Substitute dS as the known differential  
![Eqn](https://github.com/Manas-Nair1/projects/assets/138029880/909a4692-f88d-4cbb-91a7-9d97d24b69c5)  
We now take this equation for dV and substitute into the original formula for dP, and group the respective dt and ds terms  
![Eqn](https://github.com/Manas-Nair1/projects/assets/138029880/3d64d8f7-2198-46f1-9bef-420afec99ec7)
Here we get the delta value for the hedge, which is a change in Value per unit change in the underlying  
![Eqn](https://github.com/Manas-Nair1/projects/assets/138029880/1d98f3c8-342b-4cb3-b854-f696c40cf9ae)  
Setting delta equal to this makes the ds term = 0, and we get the dynamics that are entirely deterministic and thus risk free. We know that this must mean there is some risk free rate r for which the dynamics of the portfolio are  
![Eqn](https://github.com/Manas-Nair1/projects/assets/138029880/8f1ea0a4-752d-431c-8d84-974732215e42)  
We substitute the known formula for P  
![Eqn](https://github.com/Manas-Nair1/projects/assets/138029880/f59b25d2-b1cc-441e-9f95-ac3a5aa0a70f)  
We set these dynamics equal to the dynamics formulated earlier and setting the equation equal to 0, we get:  
![Eqn](https://github.com/Manas-Nair1/projects/assets/138029880/0f47fb8f-bc6a-4fb2-bd12-d0473353ed84)  
This is the common form of the Black-Sholes PDE. 











