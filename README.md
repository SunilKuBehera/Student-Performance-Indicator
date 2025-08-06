# Student Performance Indicator

## Table of Contents
- [Project Overview](#project-overview)
- [Problem Statement](#problem-statement)
- [Project Structure](#project-structure)
- [Dataset](#dataset)
- [Workflow](#workflow)
- [Key Insights from EDA](#key-insights-from-eda)
- [Setup and Installation](#setup-and-installation)
- [How to Use](#how-to-use)

## Project Overview
This project follows the complete lifecycle of a data science project, from data collection and exploratory data analysis to model training and evaluation. The goal is to understand the factors influencing student test scores and build a predictive model to estimate student performance.

## Problem Statement
The primary objective of this project is to analyze how various factors affect student performance in tests. The key variables considered are:
- Gender
- Race/Ethnicity
- Parental level of education
- Lunch type
- Test preparation course completion

The project aims to build a regression model to predict a student's average score based on these factors.

## Project Structure
The project is organized into the following structure:

```
student-performance-indicator/
├── data/
│   └── Student.csv
├── notebooks/
│   ├── 1. Data_Analysis.ipynb
│   └── 2. Model_training.ipynb
├── requirements.txt
└── README.md
```

- **`data/`**: Contains the dataset used for the project.
  - `Student.csv`: The raw dataset with student information and scores.
- **`notebooks/`**: Contains the Jupyter notebooks detailing the project workflow.
  - `1. Data_Analysis.ipynb`: This notebook covers data loading, cleaning, preprocessing, and exploratory data analysis (EDA).
  - `2. Model_training.ipynb`: This notebook focuses on feature engineering, model training, evaluation, and selecting the best predictive model.
- **`requirements.txt`**: A list of Python libraries required to run the project.
- **`README.md`**: This document, providing an overview of the project.

## Dataset
The dataset `data/Student.csv` contains information about students, including their demographics, parental background, and scores in Math, Reading, and Writing.

**Key Features:**
*   **gender**: Sex of the student (Male/Female).
*   **race_ethnicity**: Ethnicity of the student (Group A, B, C, D, E).
*   **parental_level_of_education**: The highest level of education attained by the parents.
*   **lunch**: Type of lunch the student receives (standard or free/reduced).
*   **test_preparation_course**: Whether the student completed a test preparation course.
*   **math_score**: Score in the math test.
*   **reading_score**: Score in the reading test.
*   **writing_score**: Score in the writing test.

## Workflow
The project is divided into two main parts, each corresponding to a Jupyter notebook.

### 1. Data Analysis and EDA (`1. Data_Analysis.ipynb`)
This notebook focuses on understanding and preparing the data.
1.  **Data Loading & Initial Exploration**: The dataset is loaded, and initial checks like `head()`, `shape`, `info()`, and `describe()` are performed to get a feel for the data.
2.  **Data Cleaning**:
    *   Unnecessary columns are dropped.
    *   Columns are renamed for better readability and consistency.
    *   Missing values are identified and imputed using appropriate strategies (mean for numerical, mode for categorical).
    *   Duplicate records are removed.
3.  **Feature Engineering**: New features like `total score` and `average` are created from existing score columns to provide a holistic view of student performance.
4.  **Exploratory Data Analysis (EDA)**:
    *   Univariate and bivariate analyses are conducted to uncover relationships between different features and the students' scores.
    *   Visualizations like histograms, pie charts, and violin plots are used to illustrate the distribution of data and the impact of various factors on performance.

### 2. Model Training & Evaluation (`2. Model_training.ipynb`)
This notebook builds upon the cleaned data to create a predictive model.
1.  **Data Preprocessing**: Categorical features are converted into a numerical format using one-hot encoding, and numerical features are scaled to bring them to a similar range.
2.  **Train-Test Split**: The dataset is split into training and testing sets to evaluate the model's performance on unseen data.
3.  **Model Training**: Several regression models (e.g., Linear Regression, Ridge, Lasso, ElasticNet) are trained on the training data to predict the average score.
4.  **Model Evaluation**: The performance of each model is evaluated using metrics like R-squared, Mean Absolute Error (MAE), and Root Mean Squared Error (RMSE).
5.  **Model Selection**: The best-performing model is selected based on the evaluation metrics.

## Key Insights from EDA
- **Gender**: On average, `female` students have a better `overall score`, while `male` students tend to score `higher in Math`.
- **Lunch**: Students with a `standard` lunch perform better in exams compared to those with a `free/reduced` lunch. This holds true for both male and female students.
- **Parental Education**: There is a noticeable positive correlation between the `parental level of education` and `student scores`. Students whose parents have a `master's` or `bachelor's` degree tend to perform better.
- **Race/Ethnicity**: Students from ethnic `groups A` and `group B` tend to perform poorly compared to other groups.