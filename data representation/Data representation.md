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
<link rel="stylesheet"
    type="text/css",
    href="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/css/themes/base.css" />
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

<style>
table {
font-size: 0.7em !important;
}
</style>

<!-- paginate: skip -->

# Data representation

---

<!-- paginate: true -->

# Data representation

Original representations are defined in *raw* terms of the data, and not in terms of its intended *use*:

- Manipulation
- Exploration
- Visualization

<div class="ui segment inverted highlight">
How to best represent data?
</div>

---

# How to represent data?

We will deal with two (out of many) approaches. Represent data...

<div class="ui three column doubling stackable grid container bottom">
<div class="column">

**By correlation**
I want to represent data according to the correlation of the dataset

Algorithm: `PCA`

</div>
<div class="column">

**By neighborhood**
I want to represent the data so that similar instances are similar

Algorithm: `t-SNE`.

</div>
<div class="column">

**By manifold**
I want to represent the data so that its manifold is preserved

Algorithm: `UMAP`.

</div>
</div>


---

# Principal Component Analysis (PCA)

---

# Principal component analysis (PCA)

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

Data can often be correlated, and linear dependencies can exist among variables, e.g.,

- Rent is linearly dependent on salary and food expenses
- Bank deposit is linearly dependent on salary and work
- Cardio is linearly dependent on hematocrit and $VO_2 max$

</div>
<div class="column">
<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/linalg/SVG/covariance.svg"/>
<div class="caption">

A two-variables mean-centered dataset $\bar{X}$, and the slope between the variables.

</div>
</div>
</div>

<div class="ui segment inverted highlight">
Wouldn't it be nice to remove all such dependencies, and pack them together?
</div>

---
# Vectors, linear combinations, and spaces

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

Vectors are $m$-dimensional elements in a field, and enjoy both addition and multiplication by scalar.


Composing these two, we can generate an infinite number of vectors: this is a **vector space**, and is defined by the *basis* vectors involved in the composition.

</div>
<div class="column">
<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/linalg/SVG/vector%20space.svg"/>
<div class="caption">


*Two vectors $u, v$ (in red and blue), and the plane spanned by all their linear combinations $\alpha_u u + \alpha_v v$* (in purple).


</div>

</div>
</div>

<!-- footer: "For simplicity, we consider Real fields." -->

---

# Vectors, linear combinations, and spaces

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

The simplest linear combination: scaling. Given a vector $v$, we have combination $\alpha v$, which defines a **direction** in the space.

</div>
<div class="column">

<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/linalg/SVG/direction.svg">

<div class="caption">


*A vector $u$, and the direction $\alpha u$.*


</div>

</div>
</div>

<!-- footer: "For simplicity, we consider Real fields." -->

---

# Vectors as linear combinations

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

Given a suitable set of vectors, called *basis*, we can redefine every vector as a linear combination of the basis.
Protip: is it called **basis** because it defines the **basis coordinates** of the space!


Every vector $[x_1, \dots, x_m]$ can be defined as a linear combination of the standard basis $[1, 0, \dots, 0],$ $[0, 1, \dots, 0],$ $\dots,$ $[0, 0, \dots, 1]$, with coefficients $x_1, x_2, \dots, x_m$.

</div>
<div class="column">

<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/linalg/SVG/projections_standard_basis.svg">

<div class="caption">

*A vector $x$, defined as a linear combination $\alpha_u u + \alpha_v v$.*

</div>

</div>
</div>

<!-- footer: "" -->

---

# Changes of basis

If I change the space, where do the vectors end up? I simply redefine them... in terms of the new coordinates!

<div class="img_row centered">
<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/linalg/SVG/projections_standard_basis.svg">
<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/linalg/SVG/projections_0.svg">
<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/linalg/SVG/projections_1.svg">
</div>

<div class="caption">

*A vector $x$, defined as a linear combination $\alpha_u u + \alpha_v v$, on three different bases.*

</div>

<!-- footer: "" -->

---

# Vectors and matrices

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

We encode vectors (and bases) in $(m \times n)$ matrices, easing computation of several interesting properties, including actual dimensionality. Since vectors define a space, **matrices define a space**!

