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

# Time series
Data... over time.

---

<!-- paginate: true -->

# Time series

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

A univariate series $s \in \mathcal{X}^n$ is a sequence $s = [s_1, \dots, s_n]$ of $n$ values in a domain $\mathcal{X}$. A series is defined by:

- *Type*: discrete, e.g., nucleotide bases, or continuous, e.g., stock values in a financial market
- *Sampling rate*: How often values are sampled, e.g., daily
- *Amplitude*: Values sampled, e.g., value of the stock on a particular day


</div>
<div class="column">

<img class="ui large centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/series/SVG/series.svg">

<div class="caption">

A time series.

</div>

</div>
</div>

---

# Time series

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

A univariate series $s \in \mathcal{X}^K$ is a sequence $s = [s_1, \dots, s_K]$ of $K$ values in a domain $\mathcal{X}$. A series is defined by:

- *Seasonality*: Series repeat (or almost  repeat) over time, e.g., temperature
- *Period*: How much does it take for the series to repeat itself, e.g., length of a calendar year

</div>
<div class="column">

<img class="ui large centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/series/SVG/series.svg">

<div class="caption">

A time series.

</div>

</div>
</div>

---

# Time series

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

A multivariate time series $s$ generalizes time series to multiple variables. Each instance is comprised of multiple time series, each representing a different feature.

</div>
<div class="column">


<img class="ui large centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/series/SVG/series_multi.svg">

<div class="caption">

A multivariate time series, with a variable in red, one in blue.

</div>

</div>
</div>

---

# Time series statistics

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

- Mean. Expected value $\mathbb{E}[s]$ of $s$
- Variance. Variance of $s$
- Trend: slope $\Delta$ of a linear model modeling $s$

Note: computed over time, not samples.

</div>
<div class="column">

<img class="ui large centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/series/SVG/trend.svg">

<div class="caption">

A time series, and its  trend (in beige).

</div>

</div>
</div>

---

# Time series statistics

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

- Interquantile ranges. $q_a(s) - q_b(s)$
- Skewness: is the distribution symmetric? $\mathbb{E}[(\dfrac{s - \mu}{\sigma})^3]$
- Kurtosis: what is the probability mass on the tails? $\mathbb{E}[(\dfrac{s - \mu}{\sigma})^4]$

</div>
<div class="column">
<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/linalg/SVG/density_gradient.svg">
<div class="caption">

Empirical distribution of a time series components, values color-coded by density.

</div>
</div>
</div>

---

# Time series: local behaviors

Time series can be affected by:
- *Seasonality*: the series has some repeated periodic behavior, e.g., temperatures fall every winter
- *Trends*: the series tends to have a monotonic behavior, with values increasing/decreasing

We need to analyze time series on a local scale.

---

# Time series statistics: rolling statistics

Rolling indicates the act of extracting a series of consecutive subsequences of given dimensionalities $w^1, \dots, w^k$. Each subseries gives a different view on $s$, and is thus named *window*. Given a series of windows, we can now *locally* describe a time series!

- Rolling mean
- Rolling variance
- ...

---

# Time series statistics: sliding statistics

Unlike rolling statistics, which compute a statistic over a subseries of a given series, *sliding* statistics slide a series $t$ over a series $s$, computing a statistic between the two. The act of sliding a window through a function is called *convolution*.

**Autocovariance**
How much does a component of a time series correlate with previous and future components? Slides a series over itself, computing covariance between the two components:

$$
cov(s_{t:}, s_{t + \Delta:}) = \dfrac{1}{n - \Delta} \sum_{i = 1}^{n - \Delta} s_i \cdot s_{i + \Delta}.
$$

High autocovariances may indicate seasonality in the series.

---

# Time series: sliding statistics

**Cross-correlation**
Shifted pointwise correlation of the two series $a, b$, measured as a *sliding* inner product:

$$
CC_\Delta(a, b) = \sum_{i = 1}^n a_i \cdot b_{i + \Delta}.
$$
For univariate time series, the inner product is simply a multiplication.

---

## From analyzing to transforming

---

# Representing by segmenting

Given a set of time series $S = \{s^1, \dots, s^n\}$, let $S^\subset$ be a set of $k$ subseries $s^1_\subset, \dots, s^k_\subset$. We define an alphabet $\Sigma$ of symbols, each symbol assigned to a subseries. Then, we can *segment* each series into a sequence of subseries, and represent each time series as a series of symbols in $\Sigma^*$.

$$
s^i \rightarrow \underbrace{[ s^{i, 1} \mid \dots \mid s^{i, k_i}]}_{\in \Sigma^*}
$$

