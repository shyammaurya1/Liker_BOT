from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys


class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
       # self.driver = webdriver.Firefox()
        self.driver=webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    def I_login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(3)
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(3)

        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)

        pwd = driver.find_element_by_xpath("//input[@name='password']")
        pwd.clear()
        pwd.send_keys(self.password)
        pwd.send_keys(Keys.RETURN)
        time.sleep(3)


    def I_like(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(3)

        # gathering photos
        pic_hrefs = []
        for i in range(1, 7):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                # get tags
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                # finding relevant hrefs
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                 if '.com/p/' in elem.get_attribute('href')]
                # building list of unique photos
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
                # print("Check: pic href length " + str(len(pic_hrefs)))
            except Exception:
                continue

        # Liking photos
        unique_photos = len(pic_hrefs)
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            time.sleep(3)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                time.sleep(random.randint(2, 4))
                like_button = lambda: driver.find_element_by_xpath('//span[@aria-label="Like"]').click()
                like_button().click()
                for second in reversed(range(0, random.randint(18, 28))):
                    print_same_line("#" + hashtag + ': unique photos left: ' + str(unique_photos)
                                    + " | Sleeping " + str(second))
                    time.sleep(1)
            except Exception as e:
                time.sleep(3)
            unique_photos -= 1

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


#########Extra functions##################

def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()








##############calling##################

inp=int(input("choose any one :\n click 1 for Instagram \n click 2 for twitter \n click 3 for linkedIN \n Entered : "))
if inp==1:
    if __name__ == "__main__":
        username = "humble__bubble"
        password = "@mytestingpwd1"
    #username=input("enter your username : " )
    #  password=input("enter your password : ")


        ig = InstagramBot(username, password)
        ig.I_login()

        hashtags=['goodvibes','Ai']
        while True:
            try:
                # Choose a random tag from the list of tags
                tag = random.choice(hashtags)
                ig.I_like(tag)
            except Exception:
                ig.closeBrowser()
                time.sleep(60)
                ig = InstagramBot(username, password)
                ig.I_login()



elif inp==2:
    T= TwitterBot('shyammaurya395@gmail.com','@mytestingpwd1') 
    T.T_login()
    T.T_like("cat")

elif inp==3:
    L= LinkedINBot('shyammaurya395@gmail.com','@mytestingpwd1') 
    L.L_login()
    L.L_like("job")

