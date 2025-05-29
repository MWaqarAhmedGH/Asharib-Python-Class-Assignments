# app.py

import streamlit as st
from modules.idea import Idea
from modules.validator import ValidatorEngine

st.set_page_config(page_title="AIdeaX - AI Idea Validator", page_icon="🤖")

st.title("🤖 AIdeaX - Validate Your Startup Idea Using AI")

with st.form("idea_form"):
    title = st.text_input("💡 Startup Idea Title")
    problem = st.text_area("❌ Problem You're Solving")
    solution = st.text_area("✅ Your Proposed Solution")
    audience = st.text_input("🎯 Target Audience")
    revenue_model = st.text_input("💰 Revenue Model")
    submitted = st.form_submit_button("🚀 Validate Idea")

if submitted:
    idea = Idea(title, problem, solution, audience, revenue_model)
    engine = ValidatorEngine(idea)
    st.subheader("📊 Validation Result")
    st.success(engine.generate_feedback())
