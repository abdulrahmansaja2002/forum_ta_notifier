# from xvfbwrapper import Xvfb
import time
from selenium import webdriver
import json
from utils import ForumPage, send_email, send_multiple_email
from pyvirtualdisplay import Display

# display = Display(visible=0, size=(800, 600))

# display = Xvfb()
# display.start()


# Load data from json
data = {}
with open('data.json') as json_file:
    data = json.load(json_file)

login_url = 'https://scele.cs.ui.ac.id/login/index.php?'
forum_ta_url = 'https://scele.cs.ui.ac.id/mod/forum/view.php?id=3'
TIME_TO_REFRESH = 5

browser = webdriver.Chrome()

# Login
browser.get(login_url)
username_input = browser.find_element(by='id', value='username')
password_input = browser.find_element(by='id', value='password')

username_input.send_keys(data['username'])
password_input.send_keys(data['password'])
login_button = browser.find_element(by='id', value='loginbtn')
login_button.click()

# Go to forum TA
forum_ta = ForumPage(browser, forum_ta_url)
# browser.get(forum_ta_url)

# Refresh page every 1 second
# TODO: Check if there is new post
for _ in range(20):
    time.sleep(TIME_TO_REFRESH)
    forum_ta.refresh()
    if forum_ta.is_updated():
        print("Ada post baru!!!")
        break
    else:
        print("Belum ada post baru")


# Send email (TEST)
notify_email = "abdul.rahman.saja2002@gmail.com"

message = "Forum TA sudah ada yang post"
subject = "Forum TA ada yang post"

send_email(subject, message, notify_email)


# close browser
browser.quit()

# display.stop()
