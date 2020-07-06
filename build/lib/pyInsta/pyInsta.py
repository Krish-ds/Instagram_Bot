#webdriver is used to get request open links and place to do all cool stuff 
from selenium import webdriver
#module to input words and also used to enter,space, etc., to desired fields
from selenium.webdriver.common.keys import Keys
#randon module is imported for giving random time between each operations so that it wouldn't look like a bot
from random import *
import time #its used to wait for previous function to get finished
path = "C:\Program Files\chromedriver.exe" #path of chrome driver installed
driver = webdriver.Chrome(path)#opens a chrome used for testing purpose 
driver.get('https://www.instagram.com')
def opens(username,password):
    time.sleep(randint(3,6))
    search = driver.find_element_by_name('username')
    #enter tour Username or e-mail ID here 
    search.send_keys(username)
    time.sleep(randint(2,7))
    #Enter your password
    search = driver.find_element_by_name('password')
    #send keys are used to give any keyboard key to particular web_element
    search.send_keys(password)
    time.sleep(randint(1,3))
    search.send_keys(Keys.ENTER) #presses enter key automatically 
    time.sleep(randint(4,9))
def login_no_info(username,password):#logs into Instagram but denies basic permiss
    time.sleep(randint(3,6))
    search = driver.find_element_by_name('username')
    #enter tour Username or e-mail ID here 
    search.send_keys(username)
    time.sleep(randint(2,7))
    #Enter your password
    search = driver.find_element_by_name('password')
    #send keys are used to give any keyboard key to particular web_element
    search.send_keys(password)
    time.sleep(randint(1,3))
    search.send_keys(Keys.ENTER) #presses enter key automatically 
    time.sleep(randint(4,9))
    # Does not save login info 
    search = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
    time.sleep(randint(3,6))
    # Does not on turn on notifications
    search = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
    time.sleep(randint(2,5))
def login_info(username,password):
    #opens with post notfications while you're surfing in Instagram
    time.sleep(randint(3,6))
    search = driver.find_element_by_name('username')
    #enter tour Username or e-mail ID here 
    search.send_keys(username)
    time.sleep(randint(2,7))
    #Enter your password
    search = driver.find_element_by_name('password')
    #send keys are used to give any keyboard key to particular web_element
    search.send_keys(password)
    time.sleep(randint(1,3))
    search.send_keys(Keys.ENTER) #presses enter key automatically 
    time.sleep(randint(4,9))
    # Save login info
    search = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/section/div/button').click()
    time.sleep(randint(3,6))
    # Turn on post notifications
    search = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[1]').click()
    time.sleep(randint(2,5))
def logout():
    try:
        # Goto profile
        search = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]').click()
        time.sleep(randint(2,6))
        # Click settings
        search = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div/button').click()
        time.sleep(randint(1,3))
        # Logout
        search = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/button[9]').click()
        time.sleep(randint(2,4))
    except:
        exit_post()
        time.sleep(randint(2,5))
         # Goto profile
        search = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]').click()
        time.sleep(randint(2,6))
        # Click settings
        search = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div/button').click()
        time.sleep(randint(1,3))
        # Logout
        search = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/button[9]').click()
        time.sleep(randint(2,4))
def like(): 
    try:
        search = driver.find_element_by_class_name('wpO6b ').click()
        time.sleep(randint(2,5))
    except:
        logout()
        close_all()
        raise NotImplementedError('No post is selected to like')
def unlike(): 
    try:
        # Works only when you like the post
        search = driver.find_element_by_class_name('wpO6b ').click()
        time.sleep(randint(2,5))
    except:
        logout()
        close_all()
        raise NotImplementedError('No post is selected to dislike')
def follow():
    try:
        search = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
        time.sleep(randint(2,7))
    except:
        logout()
        close_all()
        raise NotImplementedError('No post is selected to follow')
def unfollow():
    try:
        # Unfollow works only when you follow the account
        search = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
        time.sleep(randint(1,3))
        search = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[1]').click()
        time.sleep(randint(1,4))
    except:
        logout()
        close_all()
        raise NotImplementedError('No post is selected to unfollow or Selected page is not followed')
def explore():
    try:
        search = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]').click()
        time.sleep(randint(5,10))
    except:
        logout()
        close_all()
        raise NotImplementedError('You have selected a post or settings option is enabled')
def home():
    try:
        search = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[1]').click()
        time.sleep(randint(5,10))
    except:
        logout()
        close_all()
        raise NotImplementedError('You have selected a post or settings option is enabled')
def msg():
    try:
        search = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]').click()
        time.sleep(randint(3,8))
    except:
        logout()
        close_all()
        raise NotImplementedError('You have selected a post or settings option is enabled')
def first_post():
    try:
    # Selects first post in explore and it must be implemented after explore command
        search = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/div/div[1]/div[2]').click()
        time.sleep(randint(2,5))
    except:
        logout()
        close_all()
        raise NotImplementedError('Explore command should be implemented')        
def account():
    try:
    # Selects first post in explore and it must be implemented after explore command
        search = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/div').click()
        time.sleep(randint(2,5))
    except:
        logout()
        close_all()
        raise NotImplementedError('first_post() command should be implemented')   
def profile():
    try:
        search = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]').click()
        time.sleep(randint(1,4))
    except:
        logout()
        close_all()
        raise NotImplementedError('You have selected a post or settings option is enabled')
def settings():
    try:
        # Goto profile
        search = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div/button').click()
        time.sleep(randint(3,7))
        # Goto Settings
        search = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]').click()
        time.sleep(randint(2,6))
    except:
        logout()
        close_all()
        raise NotImplementedError('You have selected a post')
def exit_post():
    search = driver.find_element_by_xpath('/html/body/div[4]/div[3]/button').click()
    time.sleep(randint(1,4))
def end_scroll():
    driver.execute_script("window.scrollTo(0, 720)") 
    time.sleep(randint(4,10))
def init_scroll():
    driver.execute_script("window.scrollTo(720, 0)") 
    time.sleep(randint(4,10))
def pd():
    driver.send_keys(Keys.PAGE_DOWN)
    time.sleep(randint(1,8))
def pu():
    driver.send_keys(Keys.PAGE_UP)
    time.sleep(randint(1,8))
def ref():
    # Refreshes the instagram post.. better to use while in exlpore
    driver.refresh()
    time.sleep(randint(2,6))
def screentime(x):
    time.sleep(x) # Adjust your #SCREENTIME# on Instagram... 
def close_all():
    driver.delete_all_cookies()#Deletes all cookies on exit 
    driver.quit()





