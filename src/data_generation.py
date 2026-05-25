import os
import numpy as np
import pandas as pd

def generate_data(num_students=1000):
    print("Generating synthetic student data...")
    np.random.seed(42)
    
    # Simulate realistic features
    data = {
        'score': np.random.randint(30, 100, size=num_students),
        'time_taken': np.random.randint(20, 300, size=num_students),
        'retries': np.random.randint(0, 5, size=num_students),
        'hints_used': np.random.randint(0, 6, size=num_students)
    }
    
    df = pd.DataFrame(data)
    
    # Logical grounding for target variable (1 = understands, 0 = needs improvement)
    # High score, low retries, and low hints heavily lean towards mastery (1)
    df['understands'] = np.where(
        (df['score'] >= 70) & (df['retries'] <= 2) & (df['hints_used'] <= 2), 
        1, 0
    )
    
    # Introduce a bit of real-world noise (randomly flip 5% of labels)
    noise = np.random.choice([0, 1], size=num_students, p=[0.95, 0.05])
    df['understands'] = np.where(noise == 1, 1 - df['understands'], df['understands'])
    
    # Ensure data directory exists
    os.makedirs('data', exist_ok=True)
    
    # Export to CSV
    csv_path = 'data/quiz_data.csv'
    df.to_csv(csv_path, index=False)
    print(f"Dataset successfully saved to {csv_path} ({num_students} records).")

if __name__ == "__main__":
    generate_data()