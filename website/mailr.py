import smtplib
from email.message import EmailMessage

def kirimEmail(to,subject,body):
    msg = EmailMessage()
    msg.set_content(body)

    msg['Subject'] = subject
    msg['From'] = 'vms.info@sg.panasonic.com'
    msg['To'] = to

    # Send the message via our own SMTP server.
    server = smtplib.SMTP_SSL('157.8.1.154', 465)
    # server.login("info@siberkolosis.com", "grunge75")
    server.send_message(msg)
    server.quit()

# kirimEmail('info@siberkolosis.com','ditolak','selamat anda di tolak')