We can define a vector in terms of a linear combination of the columns of a matrix through matrix-vector multiplication. 

</div>
<div class="column">
<div class="ui two column doubling stackable grid container bottom">
<div class="column" style="margin: auto;">

$$
A =
\begin{bmatrix}
	u_1 & v_1 \\
	u_2 & v_2 \\
\end{bmatrix}
$$

</div>
<div class="column">
<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/linalg/SVG/vector%20space.svg"/>
</div>
</div>

<div class="caption">

A $(2 \times 2)$ matrix $A$, and the space spanned by it through linear combinations $A x$.

</div>

</div>
</div>

<!-- footer: "" -->

---

# Matrices as linear transformations

<div class="ui two column doubling stackable grid container bottom">
<div class="column w70">

A matrix $A$ defines a space... and thus a linear transformation! $Av$ linearly combines the columns of $A$ with coefficients given by $v$. With vectors... simply put them in a matrix too!
$$A \begin{bmatrix} & & \\ v_1 & \dots & v_n \\ &&\end{bmatrix}$$

</div>
<div class="column w25">

<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/linalg/SVG/transformation_eigenvectors.svg"/>

<div class="caption">

Linear transformations can rotate, scale, or otherwise *linearly* transform vectors.

</div>

</div>
</div>

<!-- footer: "" -->

---

# Peculiar transformations: eigenpairs

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

Among all possible directions (subspaces defined by a single vector), some $v_1, \dots, v_m$ are always scaled: $Av_1 = [\lambda_1 v_1, \dots, \lambda_m v_m]$.

</div>
<div class="column">

<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/linalg/SVG/eigenvectors.svg"/>

<div class="caption">

A linear transformation $V$ and its effects on vectors $u, v, w$: its eigenvector $u$ is stretched by a factor of $\lambda_u u$.

</div>

</div>
</div>
<div class="ui raised segment question">
<p class="question" style="display: inline;">Eigenvectors and eigenvalues</p>

The eigenvectors $v_1, \dots, v_m$ of a matrix $A$ define the stretching of the space, and their eigenvalues $\lambda_1 > \dots > \lambda_m$ define the stretching factor.

</div>


<!-- footer: "" -->

---

# Eigenvectors and correlation

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

Symmetric matrices have a peculiar relationship with eigenpairs: the eigenvectors are **orthogonal**, and thus **linearly independent**!

Symmetric matrices may be rare... but given a matrix $A$, $A A^T$ is always symmetric!

Note: if $A$ is your feature matrix... $A A^T$ is your covariance matrix.

</div>
<div class="column">
<img class="ui large centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/linalg/SVG/eigenvectors.svg"/>

<div class="caption">

A linear transformation $V$ and its effects on vectors $u, v, w$: its eigenvector $u$ is stretched by a factor of $\lambda_u u$.

</div>
</div>
</div>

<!-- footer: "" -->

---

# Symmetric matrices and eigenpairs

<div class="ui raised segment question">
<p class="question" style="display: inline;">Spectral decomposition</p>

A symmetric matrix $A$ with eigenpairs $(v_1, \lambda_1), \dots, (v_r, \lambda_r)$ admits a decomposition
$$A =
V
\begin{bmatrix}
\lambda_1 & & \\
& \dots& \\
& & \lambda_r \\
\end{bmatrix}
V^T,
$$
where $V$ is an orthogonal matrix.
</div>


<div class="ui segment inverted highlight">
We can redefine our data in terms of its directions!
</div>

<!-- footer: "" -->

---

# Linking back to data representation

|              | allow us to...                                   |
| ------------ | ------------------------------------------------ |
| Matrices     | organize our data                                |
| Projection   | map the data to another (more suitable) space    |
| Eigenvectors | define the characteristic directions of the data |
| Eigenvalues  | define the scaling across said directions        |

---

# Principal component analysis (PCA)

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

Data can often be correlated, and linear dependencies can exist among variables, e.g.,

- Rent is linearly dependent on salary and food expenses
- Bank deposit is linearly dependent on salary and work
- Cardio is linearly dependent on hematocrit and $VO_2 max$

</div>
<div class="column">
<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/linalg/SVG/covariance.svg"/>
<div class="caption">

