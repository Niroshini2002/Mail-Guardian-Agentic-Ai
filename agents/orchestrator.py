from agents.triage_agent import triage_agent
from agents.link_verification_agent import extract_urls, link_verification_agent, reflect_on_verdict
import json

def process_email(subject, body):
    result = {}
    
    # Agent 1: Triage
    triage_output = triage_agent(subject, body)
    result["triage"] = triage_output
    
    # Extract URLs
    urls = extract_urls(body)
    result["urls_found"] = urls
    
    # Agent 2: Link Verification (only if links exist)
    link_results = []
    if urls:
        for url in urls:
            verification = link_verification_agent(url, subject)
            reflection = reflect_on_verdict(verification, url)
            link_results.append({
                "url": url,
                "verification": verification,
                "reflection": reflection
            })
    result["link_analysis"] = link_results
    
    return result


if __name__ == "__main__":
    subject = "Amazon Order Confirmation"
    body = "Your order has been confirmed. Track your package here: http://amaz0n-offers.xyz/track"
    
    output = process_email(subject, body)
    print(json.dumps(output, indent=2))