We can tackle two problems independently:
- Segmentation: how to split a series into subseries?
- Transformation: what symbols do we use to define each segment?

---

# Fixed window-based segmentation

<div class="ui two column doubling stackable grid container bottom">
<div class="column w60">

 Each series $s^i$ has an often intractable number of possible subseries, which makes exhaustive search unfeasible. Instead, we choose an arbitrary window $w$, and segment each series into a set of $\dfrac{n}{w}$ subseries.

</div>
<div class="column w40">
<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/series/SVG/segmentation.svg">
<div class="caption">

A fixed window of size $w = 2$, segmenting a time series in three non-overallping adjacent windows (color-coded).

</div>
</div>
</div>

---

# Learned segmentation

We *learn* segmentations which minimize an approximation error.

<div class="ui two column doubling stackable grid container bottom">
<div class="column w60">

Piecewise Linear Approximation (PLA) defines a segmentation minimizing segment-local linear models of the data.

- Given number of segments: segmentation which distributes approximation error as evenly as possible among segments
- Given error bound: segmentation which generates the *minimum* number of segments within given error bound $\varepsilon$

</div>
<div class="column w40">

<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/series/SVG/segmentation_eps.svg">
<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/series/SVG/segmentation_k.svg">

<div class="caption">

Segmentation on minimum error (top) and given number of segments (bottom).

</div>

</div>
</div>

<!-- footer: "" --> 

---
# Learned equidistributional windows

We *learn* segmentations by their likelihood: given a desired number of segments, segments are learned to maximize their probability $p(s^i_\subset)$, which results in segments as equiprobable as possible, ideally following a uniform distribution. By maximizing probability, we maximize entropy, and thus the diversity of the subseries.

---
# Continuous transformations

|                        | Description                   | Type       | $f^\Sigma$             | $\Sigma$                   |
| ---------------------- | ----------------------------- | ---------- | ---------------------- | -------------------------- |
| Piecewise Average (PA) | Average value of the segment  | Continuous | $\mu_{s^i_\subset}$    | $\mathbb{R}$               |
| Piecewise Linear (PL)  | Slope $\nabla$ of the segment | Continuous | $\nabla_{s^i_\subset}$ | $\mathbb{R}, \mathbb{R}^2$ |

<!-- footer: "$\\mathbb{R}^2$ given by storing both slope and intercept of the linear model." --> 

---

# Two-tier segmentations

Window segmentations create series of symbols themselves! We can learn representations through a two-tier algorithm:
- continuous transformation, yielding segments $S^\subset$ with symbols in $\Sigma^\subset$
- transformation partitioning, mapping symbols in $\Sigma^\subset$ to discrete symbols in $\Sigma$

Symbols can be either categorical, or ordinal.

<!-- footer: "" --> 

---
# Symbolic aggregate approximation (SAX)

Symbolic aggregate approximation (SAX) implements a two-tier transformation:
- fixed-window segmentation followed by piecewise average transformation in subsymbols $(\Sigma^\subset)^*$
- aggregation of subsymbols into equiprobable symbols in $\Sigma$: we partition the subsymbol distribution into equiprobable buckets, each defined by a symbol in $\Sigma$

SAX symbols are discrete *and* ordinal!

<!-- footer: "" --> 

---
# Symbolic aggregate approximation (SAX)

<div class="ui three column doubling stackable grid container bottom">
<div class="column">
<img class="ui large centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/series/SVG/sax_segmentation.svg">
</div>
<div class="column">
<img class="ui large centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/series/SVG/sax_probability.svg">
</div>
<div class="column">
<img class="ui large centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/series/SVG/sax_transformed.svg">
</div>
</div>

<div class="caption">

The three steps of SAX: subsymbol induction with fixed-window average segmentation, partitioning of the subsymbol distribution, and transformation.

</div>

---
# Signal representations

Segmentations can be tricky to handle, and simply offer a representation in a domain quite different from the original. Signal representations, on the other hand, aim to define a series in terms of other series. To stick with the signal processing literature, where they are most prevalent, we'll refer to series as *signals*.

- What other signals can we leverage?
- How do we combine them to represent the original series?

<!-- footer: "" --> 


---
# Fourier analysis

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

Fourier analysis tackles **periodic** (also known as stationary) series, i.e., series which periodically repeat themselves.

- What other signals can we leverage? Sine and cosine signals at different frequencies
- How do we combine them to represent the original signal? Linear combination

</div>
<div class="column">

<img style="margin-bottom: 10px;" class="ui medium image centered" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/series/SVG/sinusoid.svg">

<img style="transform: scale(0.5, 1);" class="ui medium image centered" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/series/SVG/sinusoid.svg">

