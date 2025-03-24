# tjml-q1project

# Crash Severity Prediction

## Project Overview
- **Dataset**: "Crash Data" from [data.gov](https://catalog.data.gov/dataset/crash-data) with 24,241 instances and 42 attributes.
- **Goal**: Classify crash severity based on conditions like weather, road features, and vehicle types.
- **Process**: 
  - Preprocessing (data cleaning, feature engineering)
  - Attribute selection (e.g., CorrelationAttributeEval, ReliefF)
  - Classifier models (e.g., Naive Bayes, RandomForest)

## Files
- `main.py`: Python script for initial data preprocessing (cleaning, creating a `class` column, and saving to `new_dataset.csv`).
- `cpd-crash-incidents.csv`: Original dataset (not included, download from the link above).
- `finals.csv`: Preprocessed dataset output from applying WEKA preprocessing to `new_dataset.csv`.

## How to Run
1. Download the dataset from [data.gov](https://catalog.data.gov/dataset/crash-data).
2. Place `cpd-crash-incidents.csv` in the same directory as `main.py`.
3. Run the script:
   ```bash
   python main.py
4. Follow WEKA instructions in the report
