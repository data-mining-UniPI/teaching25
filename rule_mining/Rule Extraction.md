---
type: presentation
marp: true
paginate: true
footer: ""
topic:
---

<!-- Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Inconsolata:wght@200..900&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Raleway:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Arvo:ital,wght@0,400;0,700;1,400;1,700&display=swap" rel="stylesheet">

<!-- Semantic UI -->
<script
        src="https://code.jquery.com/jquery-3.1.1.min.js"
        integrity="sha256-hVVnYaiADRTO2PzUGmuLJr8BLUSjGIZsDYGmIJLv2b8="
        crossorigin="anonymous"></script>
<script
    src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/libs/semanticui/semantic.min.js"></script>
<link
    rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/semantic-ui@2.5.0/dist/semantic.min.css">
<link
    rel="stylesheet"
    type="text/css"
    href="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/libs/semanticui/override.css">

<!-- Mermaid -->
<script
    src="https://cdn.jsdelivr.net/npm/mermaid@10.3.0/dist/mermaid.min.js"></script>
<link
    rel="stylesheet"
    type="text/css"
    href="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/libs/mermaid/mermaid.css">

<!-- Theme -->
<link
    rel="stylesheet"
    type="text/css"
    href="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/css/themes/base.css">
<link
    rel="stylesheet"
    type="text/css"
    href="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/css/themes/unipi.css">
<link
    rel="stylesheet"
    type="text/css"
    href="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/css/themes/colors.css">

<!-- Slide size -->
<!-- <link
    rel="stylesheet"
    type="text/css",
	href="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/css/scaling/px1280_720.css"> -->

<link
    rel="stylesheet"
    type="text/css"
	href="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/css/scaling/sizing.css">

<link
    rel="stylesheet"
    type="text/css",
	href="file:////home/davine/projects/marpee/css/scaling/px1128_752.css">


<!-- paginate: skip -->

# Rule lists

---

<!-- paginate: true -->

# Association rule mining

<div class="ui two column doubling stackable grid container bottom">
<div class="column">
<div class="ui segment base pros"> 

- Known computational cost
- Simple and flexible

</div>
</div>
<div class="column">
<div class="ui segment base cons"> 

- Local optimization
- No priority: we have rule *sets*

</div>
</div>
</div>


<!-- footer: "" -->

---

# Rule lists

A *rule list* is a sorted set of rules: starting from rule $1$, if rule $i$ does not support the given instance, move to rule $i + 1$.

```python
(1) if age in (23, 26) and priors in (2, 3) then recidivous
(2) if age in (18, 20) then recidivous
(3) if sex is male and age in (21, 22) then recidivous
(4) if priors > 3 then recidivous
(5) else not_recidivous
```


<div class="caption">

Example on a recidivism prediction: convicts are judged for early release.

</div>

<!-- footer: "" -->

---

# Rule lists

<div class="ui two column doubling stackable grid container bottom">
<div class="column">
<div class="ui segment base pros"> 

- Rule priority
- Global optimization
- Compact rules

</div>
</div>
<div class="column">
<div class="ui segment base cons"> 

- Most algorithms work on categorical (often binary) data

</div>
</div>
</div>

<!-- footer: "Scalable Bayesian Rule Lists, Yang et al.

Learning Certifiably Optimal Rule Lists, Angelino et al.
" -->

---

# Adjustments to Rule Lists

Support, confidence, and other measures still hold, but we need to reconsider support: in a rule list, **the first rule to support an instance is the one predicting**.

To adjust, we treat support as an indicator variable, evaluating to $1$ for the *first* rule of a given list to apply, and $0$ otherwise:

$$
supp_{A}(r, x) =
\begin{cases}
 1 & if \text{ } r \in A\text{ is the first rule to satisfy } x \\ \\
 0 & otherwise
\end{cases}
$$


<!-- footer: "" -->

---

# Adjustments to Rule Lists

```python
(1) if age in (23, 26) and priors in (2, 3) then recidivous
(2) if age in (18, 20) then recidivous
(3) if sex is male and age in (20, 22) then recidivous
(4) if priors > 3 then recidivous
(5) else not_recidivous
```
<div class="ui two column doubling stackable grid container bottom">
<div class="column w60">

| age | priors | sex | $r_1$ | $r_2$ | $r_3$ | $r_4$ | 
| --- | ------ | --- | ----- | ----- | ----- | ----- |
| 24  | 2      | m   |       |       |       |       |
| 20  | 1      | f   |       |       |       |       |
| 20  | 5      | m   |       |       |       |       |

</div>
<div class="column w40">

What is the value of the support indicator variable?

</div>
</div>


---

# Adjustments to Rule Lists

