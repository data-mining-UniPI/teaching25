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

# Data Mining
*309AA*

---

<!-- paginate: true -->

# Data Mining

<div class="ui raised segment question">
<p class="question" style="display: inline;">Data Mining</p>

Discipline that studies the efficient extraction and analysis of information and patterns in large data collections, finally inducing information from data.

</div>

---

# Large data collections

Large collections tend are heterogeneous in...

- Source, i.e., they often gather different data sources, e.g., data from different labs, e-commerce websites, different cities/states, etc.
- Domain: scientific data, transactional data (e-commerce), traffic data, social networks, sensor data, etc.
- Language: different conventions, scales, encodings, etc.
- Refinement: often data is raw, unprocessed, or noisy

These separate data collections from datasets!

---

# Large data collections

Before we even think of analyzing and extract patterns from such data, we must store it. The first step of Data Mining is data storage and warehousing.

<img src="1.png" class="ui image medium">
<div class="caption">

Data mining pipeline, step 1.

</div>

---

# Large data collections

Simple storage does not tackle the source heterogeneity, thus we need to properly clean and integrate data. This tackles heterogeneity in language and refinement.

<img src="2.png" class="ui image large"/>
<div class="caption">

Data mining pipeline, step 1 and 2.

</div>

---

# Large data collections... after data gathering, cleaning and integration

- Sources are integrated
- Language is homogeneous: same conventions, scales, and encodings
- Refinement: data is clear of noise and outliers, and can be analyzed

---

# Information and patterns... for what?

Meant with a precise and technical connotation in other disciplines, e.g., compression, here they assume a broader meaning. 

<div class="ui raised segment question">
<p class="question" style="display: inline;">Data Mining</p>

Discipline that studies the efficient extraction and analysis of information and patterns in large data collections, finally inducing information from data.

</div>

Information... for what? For whom?

---

# Information as insight

Rather than simply find numerical regularities, in data mining we look to also find useful and interesting **patterns which can aid a human's understanding of the domain**, and to **gather insight**.

Rather than solving a given task, we look to answer questions, e.g.,
- Are there some common patterns in the data?
- Are there some anomalies?
- Are there data groups with different behaviors?

---

# Information as insight

Insight allows a human to make decisions, e.g., 

- Are there some common patterns in the data? Then maybe my heterogeneous sources are observing a common phenomenon: study said phenomenon
- Are there some anomalies? Then maybe there is a problem with my data, or I've found something new: check my data sources
- Are there data groups with different behaviors? Then I may want to study them separately

---

# Information as insight

It's January 2020, and you are analyzing health records, e.g., hospital reports, data from Pisa, Frankfurt, and Wuhan.

- Are there some common patterns in the data? You find a shared influx of new patient with respiratory diseases
- Are there some anomalies? A small set of such patients does not exhibit any common predisposing conditions
- Are there data groups with different behaviors? A group responds well to known treatment, another does not, another worsens

---

# Information as insight

Information is extracted from filtered data from which patterns are extracted. This enables the human to prompt a loop in the pipeline. Not all patterns are equally useful, thus a pattern evaluation step is required.

<img src="3.png" class="ui image massive centered"/>
<div class="caption">

Data mining pipeline, steps 1 through 4.

</div>

---

# Thought exercise

You are given a cycling data collection, with data gathered from different sources, covering all tours of thousands of cyclists from 2018 to 2024.

<div class="ui two column doubling stackable grid container bottom">
<div class="column">

**Sources**
- A social network for competitive non-professional cyclists
- A training platform for professional cyclists
- A social network for non-competitive, non-professional cyclist that cycle to explore nature

</div>
<div class="column">

**Features**
 - Speed
 - Cadence
 - Bike used
 - Track, e.g., length, elevation, climbs
 - Info on the cyclist, e.g., age

</div>
</div>

---

# Steps 1 and 2: data cleaning and integration

In data cleaning and integration, we look to find...

| Looking for...                        | Action                                        |
| ------------------------------------- | --------------------------------------------- |
| Missing values                        | Impute them, or drop the feature              |
| Out of range values                   | Standardize the sources, or drop them         |
| Different data scales                 | Standardize them                              |
| Non-informative or redundant features | Drop them                                     |
| Data semantics                        | Understand distributions and general patterns |

---

# Steps 1 and 2: data cleaning and integration


| Looking for...                        | Action                                                              | Insight?                                           |
| ------------------------------------- | ------------------------------------------------------------------- | -------------------------------------------------- |
| Missing values                        | Analyze missing values                                              | Malfunctioning sensors                             |
| Out of range values                   | Standardize the sources                                             | Professionists are much faster, but e-bikes exists |
| Different data scales                 | Miles and kilometers conversion, and adjustment for different bikes | Bikes do not really impact performance as much     |
| Non-informative or redundant features | Drop them                                                           |                                                    |
| Data semantics                        | Understand distributions and general patterns                       | Little improvement over time for amateurs          |

---

# Steps 3: data selection and transformation

Not all data is useful to extract any patterns, and must be processed accordingly.

| Looking to...           | Action                                           |
| ----------------------- | ------------------------------------------------ |
| Find anomalous data     | Remove from the analysis, or  analyze separately |
| Aggregate data          | Extract higher-level patterns                    |
| Generate novel features | Study specific phenomena                         |

---

# Steps 3: data selection and transformation

Not all data is useful to extract any patterns, and must be processed accordingly.

| Looking to...           | Action                             | Insight                                                                                     |
| ----------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------- |
| Find anomalous data     | Run an anomaly detection algorithm | Exceptional cyclists follow a steeper improvement curve                                     |
| Aggregate data          | Group by occupation and source     | Non-professional cyclists reach a performance plateau much later                            |
| Generate novel features | Create a climb difficulty index    | Tracks with lots of continuous climbing reduce performance between male and female cyclists |

---

# Steps 4 and 5: pattern extraction and evaluation

What patterns are we trying to extract?

| Looking to extract... | Patterns |
| --------------------- | -------- |
| Profiles of cyclists  | Clusters |
| Descriptive rules     | Rules    |

---

# Steps 4 and 5: pattern extraction and evaluation

**Clusters**

- Profile 1: Cyclists very good in flat terrain
- Profile 2: Cyclists very good in mountainous terrain
- Profile 3: Cyclists jack of all trades, not excelling in anything in particular

---

# Steps 4 and 5: pattern extraction and evaluation

**Rules**

```
Slim and short cyclists -> Good on mountains
Heavy, burly cyclists -> Good on flat terrains
```

---

# Summing up: data mining tasks

| Task                                      | Goal                                 |
| ----------------------------------------- | ------------------------------------ |
| Distributional and correlational analysis | Understand data behavior             |
| Outlier detection                         | Find anomalous data                  |
| Rule mining                               | Finding rule-like patterns           |
| Clustering                                | Find profiles and groups within data |
| Modeling                                  | Predict on future data               |
