import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class LinkedINBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def L_login(self):
        bot = self.bot
        bot.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
        time.sleep(3)
     
        email = bot.find_element_by_xpath("//input[@id='username']")
        password = bot.find_element_by_xpath("//input[@id='password']")
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(5)
    
    def L_like(self,hashtag):
        bot = self.bot
        bot.get('https://www.linkedin.com/search/results/content/?keywords='+ hashtag +'&origin=SWITCH_SEARCH_VERTICAL')
        time.sleep(3)
        
        c=0
        for i in range(0,8):
            
            try:    
                like=bot.find_element_by_xpath('//*[@class="reactions-react-button ember-view"]')
                like.click()
                c=c+1
                time.sleep(3)
            except:
                c=c-1
                continue   
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(5)
 
        print("No. of likes : ",c)

        

L= LinkedINBot('shyammaurya395@gmail.com','@mytestingpwd1') 
L.L_login()
L.L_like("job")