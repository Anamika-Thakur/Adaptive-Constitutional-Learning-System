import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

def train_model():
    # 1. Load dataset
    csv_path = 'data/quiz_data.csv'
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Missing {csv_path}. Please run data_generation.py first!")
        
    df = pd.read_csv(csv_path)
    
    # 2. Split Features & Target
    X = df[['score', 'time_taken', 'retries', 'hints_used']]
    y = df['understands']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 3. Feature Scaling
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # 4. Model Training
    print("Training Logistic Regression model...")
    model = LogisticRegression(random_state=42)
    model.fit(X_train_scaled, y_train)
    
    # 5. Evaluation
    y_pred = model.predict(X_test_scaled)
    acc = accuracy_score(y_test, y_pred)
    print("\n=== Model Metrics ===")
    print(f"Accuracy: {acc * 100:.2f}%")
    print("\nClassification Report:\n", classification_report(y_test, y_pred))
    
    # 6. Save Model Artifacts
    os.makedirs('models', exist_ok=True)
    joblib.dump(model, 'models/lr_model.pkl')
    joblib.dump(scaler, 'models/scaler.pkl')
    print("\nModel and Scaler successfully saved to 'models/' folder.")

if __name__ == "__main__":
    train_model()