import os
import streamlit as st
from dotenv import load_dotenv

def get_secret(key_name):
    try:
        return st.secrets[key_name]
    except Exception:
        load_dotenv()
        return os.getenv(key_name)

GROQ_API_KEY = get_secret("GROQ_API_KEY")
OPENROUTER_API_KEY = get_secret("OPENROUTER_API_KEY")