A two-variables mean-centered dataset $\bar{X}$, and the slope between the variables.

</div>
</div>
</div>

<div class="ui segment inverted highlight">
Wouldn't it be nice to remove all such dependencies, and pack them together?
</div>

---
# Principal component analysis (PCA)

PCA projects some data $X$ to $\hat{X}$  through a *linear* transformation $A$: $A X = \hat{X}$.

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

Fun fact #1: for a mean-centered $\bar{X}$, the slope is directly proportional to the covariance!
$$
\bar{\Sigma} =
\begin{bmatrix}
\sigma^2_{\bar{X}^1} & \dots & cov(\bar{X}^1, \bar{X}^n) \\
& \dots &\dots \\
 & & \sigma^2_{\bar{X}^n}
\end{bmatrix}
$$

Fun fact #2: we can measure covariance (and thus slope) through matrix multiplication $\bar{X} \bar{X}^T$.

</div>
<div class="column">
<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/linalg/SVG/covariance.svg"/>
<div class="caption">

A two-variables mean-centered dataset $\bar{X}$, and the slope between the variables.

</div>
</div>
</div>


<!-- footer: "For those interested, see the `slopes and covariance.pdf` supplement." -->

---

# PCA and the covariance matrix $\bar{\Sigma}$

PCA aims to embed collinearity in a set of novel features: each novel feature is defined in terms of linear combinations of other features.

With collinearity already embedded, are the novel features collinear?

<!-- footer: "" -->

---

<!-- paginate: hold -->
# PCA and the covariance matrix $\bar{\Sigma}$

PCA aims to embed collinearity in a set of novel features: each novel feature is defined in terms of linear combinations of other features.

With collinearity already embedded, are the novel features collinear? <span class="highlight">No!</span>
PCA aims to transform $\bar{X}$ into $\hat{X}$ with zero covariances:
$$
\bar{\Sigma} = 
\begin{bmatrix}
\sigma^2_{\bar{X}^1} & \dots & \dots & cov(\bar{X}^1, \bar{X}^n) \\
& \dots & \dots & \dots \\
 & & & \sigma^2_{\bar{X}^n}
\end{bmatrix}
\rightarrow
\hat{\Sigma} = 
\begin{bmatrix}
\sigma^2_{\hat{X}^1} & 0 & 0 & 0 \\
0 & \dots & 0 & 0\\
0 & 0 & 0& \sigma^2_{\hat{X}^n}
\end{bmatrix}.
$$

<!-- footer: "" -->

---

<!-- paginate: true -->
# PCA: mathematical formulation

We start with defining our result $\hat{X} = A \bar{X}$, and its symmetric covariance matrix $\hat{\Sigma}$, which we wish to diagonalize:
$$
(n - 1) \hat{\Sigma} = \hat{X} \hat{X}^T.
$$
With $\hat{X} = A \bar{X}$, we can rewrite this as
$$
(n - 1) \hat{\Sigma} =  A \bar{X} (A \bar{X})^T = A \bar{X}\bar{X}^T A^T
$$

<!-- footer: "Remember: the transpose of a product is the same product with inverted orders, and its components transposed: $(A B)^T = B^T A^T$." -->

---

<!-- paginate: hold -->

# PCA: mathematical formulation

We start with defining our result $\hat{X} = A \bar{X}$, and its symmetric covariance matrix $\hat{\Sigma}$, which we wish to diagonalize:
$$
(n - 1) \hat{\Sigma} = \hat{X} \hat{X}^T.
$$
With $\hat{X} = A \bar{X}$, we can rewrite this as
$$
(n - 1) \hat{\Sigma} =  A \bar{X} (A \bar{X})^T = A \bar{X} (A \bar{X})^T = A \underbrace{\bar{X}\bar{X}^T}_{= (n - 1) \bar{\Sigma}} A^T = A \bar{\Sigma}A^T.
$$

<!-- footer: "Remember: the transpose of a product is the same product with inverted orders, and its components transposed: $(A B)^T = B^T A^T$." -->

---

<!-- paginate: true -->

# PCA: leveraging eigenvectors