```python
(1) if age in (23, 26) and priors in (2, 3) then recidivous
(2) if age in (18, 20) then recidivous
(3) if sex is male and age in (20, 22) then recidivous
(4) if priors > 3 then recidivous
(5) else not_recidivous
```

| age | priors | sex | $r_1$ | $r_2$ | $r_3$ | $r_4$ |
| --- | ------ | --- | ----- | ----- | ----- | ----- |
| 24  | 2      | m   | `1`   | `0`   | `0`   | `0`   |
| 20  | 1      | f   | `0`   | `1`   | `0`   | `0`   |
| 20  | 5      | m   | `0`   | `1`   | `0`   | `0`   |

---

# CORELS: Certifiably Optimal Rule Lists

Try it online! *[https://corels.cs.ubc.ca/corels/](https://corels.cs.ubc.ca/corels/)*

<!-- footer: "Learning Certifiably Optimal Rule Lists, Angelino et al." -->

---

# Branch and bound algorithms

Family of optimization algorithms that defines a space of solutions to search, according to a given objective function. Exploring the whole space is unfeasible, hence branch and bound algorithms define:
- A **set of feasible solutions** to explore from a starting set: the *branches* of the solution tree to explore
- A **bound** for the objective: it allows to *prune* branches, thus reducing the search space


<!-- footer: "" -->

---

# Why B&B? The search tree of rules

<div class="ui two column doubling stackable grid container bottom">
<div class="column w35">

A search tree has an exponentially large number of states! For a tree of order $k$ and depth $d$, $\mathcal{O}(k^d)$ states!

</div>
<div class="column w65">
<img class="ui image centered big" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/corels1step.svg">
<div class="caption">

A branch and bound tree for rule lists, trimmed at depth $1$.

</div>
</div>
</div>


<!-- footer: "" -->

---

# Size of the rule space: full-length rule

For simplicity, assume $m$ features, each discretized in $k$ bins, and each feature can only appear in a rule once. A rule of (maximum) length $m$ can be constructed with a carthesian product of predicates from each of the $m$ $k$-large sets: we have $k^m$ combinations!

| age        | salary      | assets     |
| ---------- | ----------- | ---------- |
| `[0-18]`   | `[0, 0]`    | `[0, 0]`   |
| `[19, 21]` | `[1, 1000]` | `[1, 100]` |
| `...`      | `...`       | `...`      |

<!-- footer: "Note: we are \"only\" considering the premises: the class of the rule would add another multiplicative factor! " -->

---

# Size of the rule space: all rules

Considering shorter rules, the same applies. We consider $m - i$ sets (features) sampled from $m$ sets, for $\binom{m}{m - i}$ combinations, and $k^{m - i}$ values: a search space of $\mathcal{O}(\binom{m}{m - i} k^{m-1})$ size! Summing up over all lengths, we have 
$$
\sum_{i = 1}^{m - 1}\binom{m}{m - i} k^{m - i} + k^m
$$
possible rules. Note: to construct the space of rule lists, we have to consider all possible permutations of such rules!


<!-- footer: "Note: we are \"only\" considering the premises: the class of the rule would add another multiplicative factor! " -->

---

# Branch and bound algorithms

<div class="ui two column doubling stackable grid container bottom">
<div class="column w35">

Exploration populates a queue of states to consider: the larger the queue, the larger the computational cost. A search algorithm simply

- Inserts states in the queue
- Pops states from the queue


</div>
<div class="column w65">
<img class="ui image centered big" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/search_tree.svg">
<div class="caption">

A branch and bound tree, a set of states to explore (in grey). The associated queue includes states $3, 4, 5,$ and $6$. Insertition order in the queue depends on the search strategy.

</div>
</div>
</div>

<!-- footer: "" -->

---

# Modeling: rules

First we model the rule list as a tuple $R: (P_{R}, Y_{R}, y_R^{0})$ of

- $P_R: (p^1, \dots, p^{k^R})$ premises of the rules, i.e., their body or antecedents
- $Y_R: (y_R^1, \dots, y_R^{k^R})$ labels associated to each rule
- $y_R^0$ default label: applied when no rule is satisfied

<!-- footer: "Learning Certifiably Optimal Rule Lists, Angelino et al." -->

---

# Example
```python
(1) if age in (23, 26) and priors in (2, 3) then recidivous
(2) if age in (18, 20) then recidivous
(3) else not_recidivous
```

- $k^R$ is `2`
- $P_R: (p^1, \dots, p^{k^R})$ is `(age in (23, 26) and priors in (2, 3), age in (18, 20))`
- $Y_R: (y_R^1, \dots, y_R^{k^R})$ is `(recidivous, not_recidivous)`
- $y_R^0$ is `not_recidivous`  


<!-- footer: "Note: $k^R$ only counts non-default rules." -->

---

# Modeling: tree

<div class="ui two column doubling stackable grid container bottom">
<div class="column w35">

An ordering is defined among rules: if a rule list $R$ is a prefix of a rule $R^+$, then $R \preceq R^+$. That is, nodes in the search tree extend their parents by adding a rule to their lists.


</div>
<div class="column w60">
<img class="ui image centered large" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/corelsplus1step_single_loss.svg">
<div class="caption">

A parent and child node in the tree.

</div>
</div>
</div>

<!-- footer: "" -->

---

# CORELS: objective

In a rule list, the empirical error of the model on a labelled dataset  $(X, Y)$ is given by

$$
l(R, X, Y) = \underbrace{l_{R}(R, X, Y)}_{supported} + \underbrace{l_{0}(R, X, Y)}_{not \text{ }supported},
$$
where:
- $l_{R}(R, X, Y) = \dfrac{1}{n} \sum\limits_{x, y \in X \times Y} \sum_{j = 1}^{k^R} supp_{P_{R}}(p_{R}^j, x) \mathbb{1}[y \neq y_{R}^{j}]$
- $l_{0}(R, X, Y) = \dfrac{1}{n} \sum\limits_{x, y \in X \times Y} \underbrace{ (1 - supp(P_R, x)) }_{\text {not supported by any rule}}\mathbb{1}[y  \neq y^{0}_{R}]$

<!-- footer: "" -->

---

# CORELS: loss and lower bound

We regularize complexity of the model by weighing in its size, to define the loss $L$ of the model:

$$
L(R, X, Y) = \underbrace{l(R, X, Y)}_{error} + \underbrace{\lambda k^R}_{regularization}
$$
We can now define lower bound $b(\cdot, \cdot, \cdot)$ of the loss, which only considers instances which are supported by non-default rules:

$$
b(R, X, Y) = l_{R}(R, X, Y) + \lambda k^R \leq L(R, X, Y).
$$

<!-- footer: "" -->

---

# Trimming the space

Trimming the search tree considers up to three components:
- The current best model $R^C$, and its loss $L^C$
- An optimal list $R^*$, and its loss $L^*$
- The bounds associated to both

---
# CORELS: bound on loss

<div class="ui two column doubling stackable grid container bottom">
<div class="column w35">

For two rule lists $R, R^+$ s.t. $R \preceq R^+$

$$
b(R, X, Y) \leq L(R^+, X, Y).
$$

By definition of $l_R$, adding rules to the list can only grow $l_R$. Inductively, for **any prefix with a bound higher than desired we can trim all of its suffixes**!

</div>
<div class="column w65">
<img class="ui image centered large" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/corelsplus1step_single_loss.svg">
<div class="caption">

Rule lists, their prefix relationship, and the relationship with the loss and bound.

</div>
</div>
</div>

<!-- footer: "" -->

---

# CORELS: bound on loss


$$
\begin{align}
l_{R}(R^+, X, Y) &= \dfrac{1}{n} \sum\limits_{x, y \in X \times Y} \sum_{j = 1}^{k^{R^+}} supp_{P_{R}}(p^j, x) \mathbb{1}[y \neq y_{R}^{j}] \\ \\

&= \dfrac{1}{n} \sum\limits_{x, y \in X \times Y} ( \sum_{j = 1}^{k^{R}} supp_{P_{R}}(p^j, x) \mathbb{1}[y \neq y_{R}^{j}] +  \sum_{j = k^R}^{k^{R^+}} supp_{P_{R}}(p^j, x) \mathbb{1}[y \neq y_{R}^{j}] )\\ \\

&= \underbrace{ \dfrac{1}{n} \sum\limits_{x, y \in X \times Y} ( \sum_{j = 1}^{k^{R}} supp_{P_{R}}(p^j, x) \mathbb{1}[y \neq y_{R}^{j}])}_{l_{R}} + \underbrace{ \dfrac{1}{n} \sum\limits_{x, y \in X \times Y} \sum_{j = k^R}^{k^{R^+}} supp_{P_{R}}(p^j, x) \mathbb{1}[y \neq y_{R}^{j}] )}_{\geq 0}
\end{align}
$$

