# tjml-q1project

# Crash Severity Prediction

This repository contains a machine learning project to predict crash severity (crash, injury, or fatalities) using the "Crash Data" dataset from the Town of Cary, North Carolina. The project was completed as part of Dr. Yilmaz's Period 5 Machine Learning class by Gabriel Xu and Andrew Chen.

## Project Overview
- **Dataset**: "Crash Data" from [data.gov](https://catalog.data.gov/dataset/crash-data) with 24,241 instances and 42 attributes.
- **Goal**: Classify crash severity based on conditions like weather, road features, and vehicle types.
- **Process**: 
  - Preprocessing (data cleaning, feature engineering)
  - Attribute selection (e.g., CorrelationAttributeEval, ReliefF)
  - Classifier models (e.g., Naive Bayes, RandomForest)
- **Best Model**: CfsSubsetEval with Naive Bayes (85.05% accuracy, balanced F-measure).

## Files
- `main.py`: Python script for initial data preprocessing (cleaning, creating a `class` column, and saving to `new_dataset.csv`).
- `cpd-crash-incidents.csv`: Original dataset (not included, download from the link above).
- `new_dataset.csv`: Preprocessed dataset output from `main.py`.
- `README.md`: This file.

## How to Run
1. Download the dataset from [data.gov](https://catalog.data.gov/dataset/crash-data).
2. Place `cpd-crash-incidents.csv` in the same directory as `main.py`.
3. Run the script:
   ```bash
   python main.py