As a symmetric matrix, $\bar{\Sigma}$ enjoys an orthogonal eigenvalue decomposition $\bar{\Sigma} = \bar{V} \bar{\Lambda} \bar{V}^T$. Now, let us plug that back in $(n - 1) \hat{\Sigma}$:
$$
(n - 1) \hat{\Sigma} = A \bar{\Sigma} A^T = A (\bar{V} \bar{\Lambda} \bar{V}^T) A^T.
$$
Remember: our goal is to make this matrix **diagonal**! How do we do it?

<!-- footer: "" -->

---

<!-- paginate: hold -->

# PCA: leveraging eigenvectors

As a symmetric matrix, $\bar{\Sigma}$ enjoys an orthogonal eigenvalue decomposition $\bar{\Sigma} = \bar{V} \bar{\Lambda} \bar{V}^T$. Now, let us plug that back in $(n - 1) \hat{\Sigma}$:
$$
(n - 1) \hat{\Sigma} = A \bar{\Sigma} A^T = A (\bar{V} \bar{\Lambda} \bar{V}^T) A^T.
$$
Remember: our goal is to make this matrix **diagonal**! We already have a diagonal matrix ($\bar{\Lambda}$), ideally we'd like to remove all the other factors. We can do so because $A$ is our unknown! Let us set $A$ to $\bar{V}^T$:
$$
\begin{align}
(n - 1) \hat{\Sigma} = A (\bar{V} \bar{\Lambda} \bar{V}^T) A^T = \bar{V}^T \bar{V} \bar{\Lambda} \bar{V}^T \bar{V} &&&& \text{for } A = V^T \\
\end{align}
$$

<!-- footer: "In the last step, $A^T = (\\bar{V}^T)^T$ resolves to $\\bar{V}$ because of double transpose." -->

---

<!-- paginate: true -->

# PCA: leveraging eigenvectors

Again by property of symmetric matrices, the eigendecomposition yields orthogonal eigenvector matrices, that is, matrices $V$ whose inverse is the transpose, that is, $V$ is such that $V^{-1} V = V^T V = I$. This results in
$$
\begin{align}
(n - 1) \hat{\Sigma} = & A (\bar{V} \bar{\Lambda} \bar{V}^T) A^T = \bar{V}^T \bar{V} \bar{\Lambda} \bar{V}^T \bar{V} &&&& \text{for } A = V^T \\
(n - 1) \hat{\Sigma} = & \underbrace{\bar{V}^{-1} \bar{V}}_{= I} \text{  } \bar{\Lambda} \text{  }  \underbrace{\bar{V}^{-1} \bar{V}}_{= I} \\
(n - 1) \hat{\Sigma} = & \bar{\Lambda}, \\
\end{align}
$$
which gives us the diagonal covariance matrix $\hat{\Sigma}$ we were looking for. It follows that the linear PCA transformation is given by $A = V^T$, the transpose of the eigenvectors matrix of $\bar{X}$.

<!-- footer: "" -->

---

# PCA algorithm: a summary

1. Mean-center your data $X$, obtaining $\bar{X}$
2. Compute its eigenvectors matrix $\bar{V}$.
3. Transpose $V$ to obtain the transformation matrix $V^T$.
4. Project $\bar{X}$ through $V^T \bar{X}$, obtaining the PCA-transformed data $\hat{X}$.

<!-- footer: "" -->

---

# Using the PCA

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

**Observations**

- PCA redefines data by removing collinearity: if your data has low covariance, the transformation will have minimal effect.
- PCA performs a *linear* transformation to tackle *linear* relationships between variables. Nonlinear relationships are not influenced.

</div>
<div class="column">

**Uses**

- Feature selection: high covariance of a feature may indicate disposability.
- Dimensionality reduction: trimming columns of $\hat{X}$ lets us reduce the dimension of the resulting data.
- Clustering preprocessing: correlated features inflate object similarity.

</div>
</div>

<!-- footer: "" -->

---

# Using the PCA (poorly)

By collapsing covariant variables, instances may collapse together.

<div class="img_row centered">
<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/t-sne/SVG/colored_data_tsne.svg"/>
<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/t-sne/SVG/color1d.svg"/>
</div>
<div class="caption">

