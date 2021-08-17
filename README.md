# markov_decision
Provide a chain environment, formulate a simple MDP for and find an optimal deterministic policy for this environment using value iteration.

<img width="444" alt="Screen Shot 2021-08-17 at 11 13 17 AM" src="https://user-images.githubusercontent.com/71328646/129658509-764a1f60-d22c-46e0-8434-53ba4c258b97.png">

In this environment, there are 5 states arranged in a chain, and 2 possible actions available to the agent in each state: f (“forward”) and b (“backward”).

Each action in a state is depicted by a small black circle; the arrows from actions to states depict possible transitions, labeled by the probability with which that transition occurs given the action and previous state, and the associated reward.

Assume a discount factor of 0.9.

# Value Iteration Algorithm
There are a total of 5 states (1-5). 
Used the value iteration algorithm to find the optimal value function V^* for each state s.
V* for 1: 23.31322723 
V* for 2: 24.17311629 
V* for 3: 26.95141629 
V* for 4: 31.36141629 
V* for 5: 38.36141629

And find the optimal value function for each state-action pair:
Q*(1, f): 22.42363462 Q*(1, b): 23.31407456

Q*(2, f): 24.17396362 Q*(2, b): 24.06421556
Q*(3, f): 26.95226362 Q*(3, b): 25.25491556
Q*(4, f): 31.36226362 Q*(4, b): 27.14491556
Q*(5, f): 38.36226362 Q*(5, b): 30.14491556

Find the optimal deterministic policy π:
The optimal policy is b, f, f, f, f.