<!-- footer: "" -->

---

# CORELS: bound on loss

<div class="ui two column doubling stackable grid container bottom">
<div class="column w35">

Given a current best bound $b^C$, I can trim all states in the queue with bound $> b^C$.

</div>
<div class="column w65">
<img class="ui image centered big" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/search_tree.svg">
<div class="caption">

A branch and bound tree. States to explore highlighted in grey.

</div>
</div>
</div>

---
# CORELS: bound on length

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

For a maximum of $\bar{r}$ antecedents, the lengths $k^{R^*}, k^{R^c}$ of the optimal ($R^*$) and current ($R^c$) best rule list are related by

$$
k^{R^*} \leq \min( \dfrac{L^c}{\lambda}, \bar{r}).
$$



</div>
<div class="column">
<img class="ui image centered large" src="">

Why?
- $k^{R^*} \leq \bar{r}$ is trivial (at most $\bar{r}$ rules available)
- For $\dfrac{L^c}{\lambda}$
$$
\begin{align}
  k^{R^*}  & \leq & \dfrac{L^c} \lambda \\
  \underbrace{ \lambda k^{R^*} }_{\leq L^*}  & \leq & \underbrace{ L^c }_{ \geq L^* }
\end{align}
$$

</div>
</div>

<!-- footer: "" -->

