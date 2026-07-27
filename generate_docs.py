import os

os.makedirs("rag/knowledge_base", exist_ok=True)

docs = {
    "01_urgency_language.txt": """Phishing Pattern: Urgency-Based Language
Scammers frequently use time pressure to prevent victims from thinking 
carefully. Common phrases include "act now", "within 24 hours", "immediate 
action required", "your account will be suspended". Legitimate organizations 
rarely demand instant action via email and typically provide reasonable 
timeframes for account-related requests.""",

    "02_brand_impersonation.txt": """Phishing Pattern: Brand Impersonation
Attackers register lookalike domains that closely resemble legitimate brand 
names, such as replacing letters with numbers (amaz0n.com instead of 
amazon.com), adding extra words (amazon-security.com), or using different 
top-level domains (amazon.xyz instead of amazon.com). Always verify the 
exact domain spelling before trusting a link.""",

    "03_credential_harvesting.txt": """Phishing Pattern: Credential Harvesting
A common goal of phishing emails is to trick users into entering their 
username and password on a fake login page. These pages are often visually 
identical to the real site but hosted on a different domain. Warning signs 
include unexpected login prompts, requests to "verify your account", and 
login pages that don't match the organization's real domain.""",

    "04_suspicious_tlds.txt": """Phishing Pattern: Suspicious Top-Level Domains
Legitimate businesses typically use standard domains like .com, .org, or 
country-specific domains relevant to their location (e.g., .lk for Sri 
Lanka). Phishing sites often use unusual or cheap top-level domains such as 
.xyz, .top, .tk, .info, or .click, which are frequently used because they 
are inexpensive and easy to register anonymously.""",

    "05_generic_greetings.txt": """Phishing Pattern: Generic Greetings
Legitimate organizations that have an existing relationship with a customer 
usually address them by name. Phishing emails often use generic greetings 
like "Dear Customer", "Dear User", or "Dear Valued Member" because the 
attacker does not have access to the recipient's actual name or account 
details.""",

    "06_lottery_prize_scams.txt": """Scam Type: Lottery and Prize Scams
These emails claim the recipient has won a prize, lottery, or gift card 
they never entered. They typically request personal information or a small 
"processing fee" to claim the prize. No legitimate lottery or company 
requires payment or extensive personal information to release a prize.""",

    "07_banking_fraud_emails.txt": """Scam Type: Banking Fraud Emails
These emails impersonate banks and financial institutions, claiming there 
is unusual activity on the recipient's account, a failed transaction, or a 
need to "reverify" banking details. They direct victims to fake login pages 
designed to steal banking credentials and one-time passwords (OTPs).""",

    "08_fake_delivery_notifications.txt": """Scam Type: Fake Delivery Notifications
Attackers send emails claiming a package could not be delivered or requires 
additional customs fees, prompting the recipient to click a link or provide 
payment details. These often impersonate courier services and delivery 
companies and create urgency around a missed delivery window.""",

    "09_account_verification_scams.txt": """Scam Type: Account Verification Scams
These messages claim an account will be locked, suspended, or deleted 
unless the user "verifies" their identity by clicking a link and entering 
credentials. This is one of the most common phishing templates because it 
exploits fear of losing access to an important service.""",

    "10_https_and_padlock.txt": """Security Indicator: HTTPS and Domain Verification
The presence of "https://" and a padlock icon indicates an encrypted 
connection, but it does NOT verify that a site is legitimate or safe — 
attackers can obtain HTTPS certificates for phishing domains too. Users 
should verify the actual domain name matches the expected organization, 
not just check for the padlock icon.""",

    "11_redirect_chains.txt": """Security Indicator: Suspicious Redirect Behavior
Phishing links often use multiple redirects to obscure the final 
destination URL and evade basic filtering. A link that redirects through 
several unrelated domains before landing on a login page is a strong 
indicator of malicious intent.""",

    "12_domain_age_signal.txt": """Security Indicator: Newly Registered Domains
Phishing campaigns often use domains that were registered very recently, 
sometimes within days of the attack. A domain claiming to be an established 
bank or company but registered only weeks ago is a significant red flag 
for fraud.""",

    "13_email_url_mismatch.txt": """Detection Technique: Email-URL Correlation
Cross-referencing the claimed sender or brand in an email's content against 
the actual destination domain of embedded links is an effective phishing 
detection technique. A mismatch, such as an email claiming to be from a 
bank but linking to an unrelated or lookalike domain, strongly indicates 
phishing.""",

    "14_sensitive_info_requests.txt": """Phishing Pattern: Requests for Sensitive Information
Legitimate organizations rarely ask customers to provide passwords, PINs, 
full card numbers, or OTPs via email. Any email requesting this type of 
sensitive information directly should be treated with high suspicion, 
regardless of how official it appears.""",

    "15_spoofed_sender_addresses.txt": """Phishing Pattern: Spoofed Sender Addresses
Attackers can forge the "From" field of an email to make it appear to come 
from a trusted source. Careful inspection of the full email header and 
actual sending domain (not just the display name) often reveals 
inconsistencies that indicate spoofing.""",

    "16_attachment_based_phishing.txt": """Phishing Pattern: Malicious Attachments
Some phishing emails rely on malicious attachments (invoices, receipts, or 
documents) rather than links. Unexpected attachments, especially with 
executable extensions or requests to "enable macros", are common vectors 
for malware delivery alongside social engineering tactics.""",

    "17_social_engineering_tactics.txt": """Detection Concept: Social Engineering Tactics
Phishing relies heavily on psychological manipulation rather than technical 
exploits alone. Common tactics include creating urgency, invoking 
authority (pretending to be IT support or a company executive), and 
exploiting fear (threats of account loss or legal action) to bypass 
rational scrutiny.""",

    "18_trust_score_concept.txt": """Detection Concept: Trust Scoring
A trust score aggregates multiple risk signals (domain age, brand 
similarity, HTTPS presence, redirect behavior, language patterns) into a 
single interpretable metric. Lower scores indicate higher risk. Trust 
scoring allows systems to communicate confidence levels rather than binary 
safe/unsafe labels alone.""",

    "19_explainable_ai_security.txt": """Detection Concept: Explainable Security Reporting
Effective phishing detection systems should provide clear reasoning for 
their verdicts rather than simple binary labels. Explaining which specific 
signals (e.g., domain mismatch, urgency language, missing HTTPS) 
contributed to a decision helps users understand and trust the system's 
output, and supports better security awareness.""",

    "20_general_email_safety_tips.txt": """General Guidance: Email Safety Best Practices
Users should avoid clicking links in unsolicited emails, verify sender 
domains carefully, never share passwords or OTPs via email, hover over 
links to preview the actual destination before clicking, and contact 
organizations directly through official channels (not links in the email) 
when in doubt about a message's legitimacy.""",
}

for filename, content in docs.items():
    with open(f"rag/knowledge_base/{filename}", "w", encoding="utf-8") as f:
        f.write(content.strip())

print(f"Created {len(docs)} documents in rag/knowledge_base/")
