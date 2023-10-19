from datetime import datetime
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


class ForumPage:
    def __init__(self, browser, forum_url='https://scele.cs.ui.ac.id/mod/forum/view.php?id=3'):
        self.browser = browser
        self.forum_ta_url = forum_url
        self.browser.get(self.forum_ta_url)
        self.last_post_date = None
        

    def refresh(self):
        self.browser.refresh()

    def get_title(self):
        return self.browser.title
    
    def is_updated(self):
        first_discussion = self.browser.find_element("class name", 'discussion')
        last_post = first_discussion.find_element("class name", 'lastpost')
        # print(last_post.text)
        post_time = last_post.find_elements('xpath', '*')
        # print(post_time)
        post_time = post_time[-1]
        _, date, time = post_time.text.split(', ')
        date = f"{date}, {time}"
        date_format = "%d %b %Y, %I:%M %p"
        date = datetime.strptime(date, date_format)
        if self.last_post_date is None:
            self.last_post_date = date
            return False
        elif self.last_post_date != date:
            self.last_post_date = date
            return True
        else:
            return False


        
