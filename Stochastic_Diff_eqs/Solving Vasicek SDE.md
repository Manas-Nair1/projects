# Vasicek model
Here we will find a solution to the Vasicek differential equation, which is a type of Ornstein-Uhlenbeck process, and is mean reverting. The dynamics of R(t) are:  
![CodeCogsEqn(3)](https://github.com/Manas-Nair1/projects/assets/138029880/3c78aebb-56bf-4f0b-85e5-c3edff3c5a05)  
Lef f(t,R(t)) =
![CodeCogsEqn(4)](https://github.com/Manas-Nair1/projects/assets/138029880/de13bc3b-efe6-40ab-a22f-d376ee592a53)  
Applying Ito's Lemma and substituting dR(t), df is  
![CodeCogsEqn(5)](https://github.com/Manas-Nair1/projects/assets/138029880/6cb97e4e-4747-41cc-acce-0bfd24fd215d)  
Simplifying we get,  
![CodeCogsEqn](https://github.com/Manas-Nair1/projects/assets/138029880/9a8b8758-f010-4235-8fba-a2e734d1a9a5)  
![CodeCogsEqn(1)](https://github.com/Manas-Nair1/projects/assets/138029880/3d469a84-c8f3-44c9-8a7f-20d7964a73cc)  
We now substitute f, and integrate both sides from 0 to T,  
![CodeCogsEqn(2)](https://github.com/Manas-Nair1/projects/assets/138029880/acd3b2da-2f05-49cc-9849-0ff7867d8411)  
Evaluating the integrals, moving R(0) to the other side, and dividing out by e^{bT}, we get  
![CodeCogsEqn(3)](https://github.com/Manas-Nair1/projects/assets/138029880/2f275b56-fb63-48e2-bc9c-e6006c6dbab6)






