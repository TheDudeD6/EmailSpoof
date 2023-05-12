import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def embed_link(word, url):
    return f'<a href="{url}">{word}</a>'

def spoof_email(sender_email, receiver_email, subject, message, spoofed_domain, smtp_server, smtp_port, username, password):
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    html_message = f'<html><body>{message}</body></html>'

    html_message = html_message.replace('raptors', embed_link('raptors', 'URL LINK'))
    html_message = html_message.replace('hack', embed_link('hack', 'URL LINK'))

    msg.attach(MIMEText(html_message, 'html'))

    server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    server.login(username, password)

    num_emails = int(input("Enter the number of emails you want to send: "))
    for _ in range(num_emails):
        server.sendmail(sender_email, receiver_email, msg.as_string())

    server.quit()

spoof_email('SMTP EMAIL', 'RECEIVER', 'Important Message', 'This is a message with embedded links. raptors and hack ', 'spoof.hack.com', 'mail.SMTP.SERVER', PORT, 'USER', 'PASSWORD')
