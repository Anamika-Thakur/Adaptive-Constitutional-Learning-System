import os
import joblib
import pandas as pd

# Define paths to saved components
MODEL_PATH = 'models/lr_model.pkl'
SCALER_PATH = 'models/scaler.pkl'

def get_adaptive_recommendation(score, time_taken, retries, hints_used):
    """
    Evaluates real-time quiz metadata and assigns an adaptive path.
    """
    # Check if artifacts exist
    if not os.path.exists(MODEL_PATH) or not os.path.exists(SCALER_PATH):
        return {
            "status": "error",
            "message": "Model artifacts not found. Please run src/train.py first."
        }
        
    # Load model and scaler
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    
    # Convert inputs to a standard DataFrame matching training format
    input_data = pd.DataFrame([{
        'score': score,
        'time_taken': time_taken,
        'retries': retries,
        'hints_used': hints_used
    }])
    
    # Run data through processing pipeline
    input_scaled = scaler.transform(input_data)
    
    # Extract prediction probability for Class 1 (Understands)
    probability = model.predict_proba(input_scaled)[0][1]
    
    # Determine adaptive routing tier based on AI confidence
    if probability < 0.35:
        tier = "Easy"
        recommendation = "Review fundamental definitions. Let's look over standard materials again together."
        badge = "🌱 Knowledge Seeker"
    elif 0.35 <= probability < 0.75:
        tier = "Medium"
        recommendation = "Good foundational knowledge. Try analyzing interactive real-world legal scenarios next."
        badge = "⚖️ Apprentice Jurist"
    else:
        tier = "Hard"
        recommendation = "Superb concept mastery! Unlocking advanced landmark Supreme Court case study challenges."
        badge = "🏛️ Constitutional Scholar"
        
    return {
        "status": "success",
        "probability": probability,
        "next_tier": tier,
        "recommendation": recommendation,
        "badge": badge
    }