# Mail-Guardian-Agentic-Ai
Agentic AI system for email triage and phishing/scam detection


Mail Guardian is a multi-agent AI system designed to protect users from 
email-based threats such as spam, phishing, and scam attacks. The system 
combines two intelligent AI agents that collaboratively analyze incoming 
emails, classify their importance, and verify the legitimacy of embedded links.

By leveraging Retrieval-Augmented Generation (RAG) and carefully selected 
Large Language Models (LLMs), Mail Guardian delivers context-aware and 
explainable email security analysis.

---

## Project Overview

Mail Guardian addresses two major email security challenges:

- Identifying whether an email is legitimate, important, or spam.
- Detecting phishing and scam attempts hidden within embedded URLs.

The system adopts an agentic architecture where specialized agents 
independently perform their tasks and collaboratively provide a final 
security assessment.

---

## System Workflow

1. Incoming emails are parsed and analyzed.
2. Agent 01 classifies the email based on its content and priority.
3. Agent 02 extracts and verifies all embedded URLs.
4. The RAG pipeline retrieves relevant security knowledge when required.
5. Both agents collaborate to generate the final verdict along with security recommendations.

---

## Agent 01 – Intelligent Email Triage Agent

The Triage Agent is responsible for understanding the content of an email 
and determining its importance.

**Responsibilities**
- Classifies emails as: Important / Spam / Suspicious
- Identifies malicious or misleading language patterns
- Detects urgency-based social engineering attempts
- Prioritizes legitimate communications
- Provides explainable reasoning for its decisions

**Features**

*Content Analysis*
- Analyzes the email subject and body
- Identifies suspicious phrases such as:
  - Urgent account verification requests
  - Fake payment notifications
  - Prize and lottery scams
  - Credential harvesting attempts

*Priority Classification*
The agent categorizes emails into: Important / Spam / Suspicious

*Explainable Decision Making*
The agent provides clear reasons for its classification along with a 
recommendation for how the user should respond.

---

## Agent 02 – Phishing Intelligence & Link Verification Agent

The Link Verification Agent goes beyond traditional URL checking by 
intelligently detecting phishing and scam attempts.

**Responsibilities**
- Extracts URLs from emails
- Verifies domain legitimacy
- Detects phishing and scam links
- Identifies brand impersonation attacks
- Analyzes malicious intent
- Generates explainable security reports

**Core Components**

*URL Extractor*
- Identifies all URLs present within an email
- Handles multiple and shortened links

*Domain Reputation Checker*
Analyzes:
- HTTPS availability
- Suspicious URL patterns
- Redirect behavior
- Domain legitimacy indicators

*Brand Impersonation Detector*
Detects domains attempting to mimic legitimate organizations 

*Intent Analyzer*
Detects possible malicious intentions such as:
- Credential theft
- Payment scams
- Banking fraud
- Fake delivery notifications
- Account verification scams

*Trust Score Generator*
Assigns a trust score between 0 and 100, along with a corresponding risk level.

*Explainable Report Generator*
Provides detailed explanations for its verdict instead of simply labeling 
a URL as malicious.

---

## Email–URL Correlation Analysis (Unique Feature)

Mail Guardian performs cross-verification between the email content and 
embedded URLs, comparing the claimed sender/brand against the actual 
destination domain to detect brand mismatches. This enables the system to 
identify sophisticated phishing attacks that imitate trusted organizations.

---

## Agentic Design Patterns Used

| Pattern | Where It's Used | Purpose |
|---|---|---|
| Router | `agents/triage_agent.py` → `triage_agent()` | Classifies and routes each email into Important / Spam / Suspicious |
| Tool-use | `agents/link_verification_agent.py` → `extract_urls()`, `link_verification_agent()` | Extracts URLs and analyzes domain/brand legitimacy as a discrete tool step |
| Reflection | `agents/link_verification_agent.py` → `reflect_on_verdict()` | A second model independently re-checks the initial phishing verdict before finalizing it |
| Orchestrator | `agents/orchestrator.py` → `process_email()` | Coordinates Agent 1 and Agent 2 into a single end-to-end pipeline, passing structured data between them |

---

## Agent-to-Agent Communication

Agent 1 (Triage) and Agent 2 (Link Verification) communicate through a 
structured JSON hand-off, coordinated by the orchestrator:

```
User Input (subject, body)
        │
        ▼
┌───────────────────┐
│ Agent 1: Triage     │───▶ { classification, reasons, recommendation }
└───────────────────┘
        │
        ▼
   URL Extraction
        │
        ▼
┌────────────────────────┐
│ Agent 2: Link Verification│───▶ { verdict, trust_score, risk_level, reasons }
│         + Reflection       │───▶ (second model re-validates the verdict)
└────────────────────────┘
        │
        ▼
Combined Security Report
```

