# from xvfbwrapper import Xvfb
import time
from selenium import webdriver
import json
from utils import send_email, send_multiple_email

# display = Xvfb()
# display.start()

data = {}
with open('data.json') as json_file:
    data = json.load(json_file)

login_url = 'https://scele.cs.ui.ac.id/login/index.php?'
forum_ta_url = 'https://scele.cs.ui.ac.id/mod/forum/view.php?id=3'

browser = webdriver.Chrome()
browser.get(login_url)
username_input = browser.find_element(by='id', value='username')
password_input = browser.find_element(by='id', value='password')

username_input.send_keys(data['username'])
password_input.send_keys(data['password'])
login_button = browser.find_element(by='id', value='loginbtn')
login_button.click()



browser.get(forum_ta_url)
for _ in range(2):
    time.sleep(1)
    browser.refresh()

notify_email = "abdul.rahman.saja2002@gmail.com"

message = "Forum TA sudah ada yang post"
subject = "Forum TA ada yang post"

send_email(subject, message, notify_email)

print(browser.title)

browser.quit()

# display.stop()
