---
type: presentation
marp: true
paginate: true
footer: ''
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
    type="text/css",
    href="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/libs/semanticui/override.css">

<!-- Mermaid -->
<script
    src="https://cdn.jsdelivr.net/npm/mermaid@10.3.0/dist/mermaid.min.js"></script>
<link
    rel="stylesheet"
    type="text/css",
    href="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/libs/mermaid/mermaid.css">

<!-- Theme -->
<link
    rel="stylesheet"
    type="text/css",
    href="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/css/themes/base.css">
<link
    rel="stylesheet"
    type="text/css",
    href="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/css/themes/unipi.css">
<link
    rel="stylesheet"
    type="text/css",
    href="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/css/themes/colors.css">

<!-- Slide size -->
<link
    rel="stylesheet"
    type="text/css",
	href="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/css/scaling/px1280_720.css">

<link
    rel="stylesheet"
    type="text/css",
	href="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/css/scaling/sizing.css">

<!-- paginate: skip -->

# Supervised tasks

---

<!-- paginate: true -->

# Three approaches to classification

By any means, not the only ones!

<div class="ui three column doubling stackable grid container bottom">
<div class="column">

**Trees**

Can I learn a space partition that separates the data according to its label?

</div>
<div class="column">

**Linear**

Can I predict the label through linear modeling?

</div>
<div class="column">

**Neural**

Can I predict through computational graphs?

</div>
</div>

<div class="ui three column doubling stackable grid container bottom">
<div class="column">
<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/papers/pivot_tree/4x/pivot_tree@4x.png">
</div>
<div class="column">
<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/computational_graph.svg">
</div>
<div class="column">
<img class="ui small centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/network.svg">
</div>
</div>

---

# Trees
*Yet again*

---

# Splitting trees

Inducing Decision Trees depends roughly on two factors:
- Split function $f_i$: how do I route instances in my subtrees?
- Split loss: how do I evaluate the quality of a split?

<!-- footer: "We are considering binary trees." -->

---

# Split function: Univariate

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

The de facto standard:
$$
f_i(x) \equiv x_i \leq \theta_i.
$$

<div class="ui segment base pros"> 

- Highly interpretable
- Easy to control complexity

</div>

<div class="ui segment base cons"> 

- Limited capacity

</div>

</div>
<div class="column">
<img class="ui image large centered" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/univariate_split.svg">
<div class="caption">

A univariate split: the split is orthogonal to the axes.

</div>
</div>
</div>


<!-- footer: "" -->

---

# Split function: Multivariate

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

A higher-capacity model, with a more expressive split function:
$$
f_i(x) \equiv x \theta + \theta^0
$$

Since they generate "oblique" (non axis-parallel) splitting hyperplanes, they are also called *oblique* trees.

<div class="ui segment base pros"> 

- Shallower tree
- Higher capacity

</div>

<div class="ui segment base cons"> 

- Dubious interpretabilty

</div>

</div>
<div class="column">
<img class="ui image large centered" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/multivariate_split.svg">
<div class="caption">

A multivariate split: the split is not orthogonal to the axes. Also called *oblique* split.

</div>
</div>
</div>

<!-- footer: "Decision Tree SVM: An extension of linear SVM for non-linear classification. Nie et al." -->

---

# Split function: Probabilistic

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

Probabilistic routing defined by a learned probability distribution $p_i$:

$$
f_i(x) \equiv p_i(x ; \theta_i).
$$

Instances are routed to all leaves in the tree, accumulating probability density at each node. The prediction can then be given by the leaf with higher probability mass, or average class probabilities across leaves.

</div>
<div class="column">
<img class="ui image large centered" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/soft_tree.svg">
<div class="caption">

A probabilistic tree: an instance is routed to each leaf, accumulating probability mass along the path.

</div>
</div>
</div>

<!-- footer: "Distilling a Neural Network Into a Soft Decision Tree, Frosst and Hinton." -->

---

# Split function: Probabilistic

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

Instances are routed to all leaves in the tree, accumulating probability density at each node. The prediction can then be given by the leaf with higher probability mass, or average class probabilities across leaves.

<div class="ui segment base pros"> 

- High flexibility
- Better on non-relational data, e.g., images

</div>

<div class="ui segment base cons"> 

- Lower interpretabilty

</div>
</div>
<div class="column">
<img class="ui image large centered" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/soft_tree.svg">
<div class="caption">

A probabilistic tree: an instance is routed to each leaf, accumulating probability mass along the path.

</div>
</div>
</div>

<!-- footer: "Distilling a Neural Network Into a Soft Decision Tree, Frosst and Hinton." -->

---

# Linear models
Or are they?

---

<!-- paginate: true -->

# Linear modeling

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