<img style="margin-top: 10px;" class="ui medium image centered" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/series/SVG/cosx_p_cos2x.svg">

<div class="caption">

Two signals $\cos(x), \cos(2x)$, and a linear combination $\cos(x) + cos(2x)$.

</div>

</div>
</div>

<!-- footer: "" --> 


---

# Fourier analysis

As a linear transformation, we need to learn a set of coefficients $\alpha$ which map the basis to the signal $s$. In Fourier analysis, we constrain $\alpha \in \mathbb{R}^+$:
- basis signals which do not contribute to the signal have a $0$ coefficient
- basis signals which do contribute do so with a positive coefficient $\alpha_j > 0$

To compute $\alpha$ we can thus use *inner products*, e.g., dot product, which are guaranteed to satisfy both.

<!-- footer: "" --> 

---

# The basis: sinusoids

First, we define the basis of the transformation. We use sinusoids, i.e., $\sin$/$cos$ signals defined by a phasor $\psi$.


<svg id="phasor" class="svgWithText" width="600" height="150" style="margin-left: 50px; margin-right: 100px;"><g class="x axis" transform="translate(0,75)" style="opacity: 0.25;"><path class="domain" d="M0,0V0H150V0"></path></g><g class="y axis" transform="translate(75,0)" style="opacity: 0.25;"><path class="domain" d="M0,0H0V150H0"></path></g><circle cx="75" cy="75" r="60" stroke-width="1.5" stroke="black" fill="none" opacity="0.5"></circle></svg>

<script type="text/javascript" src="https://cdn.jsdelivr.net/gh/jackschaedler/circles-sines-signals@latest/third_party/d3/d3.min.js"></script>
<script>
var PHASOR_FREQUENCY = 2;
var PHASOR_AMPLITUDE = 1;
var TARGET_PHASOR_FREQUENCY = 2;
var TARGET_PHASOR_AMPLITUDE = 1;
var PHASOR_INTERPOLATOR = d3.interpolateNumber(PHASOR_FREQUENCY, TARGET_PHASOR_FREQUENCY);
var PHASOR_AMP_INTERPOLATOR = d3.interpolateNumber(PHASOR_AMPLITUDE, TARGET_PHASOR_AMPLITUDE);
var PHASOR_INTERPOLATION = 1.0;
var PHASOR_AMP_INTERPOLATION = 1.0;
function GET_PHASOR_FREQUENCY() {
	return PHASOR_INTERPOLATOR(Math.min(PHASOR_INTERPOLATION, 1.0));
}
function GET_PHASOR_AMPLITUDE() {
	return PHASOR_AMP_INTERPOLATOR(Math.min(PHASOR_AMP_INTERPOLATION, 1.0));
}
function updateFreq(freq) {
	PHASOR_FREQUENCY = GET_PHASOR_FREQUENCY();
	TARGET_PHASOR_FREQUENCY = freq;
	PHASOR_INTERPOLATION = 0.0;
	PHASOR_INTERPOLATOR = d3.interpolateNumber(PHASOR_FREQUENCY, TARGET_PHASOR_FREQUENCY);
}
function updateAmp(amp) {
	PHASOR_AMPLITUDE = GET_PHASOR_AMPLITUDE();
	TARGET_PHASOR_AMPLITUDE = amp / 5000;
	PHASOR_AMP_INTERPOLATION = 0.0;
	PHASOR_AMP_INTERPOLATOR = d3.interpolateNumber(PHASOR_AMPLITUDE, TARGET_PHASOR_AMPLITUDE);
}
</script>
<script type="text/javascript" src="https://cdn.jsdelivr.net/gh/jackschaedler/circles-sines-signals@latest/js/phasor_sine.js"></script>

<div class="caption">

A phasor $\psi$, and the $\sin$ series generated.

</div>

<!-- footer: "" --> 


---
# The basis: sinusoids

First, we define the basis of the transformation. We use sinusoids, i.e., $\sin$/$cos$ signals defined by a phasor $\psi$.

<svg id="phasor2" class="svgWithText" width="150" height="350" style=""><g class="x axis" transform="translate(0,75)" style="opacity: 0.25;"><path class="domain" d="M0,0V0H150V0"></path></g><g class="y axis" transform="translate(75,0)" style="opacity: 0.25;"><path class="domain" d="M0,0H0V150H0"></path></g><circle cx="75" cy="75" r="60" stroke-width="1.5" stroke="black" fill="none" opacity="0.5"></circle></svg>
<script type="text/javascript" src="https://cdn.jsdelivr.net/gh/jackschaedler/circles-sines-signals@latest/js/phasor_cosine.js"></script>

