---
type: presentation
marp: true
paginate: true
footer: ''
topic: 
---

<!-- Made with marpee: https://github.com/msetzu/marpee -->
<!-- Made with marp: https://marp.app -->

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

# Gradient-based optimization
*Exploiting gradient*

---

<!-- paginate: true -->

# The computational graph

We can generalize several gradient-based optimization to *computational graphs*, objects which compute a generic function $f(x)$. Functional form: $h(\omega^T x)$. Note: $\omega^T x$ is simply a linear combination of $x$.

<img class="ui large centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/computational_graph.svg">
<div class="caption">

A computational graph: nodes indicate objects involved in the computation, and edges indicate their flow in the graph.

</div>

---
# The forward pass: computing $f(x)$

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

To compute $f(x)$, we navigate the graph $g$ bottom-up:
- Nodes are either
	- data: stores some data
	- functions: computes a function the sum of incoming edges
- Edges are weights in a weight space $\Theta$, weighting the node traversing them

</div>
<div class="column">
<img class="ui large centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/computational_graph.svg">
<div class="caption">

A forward pass in $g$: $x_i$ is weighted by $\omega_i$, then $h$ is computed on their sum. Opacity of edges scaled with value of $\omega_\cdot$.

</div>
</div>
</div>

---
# The forward pass: computing $f(x)$

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

In a computational graph, we have
- Parameters $\theta$ given the weights on the nodes
- Structure given by the graph's architecture and functions

</div>
<div class="column">
<img class="ui large centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/computational_graph.svg">
<div class="caption">

A computational graph $g$ computing $h(w^T x)$. The structure is given by the operations ($h, \cdot$), while the parameters ($\omega_1, \omega_2, \omega_3, \omega_4$).

</div>
</div>
</div>

---
# Parameters and structure

The parameters-structure dichotomy is not unique to computational graphs, and we can find this also on other models. Note that pure algorithms with no learning involved, e.g., Naive Bayes, do not have this distinction, and everything is structure.

<div class="img_row centered">
<img class="ui medium image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/parameterspace.svg">
<img class="ui medium image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/k_parameters.svg">
<img class="ui medium image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/tree_parameters.svg">
</div>
<div class="caption">

A generic parameter space $\Theta$ (left), one for $k$-NN (center), and a subset of one for Decision Trees (right).

</div>

---
# The backward pass: improving $\theta$

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

Given a loss $L$ computed with a differentiable loss function $l$, as we have done for Gradient Boosting Machines, we can find directions in the model space where the $L$ decreases.

Note: in computational graphs, we optimize over the parameter space, i.e., over $\Theta$.

</div>
<div class="column">
<img class="ui large centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/backward_pass.svg">
<div class="caption">

A backward pass in $g$: change parameters indicated by the gradient indicates the direction towards which move parameters to minimize $l$.

</div>
</div>
</div>

---
# Scaling up: layering graphs

<div class="ui two column doubling stackable grid container bottom">
<div class="column w60">

The backward pass is made possible by the differentiability of the loss... but this can be applied also to the functions within $g$: if a function $h_i$ within $g$ is differentiable, then I can **recursively compute gradients** on it! 
<div class="ui raised segment question">
<p class="question" style="display: inline;">Chain rule of calculus</p>

The derivative of a composite function $f = f_1 \circ f_2$ is
$$
\dfrac{\partial f}{ \partial x} = \dfrac{\partial f_1}{ \partial f_2} \dfrac{\partial f_2}{ \partial x} 
$$

</div>
</div>
<div class="column w40">
<img class="ui large centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/backward_pass.svg">
<div class="caption">

A backward pass in $g$: change parameters indicated by the gradient indicates the direction towards which move parameters to minimize $l$.

</div>
</div>
</div>

---
# Scaling up: layering graphs

Applying the chain rule recursively, and going *down* the computational graph, we can compute optimization directions for all parameters! The algorithm chaining back the loss gradient is called *backpropagation*.

<div class="ui two column doubling stackable grid container bottom">
<div class="column">
<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/network.svg">
</div>
<div class="column">
<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/backward_prop.svg">
</div>
</div>
<div class="caption">

