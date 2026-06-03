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

    subject = "Weekly Fund Requirement"

    body = f"""
Namaskaram {name},

Please share your weekly requirement using the link below:

{form_link}

Pranam,
Pratik
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