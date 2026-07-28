import streamlit as st
from agents.orchestrator import process_email

st.set_page_config(page_title="Mail Guardian", page_icon="🛡️")

st.title("🛡️ Mail Guardian")
st.subheader("Agentic Email Triage & Phishing Detection System")

st.markdown("---")

sender_email = st.text_input("Sender Email Address")
subject = st.text_input("Email Subject")
body = st.text_area("Email Body", height=200)

import json

if st.button("Analyze Email"):
    if subject and body:
        with st.spinner("Analyzing email..."):
            result = process_email(subject, body)
        
        st.markdown("---")
        st.subheader("📋 Analysis Results")
        
        # Parse triage result (it's a JSON string)
        triage_data = json.loads(result["triage"])
        
        # Display Triage Classification
        classification = triage_data.get("classification", "Unknown")
        if classification == "Important":
            st.success(f"✅ Classification: **{classification}**")
        elif classification == "Spam":
            st.warning(f"⚠️ Classification: **{classification}**")
        else:
            st.error(f"🚨 Classification: **{classification}**")
        
        st.write("**Why:**")
        for reason in triage_data.get("reasons", []):
            st.write(f"- {reason}")
        
        st.info(f"**Recommendation:** {triage_data.get('recommendation', '')}")
        
        # Display Link Analysis (if any URLs found)
        if result["link_analysis"]:
            st.markdown("---")
            st.subheader("🔗 Link Verification")
            
            for link in result["link_analysis"]:
                reflection_data = json.loads(link["reflection"])
                
                st.write(f"**URL:** `{link['url']}`")
                
                verdict = reflection_data.get("verdict", "unknown")
                trust_score = reflection_data.get("trust_score", "N/A")
                risk_level = reflection_data.get("risk_level", "N/A")
                
                if verdict == "phishing":
                    st.error(f"🚨 Verdict: **PHISHING DETECTED** | Trust Score: {trust_score}/100 | Risk: {risk_level}")
                else:
                    st.success(f"✅ Verdict: **GENUINE** | Trust Score: {trust_score}/100 | Risk: {risk_level}")
                
                st.write("**Why:**")
                for reason in reflection_data.get("reasons", []):
                    st.write(f"- {reason}")
                
                st.info(f"**Recommendation:** {reflection_data.get('recommendation', '')}")
        else:
            st.markdown("---")
            st.write("No links found in this email.")
    else:
        st.warning("Please fill in the subject and body.")

st.markdown("---")
st.caption("No email data is stored. Analysis is performed in-memory only.")