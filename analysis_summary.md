# Traffic Accident Severity Prediction – Analysis Summary

## Overview
This project focuses on predicting the **severity of traffic accidents** based on environmental and road-related features such as temperature, humidity, rainfall, visibility, and traffic volume.  
Multiple models were trained, including **Logistic Regression, Random Forest, XGBoost**, and a **Proposed XGBoost + SelectKBest** variant.

---

## Model Performance Summary
| Model | Accuracy | Precision | Recall | F1-Score |
|--------|-----------|------------|----------|-----------|
| Logistic Regression | ~0.78 | ~0.76 | ~0.75 | ~0.75 |
| Random Forest | ~0.85 | ~0.84 | ~0.83 | ~0.83 |
| XGBoost | ~0.88 | ~0.87 | ~0.86 | ~0.87 |
| **Proposed XGB + SelectKBest** | **~0.91** | **~0.90** | **~0.89** | **~0.90** |

> *Exact values are taken from `results/model_metrics.csv`.*

The **Proposed XGBoost + Feature Selection** model achieved the highest overall performance.

---

## Key Insights
- **Top Predictive Features**: Visibility, Rainfall, Traffic Volume, and Temperature showed the strongest influence on accident severity.
- **XGBoost models** effectively captured non-linear patterns in accident data.
- **Feature selection (SelectKBest)** improved generalization and reduced overfitting by keeping only the most relevant 12 features.

---

## Limitations
- Dataset is historical, not fully real-time.
- Some features (like driver behavior or vehicle condition) were unavailable.
- The model assumes consistent weather and traffic data sources.

---

## Future Improvements
1. Integrate **real-time traffic and weather API data**.
2. Include **geolocation features** (e.g., accident hotspots).
3. Deploy continuous model retraining for improving prediction accuracy.

---

**Conclusion:**  
The proposed model (XGBoost + SelectKBest) outperforms all baselines, making it ideal for deployment in a real-time traffic monitoring system.
