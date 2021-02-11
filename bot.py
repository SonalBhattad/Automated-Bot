from selenium import webdriver                                
from selenium.webdriver.chrome.options import Options
import time
import re
import random

driver = webdriver.Chrome()
options=Options()
options.add_argument("--disable-notifications")   #disables all popup notifications

class Facebook():
    def __init__(self,mail,passw):
        self.mail = mail
        self.passw = passw

    def info(self):                       
        driver.get('https://facebook.com')           #opens up the fb homepage
        username = driver.find_element_by_id('email')
        time.sleep(2)
        username.send_keys(self.mail)                     #passing your mailid entered while calling this function.
    
        password = driver.find_element_by_id('pass')
        time.sleep(2)
        password.send_keys(self.passw)                    #passing your password entered while calling this function.

        submit = driver.find_element_by_id("u_0_b")      #finds the login button
        submit.click()
    
    def accept_req(self):
        time.sleep(2)
        driver.get('https://facebook.com/friends') #opens up the fb friend requests page
        time.sleep(5)
        accept = driver.find_element_by_xpath('//*[@aria-label="Confirm"]')   #find button that says confirm
        driver.implicitly_wait(10)   #waiting until browser finds the required path
        accept.click()    #accepts the request by clicking on confirm button
        
    def Status(self):
        time.sleep(2)
        driver.get('https://facebook.com/me') #me=your profile name 
        time.sleep(2)
        message = driver.find_element_by_class_name("a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7").click() #find what's on your mind text box
        message.send_keys("It's a nice day")     #enter your text
        message.driver.find_element_by_xpath('//*[@aria-label="Post"]').click()  #click on post to update your status
        
    def getposts(source):
        post_id = re.findall('post_fbid.*?}', source)    #finds all the recent posts
        if post_id:
            return post_id[0].split(':')[-1][:-1]   #gets the most recent post (1)
        else:
            return '0'

    def comment_on_post(self):
        target_user = random.choice(config['profiles_to_comment'])
        driver.get(target_user)
        time.sleep(2)
        post_id = get_recent_post(driver.page_source)
        driver.get(target_user.replace('facebook', 'm.facebook') + f'posts/{post_id}')
        commentbox = driver.find_element_by_id('composerInput')  #fb post comment box has composerInput id
        commenbox.click()
        commentbox.send_keys("hello")  #your text
        time.sleep(2)
        send = find_element_by_tag_name('button')[0]  #finds the post button
        send.click()
        
logininfo = Facebook("your email","your password")   #enter your email id & password
logininfo.info()
print("You are logged in!")
time.sleep(10)         #wait because the page may take sometime to load 
logininfo.accept_req()
print("Friend request accepted")
time.sleep(10)
logininfo.status()
print("Status updated successfully")
time.sleep(10)
comment_on_post()
print("Comment added")
time.sleep(5)
driver.quit()   #exit the browser
