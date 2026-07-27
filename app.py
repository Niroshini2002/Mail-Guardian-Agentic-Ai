import streamlit as st
from agents.orchestrator import process_email

st.set_page_config(page_title="Mail Guardian", page_icon="🛡️")

st.title("🛡️ Mail Guardian")
st.subheader("Agentic Email Triage & Phishing Detection System")

st.markdown("---")

sender_email = st.text_input("Sender Email Address")
subject = st.text_input("Email Subject")
body = st.text_area("Email Body", height=200)

if st.button("Analyze Email"):
    if subject and body:
        with st.spinner("Analyzing email..."):
            result = process_email(subject, body)
        
        st.markdown("---")
        st.subheader("Results")
        
        st.json(result)
    else:
        st.warning("Please fill in the subject and body.")

st.markdown("---")
st.caption("No email data is stored. Analysis is performed in-memory only.")