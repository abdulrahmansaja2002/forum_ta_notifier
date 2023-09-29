import smtplib
import json

with open('data.json') as json_file:
    data = json.load(json_file)

smtp_server = data['smtp_server']
smtp_user = data['smtp_user']
smtp_password = data['smtp_password']
smtp_port = data['smtp_port']



def send_email(subject, message, receiver):
    try:
        print("Sending email")
        s = smtplib.SMTP(smtp_server, smtp_port)
        s.starttls()
        s.login(smtp_user, smtp_password)
        s.sendmail(smtp_user, receiver, f"Subject: {subject}\n\n{message}")
        s.quit()
        print("Email sent")
    except Exception as e:
        print(e)

def send_multiple_email(subject, message, receivers):
    s = smtplib.SMTP(smtp_server, smtp_port)
    s.starttls()
    s.login(smtp_user, smtp_password)
    for receiver in receivers:
        s.sendmail(smtp_user, receiver, f"Subject: {subject}\n\n{message}")
    s.quit()
