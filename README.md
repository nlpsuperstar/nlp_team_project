# Predicting Coding Language - Classification Project


### Table of Contents
---

I.   [Project Overview             ](#i-project-overview)
1.   [Description                  ](#1-description)
2.   [Deliverables                 ](#2-deliverables)

II.  [Project Summary              ](#ii-project-summary)
1.   [Goals                        ](#1-goals)
2.   [Initial Thoughts & Hypothesis](#2-initial-thoughts--hypothesis)
3.   [Findings & Next Phase        ](#3-findings--next-phase)

III. [Data Context                 ](#iii-data-context)
1.   [Database Relationships       ](#1-database-relationships)
2.   [Data Dictionary              ](#2-data-dictionary)

IV.  [Process                      ](#iv-process)
1.   [Project Planning             ](#1-project-planning)
2.   [Data Acquisition             ](#2-data-acquisition)
3.   [Data Preparation             ](#3-data-preparation)
4.   [Data Exploration             ](#4-data-exploration)
5.   [Modeling & Evaluation        ](#5-modeling--evaluation)
6.   [Product Delivery             ](#6-product-delivery)

V.   [Modules                      ](#v-modules)

VI.  [Project Reproduction         ](#vi-project-reproduction)



### I. Project Overview
---

#### 1. Description

For this project, we scraped data from GitHub repository README files. Our goal was to build a model that can predict what programming language a repository is, given the text of the README file.

#### 2. Deliverables

- A well-documented jupyter notebook that contains your analysis
- One or two google slides suitable for a general audience that summarize your findings. Include a well-labelled visualization in your slides.

### II. Project Summary
---

#### 1. Goals

Our goal was to build a model that can predict what programming language a repository is, given the text of the README file. Our data was acquired by scraping the starred repos on GitHub. We brought in 506 observations and based on the distribution of the languages, we decided to see if we can predict if the main language of the repositories was JavaScript or not.

#### 2. Initial Thoughts & Hypothesis

We knew JavaScript is one of the most popular programming languages used for a variety of web applications, mobile and desktop applications, to web games. We initially thought any projects relating to web development would be good indicators of using JavaScript.


#### 3. Findings & Next Phase

Using Natural Language Processing techniques such as stemming, lemmatization, sentiment analysis and word distributions amongst the different languages, we were able to analyze and compare repositories written in JavaScript to those not written in JavaScript. Through our analysis, we found the most frequently used words used by repositories written in JavaSript versus those not written in JavaScript, most frequently used bigrams, created word clouds, as well as sentiment analysis.

With a baseline of ~60.5%, we were able to create machine learning models that were able to successfuly predict whether or not a repository was written in JavaScript or not with an accuracy of 77.78%. The features given to our models were the clean, stemmed and lemmatized versions of our data, and our top performing model was Mulinomial Naive Bayes model.

### III. Data Context
---

#### 1. Data Acquired

All of our data was acquired through web scraping off of GitHub website. We chose to scrape from the top "starred" repositories as we felt they would be the most complete and comprehensive. We chose not to pick from a list based on a topic since we felt there would be an unequal representation of programming languages based on the goal of the projects.

#### 2. Data Dictionary

DataFrames used in this project contain the following variables. 

| Variable               | Definition                                         | Data Type  |
|:----------------------:|:--------------------------------------------------:|:----------:|
| repo                   | github repository url                              | object     |
| language               | programming language of the repository             | object     |
| clean                  | "cleanned" versions of the readme contents         | object     |
| stemmed                | "stemmed" versions of the readme contents          | object     |
| lemmatized             | "lemmatized" versions of the readme contents       | object     |
| message_length         | length of clean readme content character           | int64      |
| word_count             | count of clean readme content words                | int64      |
| avg_word_length        | message length/word count                          | float64    |
| is_javascript *        | boolean for if the repository is in javascript     | bool       |
| sentiment              | sentiment analysis applied to clean readme contents| float64    |


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  * Target variable

### IV. Process
---

#### 1. Project Planning
🟢 **Plan** ➜ ☐ _Acquire_ ➜ ☐ _Prepare_ ➜ ☐ _Explore_ ➜ ☐ _Model_ ➜ ☐ _Deliver_

- [x] Build this README containing:
    - Project overview
    - Initial thoughts and hypotheses
    - Project summary
    - Instructions to reproduce
- [x] Plan stages of project and consider needs versus desires

#### 2. Data Acquisition
✓ _Plan_ ➜ 🟢 **Acquire** ➜ ☐ _Prepare_ ➜ ☐ _Explore_ ➜ ☐ _Model_ ➜ ☐ _Deliver_

- [x] Find a list of repositories on Github
- [x] Build dataset from scraping a list of "most starred" repositories on GitHub
- [x] Make sure the dataset includes at least 100 repositories

#### 3. Data Preparation
✓ _Plan_ ➜ ✓ _Acquire_ ➜ 🟢 **Prepare** ➜ ☐ _Explore_ ➜ ☐ _Model_ ➜ ☐ _Deliver_

- [x] Address missing or inappropriate values, including outliers
- [x] Plot distribution of languages
- [x] Encode "clean", "stemmed", "lemmatized" and "sentiment" columns
- [x] Create target variable column "is_javascript"
- [x] Consider and create new features as needed
- [x] Split data into `train`, and `test`

#### 4. Data Exploration
✓ _Plan_ ➜ ✓ _Acquire_ ➜ ✓ _Prepare_ ➜ 🟢 **Explore** ➜ ☐ _Model_ ➜ ☐ _Deliver_

- [x] Explore value_counts of repos for each language
- [x] Create dataframes for each language to visualize word coutns
- [x] Visualize the most frequently used word counts for JavaScript and Non JavaScript repos
- [x] Visualize the most frequentlu used bigrams for JavaScript and Non JavaScript repos
- [x] Create WordClouds for JavaScript and Non JavaScript repos
- [x] Plot relationships between word count and word length amongst repo languages
- [x] Vizualie sentiment values amongst languages

#### 5. Modeling & Evaluation
✓ _Plan_ ➜ ✓ _Acquire_ ➜ ✓ _Prepare_ ➜ ✓ _Explore_ ➜ 🟢 **Model** ➜ ☐ _Deliver_

- [x] Establish baseline prediction
- [x] Create, fit, and predict with models
- [x] Evaluate models with out-of-sample data
- [x] Utilize best performing model on `test` data
- [x] Summarize findings

#### 6. Product Delivery
✓ _Plan_ ➜ ✓ _Acquire_ ➜ ✓ _Prepare_ ➜ ✓ _Explore_ ➜ ✓ _Model_ ➜ 🟢 **Deliver**
- [x] Prepare Jupyter Notebook of project details through data science pipeline
    - Python code clearly commented when necessary
    - Sufficiently utilize markdown
    - Appropriately title notebook and sections
- [x] With additional time, continue with exploration beyond MVP
- [x] Proof read and complete README and project repository

### V. Modules
---

The created modules used in this project below contain full comments an docstrings to better understand their operation. Where applicable, all functions used `random_state=19` at all times. Use of functions requires access credentials to the Codeup database and an additional module named `env.py`. See project reproduction for more detail.

- [`acquire`](https://github.com/nlpsuperstar/nlp_team_project/blob/master/acquire.py): contains functions to web scrape the data off of GitHub. We've also included the list of repositories we decided to use for our particular project.
- [`prepare`](https://github.com/nlpsuperstar/nlp_team_project/blob/master/prepare.py): contains functions used to prepare readme contents for NLP analysis.
- [`modeling`  ](https://github.com/nlpsuperstar/nlp_team_project/blob/master/modeling.py): contains functions to create, test models and visualize their performance.

### VI. Project Reproduction
---

To recreate and reproduce results of this project, you will need a GitHub account, obtain your own GitHub token, and store it in an env.py file. You will also need all of the modules listed above to either webscrape a new list of repositories, or use our existing list, "REPOS", contained in the acquire.py script.