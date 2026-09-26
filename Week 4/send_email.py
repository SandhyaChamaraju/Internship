import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def send_automated_email():
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 465
    SENDER_EMAIL = os.getenv("MY_EMAIL_ADDRESS", "sandhyachamaraju@gmail.com")
    SENDER_PASSWORD = os.getenv(
        "MY_APP_PASSWORD", "fqjb iyqa zppm eihi"
    )
    RECIPIENT_EMAIL = "recipient_address@example.com"

    message = MIMEMultipart()
    message["From"] = SENDER_EMAIL
    message["To"] = RECIPIENT_EMAIL
    message["Subject"] = "Automated System Alert: Task Complete"
    body_text = """
    Hello,

    This is an automated notification sent via your Python automation script.
    The scheduled operations have completed successfully.

    Best regards,
    Python Automation Bot
    """
    message.attach(MIMEText(body_text, "plain"))
    try:
        print("Connecting to secure SMTP server...")
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            print("Authentication successful. Sending message...")

            server.send_message(message)

        print("✔ Email sent successfully!")

    except smtplib.SMTPAuthenticationError:
        print(
            "❌ Authentication failed. Verify your App Password is correct."
        )
    except Exception as e:
        print(f"❌ Failed to dispatch email. Error details: {e}")


if __name__ == "__main__":
    send_automated_email()
    
