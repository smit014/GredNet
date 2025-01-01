import smtplib
from email.mime.text import MIMEText
from src.config import Config
from fastapi.responses import JSONResponse

#$ Utility function to send email.
def send_email(to_email: str, subject: str, body: str):
    try:
        # Email configuration
        smtp_server = Config.MAIL_HOST
        smtp_port = Config.MAIL_PORT
        sender_email = Config.MAIL_USERNAME
        sender_password = Config.MAIL_PASSWORD

        # Email message
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = to_email

        # Send email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, msg.as_string())

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "status": False,
                "code": 500,
                "message": f"Unexpected error: {str(e)}",
                "data": {},
            },
        )
