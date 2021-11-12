import smtplib

def kirimEmail(to,subject,body):
    msg = EmailMessage()
    msg.set_content(body)

    msg['Subject'] = subject
    msg['From'] = 'info@siberkolosis.com'
    msg['To'] = to

    # Send the message via our own SMTP server.
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("me@gmail.com", "password")
    server.send_message(msg)
    server.quit()


'''
def kirimEmail(to,subject,body):
    gmail_user = 'info@siberkolosis.com'
    gmail_password = 'grunge75'

    sent_from = gmail_user
    to = [to]
    subject = subject
    body = body

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        smtp_server = smtplib.SMTP_SSL('mail.privateemail.com', 465)
        smtp_server.ehlo()
        # smtp_server.starttls()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to, email_text)
        smtp_server.close()
        print ("Email sent successfully!")
    except Exception as ex:
        print ("Something went wrong….",ex)
'''