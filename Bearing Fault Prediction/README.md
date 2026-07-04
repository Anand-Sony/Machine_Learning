# Bearing Fault Prediction using Machine Learning

## Overview
This repository demonstrates **bearing fault diagnosis** using Machine Learning techniques on vibration signal features extracted from rolling element bearings. The objective is to classify the health condition of a bearing into one of six fault categories by analyzing frequency-domain and statistical features.

The project compares multiple supervised learning algorithms, including:

- Decision Tree Classifier
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)

The models are trained on engineered vibration features extracted from bearing signals and evaluated using standard classification metrics.

---

## Dataset

The dataset is sourced from **Kaggle** and contains extracted vibration features instead of raw time-series signals.

### Features

#### Frequency Domain Features
- FFT_0 – FFT_9

#### Statistical Features
- Crest Factor
- Shape Factor
- Impulse Factor
- Clearance Factor
- Mean Absolute Change
- Root Mean Square of First Difference
- Shannon Entropy
- Energy
- Form Factor
- Zero Crossing Rate
- Turning Point Ratio

> **Note:** `start_time` is removed during preprocessing because it does not contribute to prediction.

---

## Target Classes

| Label | Bearing Condition |
|--------|-------------------|
| 1 | Normal Bearing |
| 2 | Inner Race Fault |
| 3 | Outer Race Fault |
| 4 | Ball Fault |
| 5 | Combination Fault |
| 6 | Severe Fault |

---

## Project Workflow

1. Load the dataset
2. Remove unnecessary columns
3. Check missing values
4. Split features and target
5. Standardize numerical features
6. Apply PCA (for dimensionality reduction)
7. Train Machine Learning models
8. Evaluate model performance
9. Optimize hyperparameters using GridSearchCV
10. Predict bearing health for new samples

---

## Machine Learning Models

### Decision Tree
- Criterion: Gini / Entropy
- Maximum Depth
- Minimum Samples per Leaf

### K-Nearest Neighbors (KNN)
- Standardized input features
- Euclidean distance
- Default neighbors

### Support Vector Machine (SVM)
- RBF Kernel
- Hyperparameter tuning using GridSearchCV
- Optimized C parameter

---

## Model Performance

| Model | Test Accuracy |
|--------|---------------|
| Decision Tree | ~66% |
| KNN | ~70% |
| SVM (Default) | ~78% |
| SVM (Optimized) | **~86%** |

The optimized **Support Vector Machine (SVM)** achieved the best overall performance after hyperparameter tuning.

---

## Evaluation Metrics

The following metrics are used to evaluate model performance:

- Accuracy Score
- Confusion Matrix
- Mean Squared Error (MSE)
- R² Score
- Precision
- Recall

---

## Libraries Used

```python
pandas
numpy
matplotlib
seaborn
scikit-learn
pydotplus
IPython.display
```

---

## Repository Structure

```
Bearing-Fault-Prediction/
│
├── Decision Tree.ipynb
├── KNN.ipynb
├── Support Vector Machine (SVC).ipynb
├── Bearing Feature Extracted Full.csv
├── Bearing Feature Extracted Full(new_one).csv
└── README.md
```

---

## Results

- Data preprocessing significantly improves model performance.
- Standardization is essential for distance-based and kernel-based algorithms.
- PCA reduces dimensionality while preserving most of the information.
- Hyperparameter tuning with GridSearchCV further improves classification accuracy.
- Among all evaluated models, **Support Vector Machine (RBF Kernel)** achieved the highest accuracy of approximately **86%**.

---

## Future Improvements

- Random Forest
- XGBoost
- LightGBM
- CatBoost
- Neural Networks (ANN)
- Deep Learning with CNN/LSTM on raw vibration signals
- Feature selection techniques
- Cross-validation and ensemble learning

---

## Applications

- Predictive Maintenance
- Industrial Condition Monitoring
- Rotating Machinery Health Diagnosis
- Smart Manufacturing
- Industry 4.0
- Fault Detection Systems

---

## Author

**Anand Sony**

If you find this project useful, consider giving the repository a ⭐.