A multi-layered computational graph, and its forward (left) and backward (right) pass. The chain rule enables propagation of updates back and over the entire network.

</div>

---
# Neural networks

Neural networks implement computational graphs.

<div class="ui two column doubling stackable grid container bottom">
<div class="column">
<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/network.svg">
<div class="caption">

A visualization of a neural network.

</div>
</div>
<div class="column">

Some nomenclature:

- Layer: set of all adjacent nodes
- Block: collection of consecutive layers
- Activation function: functions found in nodes
- Hidden layer: a layer, except the first or last one
- Output layer/nodes: layer/nodes yielding the computed $f_\theta(x)$

</div>
</div>

---
# Neural networks: the training loop

Fitting a neural network consists in, at a very high level, repeatedly computing forward and backward passes, each pair improving on the current loss.

<div class="ui six column doubling stackable grid container bottom">
<div class="column">
<img class="ui small centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/network.svg">
</div>
<div class="column">
<img class="ui small centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/backward_prop.svg">
</div>
<div class="column">
<img class="ui small centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/network.svg">
</div>
<div class="column">
<img class="ui small centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/backward_prop.svg">
</div>
<div class="column">
<img class="ui small centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/network.svg">
</div>
<div class="column">
<img class="ui small centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/backward_prop.svg">
</div>
</div>

<div class="caption">

Consecutive foreward and backward passes on a network, each backward pass leverages gradients of the loss to find local directions of loss minimization, which are then used to fit the model.

</div>

---
# Learning in neural networks

---
# Stochastic learning

Backpropagation takes care of defining optimal directions for the parameters, but how do we estimate and leverage these directions?

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

Estimating directions: Through stochastic gradient, by computing gradient on a *batch* of data, rather than the whole dataset.

Provides a good approximation and a much faster computation.

</div>
<div class="column">
<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/stochastic_sgd.svg"/>
<div class="caption">

The gradient $\nabla L^X$ estimated on the some data $X$, and gradients $\nabla L^{X1}, \nabla L^{X2}$ estimated on subsets of $X1, X2$ of $X$.

</div>
</div>
</div>

---
# Stochastic learning

Backpropagation takes care of defining optimal directions for the parameters, but how do we estimate and leverage these directions?

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

Batches can be aggregated, the directions they yield combined: a training-specific approach to combat overfit.


</div>
<div class="column">
<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/stochastic_sgd.svg"/>
<div class="caption">

The gradient $\nabla L^X$ estimated on the some data $X$, and gradients $\nabla L^{X1}, \nabla L^{X2}$ estimated on subsets of $X1, X2$ of $X$.

</div>
</div>
</div>

---
# Momentum

Backpropagation takes care of defining optimal directions for the parameters, but how do we estimate and leverage these directions?

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

Estimating weight update: Update directions are weighted by a possibly decaying learning rate $\eta$, and possibly weighted by past updates (Adam, RMSProp, Nesterov momentum).

</div>
<div class="column">
<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/momentum.svg"/>
<div class="caption">

Momentum controls the weight of the parameter updates: the lower, the lesser the impact of the direction, and vice versa.

</div>
</div>
</div>

---
# Regularization

Regularization of neural networks can take many forms.


<div class="ui two column doubling stackable grid container bottom">
<div class="column">

**Weight regularization**

The loss includes a term $\mid\mid \Omega \mid\mid_2$ to penalize large weights in the network, as higher weights tend to increase the network capacity.

</div>
<div class="column">

**Dropout**

Random deletion of network connections, aims to create networks less reliant on a small number of neurons. 

</div>
</div>

---
# Early stopping

As fitting goes on, we adapt the capacity of the network. How do we prevent the model to overfit? Early stopping!

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

We keep two rolling statistics:
1. The gap between train and validation error
2. Train error

We stop when 1. grows larger (to avoid overfit), or 2. does not lower (to avoid unnecessary training).

</div>
<div class="column">
<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/biasvariance.svg"/>
<div class="caption">

Model error on training (blue) and validation (red) data: as iterations go by, the model lowers its loss, possibly incurring in overfit.

