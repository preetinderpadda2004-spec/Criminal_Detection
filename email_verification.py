import smtplib
from email.message import EmailMessage

def sendEmail(to, message, subject):
    try:
        msg = EmailMessage()
        msg.set_content(message)
        msg['Subject'] = subject
        msg['To'] = to
        msg['From'] = 'vmm.testing.email2@gmail.com'
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('vmm.testing.email2@gmail.com', 'tirllvbbhctznive')

        server.send_message(msg)
        print('Mail Sent')
        server.quit()
        return True
    except:
        return False