2-dimensional instances, and a 1-dimensional mapping.

</div>
<div class="ui compact message quote">
<img class="ui tiny circular left floated image author" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/people/geoffreyhinton_squared.jpeg">
<p style="margin: 0;">What if we instead represent by neighborhood?</p>
<p class="description">Geoffrey Hinton, <a href="https://cs.nyu.edu/~roweis/papers/sne_final.pdf">Stochastic neighbor embedding</a>. 2002</p>
</div>

<!-- footer: "" -->

---

# $t$-distributed Stochastic Neighbor Embedding ($t$-SNE)

$t$-SNE focuses on data clusters rather than subspace representation, and again maps the original data $X$ to a representation $\hat{X}$.


$t$-SNE tackles this problem in two phases:
1. <span class="highlight">Similarity phase</span> In the original space $\mathcal{X}$, how similar is $x_i$ to $x_j$?
2. <span class="highlight">Embedding phase</span> In the mapped space $\hat{\mathcal{X}}$, how similar is $\hat{x_i}$ to $\hat{x_j}$?

<!-- footer: "" -->

---

# Similarity phase

How similar is $x_i$ to $x_j$? Even better, **what is the probability that $x_j$ is a neighbor of $x_i$**?

<!-- footer: "" -->

---

# Neighboring phase

How similar is $x_i$ to $x_j$? Even better, **what is the probability that $x_j$ is a neighbor of $x_i$**?

<div class="ui raised segment question">
<p class="question" style="display: inline;">Neighboring through distribution.</p>

<div class="ui two column doubling stackable grid container bottom">
<div class="column w65">

Every instance $x_i$ defines a probability distribution $P_i = \mathcal{N}(x_i, \sigma^2_i)$ of neighboring.

$p_{j \mid i} = P_i(x_j)$ estimates the probability of $x_j$ being a neighbor of $x_i$ on the basis of their euclidean distance $\mid \mid x_i - x_j \mid \mid$.

In general, $\sigma^2_i \neq \sigma^2_j$, hence $p_{i, j} = \dfrac{1}{2} (p_{j \mid i} + p_{i \mid j})$.

</div>
<div class="column w35">
<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/linalg/SVG/relative_density.svg"/>

<div class="caption">

A Normal $\mathcal{N}(\mu, \sigma)$ distribution centered on $\mu$ (the red instance), and the relative density of another instance $x_j$ (in pink).

</div>

</div>
</div>

</div>

<!-- footer: "" -->

---

# Neighboring phase: locality

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

$\sigma^2_i$ defines the bandwidth of the Gaussian, and as such, the density of the cluster. We choose $\sigma_i^2$ so that the resulting local distribution, and thus clustering, has a controlled intra-cluster similarity.


</div>
<div class="column">

<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/linalg/SVG/distribution_shift.svg"/>

<div class="caption">

A Normal $\mathcal{N}(\mu, \cdot)$ distribution at different bandwidths $\sigma_1, \dots, \sigma_k$.

</div>

</div>
</div>

<!-- footer: "" -->

---

# Neighboring phase: defining locality

The *perplexity* hyperparameter $h$ quantifies the heterogeneity of the distribution: the larger the perplexity, the more heterogeneous the cluster, and the farther the points included in the cluster: $
h = Perp(P_i) = 2^{H(P_i)}.$


<div class="img_row centered">
<img style="vertical-align: top;" class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/linalg/SVG/distribution_shift.svg"/>
<img class="ui huge centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/t-sne/SVG/perplexity.svg"/>
</div>

<!-- footer: "$H(P_i)$ measures the entropy $H(P_i) = \\dfrac{1}{2} \\log (2 \\pi \\sigma_i^2) + \\dfrac{1}{w}$ of the distribution." -->

---

# Neighbors as a starting representation

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

The neighboring step generates a (soft) neighboring matrix $S$ akin to the one we use in clustering. The subsequent goal of $t$-SNE: to learn a representation $\hat{X}$ with as close a neighboring matrix $\hat{S}$ as possible.


</div>
<div class="column">

<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/t-sne/SVG/distribution_distance.svg"/>

<div class="caption">

