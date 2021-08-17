# markov_decision
Provide a chain environment, formulate a simple MDP for and find an optimal deterministic policy for this environment using value iteration.

<img width="444" alt="Screen Shot 2021-08-17 at 11 13 17 AM" src="https://user-images.githubusercontent.com/71328646/129658509-764a1f60-d22c-46e0-8434-53ba4c258b97.png">

In this environment, there are 5 states arranged in a chain, and 2 possible actions available to the agent in each state: f (“forward”) and b (“backward”).

Each action in a state is depicted by a small black circle; the arrows from actions to states depict possible transitions, labeled by the probability with which that transition occurs given the action and previous state, and the associated reward.

Assume a discount factor of 0.9.

# Value Iteration Algorithm
There are a total of 5 states (1-5). 
Used the value iteration algorithm to find the optimal value function V^* for each state s.
<img width="410" alt="Screen Shot 2021-08-17 at 3 19 17 PM" src="https://user-images.githubusercontent.com/71328646/129681399-5eed6abf-cf46-4eb6-881c-12dd9d9c2f4b.png">


And find the optimal value function for each state-action pair:
<img width="410" alt="Screen Shot 2021-08-17 at 3 19 37 PM" src="https://user-images.githubusercontent.com/71328646/129681458-33a7bc71-a718-41e0-a2f7-a8091579576e.png">


Find the optimal deterministic policy π:
The optimal policy is b, f, f, f, f.