Linear models are simple, generally interpretable, family of models. Typically used for tasks on

- Representation, e.g., PCA, PLA: can I find an alternative, *linear* representation of my data?
- Classification, e.g., Linear regression: can I predict a variable as a *linear* model of my data?

</div>
<div class="column">

<img class="ui image large centered" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/linalg/SVG/planes.svg">
<div class="caption">

Dataset of two classes, and a linear model separating them.

</div>

</div>
</div>

<!-- footer: "" -->

---

# Linear models for classification


<div class="ui two column doubling stackable grid container bottom">
<div class="column">

A linear model parameterized by $\omega$ has form
$$
f \equiv \omega^T x,
$$
and can be leveraged for classification with a suitable activation function, e.g., $f(x) \equiv \sigma( \omega^T x )$. 


</div>
<div class="column">
<img class="ui image large centered" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/computational_graph.svg">
<div class="caption">

An architectural illustration of a linear model. Note: such models include a bias term, not included in the figure.

</div>
</div>
</div>

<!-- footer: "" -->

---

# Linear models for classification


<div class="ui two column doubling stackable grid container bottom">
<div class="column">
<img class="ui image large centered" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/computational_graph.svg">
<div class="caption">

An architectural illustration of a linear model. Note: such models include a bias term, not included in the figure.

</div>
</div>
<div class="column">

<div class="ui segment base pros"> 

- Interpretable, somewhat actionable
- Ease of optimization
- Strong baseline

</div>
<div class="ui segment base cons"> 

- Limited capacity

</div>
</div>
</div>

<!-- footer: "" -->

---

# From linear... to additive


<div class="ui two column doubling stackable grid container bottom">
<div class="column">

The interpretability of linear models comes from their *additive* nature: each component has a measurable and independent contribution $\omega_i x_i$.

Their limitation also comes from this, as there is no real learned representation of the data.


</div>
<div class="column">
<img class="ui image large centered" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/computational_graph.svg">
<div class="caption">

An architectural illustration of a linear model. Note: such models include a bias term, not included in the figure.

</div>
</div>
</div>

<!-- footer: "Note: *independency* in the model, not necesarilly in the data!" -->

---

# Generalized Additive Models


<div class="ui two column doubling stackable grid container bottom">
<div class="column">

Generalized Additive Models ($GAM$s) generalize linear models by introducing *per-feature* learned representations:

$$
f(x) \equiv \sum^m \omega_i f_i(x_i) + \omega_0.
$$

Each feature enjoys a *learned* representation given by a parametric *shape* function $f_i$ of arbitrary complexity.

</div>
<div class="column">
<img class="ui image large centered" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/GAM.svg">
<div class="caption">

An architectural illustration of a $GAM$. Each block $f_i$ indicates a differentiable shape function.

</div>
</div>
</div>

<!-- footer: "Generalized additive models, D. F. McCaffrey." -->

---

# Generalized $Additive$ Models


<div class="ui two column doubling stackable grid container bottom">
<div class="column">

$$
f(x) \equiv \sum^m \omega_i f_i(x_i) + \omega_0.
$$

Typical shape functions:
- identity (linear models)
- neural networks

<div class="caption">

An architectural illustration of a $GAM$.

</div>
</div>
<div class="column">
<img class="ui image large centered" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/GAM.svg">
</div>
</div>

<!-- footer: "" -->


---

# Ensemble methods
*Tackling variance, once more*

---
# Mitigating variance... or not

As highlighted by the bias-variance decomposition, learning algorithms can incur in a variance in terms of generalization. We have seen two strategies to mitigate this:
- Cross validation: reduce variance by increasing samples
- Regularization: reduce variance by reducing capacity

There exists a third way, somewhat related, approach: leverage variance.

---
# Bagging

Bagging leverages learning algorithms with **moderate-to-high variance**: rather than learn a single model $f_\theta$, it learns a set of models $f_1, \dots, f_T$, and combines them into one. A bagging model is of the form
$$
f_\theta(x) = \sum_{i = 1}^T\eta f_i(x), \hspace{2cm} \eta \in \mathbb{R}.
$$

Following the bias-variance, bagging algorithms aim to learn a model on separate samples of the original distribution. 

<div class="ui segment inverted highlight">
Assumption: models retain a low-enough bias to be accurate on their respective bags.
</div>


---

# Bagging

<div class="img_row centered">
<img class="ui image large centered" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/probabilities/SVG/data.svg">
<img class="ui image large centered" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/probabilities/SVG/bagging.svg">
</div>

<div class="caption">

On the left, data, sampled from the data distribution. On the right, a visualization of bagging: samples are split in several bags (here, color-coded). Each bag is used to learn a different model, which will then be part of an ensemble.

</div>

---

# Bagging: computational complexity

