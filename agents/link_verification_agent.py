import os
import re
from dotenv import load_dotenv
from groq import Groq
from openai import OpenAI
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from corsconfig import GROQ_API_KEY, OPENROUTER_API_KEY


groq_client = Groq(api_key=GROQ_API_KEY)
openrouter_client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY
)

def extract_urls(email_body):
    url_pattern = r'https?://[^\s]+'
    urls = re.findall(url_pattern, email_body)
    return urls

def link_verification_agent(url, brand_context=""):
    prompt = f"""
    You are a phishing intelligence agent. Analyze this URL and determine
    if it is genuine or a phishing/scam attempt.

    Check for:
    - Brand impersonation (e.g., "amaz0n" instead of "amazon", extra words/dashes)
    - Suspicious domain patterns (unusual TLDs like .xyz, .top, misspellings)
    - Whether the URL matches the claimed sender/brand in the email context

    URL: {url}
    Email context: {brand_context}

    Respond ONLY in this JSON format:
    {{
        "verdict": "genuine/phishing",
        "trust_score": 0-100,
        "risk_level": "LOW/MEDIUM/HIGH",
        "reasons": ["reason1", "reason2"],
        "recommendation": "what the user should do"
    }}
    """

    response = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

def reflect_on_verdict(initial_result, url):
    prompt = f"""
    Review this phishing analysis and verify if the verdict is accurate.
    Confirm or correct the assessment if needed.

    Initial Analysis: {initial_result}
    URL: {url}

    Respond in the same JSON format as before.
    """
    response = openrouter_client.chat.completions.create(
        model="nvidia/nemotron-3-ultra-550b-a55b:free",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    test_url = "http://amaz0n-offers.xyz/track"
    result = link_verification_agent(test_url, "Amazon Order Confirmation")
    print("LINK VERIFICATION:")
    print(result)
    
    reflection = reflect_on_verdict(result, test_url)
    print("\nREFLECTION:")
    print(reflection)

