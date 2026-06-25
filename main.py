import pandas as pd
import smtplib
from email.mime.text import MIMEText
import os

#gmail_email = os.getenv("GMAIL_EMAIL")
#gmail_password = os.getenv("GMAIL_APP_PASSWORD")

gmail_email = "pratikbhatkulkar1957@gmail.com"
gmail_password = "ndkj gigs eftr fwsh"

df = pd.read_csv("emails.csv")

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(gmail_email, gmail_password)
FORM_BASE = "https://docs.google.com/forms/d/e/1FAIpQLSdYIvexHYQbncVSnvyZx7A6wm8Xojb7m_IRL7mVghLNgKw-LA/viewform"
def create_form_link(name, department):
    return f"{FORM_BASE}?entry.1045781291={name}&entry.2005620554={department}"

for _, row in df.iterrows():
    name = row["Name"]
    email = row["Email"]
    department = row["Department"]

    form_link = create_form_link(name, department)

    subject = " Fund Requirement Form - High-Value Payment Details"

    body = f"""
Namaskaram {name},

As part of our fund planning process and to ensure timely processing of payments, Finance is collecting details of high-value payment requirements expected during the upcoming period.

Request you to fill in this Google Form with details of all payment requests with details of all payment requests from your department/team that exceed the limits specified below. This exercise will help us plan funds in advance and streamline the payment process.

Entity	Bill Payment/ Advance Exceeding
Isha Outreach	2 lakhs
Isha Institute of Inner Sciences	2 lakhs
Shri Yogini Trust	5 lakhs
Isha Education	5 lakhs
Isha Foundation	10 lakhs
We request you to submit the details promptly upon receipt of this email.

Thank you for your cooperation.

Pranam,
Trust Finance

{form_link}
"""

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = gmail_email
    msg["To"] = email

    try:
        server.sendmail(gmail_email, email, msg.as_string())
        print(f"Email sent to {email}")

    except Exception as e:
        print("Failed:", email, e)

server.quit()
