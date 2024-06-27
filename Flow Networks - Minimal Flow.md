# Flow Networks - Minimal Flow When Capacities Block The Flow

## Problem 

### Minimum Flow in a Network

Given a flow network $G = (V, E)$ with the following properties:

- A source $s$ and a sink $t$, where $s \neq t \in V$
- Positive edge capacities $c(e) > 0$ for all $e \in E$
- For any pair of vertices $u \neq v$, at most one of the edges $(u,v)$ or $(v,u)$ exists in $G$

Define a "legal flow" as a function $f : E \to \mathbb{R}$ satisfying:

1. Flow Conservation: For every vertex $v \neq s,t$:
   $$\sum_{(u,v)\in E} f(u,v) = \sum_{(v,w)\in E} f(v,w)$$

2. Minimum Flow Constraint: For every edge $e \in E$:
   $$f(e) \geq c(e)$$
   Note: Unlike standard flow problems, here the capacity $c(e)$ represents a lower bound on the flow.

### Task
Assuming you are given a legal flow $f$ that satisfies both conditions above, design an algorithm to find a legal flow of minimum value.

### Instructions
1. Describe your algorithm clearly and concisely.
2. Explain the key steps and reasoning behind your approach.

## Solution

### Algorithm for Minimum Legal Flow

**Step 1: Define a New Capacity Function**<br>
Define $c': E \to [0, \infty)$ as $c'(e) := f(e) - c(e)$ for each edge $e \in E$.
<br><br>
**Step 2: Apply Edmonds-Karp Algorithm**<br>
Use the Edmonds-Karp algorithm to find a maximum flow $g : E \to \mathbb{R}$ in $G$, using $c'$ as the capacity function.
<br><br>
**Step 3: Construct the Minimum Flow**<br>
Define a new flow function $h : E \to \mathbb{R}$ as $h(e) := f(e) - g(e)$ for each edge $e \in E$.
<br><br>

### Justification

#### Legality of $h$: <br>

  - Minimum flow constraint: <br> <br> $$h(e) = f(e) - g(e) \geq f(e) - c'(e) = f(e) - (f(e) - c(e)) = c(e)$$

  - Flow conservation:<br> <br> For any vertex $v \neq s,t$,
    $$\sum_{(u,v)\in E} h(u,v) = \sum_{(u,v)\in E} (f(u,v) - g(u,v)) = \left(\sum_{(u,v)\in E} f(u,v) - \sum_{(u,v)\in E} g(u,v)\right)$$
    $$\left(\sum_{(v,w)\in E} f(v,w) - \sum_{(v,w)\in E} g(v,w)\right) = \sum_{(v,w)\in E} h(v,w)$$

#### Minimality of $h$:
   Assume, for contradiction, that there exists a legal flow $t : E \to \mathbb{R}$ such that $C(t) < C(h)$.
   Define $\mu(e) := f(e) - t(e)$. Then:
   - $\mu$ is a legal flow in $G$ with respect to capacity $c'$
   - $C(\mu) = C(f - t) = C(f) - C(t) > C(f) - C(h) = C(f) - (C(f - g)) = C(g)$
   
   This contradicts the maximality of $g$. Therefore, $h$ must be minimal.

### Intuition
The algorithm essentially "subtracts" the maximum flow (with respect to the new capacity function) from the given legal flow. This process minimizes the flow while maintaining its legality.
