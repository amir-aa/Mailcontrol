import smtplib,ssl
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
SMTPSERVER="smtp.zoho.com"
SMTPPORT=587

    
def SendEmail(From:str,To:str,Password:str):

   
    message=EmailMessage()
    
    message.set_content(f"""TEXT""")
    message["Subject"]="Welcome to site"
    message['From'] = From
    message['To'] = To
    context = ssl.create_default_context()
    with smtplib.SMTP(SMTPSERVER, SMTPPORT) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(From, Password)
        server.sendmail(From, To, message.as_string())

