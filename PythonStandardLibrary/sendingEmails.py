from email.mime.multipart import MIMEMultipart  # multiimportemailextension
from email.mime.text import MIMEText
import smtplib
from pathlib import Path
from string import Template

template = Template(Path("template.html").read_text())


message = MIMEMultipart()
message["from"] = "amalienovember@gmail.com"
message["to"] = "test@gmail.com"
message["subject"] = "this is a test"
message.attach(MIMEText(template.substitute({"name": "amalie"}), "html"))


with smtplib.SMTP(host="smtp.gmail.com", port=578) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("testuser@gmail.com", "lalalala")
    smtp.send_message(message)

    print("sent")
