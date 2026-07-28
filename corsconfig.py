import os
import streamlit as st
from dotenv import load_dotenv

def get_secret(key_name):
    try:
        return st.secret[key_name]
    except Exception:
        load_dotenv()
        return os.getenv(key_name)

GROQ_API = get_secret("GROQ_API")
OPENROUTER_API = get_secret("OPEN_ROUTER_API")