Instances lied on a Normal (left) and $t$-student (right) distribution, induced by the original representation $X$, and by the $t$-SNE representation $\hat{X}$, respectively. $t$-SNE aims to make the densities on the two as similar as possible.

</div>

</div>
</div>

<!-- footer: "" -->

---

# Searching for neighbors in $\hat{\mathcal{X}}$ 

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

$\mathcal{\hat{X}}$ is typically a lower dimensional space than $\mathcal{X}$, in which the tails Gaussian distributions decrease rapidly, and far-away instances end up crowding them. Rather, $t$-SNE employs a $t$-student distribution with 1 degree of freedom, which has much slacker tails.

</div>
<div class="column">
<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/t-sne/SVG/distribution_distance.svg"/>

<div class="caption">

Instances lied on a Normal (left) and $t$-student (right) distribution: $t$-SNE aims to make the densities on the two as similar as possible.

</div>
</div>
</div>

<!-- footer: "The low tail and consequent concentration of instances on the tails is called 'overcrowding'. " -->

---
# Searching for neighbors in $\hat{\mathcal{X}}$ 

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

<div class="ui raised segment question">
<p class="question" style="display: inline;">Representation optimization.</p>

$t$-SNE minimizes the distance between $S$ and $\hat{S}$ through Kullback-Leiber divergence. Each $P_i$ induces a minimization
$$
KL(P_i \mid\mid \hat{P_i}) = \sum_{j \neq i}  p_{j \mid i} \log \dfrac{p_{j \mid i}}{\hat{p}_{j \mid i}}
$$

</div>


</div>
<div class="column">
<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/t-sne/SVG/distribution_distance.svg">

<div class="caption">

Densities of various points on the original normal distribution (left), and on the $t$-student distribution (right).

</div>

</div>
</div>

<!-- footer: "The low tail and consequent concentration of instances on the tails is called 'overcrowding'. " -->

---

# Using $t$-SNE

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

- $t$-SNE computes a full similarity matrix, thus it can be computationally expensive on extremely large datasets
- Unlike PCA, the transformation is not linear, and thus expressively more powerful (at the cost of interpretability)
- Perplexity is an hyperparameter that should be tuned

</div>
<div class="column">

- The optimization algorithm hides another set of parameters, which can result in nondeterministic results
- Perplexity is, in some hard-to-define way, related to dataset size. The more points in the dataset, the higher the inherent heterogeneity of the cluster, the higher the required perplexity. How much higher?

</div>
</div>

<!-- footer: "Ridiculously good visualization at [https://distill.pub/2016/misread-tsne/](https://distill.pub/2016/misread-tsne/) "-->

---
# PCA VS $t$-SNE

|                    | PCA                     | $t$-SNE          |
| ------------------ | ----------------------- | ---------------- |
| Transformation     | Linear                  | Nonlinear        |
| Hyperparameters    | None                    | Perplexity       |
| Determinism        | Deterministic           | Nondeterministic |
| Interpretability   | Interpretable           | Noninterpretable |
| Locality           | Global                  | Local            |
| Computational cost | Low, $\mathcal{O}(n^3)$ | High             |

<!-- footer: ""-->

---
# A third way: Uniform Manifold Approximation and Projection

PCA and $t$-SNE tackle locality as a dichotomy: either global, or local, and are thus not *locally-adaptive*:
- PCA: we study spectral decomposition of the whole dataset
- $t$-SNE: we define perplexity over the whole dataset

<div class="ui compact message quote">
<img class="ui tiny circular left floated image author" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/people/leland_squared.jpg">
<p style="margin: 0;">What if we adapt the neighborhoods?</p>
<p class="description">Leland McInnes, <a href="https://arxiv.org/abs/1802.03426">UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction</a>. 2018</p>
</div>

---
# UMAP and the adaptive manifold

Both  $t$-SNE and UMAP approximate the data manifold, only the former can only approximate it accurately for uniform manifolds! *Unlike* $t$-SNE, UMAP locally adapts the manifold to each instance, thus defining *adaptive* neighborhoods, **each instance** defining its neighborhood with **its own parameterization**.


