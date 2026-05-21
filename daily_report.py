import os
from dotenv import load_dotenv

from jira_engine import generate_report
from pdf_generator import generate_pdf_report
from email_sender import send_email_with_attachment

load_dotenv()

report = generate_report()
pdf_file = generate_pdf_report(report)

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")

RECEIVER_EMAILS = os.getenv("RECEIVER_EMAILS", "").split(",")

SUBJECT = "Daily AI Delivery Intelligence Report"

BODY = """
Hello Team,

Please find attached the latest AI Delivery Intelligence Report.

Regards,
AI Delivery Intelligence Agent
"""

result = send_email_with_attachment(
    sender_email=SENDER_EMAIL,
    app_password=APP_PASSWORD,
    receiver_emails=RECEIVER_EMAILS,
    subject=SUBJECT,
    body=BODY,
    attachment_path=pdf_file
)

print(result)