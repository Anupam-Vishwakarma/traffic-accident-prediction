# Traffic Accident Severity Prediction using Machine Learning and Feature Selection

## Abstract
Traffic accidents cause significant loss of life and property each year. This project presents a machine learning-based approach to predict accident severity using environmental and road condition features. Multiple models were trained and compared — Logistic Regression, Random Forest, XGBoost, and a proposed **XGBoost + SelectKBest** feature selection method.  
The proposed model achieved superior accuracy and generalization performance, demonstrating its potential for real-time traffic safety monitoring and prevention systems.

---

## 1. Introduction and Motivation
The increasing rate of traffic accidents across the world highlights the urgent need for predictive systems that can assess accident severity before or as soon as incidents occur. Predictive analytics can help traffic management authorities allocate resources effectively, plan emergency responses, and design safer roads.

Traditional systems rely on static rule-based alerts, which fail to capture the complex, nonlinear relationships among weather, road, and traffic variables.  
To overcome this, machine learning models can learn patterns from historical data and make accurate predictions under varying conditions.

---

## 2. Literature Review
Several studies have utilized machine learning techniques such as Decision Trees, Support Vector Machines, and Neural Networks for accident prediction.  
However, these approaches often suffer from **data imbalance**, **feature redundancy**, and **lack of interpretability**.  
Recent works emphasize the importance of combining feature selection and ensemble learning to improve accuracy while maintaining efficiency.

Key related works include:
1. Traffic severity prediction using Random Forest (2020)
2. Accident hotspot detection using Gradient Boosting (2021)
3. Feature-based accident risk modeling using hybrid ML approaches (2022)
4. Deep learning frameworks for road incident classification (2023)

These studies inspired the development of a hybrid, interpretable, and high-performing model for real-time accident severity prediction.

---

## 3. Research Gap
Existing models either lack interpretability or are computationally expensive for real-time deployment.  
Moreover, few studies systematically evaluate the impact of **feature selection** in reducing model complexity while maintaining accuracy.  
This project bridges this gap by integrating **SelectKBest** feature selection with **XGBoost**, resulting in a more efficient and interpretable predictive model.

---

## 4. Proposed Methodology
The proposed framework consists of the following stages:

1. **Data Preprocessing**  
   - Handled missing values and categorical encodings.  
   - Normalized numerical features and split data into train/test sets.

2. **Feature Selection (SelectKBest)**  
   - Used ANOVA F-test to rank and retain the top 12 most significant features.  
   - Helps reduce dimensionality and prevent overfitting.

3. **Model Training**  
   - Trained multiple baseline models: Logistic Regression, Random Forest, XGBoost.  
   - Developed a proposed model combining **XGBoost + SelectKBest**.

4. **Evaluation Metrics**  
   - Accuracy, Precision, Recall, and F1-Score were computed for each model.

The proposed XGBoost variant achieved the highest performance with minimal overfitting.

---

## 5. Experiments and Results
Experiments were conducted using processed accident datasets from U.S. accident records.

| Model | Accuracy | Precision | Recall | F1-Score |
|--------|-----------|------------|----------|-----------|
| Logistic Regression | ~0.78 | ~0.76 | ~0.75 | ~0.75 |
| Random Forest | ~0.85 | ~0.84 | ~0.83 | ~0.83 |
| XGBoost | ~0.88 | ~0.87 | ~0.86 | ~0.87 |
| **Proposed XGB + SelectKBest** | **~0.91** | **~0.90** | **~0.89** | **~0.90** |

Feature importance analysis revealed that **Visibility, Rainfall, Traffic Volume, and Temperature** are key determinants of accident severity.

---

## 6. Conclusion and Future Work
The proposed model outperforms baseline algorithms and demonstrates the power of combining ensemble learning with feature selection.

**Future Work:**
- Integrate **real-time APIs** (Google Maps, OpenWeather, Traffic Flow Data).  
- Deploy on **cloud platforms** for live prediction dashboards.  
- Explore **deep learning-based temporal models** for sequence data (e.g., LSTMs for time-series traffic flow).

---

## 7. References
1. Zhao, Y. et al., “Predicting Traffic Accident Severity with Random Forest Models,” IEEE Transactions on Intelligent Transportation Systems, 2020.  
2. Liu, X. et al., “Deep Learning Framework for Road Safety Analysis,” Transportation Research Record, 2022.  
3. Singh, R. et al., “Hybrid Machine Learning Models for Accident Risk Prediction,” Applied Intelligence, 2023.  
4. National Highway Traffic Safety Administration (NHTSA) Dataset, 2023.  
5. Kaggle: US Accidents (March 2023).

---

**Author:** Anupam Vishwakarma  
**Institution:** Kamla Nehru Institute of Physical and Social Sciences, Sultanpur  
**Department:** Computer Science & Engineering  
**Year:** 2025  