<div class="caption">

A phasor $\psi$, and the $\cos$ series generated.

</div>

<!-- footer: "" --> 

---
# Sinusoids define amplitude

For a phasor $\psi$, we can define the period $t_0$ as the time required for the phasor to complete one rotation over the unit circle, and the frequency $f_0 = t_0^{-1}$ as the rotations per unit of time. Then, at time $t$, the phasor defines a series component with amplitude
$$
s_{t} = \underbrace{\alpha}_{amplitude \text{ } scaling} \cos(\overbrace{2\pi f_0 t}^{angle \text{ } \theta_{0, t}} \text{ } \underbrace{+ \phi}_{shifting}).
$$

<!-- footer: "The shift $\\phi$ indicates the shift of the sinusoid itself with respect to $t = 0$. A nice interactive visualization [here](https://brianmcfee.net/dstbook-site/content/ch01-signals/Waves.html#id5)." --> 

---

# Sinusoids and the complex unit circle

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

By Euler, we can map complex numbers to the complex unit circle.
$$
e^{-i\theta} = \cos(\theta) + i\sin(\theta).
$$

</div>
<div class="column">

<img src="https://brianmcfee.net/dstbook-site/_images/5fbcdf6e32da575cb95a33aa78a48f92982eeb22caef96ae0d77206015728313.svg" class="ui medium centered image">
<div class="caption">

The complex unit circle and an imaginary number $z = e^{-i\theta}$. As in linear algebra, we can define a vector $(z_{\mathbb{R}}, z_{\mathbb{C}})$ through the standard basis, in this case $(1, 0), (0, i)$.

</div>
</div>
</div>

<!-- footer: "" --> 

---

# Fourier, and the frequency domain

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

Phasors of different frequencies are the building block of the Fourier representation of the signal: we will map signals to a *frequency domain* populated by sinusoids of different frequencies. 

</div>
<div class="column">
<div class="img_row centered" style="margin-top: 25px;">
<img class="ui large centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/series/4x/frequency_domain@4x.png">
</div>
<div class="caption">