</div>

</div>
</div>

---

# Structure

---

# Activation functions

Activation functions impact the flow of data throughout the network, and their outputs are called *activations*. Different activations define different *representations* of the data, which, unlike in PCA, are dependent on learned parameters.

<div class="ui two column doubling stackable grid container bottom">
<div class="column">


|              | Formulation                             | Heads    |
| -------- | --------------------------------------- | -------- |
| Identity | $\omega^T x$                            | $1$      | 
| Logistic | $\dfrac{1}{1 + e^{- \omega^T x}}$       | $1$      |
| ReLU     | $\max\{0, \omega^T x\}$                 | $1$      |
| Softmax  | $\dfrac{exp(\omega_i x_i)}{exp(w^T x)}$ | $\geq 1$ |
| ...      | ...                                     | ...      |


</div>
<div class="column">
<img class="ui medium centered image" src="https://upload.wikimedia.org/wikipedia/commons/5/5b/Activation_logistic.svg">
<br>
<img class="ui medium centered image" src="https://upload.wikimedia.org/wikipedia/commons/f/fe/Activation_rectified_linear.svg">

<div class="caption">

Logistic (top) and ReLU (bottom) activation functions.

</div>
</div>
</div>


<!-- footer: "Remember, $\\omega^T x$ is the sum of the incoming edges in the node." -->

---
# Activation functions

As the last operation in the network, activation functions play different roles.

|          | Formulation                             | Heads    | Task            |
| -------- | --------------------------------------- | -------- | --------------- |
| Identity | $\omega^T x$                            | $1$      | Regression      |
| Logistic | $\dfrac{1}{1 + e^{- \omega^T x}}$       | $1$      | Classification* |
| ReLU     | $\max\{0, \omega^T x\}$                 | $1$      | Regression*     |
| Softmax  | $\dfrac{exp(\omega_i x_i)}{exp(w^T x)}$ | $\geq 1$ | Classification* |

<!-- footer: "*Indirectly: classification is often rendered as a continuous value (to turn into discrete), while regression may be bounded, e.g., to be positive by ReLU." -->

---
# Architectures

<!-- footer: "" -->

---
# To fit or not to fit, this is the question

Given their high capacity, and innate ability to encode data, networks are often not fit from scratch. Rather, a network is fit on a task, then *adapted* to other tasks.

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

**Fine-tuning**

A network is first trained on a general task and a large dataset, then some more training is performed on the smaller, specialized task.

</div>
<div class="column">

**Adapters**

Small networks are fit to "steer" the parameters of a larger network to solve a specific task. They are then included in the desired architecture.

</div>
</div>

---
# Network architectures: ResNet

Architectures have proven to be extremely important, and in several cases, the application dictates the network architecture. On tabular dataset, residual networks (ResNets) are a particularly strong baseline. They have a functional form $f(x) = x + h(x)$.


<img class="ui large centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/skipconnection_alternate.svg">
<div class="caption">

A residual block: a node is forwarded to the next layer, and to the one after it as well. Residual (also called *skip*) connections allow a more effective backpropagation. Weights on the skip connection are set to $1$ to preserve data.

</div>

---
# Network architectures: FeatureTransformer

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

Blocks constructs circuits of similarity, computing degrees of "attention" between features, and representations. Similarity then weighs on skip connections. Functional form: $f(x^i) = f(x^i) + \sum_{j \neq i} \alpha_{i, j} x^j$.

</div>
<div class="column">
<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/ml/SVG/attention.svg">
<div class="caption">

An attention block: similarities between representations are computed through a (scaled) multiplication. Addition through a residual connection allows representations to explicitly influence each other

</div>
</div>
</div>

---

# References

|                     | Reference                                                                                        |
| ------------------- | ------------------------------------------------------------------------------------------------ |
| Neural Networks     | Deep Learning. I. Goodfellow, Y. Bengio, A. Courville. Sections 6.1-6.5, 7.1, 7.8                |
| Feature Transformer | [On Embeddings for Numerical Features in Tabular Deep Learning](http://arxiv.org/abs/2203.05556) |
| ResNet              | [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385)                                                                                                 |
