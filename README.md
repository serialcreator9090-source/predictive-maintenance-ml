# Predictive Maintenance & Machine Failure Diagnosis

A machine-learning project that analyses machine operating conditions to estimate machine failure risk, with an interactive Streamlit dashboard.

## Overview

Unexpected machine failures can cause downtime and maintenance costs. This project explores how machine sensor measurements can be used to classify potential failures using machine-learning models.

## Dataset

This project uses the **AI4I 2020 Predictive Maintenance Dataset**, a synthetic benchmark dataset.

The input features used by the dashboard are:

- Air temperature (K)
- Process temperature (K)
- Rotational speed (rpm)
- Torque (Nm)
- Tool wear (min)

The target is whether a machine failure occurs.

## Project Workflow

1. Explored the dataset using Pandas, Matplotlib and Seaborn.
2. Examined data quality, class imbalance, feature distributions and correlations.
3. Compared Logistic Regression, Decision Tree and Random Forest classifiers.
4. Evaluated models using precision, recall, F1-score, confusion matrix and average precision.
5. Investigated classification-threshold tuning to balance failure detection and false alarms.
6. Saved the trained model using Joblib.
7. Built an interactive dashboard using Streamlit.

## Technologies Used

- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook

## Run the Dashboard

### 1. Clone the repository

```bash
git clone https://github.com/serialcreator9090-source/predictive-maintenance-ml.git
cd predictive-maintenance-ml
```

### 2. Install dependencies

```bash
pip install pandas numpy scikit-learn joblib streamlit
```

Install any additional dependencies required by the notebook if needed.

### 3. Run the application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal.

## Model Evaluation

The project investigates model performance under class imbalance. Precision, recall and F1-score are considered alongside accuracy because correctly detecting failures is important.

Add the verified final test-set metrics here once they have been confirmed against the final model and classification threshold.

## Limitations

- The dataset is synthetic and does not establish performance on real industrial equipment.
- The dashboard uses manually entered sensor values; it is not connected to live factory sensors.
- Predictions are educational demonstrations and should not be used as the sole basis for real-world maintenance or safety decisions.

## Future Improvements

- Connect the system to simulated or live sensor streams.
- Add automated tests and improve error handling.
- Explore time-series monitoring and anomaly detection.
- Investigate deployment and monitoring approaches.

## Author

Developed as a learning project exploring machine learning and industrial predictive maintenance.

## Model Evaluation

The final Random Forest model was evaluated on a held-out test set of 2,000 samples using a classification threshold of 0.4.

| Metric | Result |
|---|---:|
| Test accuracy | 98.4% |
| Failure precision | 86% |
| Failure recall | 63% |
| Failure F1-score | 0.73 |
| Average precision | 0.7889 |

### Confusion Matrix

| | Predicted: No Failure | Predicted: Failure |
|---|---:|---:|
| Actual: No Failure | 1,925 | 7 |
| Actual: Failure | 25 | 43 |

### Interpretation

- **Accuracy:** 98.4% of all test samples were classified correctly.
- **Precision:** 86% of predicted failures were actual failures.
- **Recall:** The model detected 63% of actual failures.
- **F1-score:** 0.73 summarizes the balance between failure precision and recall.
- **Average precision:** 0.7889 measures precision-recall performance across classification thresholds.

Although overall accuracy is high, the model missed 25 of the 68 actual failures in the test set. This highlights the importance of evaluating failure detection using recall and other metrics rather than accuracy alone.

These results apply to the synthetic AI4I 2020 benchmark dataset and do not establish performance on real industrial equipment.