Given by the computational complexity of each model. For a uniform learning time of $\mathcal{O}(c)$ of $k$ bags, the cost is simply $\mathcal{O}(kc)$, hence $\mathcal{O(c)}$.

For non-uniform costs, the computational complexity is upper-bounded by $\max_{c \in C} \mathcal{O(c)}$, hence it is again $\max_{c \in C} \mathcal{O(c)}$.

<!-- footer: "Remember: in asymptotical terms, constants are not considered." -->

---
# Random Forests

Decision Trees show a moderate variance, and thus are a perfect candidate. Random Forests sample a set of *bags* by sampling:

- Random instances, through stratification
- Random features within the bag

Thus creating learning sets heterogeneous in both instances and features. Bags are sampled with replacement!

<!-- footer: "" -->

---

# Bagging

<div class="img_row centered">
<img class="ui image huge centered" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/probabilities/SVG/randomforest_nolines.svg">
</div>

<div class="caption">

On the bottom, the bagged data, each bag indicated by a different color. On top, a set of learned trees, color-coded as the bag they have been learned from: the red tree has been learned on the red bag, and so forth. Note: Random Forest samples bags with replacement: an instance may be part of $0$ up to $K$ bags.

</div>

---

# Random forests: computational complexity

As a bagging model, the computational complexity is given by the complexity of the single tree. 

<!-- footer: "Remember: in asymptotical terms, constants are not considered." -->

---

# Random Forests

<div class="ui segment base pros"> 

- Simple definition with high variance models
- Interpretable-ish results
- Fast learning

</div>
<div class="ui segment base cons"> 

- Weak to high degrees of covariance
- Sampling *with replacement*: risk of high correlation
- Random bagging

</div>

<!-- footer: "" -->

---
# Bagging... what?

How would *you* bag?

<div class="img_row centered">
<img class="ui image large centered" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/probabilities/SVG/data.svg">
<img class="ui image medium centered" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/overfit.svg">
</div>

---
# From bagging... to Boosting

With bagging models, we assume locality in the data distribution, and thus learn different models on different bags. Up to re-sampling, each instance is uniquely predicted by one model. If models have high-enough bias, then we are not gaining much from bagging data. 

The *hard* bags of bagging are limited by the bias of each model: if none of them are good enough, their number does not matter, and dividing the task yields no advantage. In other words, **in a crowd of weak learners, there's no wisdom to be had**.

<div class="ui compact message quote">
<img class="ui tiny circular left floated image author" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/people/schapire_square.png">
<p style="margin: 0;">Why don't we bag the task instead?</p>
<p class="description">Robert E. Schapire, <a href="http://rob.schapire.net/papers/strengthofweak.pdf">The Strength of Weak Learnability.</a></p>
</div>


<!-- footer: "" -->

---
# Boosting

Boosting creates *fuzzy soft* bags, wherein instances are jointly predicted by all models, thus **decomposing the task**, rather than the data!

<div class="img_row centered">
<img class="ui image large centered" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/probabilities/SVG/bagging.svg">
<img class="ui image large centered" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/probabilities/SVG/boostingcolored.svg">
</div>

<div class="caption">

Bagging VS Boosting. In bagging, each bag is used to learn a model. In boosting, bags are *fuzzy*, and the task is decomposed so that each model predicts a subset of it.

</div>

<!-- footer: "" -->

---
# Boosting: a general formulation

Like bagging, we have a model of the form
$$
f_T(x) = \sum_{i = 1}^T \eta_i f^i(x),  \eta_{i} \in \mathbb{R},
$$
which is learned iteratively: first $f_1$, then $f_2$, etc. Sums and multiplications by scalar: looks like a job for linear algebra!

---
# Boosting and the functional (linear) space

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

Since we are operating with finite datasets, we can interpret functions as vectors $\vec{{f_i}} = [f_i(x_1),$ $\dots, f_i(x_{n})]$ in a vector space. Thus, we can interpret operations on functions as operations on vectors:
- $f + g = \vec{f} + \vec{g}$
- $\eta f = \eta \vec{f}$
- $f \cdot g = \vec{f} \cdot \vec{g}$

</div>
<div class="column">
<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/models_space.svg">
<div class="caption">

A model space of decision trees: in this space, summing allows us to generate novel decision trees, while inner products allows us to compute their alignment.

</div>
</div>
</div>

---
# Boosting: exploring the functional space

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

Boosting models are learned iteratively, each additional model $f_{t + 1}$ looking to reduce a predefined loss
$$
L_{t + 1} = l(Y_i, f_t(x) + \eta_{t + 1} f_{t + 1}).
$$

The additional function $f_{t + 1}$ is one of possibly many (possibly infinite) directions we can take in functional space. We want to pick the direction minimizing loss! What direction minimizes loss?

