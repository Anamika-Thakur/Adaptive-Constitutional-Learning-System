#  Adaptive Constitutional Learning System  
### Personalized Ed-Tech using Logistic Regression

Adaptive Constitutional Learning System is a machine learning-powered educational platform that dynamically adjusts quiz difficulty based on a learner’s performance and behavioral patterns.

Instead of assigning students a static score and identical learning path, the system analyzes quiz interactions such as score, retries, hints used, and completion time to estimate conceptual understanding using Logistic Regression.

Based on the model’s confidence score, learners are routed into personalized difficulty tiers — creating a virtual tutor–like adaptive learning experience focused on constitutional literacy.

---

#  Project Goals

- Predict whether a learner understands a constitutional concept.
- Dynamically adapt quiz difficulty using confidence-based routing.
- Simulate intelligent personalized learning behavior.
- Build an end-to-end ML pipeline from data generation to deployment.
- Demonstrate how Machine Learning can enhance Ed-Tech systems.

---

#  Features Used

The model predicts learner understanding using the following features:

- Quiz Score
- Time Taken
- Number of Retries
- Hints Used

These behavioral indicators help estimate whether a learner has genuinely mastered a topic or requires additional support.

---

#  Techniques Applied

- Logistic Regression
- StandardScaler Feature Scaling
- Synthetic Dataset Generation
- Probability-Based Prediction (`predict_proba`)
- Confidence Threshold Routing
- Train/Test Split
- Model Serialization using Pickle
- Real-Time Predictions with Streamlit

---

#  How the System Works

The project follows a complete adaptive ML pipeline:

```text
Student Interaction
        ↓
Behavioral Data Collection
        ↓
Feature Scaling
        ↓
Logistic Regression Prediction
        ↓
Confidence Score Calculation
        ↓
Adaptive Difficulty Recommendation
```
---

Streamlit App Link : https://adaptive-constitutional-learning-system-q8lrxzpjcgwen38ufaewrz.streamlit.app/
