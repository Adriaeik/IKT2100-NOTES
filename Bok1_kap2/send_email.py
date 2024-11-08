import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl

# E-postinnstillinger
smtp_server = 'smtp.mail.yahoo.com'
smtp_port = 465  # Bruk 465 for SSL
sender_email = 'adrianpython28@yahoo.com'
sender_password = 'Rbk.lfc123'
receiver_email = 'eikeland.adrian.valaker@gmail.com'

# Opprett ein e-postmelding
subject = 'Test E-post'
body = 'Dette er ein test e-post sendt frå eit Python-skript!'

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# SSL-kontekst
context = ssl.create_default_context()

server = None
try:
    # Bruk SMTP med SSL
    server = smtplib.SMTP_SSL(smtp_server, smtp_port, context=context)
    server.login(sender_email, sender_password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    print('E-post sendt!')

except Exception as e:
    print(f'Ein feil oppstod: {e}')

finally:
    if server:
        try:
            server.quit()
        except Exception as e:
            print(f'Klarte ikkje å avslutte forbindelsen på riktig måte: {e}')

## 2F928UZ9T6R264VC5QLWE3E8, fra TWILIO
# sender_email = 'adrianpython28@yahoo.com'
# sender_password = '********'
# receiver_email = 'eikeland.adrian.valaker@gmail.com'