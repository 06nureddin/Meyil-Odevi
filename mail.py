import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "muharremnureddin@gmail.com"
password = "hyznbkanpfxmfihx"
toaddr = "assasinpattis1@gmail.com"

# Instance of MIMEMultipart
message = MIMEMultipart()

# Storing the senders email
message["From"] = fromaddr

# Storing the recivers email
message["To"] = toaddr

# Storing the subject
message["subject"] = "Mail ödevi"

body = "Mail ödevi"

message.attach(MIMEText(body,"plain"))

s = smtplib.SMTP("smtp.gmail.com", 587)

s.starttls()

s.login(fromaddr, "hyznbkanpfxmfihx")

text = message.as_string()

s.sendmail(fromaddr, toaddr, text)

s.quit()