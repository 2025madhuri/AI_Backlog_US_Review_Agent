import smtplib
from email.message import EmailMessage


def send_email_with_attachment(
    sender_email,
    app_password,
    receiver_emails,
    subject,
    body,
    attachment_path
):
    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = ", ".join(receiver_emails)
    msg["Subject"] = subject

    msg.set_content(body)

    with open(attachment_path, "rb") as file:
        file_data = file.read()
        file_name = attachment_path.split("/")[-1]

    msg.add_attachment(
        file_data,
        maintype="application",
        subtype="pdf",
        filename=file_name
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)

    return "Email sent successfully"