[A visualization](https://pair-code.github.io/understanding-umap/) of a possible adaptive neighborhood definition: distance to the $k$-th neighbor adaptively and locally determines the manifold. Each instance stretches the space so that its own neighborhood has a given volume.

---
# UMAP and the connectivity graph

The computed distances induce a connectivity graph, and thus an adjacency matrix $A$, its edges measuring distances among instances. After turning distances into probabilities, UMAP optimizes a distance on $A$, to make it so that all and only the edges on the original manifold also appear in the transformed manifold with the same magnitude. 

---
# UMAP and the connectivity graph

For the set of edges $E$, UMAP minimizes

$$
-\sum_{e \in E} (\underbrace{ \Pr(e; X) \log(\Pr(e; Z)) }_{existing \text{ } edges} + \underbrace{(1 - \Pr(e; Z))\log(1 - \Pr(e; X))}_{non-existing \text{ } edges}),
$$
where $\Pr(e; X), \Pr(e; Z)$ indicate the probability of edge $e$ in the original and transformed representation, respectively.

---
# PCA VS $t$-SNE VS UMAP

|                    | PCA                     | $t$-SNE          | UMAP                     |
| ------------------ | ----------------------- | ---------------- | ------------------------ |
| Transformation     | Linear                  | Nonlinear        | Nonlinear                |
| Hyperparameters    | None                    | Perplexity       | Neighborhood size        |
| Determinism        | Deterministic           | Nondeterministic | Nondeterministic         |
| Interpretability   | Interpretable           | Noninterpretable | Noninterpretable         |
| Locality           | Global                  | Local            | Adaptive                 |
| Computational cost | Low, $\mathcal{O}(n^3)$ | High             | Low, but higher than PCA |

<!-- footer: ""-->

---
# Data representation: which to choose?



<div class="ui three column doubling stackable grid container bottom">
<div class="column">

**PCA**

<div class="ui segment base pros">

- Strong mathematical foundation
- Interpretable results
- Extremely fast

</div>
<div class="ui segment base cons">

- Global

</div>

</div>
<div class="column">

$t$**-SNE**

<div class="ui segment base pros">

- Powerful

</div>
<div class="ui segment base cons">

- Slow
- Sensitive to initialization and parameters
- Parameters a bit obscure

</div>

</div>
<div class="column">

**UMAP**

<div class="ui segment base pros">

- Adaptive
- Interpretable parameters
- Strong mathematical foundation
- Fast

</div>
<div class="ui segment base cons">

- Sensitive to initialization

</div>

</div>
</div>

---
# Space representations

Representations allows us to map data into another space. What if we pick a space of smaller dimensionality?

<div class="img_row centered">
<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/linalg/SVG/covariance.svg"/>
<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/linalg/SVG/no_correlation.svg"/>
<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/linalg/SVG/dim1_mapping.svg"/>
</div>
<div class="caption">

From the original dataset, to an alternative representation, to a smaller space representation.

</div>

---

# Space representations in PCA

<div class="ui two column doubling stackable grid container bottom">
<div class="column">


PCA is a linear transformation $A \bar{X} = \hat{X}$, and as such it follows standard dimension rules on matrix-* multiplication: $(m \times n)(n \times k)$ yields a matrix $(m \times k)$. We can trim columns off of $\hat{X}$... but at what cost?

</div>
<div class="column">

<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/t-sne/SVG/scree_lambda.svg"/>

<div class="caption">

Eigenvalues in decreasing order of magnitude: larger eigenvalues increase the magnitude of instances, lower instead lower it. We can trim this with the elbow method: look for a value of maximum change in eigenvalues.

</div>

</div>
</div>

---

# Space representations in PCA

<div class="ui two column doubling stackable grid container bottom">
<div class="column">


PCA is a linear transformation $A \bar{X} = \hat{X}$, and as such it follows standard dimension rules on matrix-* multiplication: $(m \times n)(n \times k)$ yields a matrix $(m \times k)$. We can trim columns off of $\hat{X}$... but at what cost?

</div>
<div class="column">

<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/t-sne/SVG/scree_norm.svg"/>

<div class="caption">

PCA norm on an increasing number of trimmed dimensions. We can trim this with the elbow method: look for a value of maximum change in eigenvalues.

</div>

</div>
</div>
