import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)
print("Connected!")

sample_email_subject="URGENT: Your account has been locked.Verify Now!"
sample_email_body="Dear customer,we have detected unusual activity on your account.Please verify your identity immediately by clicking the link below.Failure to do so within 24 hours may result in permanent aaccount suspension."

def triage_agent(subject,body):
  prompt=f"""
  You are an email security triage agent.Analyze the following email and classify it as one of:Important,Spam, or Suspicious.

  Look for these patterns:
  -Urgency-based language(e.g,"act now", "24 hours","immediately")
  -Requests for sensitive information or account verification
  -Threats of account suspension or loss
  -Generic greetings instead of personalized ones.


Subject:{subject}
Body:{body}

Respond ONLY in this JSON format:
{{
"classification":"Important,Spam,or Suspicious",
"reasons":["reason1","reason2"],
"recommendation":"what the user should do"
}}
"""
  response=client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role":"user","content":prompt}]
  )
  return response.choices[0].message.content

if __name__ == "__main__":
    subject = "URGENT: Your account has been locked. Verify Now!"
    body = "Dear customer, we have detected unusual activity..."
    result = triage_agent(subject, body)
    print(result)