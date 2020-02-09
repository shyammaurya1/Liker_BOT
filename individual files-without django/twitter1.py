import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(3)
     
        email = bot.find_element_by_class_name('text-input')
        password = bot.find_element_by_name('session[password]')
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(5)
    
    def like(self,hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typed_query&f=image')
        time.sleep(3)

        bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(3)
        #liking starts here.......
        for _ in range(1,4):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            
            heart=bot.find_element_by_xpath('//div[contains(@data-testid,"like")]')
            heart.click()
            time.sleep(5)
            print("yeee....!")



            

T= TwitterBot('shyammaurya395@gmail.com','@mytestingpwd1') 
T.login()
T.like("beauty")