</div>
<div class="column">
<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/boosting_candidates.svg">
<div class="caption">

$f_1$ and some (of possibly infinite) directions $f_{2}$.

</div>
</div>
</div>

---
# Exploring optimization: the gradient

<div class="ui two column doubling stackable grid container bottom">
<div class="column w60">

The one **minimizing** $L^{t + 1}$! To know such direction, we rely on calculus, i.e., we compute the gradient of $L^{t + 1}$ w.r.t. $f^t: \nabla_{f_T} L^{t + 1}$. The negated gradient is the direction of minimization.

</div>
<div class="column w35">
<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/boosting_loss_iteration.svg">
<div class="caption">

Boosting and iterative optimization: we construct the model one loss improvement at a time, exploring the loss space.

</div>

</div>
</div>

---
# Exploring optimization: the gradient

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

Note: the space of models $\mathcal{F}$ to which $f_{t + 1}$ belongs may not be continuous, thus we can't necessarily directly define $f_{t + 1}$, so we choose the closest match, i.e., a $f_{t + 1}$ maximizing its similarity:
$$
f_{t + 1} = arg\max_{f \in \mathcal{F}} f \cdot - \nabla_{f^T} L^{t + 1}.
$$

</div>
<div class="column">
<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/boosting_models_iteration.svg">
<div class="caption">

Boosting and iterative optimization: each model is added to the boosting model, thus moving across the model space.

</div>
</div>
</div>

---
# The gradient in boosting: residuals

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

In boosting models, gradient of the loss gives us a search direction, but also a *residual*: practically, since each model is additive, gradients define directions as much as *residuals* we want to optimize. Thus, we fit models on datasets $(X, -\nabla L^t)$.

</div>
<div class="column">
<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/boosting_models_iteration.svg">
<div class="caption">

Boosting and iterative optimization: each model is added to the boosting model, thus moving across the model space.

</div>
</div>
</div>



---
# Boosting: a most generic algorithm

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

Knowing how to learn a model, we can inductively define any boosting algorithm:

1. Initialize $f_1$
2. Find optimal direction $- \nabla_{f_t} L^t$
3. Find admissible direction $f_{t}$
4. Find learning step $\eta_{t}$
5. Learn $f^t$
6. Go to 2.

</div>
<div class="column">
</div>
</div>

---
# Boosting: a most generic algorithm

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

Knowing how to learn a model, we can inductively define any boosting algorithm:

1. Initialize $f_1$
2. Find optimal direction $- \nabla_{f_t} L^t$
3. Find admissible direction $f_{t}$
4. Find learning step $\eta_{t}$
5. Learn $f^t$
6. Go to 2.

</div>
<div class="column">

Notes

- The function space could be anything: the space of Decision Trees (Gradient-Boosted Trees), of Logistic Regression (Logitboost), etc.
- Regularization is usually applied to $f_t$: allows to have weak learners, which helps with decreasing overfit

</div>
</div>

---
# Boosting and its many flavors

- **Adaboost.** Uses an exponential loss, adapts $\eta$ with a closed form search
- **Gradient-Boosted Trees.** Leverage Decision Trees as models
- **XGBoost.** Leverages trees, and uses a more robust loss approximation through the Hessian, rather than the gradient

---
# Boosting and bagging: regularization

Regularization is performed directly on the weak learners (to make sure we keep variance high), but can be applied post-hoc too through pruning!

---

# Boosting: computational complexity

Unlike bagging, models are learned iteratively - see the general algorithm. Thus the computational complexity for $k$ models is given by $\mathcal{O}(kc)$.

<!-- footer: "Remember: in asymptotical terms, constants are not considered." -->

---
# Boosting

<div class="ui two column doubling stackable grid container bottom">
<div class="column">
<div class="ui segment base pros"> 

- Model-agnostic
- Given some relatively likely theoretical assumptions, has extremely low bias
- Unlikely to overfit
- Computationally quick

</div>
<div class="ui segment base cons"> 

- Largely uninterpretable

</div>
</div>
<div class="column">
<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/boosting_models_iteration.svg">
<div class="caption">

Boosting: we iteratively refine the model $f^T$ by exploring the function and loss space.

</div>
</div>
</div>

<!-- footer: "" -->

---

# References

|                   | Source                                                                      |
| ----------------- | --------------------------------------------------------------------------- |
| Bias, Variance    | Deep Learning. I. Goodfellow, Y. Bengio, A. Courville. Sections 5.4         |
| Boosting, Bagging | Deep Learning. I. Goodfellow, Y. Bengio, A. Courville. Sections 7.11        |
| Random Forests    | [Random Forests](https://link.springer.com/article/10.1023/A:1010933404324) |

References to specific papers indicated in the slides footers'.