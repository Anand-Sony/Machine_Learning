# Diabetes Prediction using Machine Learning & Artificial Neural Network

## Overview
This project predicts whether a person is diabetic or not using the Pima Indians Diabetes Dataset. Multiple machine learning techniques were used to preprocess the data, train classification models, and evaluate their performance. The project also compares a traditional Machine Learning model (K-Nearest Neighbors) with an Artificial Neural Network (ANN).

---

## Dataset
The dataset is based on the **Pima Indians Diabetes Database** provided by the National Institute of Diabetes and Digestive and Kidney Diseases (NIDDK).

It contains diagnostic measurements of female patients who are at least 21 years old and of Pima Indian heritage.

### Features
- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

### Target
- **Outcome**
  - 0 → Non-Diabetic
  - 1 → Diabetic

---

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- TensorFlow / Keras
- Jupyter Notebook

---

## Project Workflow

1. Load the dataset
2. Perform data exploration
3. Check for missing values
4. Split the dataset into training and testing sets
5. Standardize features using StandardScaler
6. Apply Principal Component Analysis (PCA) for dimensionality reduction
7. Train a K-Nearest Neighbors (KNN) classifier
8. Evaluate the model using:
   - Confusion Matrix
   - Accuracy Score
9. Build an Artificial Neural Network (ANN)
10. Train the ANN using TensorFlow/Keras
11. Predict diabetes for new patient data

---

## Machine Learning Models

### K-Nearest Neighbors (KNN)

- Feature Scaling using StandardScaler
- Classification using KNN
- Model Evaluation using Accuracy Score and Confusion Matrix

### Artificial Neural Network (ANN)

Network Architecture:
- Input Layer
- Hidden Layer (10 neurons, ReLU activation)
- Output Layer (1 neuron, Sigmoid activation)

Optimizer:
- Adam

Loss Function:
- Binary Crossentropy

Evaluation Metric:
- Accuracy

---

## Results

KNN Model Accuracy:
- **78.79%**

The ANN was trained for **200 epochs** and achieved comparable performance for binary diabetes classification.

---

## Repository Structure

```
Project_1/
│
├── Python_code.ipynb      # Complete implementation
├── dataset.csv            # Diabetes dataset
├── Report.docx            # Project report
└── README.md              # Project documentation
```

---

## Libraries Used

```python
numpy
pandas
matplotlib
seaborn
scikit-learn
tensorflow
```

---

## Future Improvements

- Hyperparameter tuning
- Cross-validation
- Feature engineering
- Handling missing or zero values more effectively
- Compare additional algorithms such as:
  - Random Forest
  - XGBoost
  - Support Vector Machine
  - Logistic Regression

---

## Author

**Anand Soni**

Mechanical Engineering Undergraduate  
Malaviya National Institute of Technology (MNIT), Jaipur

GitHub: https://github.com/Anand-Sony

---

## License

This project is intended for educational and learning purposes.
