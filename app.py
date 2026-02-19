import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
import streamlit as st
from query_understanding import analyze_query
from recommendation_engine import recommend_next_step

st.set_page_config(page_title="AI Teaching Assistant", layout="centered")

st.title("📚 AI-Powered Teaching Assistant")

st.write("This system understands student queries and recommends adaptive learning paths.")

st.divider()

# Input Section
query = st.text_input("Enter your question:")

score = st.slider("Quiz Score", 0, 100, 50)
attempts = st.number_input("Number of Attempts", min_value=1, value=1)
time_spent = st.number_input("Time Spent (minutes)", min_value=1, value=10)

if st.button("Analyze"):

    if query.strip() == "":
        st.warning("Please enter a question.")
    else:
        # Step 1: Query Understanding
        result = analyze_query(query)

        st.subheader("🔎 Query Understanding")
        st.json(result)

        # Step 2: Recommendation
        recommendation = recommend_next_step(
            score,
            attempts,
            time_spent,
            result["topic"]
        )

        st.subheader("📈 Adaptive Recommendation")
        st.json(recommendation)