---

# CORELS: bound on length

<div class="ui two column doubling stackable grid container bottom">
<div class="column w35">

Given a current best loss $b^C$, I can trim all states at depth $> \max(\dfrac{L^c}{\lambda}, \bar{r})$.

</div>
<div class="column w65">
<img class="ui image centered big" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/search_tree.svg">
<div class="caption">

A branch and bound tree. States to explore highlighted in grey.

</div>
</div>
</div>

---

# CORELS: bounds on rule accuracy

We can further trim the branched states by bounding the number of correctly classified instances by any rule. In other words, for an optimal rule list, what is the minimum accuracy $\alpha^p$ a new rule $p$ should have to be added?

We define $\alpha^p$ and the related loss $l^p$ as 

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

$$
\alpha^p \equiv \dfrac{1}{n} \sum_{i = 1}^n supp(p, x^i) \mathbb{1}[y_{i} = y^p],
$$

</div>
<div class="column">

$$
l^p \equiv \dfrac{1}{n} \sum_{i = 1}^n supp(p, x^i) \mathbb{1}[y^{i} \neq y^{p}].
$$


</div>
</div>


<!-- footer: "" -->

---

# CORELS: bounds on rule accuracy

In the worst-case scenario, all instances covered by $p$ are instead covered by other rules and misclassified, thus the difference is bounded by $p$'s accuracy
$$
l(R, X, Y) - l(R + [p], X, Y) \leq \alpha^p.
$$

We can directly relate this to the regularization hyperparameter $\lambda$!

---

# CORELS: bounds on rule accuracy

$$
\begin{align}
l(R, X, Y) - l(R + [p], X, Y) &\leq \alpha^i & \\
l(R, X, Y) &\leq \alpha^i + l(R + [p], X, Y) & \text{ move to RHS }\\
l(R, X, Y) + \lambda k^R  &\leq \alpha^i + l(R + [p], X, Y) + \lambda k^R & \text{ add  } \lambda k^R \text{ to both sides } \\
L(R, X, Y) & \leq \alpha^i + L(R + [p], X, Y) - \lambda & \text{ by definition of }  L \text{, and } k^{R + [p]} = k^R - 1\\
- \alpha_i + L(R, X, Y) & \leq L(R + [p], X, Y) - \lambda & \text{ move to LHS }\\
\alpha_i -  L(R, X, Y) & \geq - L(R + [p], X, Y) + \lambda & \text{ sign flip }\\
\end{align}
$$

Note that $L(R, X, Y) \leq L(R + [p], X, Y)$, thus it must be  $\alpha_i \geq \lambda$: **any rule added to the list must have accuracy higher than** $\lambda$**!**

<!-- footer: "" -->

---

# CORELS: three bounds

<div class="ui three column doubling stackable grid container bottom">
<div class="column">

**Loss increase**

More rules, higher loss.

$$
b(R, X, Y) \leq L(R^+, X, Y)
$$

</div>
<div class="column">

**List length**

Lists longer than

$$
\min( \dfrac{R^c}{\lambda}, \bar{r})
$$

can be ignored.

</div>
<div class="column">

**Rule accuracy**

A rule $p$ should be added if and only if it has accuracy $\alpha^p \geq \lambda$.

</div>
</div>

---

**Algorithm**

```python
queue = [()]
current_best, current_best_state = +inf, None
while len(queue) > 0:
	state = queue.pop()  # get state
	if bound(state, data, labels) < current_best:
		state_loss = L(state, data, labels)
		# update if new best is found
		if state_loss < current_best:
			current_best = state_loss
			current_best_state = state

		# branch: trim() uses the bounds to trim suboptimal states
		new_states = state.children() 
		queue.push_all([s for s in new_states
                        if not trim(s, data, labels, state)])
	

return current
```

---

# References

- *Learning Certifiably Optimal Rule Lists for Categorical Data*, Elaine A., Larus-Stone N., Alabi D., Seltzer M, Rudin C. *Journal of Machine Learning Research* (Journal version)
- *Learning Certifiably Optimal Rule Lists for Categorical Data*, Elaine A., Larus-Stone N., Alabi D., Seltzer M, Rudin C. *SIGKDD 2017* (Conference version)

Note: only the bounds in the slides are part of the program.