Sinusoid signals of different frequencies define a basis in the frequency domain. An interactive visualization can be found [here](https://brianmcfee.net/dstbook-site/content/ch01-signals/Waves.html#id5).

</div>
</div>
</div>

<!-- footer: "" --> 

---
# Fourier, and the coefficients

Having defined a basis, we now need to learn the coefficients $\alpha$. Coefficients ought to measure the presence of a frequency, and its scaling. Thus, $\alpha \neq 0$ for frequencies present in $s$, and $\alpha_j = 0$ for frequencies not present. Inner products, e.g., dot products, satisfy both conditions: the coefficients will be given by the inner product of basis signals and the signal $s$:
$$
\alpha_j = s \cdot \psi_j.
$$

<!-- footer: "" --> 

---

# A small caveat: orthogonality... again?

Signals may be out orthogonally out of phase, thus inducing null products, leading to misses on the basis. To tackle this, we use the orthogonal components of the basis: the $\sin$  component of the phasor!
$$
s_t = \sum_{\rho = 1}^{n} \alpha_\rho (\cos(\theta_{\rho, t}) + i \sin(\theta_{\rho, t}))
$$
<!-- footer: "Remember: by definition, inner product satisfy $a \\cdot b = 0$ for $a, b$ orthogonal!" --> 

---

# Discrete-Time Fourier Transform (DTFT)

Signals may be out orthogonally out of phase, thus inducing null products, leading to misses on the basis. To tackle this, we use the orthogonal components of the basis: the $\sin$  component of the phasor!
$$
s_t = \sum_{\rho = 1}^{n} \alpha_\rho (\cos(\theta_{\rho, t}) + i \sin(\theta_{\rho, t}))
$$

Finally, we leverage Euler, and have
$$
s_j = \sum_{\rho = 1}^{n} \alpha_\rho e^{\theta_{\rho, t}} = \sum_{\rho = 1}^{n} \alpha_\rho e^{-2\pi f_\rho t}
$$

<!-- footer: "Remember: by definition, inner product satisfy $a \\cdot b = 0$ for $a, b$ orthogonal!" --> 

---
# Discrete-Time Fourier Transform


<div class="ui two column doubling stackable grid container bottom">
<div class="column">
<div class="ui segment base pros">

- Quick: $\mathcal{O}(n \log n)$
- Decomposition in separate and different signals

</div>
</div>
<div class="column">
<div class="ui segment base cons"> 

- Decomposition defined exclusively for sinusoidal series
- Decomposition of *periodic* series
- Decomposition exclusively in terms of frequency, not time

</div>
</div>
</div>

<!-- footer: "" --> 

---
# Wavelets

Wavelet tackle several weaknesses of Fourier Transforms.

<div class="ui segment VS">
<div class="ui two column very relaxed grid">
<div class="column">

**Fourier Transform**: $\psi_\kappa$

- Decomposition defined exclusively for sinusoidal series
- Decomposition of *periodic* series
- Decomposition exclusively in terms of frequency, not time

</div>
<div class="column">

**Wavelets**: $\psi_{\kappa, \tau}$

- Flexible decomposition defined by *mother wavelets*
- Decomposition of arbitrary series
- Wavelets parameterized in frequency **and** time

</div>
</div>
<div class="ui vertical divider">
VS
</div>
</div>


---

# Wavelets

Wavelets (little waves) aim to replace sinusoidal phasors, and are both more general, and flexible enough for domain-specific application. A wavelet $\psi_{\kappa, \tau}: \mathbb{R} \rightarrow \mathbb{R}$ is a function s.t.
- $\int_{- \infty}^{+\infty} \psi_{\kappa, \tau}(t) \,dt = 0$ *(zero mean)*
- $\int_{- \infty}^{+\infty} \psi_{\kappa, \tau}(t)^2 \,dt \neq \infty$ *(finite energy)* or *(compact support)*

Finite energy makes it so a wavelet, unlike a sinusoidal function, is bounded: thus, by construction, wavelets **can be localized in time**!

<div class="img_row centered" style="margin-top: 25px;">
<img class="ui small centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/series/SVG/mexican.svg">
<img class="ui small centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/series/SVG/morlet.svg">
<img class="ui small centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/series/SVG/meyer.svg">
</div>
<div class="caption">

Three wavelets: Mexican Hat, Morlet, Meyer.

</div>

---

# Surfing the series with wavelets


<div class="ui two column doubling stackable grid container bottom">
<div class="column">

Localization is innate in wavelets by their own definition. A *mother wavelet* $\psi_{K, T}$ defines a family of *daughter* wavelets defined by
- A frequency $\kappa$: shrink or stretch the daughter wavelet
- A shift $\tau$: pushes or pulls the daughter wavelet across time.

We define a daughter wavelet $\psi_{\kappa, \tau}$ as

$$
\psi_{\kappa, \tau}(t) = \dfrac{1}{\sqrt{\kappa}}\psi(\dfrac{t - \tau}{\kappa}).
$$

</div>
<div class="column">
<div class="img_row centered">
<img style="transform: scale(0.5, 1);" class="ui small centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/series/SVG/mexican.svg">
<img style="transform: scale(0.5, 1); margin-left: 100px;" class="ui small centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/series/SVG/meyer.svg">
</div>

<div class="img_row centered">
<img style="transform: scale(1, 1);" class="ui small centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/series/SVG/mexican.svg">
<img style="transform: scale(1, 1); margin-left: 100px;" class="ui small centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/series/SVG/meyer.svg">
</div>

<div class="img_row centered">
<img style="transform: scale(1.5, 1);" class="ui small centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/series/SVG/mexican.svg">
<img style="transform: scale(1.5, 1); margin-left: 100px;" class="ui small centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/series/SVG/meyer.svg">
</div>

<div class="caption">

Stretched wavelets: Mexican Hat wavelet (left column), and Meyer wavelet (right column).

</div>

</div>
</div>

---

# Wavelets Transforms

Moving from sinuoidal phasors to wavelets is seamless in the formulation
$$
\underbrace{\sum_{\rho = 1}^n \alpha_\rho \psi_\kappa(t)}_{Discrete \text{ } Fourier} \rightarrow \underbrace{\sum_{t = 1}^n \alpha_\rho \psi_{\kappa, \tau}(t)}_{Wavelet \text{ } Transform}.
$$
Wavelets are convoluted across the series, producing a list of coefficients. $\kappa$ and $\tau$ are dyadic, i.e., they are taken as powers of $2$: $\tau = 2^{-i}, \tau = k 2^{-i}$.

---
## From representations to motifs

---

# Time series: motifs 

Motifs tie strongly with subseries extraction for discretization: if representation algorithms extracted to *represent*, and thus describe, motif extraction algorithms instead extract subseries to *represent*, and thus *discriminate*. In other words, a *motif* is a subseries characteristic of a set of series. We can search motifs following the two views:

- descriptive: a motif is a reoccurring subseries in the set $S$
- discriminative: a motif is a reoccurring subseries in the set $S$... and not reoccurring in another set $S^\neq$. Also called a *shapelet*

---

# Searching for Motifs

The first step is already solved! We know how to extract a set of subseries $S_\subset$ from series representation. We need to quantify the descriptive and discriminative power of candidate motifs.


**Descriptive power**. Distance of $s^i_\subset$ with respect to all possible subseries of $s^j$ yields distances $D_{i, S} = \{d^1_{i, j}, \dots, d^{k}_{i, j}\}$. Descriptive power given by lower distances, e.g., $\min D$
**Discriminative power.** Comparison of descriptive power with respect to $S$ and $S^\neq$, e.g.,  $\dfrac{\min D_{i, S}}{\min D_{i, S^\neq}}$

---
# From motifs to shapelets

Since motifs are supposed to discriminate, why not directly measure their discriminative power? Partition subseries in $S \cup S^\neq$ according to their distance from a given candidate $s^i_\subset$ and a threshold $\beta$, obtaining two sets $S^{\leftarrow}_{\beta}, S^{\rightarrow}_{\beta}$. Then, compute a discrimination measure, e.g., entropy, information gain, etc., on the two sets $S^{\leftarrow}_{\beta}, S^{\rightarrow}_{\beta}$. The larger the measure, the higher the discriminative power!

<img class="ui huge centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/series/SVG/shapelet_split.svg">
<div class="caption">

A shapelet (in black), a threshold $\beta$, and the two sets $S^{\leftarrow}_{\beta}, S^{\rightarrow}_{\beta}$ (left and right, in blue and red, respectively).

</div>

--- 
# Time series: alignment

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

An alignment (or matching) $A = [(i, j)]^{\max{ \{ n, m \}}}$ of two time series $l, u$ with components $[l_1, \dots, l_n],$ $[u_1, \dots, u_m]$ is an assignment of each component $l_i$ of $l$ to a component $u_j$ of $u$. An alignment $A$ induces an alignment *cost* $C_A$ quantifying how unaligned the two series are. 


</div>
<div class="column">
<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/series/SVG/straight_match.svg">
<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/series/SVG/dtw.svg">
<div class="caption">

Two possible alignments (in beige) of an *upper* series $s^1$ (in red), and a *lower* series $s^2$ (in blue). The bottom alignment is $A = [(0, 0), (1, 0), (2, 1), (3, 1), (4, 2), (4, 3),$ $(5, 4), (5, 5)]$.

</div>
</div>
</div>

<!-- footer: "We are going to assume equal time sampling for both series." --> 

---
# Alignment: local cost

Alignment costs $C_\cdot$ are based on two separate costs:

- *local* (component-wise, or point-wise) alignment cost $c^A_{i, j}$: defines the cost of aligning $l_i$ with $l_j$. *How much do I pay for this alignment?*
- *match* alignment cost $c^\Sigma_{i, j}$: defines the cost of foregoing matching $i$ with $j$, in favor of a lower-cost $i' \neq i$. *How much would I pay for another alignment?*

Alignment algorithms look to minimize a combined cost of the two.

<!-- footer: "" --> 

---

# Alignment: straight match

<img class="ui large centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/series/SVG/straight_match.svg">
<div class="caption">

A straight match alignment.

</div>

<!-- footer: "" --> 

---
# Alignment: straight match

Trivial alignment: each point $l_i$ is assigned to $l_i$. The alignment induces a pairwise alignment cost of $c^a_{i, i} = \mid\mid l_i - u_i \mid\mid_p$. The alignment cost $C_A$ is given by the sum of the pairwise alignments:
$$C_A = \sum_{i, i} c^a_{i, i} = \sum_{i} \mid\mid l_i - u_i \mid\mid_p.$$
Since $i$ is always aligned with $j$, it follows that $c^\Sigma_{i, j} = 0$. This produces an alignment $A = [(l_i, u_i)]^{K}$, only applicable for $m = n$.

<div class="ui segment inverted highlight">
Applicable to series with the same sampling rate!
</div>

<!-- footer: "" --> 

---

# Alignment: straight match

<img class="ui large centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/series/SVG/straight_match.svg">

<div class="caption">

Two possible alignments of an *upper* series $s^1$, and a *lower* series $s^2$.

</div>


<div class="ui two column doubling stackable grid container bottom">
<div class="column">
<div class="ui segment base pros">

- Simple definition
- Minimizes norm cost
- Quick: $\mathcal{O}(n)$

</div>
</div>
<div class="column">
<div class="ui segment base cons"> 

- Only applicable to equal-length series
- Assumes alignment

</div>
</div>
</div>

<!-- footer: "" --> 

---
# Alignment: Shifted match

Not all time series are already aligned! Given a component $l_i$, we need to *look for* an aligning $u_j$, under a *shift assumption*.

<div class="ui raised segment question">
<p class="question" style="display: inline;">Shifted alignment.</p>


Assuming some subseries of either $l, u$ are shifted, under a shifted alignment:
- **Warp, Replication.** Each component $l_i$ can be assigned to any component $u_j$
- **Planarity.** Assignments are monotonic: a successive point cannot be assigned backwards: $\forall i, j. (l_i, u_j) \in A \implies (l_{i + 1}, u_{j - 1}) \notin A$ 


</div>

<!-- footer: "" --> 

---
# Alignment: Shifted match

If properly performed, a shifted match minimizes norm cost, and emulates a straight alignment... with additional aligned components.

<video style="width: 40%;" controls src="https://rtavenar.github.io/blog/fig/dtw_path.webm">animation</video>
<div class="caption">

A shifted match alignment as a straight match alignment.

</div>

---
# Shifting as Warping

<div class="ui segment inverted highlight">

**Warp, Replication.** Each component $l_i$ can be assigned to any component $u_j$.

</div>

By *warping*, we replicate a component, warping it also further in the series. This allows us to replicate components, and emulate a straight match.

- *no warp*: the assignment $(l_i, u_j)$ is attempted as is
- *lower warp*: the assignment $(l_i, u_j)$ is attempted on $(l_{i + 1}, u_j)$, replicating the component on the lower series $u$
- *upper warp*: the assignment $(l_i, u_j)$ is attempted on $(l_i, u_{j + 1})$, replicating the component on the upper series $v$

---

# Dynamic Time Warping (DTW)

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

DTW divides the alignment problem in two steps:
1. compute a cumulative minimal alignment cost matrix $C^\Sigma$, defining the minimal alignment cost of every pair of components $l_i, u_j$
2. search an alignment $A$ on $C^\Sigma$, minimizing the alignment cost

</div>
<div class="column">
<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/series/SVG/dtw_3_4.svg">

<br>

$$
C^\Sigma
\begin{bmatrix}
0.495& 0.613& 0.429& 0.618  \\
0.524& 0.350& 0.536& 0.885 \\
0.458& 0.214& 0.511& 0.194 \\
\end{bmatrix}
$$


<div class="caption">

A DTW alignment (top), and a cumulative alignment cost matrix $C^\Sigma$ (bottom).
The $(i, j)$ component holds the cumulative cost of aligning the $l_i, u_j$.

</div>
</div>
</div>

<!-- footer: "$\\Sigma$ stands for sum, unlike the alphabet used in SAX representation." --> 

---

# Warping in Dynamic Time Warping

$C^\Sigma$ computes a *minimal* and *cumulative*: $c^\Sigma_{i, j}$ may be $\neq 0$!

- base case: the alignment $(l_1, u_1)$ has minimal cost. This is trivially true, since there are no accumulated costs, i.e., $C^\Sigma_{1, 1} = \mid\mid l_1 - u_1 \mid\mid_p$
- inductive case: $i, j$ fall within the three warping categories, thus it must be one of three cases
  - *(no warp)* $i, j$: the accumulated cost is $c^\Sigma_{i, j} = C^\Sigma_{i - 1, j - 1}$
  - *(lower warp)* $i$ has warped: the accumulated cost is $c^\Sigma_{i, j} = C^\Sigma_{i - 1, j}$
  - *(upper warp)* $j$ has warped: the accumulated cost is $c^\Sigma_{i, j} = C^\Sigma_{i, j - 1}$

<!-- footer: "" --> 

---

# Computing warp cost

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

Entries in $C^\Sigma$ are computed as

$$
\begin{align}
    C^\Sigma_{i, j} &= c^a_{i, j} + c^\Sigma_{i, j}& \\
    &= \underbrace{\mid\mid l_i - u_j \mid\mid_p}_{alignment \text{ } cost} + \min \{
        \underbrace{C^\Sigma_{i - 1, j - 1}}_{no \text{ } warp},
        \underbrace{C^\Sigma_{i, j - 1}}_{lower \text{ } warp},
        \underbrace{C^\Sigma_{i - 1, j}}_{upper \text{ } warp}
    \} \\
\end{align}
$$


</div>
<div class="column">


$$
C^\Sigma
\begin{bmatrix}
0.495& 0.613& 0.429& 0.618  \\
0.524& 0.350& 0.536& 0.885 \\
0.458& 0.214& 0.511& 0.194 \\
\end{bmatrix}
$$

$$
C^\leftarrow =
\begin{bmatrix}
- & \leftarrow & \leftarrow & \leftarrow \\
\uparrow & \nwarrow & \uparrow & \leftarrow \\
\uparrow & \uparrow & \leftarrow & \leftarrow
\end{bmatrix}
$$

<div class="caption">

Directions of minimal accumulated cost $C^\leftarrow$ over $C^\Sigma$: entries indicate which alignment choice has produced the minimal cost.

</div>

</div>
</div>


---

# Searching for the lowest cost alignment

As a matrix of minimal accumulated alignment cost, we know that for each component $i, j$ in $C^\Sigma$, we have, by construction, the minimal cost to align up to $i, j$.
Thus, we can simply start from the last alignment, and follow $C^\leftarrow$ backwards for the warps of minimal cost!

$$
C^\leftarrow =
\begin{bmatrix}
\textcolor{red}{-} & \leftarrow & \leftarrow & \leftarrow \\
\uparrow & \textcolor{red}{\nwarrow} & \uparrow & \leftarrow \\
\uparrow & \textcolor{red}{\uparrow} & \textcolor{red}{\leftarrow} & \textcolor{red}{\leftarrow}
\end{bmatrix},

A = [(1, 1), (2, 2), (3, 2), (3, 3), (3, 4)]
$$

<div class="caption">

Directions of minimal accumulated cost $C^\leftarrow$ over $C^\Sigma$: the red path from the last entry indicates induces the alignment of minimal cost. The alignment $A$ is given by the indices of the path.

</div>

---

# Dynamic Time Warping

<img class="ui medium centered image" src="https://cdn.jsdelivr.net/gh/msetzu/marpee@latest/assets/imgs/series/SVG/dtw.svg">
<div class="caption">

A Dynamic Time Warping alignment.

</div>

<div class="ui two column doubling stackable grid container bottom">
<div class="column">
<div class="ui segment base pros">

- Minimizes norm cost on shifted series

</div>
</div>
<div class="column">
<div class="ui segment base cons"> 

- High cost of $\mathcal{O}(m n)$

</div>
</div>
</div>

---
# Constraining alignments

Within $C^\Sigma$, we have several possible movements:
- alongside a row ($i$ is constant): indicate a sequence of upper warps, as we are aligning one component of $l$ with consecutive components of $u$
- alongside a column ($j$ is constant): indicate a sequence of lower warps, as we are aligning one component of $u$ with consecutive components of $l$
- diagonally (neither $i$ nor $j$ is constant): indicate a no-warp alignment

---

# Sakoe-Chiba search

The optimal search we have highlighted can move almost arbitrarily over $C^\Sigma$, inducing arbitrarily large row- and column-segments, and thus arbitrarily large warps.
Sakoe-Chiba search instead constraints the alignment $A$ to be such that $\forall i, j \in A. \mid i - j \mid < \gamma$ by introducing a search radius $\gamma$, and binding the maximum warp size of either series.

<video style="width: 25%;" controls src="https://rtavenar.github.io/blog/fig/sakoechiba_matrices.webm">animation</video>

---

# Itakura parallelogram

The Itakura constraint instead binds the slope of segments, effectively binding consecutive warps.
For any two $(i, j), (k, l) \in A. k \geq i, l \geq j. \frac{l - j}{k - i} < \alpha$.

<video style="width: 25%;" controls src="https://rtavenar.github.io/blog/fig/itakura_matrices.webm">animation</video>


---

## From alignment to similarity

---

# Time series: similarity

| Similarity           | Similar if...                | Measure              | Sensitive to     |
| -------------------- | ---------------------------- | -------------------- | ---------------- |
| Straight match       | Similar values               | Norm (Euclidean)     | Time shifts      |
| Dynamic Time Warping | Similar (interleaved) shapes | Norm                 |                  |
| Autocovariance       | Seasonal                     | Inner product        | Amplitude shifts |
| Statistical          | Similar statistics           | Mean, Variance, etc. |                  |

---
# References

<style scoped>
table * {
font-size: 0.9em !important;
}
</style>

| Topic                  | Reference                                                                                                       |
| ---------------------- | --------------------------------------------------------------------------------------------------------------- |
| Fourier Transform      | [Digital Signals Theory e-book](https://brianmcfee.net/dstbook-site/content/intro.html), Chapters 1, 2, 4, 5, 9 |
| Wavelet Transform      | Data-driven science and engineering. By S. L. Brunton, J. N. Kutz, 2nd edition. 2.5                             |
| Shapelets              | [Time series shapelets: a new primitive for data mining](https://dl.acm.org/doi/10.1145/1557019.1557122)        |
| Dynamic Time Warping   | [An introduction to Dynamic Time Warping](https://rtavenar.github.io/blog/dtw.html)                             |

Credits for some images and animations to [Romain Tavenard](https://rtavenar.github.io).