---

## RAG Pipeline

The Retrieval-Augmented Generation (RAG) pipeline enhances contextual 
understanding by retrieving domain-specific security knowledge.

**Components**
- Email security knowledge base (20 documents covering phishing patterns, 
  scam types, and detection concepts)
- Chunking strategy: each document covers a single, focused topic, so no 
  further text splitting was required
- Embedding model: `all-MiniLM-L6-v2` (sentence-transformers) — compact, 
  fast, and runs locally with no API cost
- Vector store: ChromaDB (persistent local storage)
- Context-aware retrieval to support agent decision-making

**Retrieval Evaluation (5 sample queries):**

| Query | Top Match | Relevant? |
|---|---|---|
| "email asking to verify account urgently" | Account Verification Scams | ✅ Yes |
| "suspicious domain with numbers instead of letters" | Brand Impersonation | ✅ Yes |
| "email claiming I won a prize" | Lottery and Prize Scams | ✅ Yes |
| "link that redirects multiple times" | Suspicious Redirect Behavior | ✅ Yes |
| "email requesting my password directly" | Credential Harvesting | ✅ Yes |

All 5 test queries retrieved highly relevant documents from the knowledge 
base, confirming the embedding model effectively captures semantic 
similarity between user queries and domain-specific security content.

---

## Final Output Format

The system produces a combined verdict including:
- Email Classification (Important / Spam / Suspicious)
- Link Verification (Safe / Phishing Detected)
- Trust Score (0–100)
- Reasons behind the verdict
- A recommendation for the user

---

## Why Mail Guardian?

Mail Guardian combines:
- Multi-Agent AI Architecture
- Intelligent Email Triage
- Phishing Intelligence Detection
- Trust Score Generation
- Brand Impersonation Detection
- Email–URL Correlation Analysis
- Retrieval-Augmented Generation (RAG)
- Explainable AI-Based Security Reporting

By integrating collaborative AI agents with contextual threat analysis, 
Mail Guardian provides a robust and transparent approach to email security.

---

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Niroshini2002/Mail-Guardian-Agentic-Ai.git
   cd Mail-Guardian-Agentic-Ai
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root with the following keys:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   OPENROUTER_API_KEY=your_openrouter_api_key_here
   ```

4. Build the RAG vector store (one-time setup):
   ```bash
   python generate_docs.py
   python rag/ingest.py
   ```

5. Run the Streamlit app locally:
   ```bash
   streamlit run app.py
   ```

---

## Model Selection Strategy

| Sub-task | Model (Provider) | Why Chosen |
|---|---|---|
| Email triage / classification | Llama 3.1 8B Instant (Groq) | Very low latency and cost, sufficient reasoning for a straightforward classification task |
| Link verification / phishing analysis | Llama 3.1 8B Instant (Groq) | Fast initial analysis of URL and domain patterns |
| Verdict reflection / validation | Nvidia Nemotron 3 Ultra (OpenRouter, free tier) | A second, independent model reviews the initial verdict, adding a validation layer and reducing single-model blind spots |

---

## Architecture Diagram

```
User Input (Sender, Subject, Body)
            │
            ▼
   ┌─────────────────┐
   │   Agent 1:        │
   │   Triage Agent     │──── classifies: Important / Spam / Suspicious
   └────────┬──────────┘
            │
            ▼
   URL Extraction (regex)
            │
            ▼
   ┌─────────────────────────┐
   │   Agent 2:                 │
   │   Link Verification        │──── queries RAG knowledge base
   │   + Reflection               │──── verdict: Genuine / Phishing + Trust Score
   └────────┬────────────────────┘
            │
            ▼
   Combined Security Report
   (Classification + Verdict + Trust Score + Recommendation)
```

---

## Live Demo

https://mail-guardian-agentic-ai-7.streamlit.app/

---

## Known Limitations

- No persistent error handling yet for API failures, rate limits, or malformed model responses
- Free-tier OpenRouter models may change availability without notice
- The system currently processes one email at a time (no batch processing)
- RAG knowledge base is a curated set of general phishing patterns rather 
  than a live threat-intelligence feed, so it will not catch entirely novel 
  attack patterns not represented in the knowledge base
- No persistent storage of user-submitted emails (by design, for privacy — 
  see Security & Privacy Considerations below)

---

## Security & Privacy Considerations

- No email data is stored on the server or in any database
- Input is processed in-memory only and discarded after the response is returned
- All data transmission occurs over HTTPS (Streamlit Cloud default)
- Email content is sent to third-party LLM providers (Groq/OpenRouter) for 
  analysis as part of the agentic pipeline — no persistent storage occurs 
  at any stage
