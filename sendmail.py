import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

msg = MIMEMultipart()
msg['From'] = 'flakesns@gmail.com'
msg['To'] = 'client@yahoo.com'
msg['Subject'] = 'Basic SMTP email with Python'
message = 'Here is the basic text in the email body'
msg.attach(MIMEText(message))

mailserver = smtplib.SMTP('mail.gmail.com',587)
# identify ourselves to smtp gmail client
mailserver.ehlo()

# re-identify ourselves as an encrypted connection
mailserver.ehlo()
mailserver.login('flakesns@gmail.com', 'email_password_here')

mailserver.sendmail('flakesns@gmail.com','client@yahoo.com',msg.as_string())

mailserver.quit()
