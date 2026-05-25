import streamlit as st
from src.adaptive_engine import get_adaptive_recommendation

# Page Layout & Config
st.set_page_config(page_title="Constitutional AI Analyzer", page_icon="📜", layout="centered")

st.title("📜 Constitutional Quiz AI Analyzer")
st.write("An adaptive engine leveraging Logistic Regression to measure student concept mastery and customize learning paths.")

st.markdown("---")

# UI Form Inputs
st.subheader("📊 Simulate Student Quiz Performance")

col1, col2 = st.columns(2)

with col1:
    topic = st.selectbox("Select Quiz Module", ["Fundamental Rights", "Directive Principles", "Judiciary System", "Parliamentary Framework"])
    score = st.slider("Quiz Score (out of 100)", min_value=0, max_value=100, value=75, step=5)
    time_taken = st.slider("Time Spent (seconds)", min_value=10, max_value=300, value=90, step=10)

with col2:
    retries = st.number_input("Number of Retries on Questions", min_value=0, max_value=10, value=1, step=1)
    hints_used = st.number_input("Total Hints Requested", min_value=0, max_value=10, value=0, step=1)

# Analysis Trigger
if st.button("Analyze Metrics & Adaptive Route", type="primary"):
    with st.spinner("AI engine evaluating performance profile..."):
        # Fetch data back from processing engine
        result = get_adaptive_recommendation(score, time_taken, retries, hints_used)
        
        if result["status"] == "error":
            st.error(result["message"])
        else:
            st.markdown("---")
            st.subheader("🎯 Engine Evaluation Metrics")
            
            # Highlight Mastery Score
            prob_percentage = result["probability"] * 100
            st.metric(label="Calculated Concept Mastery Probability", value=f"{prob_percentage:.1f}%")
            
            # Progress bar representation
            st.progress(result["probability"])
            
            # Display Recommendations
            st.markdown(f"### Next Target Difficulty: **{result['next_tier']}**")
            st.info(f"📋 **Actionable Step:** {result['recommendation']}")
            
            # Gamification Element
            st.success(f"🏆 **Earned Badge:** {result['badge']} for the *{topic}* module!")