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

This project serves to use clustering and linear regression methodologies to find drivers for `log_error` in *single-unit properties* sold in 2017 in the `zillow` database.

#### 2. Deliverables

- GitHub repository and [README](#finding-drivers-of-zestimate-errors) stating project overview, goals, findings, and summary
- Jupyter [Notebook](https://nbviewer.jupyter.org/github/ray-zapata/project_clustering_zillow/blob/main/zestimate_error_report.ipynb) showing high-level view of process through data science pipeline
    - See the [`exploration.ipynb`](https://nbviewer.jupyter.org/github/ray-zapata/project_clustering_zillow/blob/main/exploration.ipynb) notebook for a more detailed view through the exploration process
    - See the [`modeling.ipynb`](https://nbviewer.jupyter.org/github/ray-zapata/project_clustering_zillow/blob/main/modeling.ipynb) notebook for a more detailed look into the twelve models created
- Python module(s) to automate the data acquisition and preparation process


### II. Project Summary
---

#### 1. Goals

The primary focus of the project was to set out and discover potential drivers of the log_error of the Zillow® Zestimate for single-unit properties sold during 2017. In this context, log_error is equal to 𝑙𝑜𝑔(𝑍𝑒𝑠𝑡𝑖𝑚𝑎𝑡𝑒) − 𝑙𝑜𝑔(𝑆𝑎𝑙𝑒𝑃𝑟𝑖𝑐𝑒). After sufficient exploration, these potential drivers would be used as features in predicting the log_error with linear regression algorithms. In attempt to find these drivers, clustering methodologies were used to explore any meaningful groups that are present in the data.

#### 2. Initial Thoughts & Hypothesis

It was initially suspected that a significant factor in `log_error` deviating from zero would be due to the under- or over-estimation of property value based on property's physical location. All observations carried through preparation had several methods for location testing, including census precincts and latitudinal & longitudinal geographic coordinates. This would be the initial hypothesis, that property location, when appropriately segmented into geographic of sociological divisions, would have a strong correlation to `log_error`.

#### 3. Findings & Next Phase

Using clustering and linear regression machine learning methodologies, it was discovered there may be some potential standing to the initial hypothesis. Several clusters were formed, two of which utilized location-based features, and these clusters would be recommended by feature selection algorithms for model predictions. While not a significant increase, the best performing model on out-of-sample data was carried into final testing on the 20% `test` data set where it just barely edged out the root mean squared error of the baseline created using the mean of `log_error`. Given the shape of the plotted residuals and the abysmally low percentage change in RMSE from model to baseline mean, it is unlikely this produced any insights of value. There is much more work to be done in understanding the question of what is driving the Zestimate errors.

Due to the scope and time frame of this project, it was not attempted to go into a more exhaustive exploration of location features in finding the drivers sought. With additional time and resources, it is desirable to attempt to use either paid or open-source geocoding tools and methodologies in obtaining more precise locations of properties and the neighborhoods, zip codes, and street blocks in which the exist. In future ventures regarding drivers of `logerror`, it would also be desirable to test for finding drivers which are more likely to result in specifically either over or under estimation of property value.

### III. Data Context
---

#### 1. Database Relationships

The Codeup `zillow` SQL database contains twelve tables, nine of which have foreign key links with our primary table `properties_2017`: `airconditioningtype`, `architecturalstyletype`, `buildingclasstype`, `heatingorsystemtype`, `predictions_2017`, `propertylandusetype`, `storytype`, `typeconstructiontype`, and `unique_properties`. Each table is connected by a pointed arrow with the corresponding foreign keys that link them. Many of these tables are unused in this project due to missing values, and this database map serves only to define the database.



#### 2. Data Dictionary

Following acquisition and preparation of the initial SQL database, the DataFrames used in this project contain the following variables. Contained values are defined along with their respective data types.

| Variable               | Definition                                         | Data Type  |
|:----------------------:|:--------------------------------------------------:|:----------:|
| acreage                | conversion of lot_square_feet into acres           | float64    |
| age                    | age of property as of 2017                         | int64      |
| bathrooms              | count of full- and half-bathrooms                  | float64    |
| bed_sqft_age_clstr_#   | boolean for five clusters of bed_sqft_age          | uint8      |
| bedrooms               | count of bedrooms                                  | int64      |
| bedrooms_per_sqft      | ratio of bedrooms to structure_square_feet         | float64    |
| census_tractcode       | US census tract codes for non-precise location     | float64    |
| full_bathrooms         | count of only full-bathrooms                       | int64      |
| la_county              | boolean for if county is within Los Angeles County | int64      |
| land_value_usd         | value of land in U.S. dollars                      | float64    |
| lat_long_clstr_#       | boolean for five clusters of lat_long              | uint8      |
| latitude               | latitudinal geographic coordinate of property      | float64    |
| log_error *            | difference of log(Zestimate) and log(SalePrice)    | float64    |
| longitude              | longitudinal geographic coordinate of property     | float64    |
| lot_rooms_clstr_#      | boolean for five clusters of lot_rooms             | uint8      |
| lot_square_feet        | size of lot(land) in square feet                   | float64    |
| orange_county          | boolean for if county is within Orange County      | int64      |
| parcel_id              | unique identifier of property                      | int64      |
| property_id            | unique identifier of property                      | int64      |
| property_value_usd     | value of property in entirety in U.S. dollars      | float64    |
| room_count             | count of bedrooms and full- and half-bathrooms     | float64    |
| structure_square_feet  | dimensions of structure on property in square feet | float64    |
| structure_value_usd    | value of structure on property in U.S. dollars     | float64    |
| tax_amount_usd         | most recent tax payment from property owner        | float64    |
| tract_size_age_clstr_# | boolean for five clusters of tract_size_age        | uint8      |
| transaction_date       | most recent date of property sale                  | datetime64 |
| year_built             | year structure was originally built                | int64      |

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

- [x] Obtain initial data and understand its structure
    - Obtain data from Codeup database with appropriate SQL query
- [x] Remedy any inconsistencies, duplicates, or structural problems within data
- [x] Perform data summation

#### 3. Data Preparation
✓ _Plan_ ➜ ✓ _Acquire_ ➜ 🟢 **Prepare** ➜ ☐ _Explore_ ➜ ☐ _Model_ ➜ ☐ _Deliver_

- [x] Address missing or inappropriate values, including outliers
- [x] Plot distributions of variables
- [x] Encode categorical variables
- [x] Consider and create new features as needed
- [x] Split data into `train`, `validate`, and `test`

#### 4. Data Exploration
✓ _Plan_ ➜ ✓ _Acquire_ ➜ ✓ _Prepare_ ➜ 🟢 **Explore** ➜ ☐ _Model_ ➜ ☐ _Deliver_

- [x] Visualize relationships of variables
- [x] Formulate hypotheses
- [x] Use clustering methodology in exploration of data
    - Perform statistical testing and visualization
    - Use at least 3 combinations of features
    - Document takeaways of each clustering venture
    - Create new features with clusters if applicable
- [x] Perform statistical tests
- [x] Decide upon features and models to be used

#### 5. Modeling & Evaluation
✓ _Plan_ ➜ ✓ _Acquire_ ➜ ✓ _Prepare_ ➜ ✓ _Explore_ ➜ 🟢 **Model** ➜ ☐ _Deliver_

- [x] Establish baseline prediction
- [x] Create, fit, and predict with models
    - Create at least four different models
    - Use different configurations of algorithms, hyper parameters, and/or features
- [x] Evaluate models with out-of-sample data
- [x] Utilize best performing model on `test` data
- [x] Summarize, visualize, and interpret findings

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

- [`acquire`](https://raw.githubusercontent.com/ray-zapata/project_clustering_zillow/main/acquire.py): contains functions used in initial data acquisition leading into the prepare phase
- [`prepare`](https://raw.githubusercontent.com/ray-zapata/project_clustering_zillow/main/prepare.py): contains functions used to prepare data for exploration and visualization
- [`explore`](https://raw.githubusercontent.com/ray-zapata/project_clustering_zillow/main/explore.py): contains functions to visualize the prepared data and estimate the best drivers of property value
- [`wrangle`](https://raw.githubusercontent.com/ray-zapata/project_clustering_zillow/main/wrangle.py): contains functions to prepare data in the manner needed for specific project needs
- [`model`  ](https://raw.githubusercontent.com/ray-zapata/project_clustering_zillow/main/model.py): contains functions to create, test models and visualize their performance

### VI. Project Reproduction
---

To recreate and reproduce results of this project, you will need to create a module named `env.py`. This file will need to contain login credentials for the Codeup database server stored in their respective variables named `host`, `username`, and `password`. You will also need to create the following function within. This is used in all functions that acquire data from the SQL server to create the URL for connecting. `db_name` needs to be passed as a string that matches exactly with the name of a database on the server.

After its creation, ensure this file is not uploaded or leaked by ensuring git does not interact with it. When using any function housed in the created modules above, ensure full reading of comments and docstrings to understand its proper use and passed arguments or parameters.

[[Return to Top]](#finding-drivers-of-zestimate-errors)
