import streamlit as st

# Page configuration
st.set_page_config(page_title="Git Wrapped - Vaibhavk121", layout="wide")

# Title and header
st.title("@vaibhavk121")
st.header("2024 Year in Code")
st.write("Code, Commit, Conquer: A Year of Challenges and Triumphs in 2024!")

# Contribution graph placeholder
st.markdown("### Contribution Graph")
# st.image("gitwrapped.jpg", use_column_width=True)

# Metrics in a grid
col1, col2, col3 = st.columns(3)
col1.metric("Universal Rank", "Top 50%")
col2.metric("Longest Streak", "5 days")
col3.metric("Total Commits", "102")

col4, col5, col6 = st.columns(3)
col4.metric("Most Active Month", "July")
col5.metric("Most Active Day", "Thursday")
col6.metric("Top Language", "Python")

# Power level
st.markdown("### Power Level")
st.info("Adventurer")
