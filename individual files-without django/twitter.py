import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def T_login(self):
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
    
    def T_like(self,hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typed_query&f=image')
        time.sleep(3)

        bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(3)
        #liking starts here.......
        c=0
        for _ in range(1,8):
            
            
            
            bot.find_element_by_xpath('//div[contains(@class,"css-1dbjc4n r-1awozwy r-1iusvr4 r-16y2uox r-5f2r5o r-1gmbmnb r-bcqeeo")]').click()
            try:
                c=c+1
                time.sleep(3)
                heart=bot.find_element_by_xpath('//div[contains(@data-testid,"like")]')
                heart.click()
                time.sleep(2)
                bot.back()
                
            except:
                c=c-1
                continue
            #bot.execute_script("window.history.go(-1)")
           
            time.sleep(5)
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(3)
                
           
        print("liked : ",c)



            

T= TwitterBot('shyammaurya395@gmail.com','@mytestingpwd1') 
T.T_login()
T.T_like("cat")