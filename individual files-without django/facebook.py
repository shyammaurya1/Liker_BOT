from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class liker_Bot:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.driver=webdriver.Firefox()
############################# Facebook ##############################################
    def Flogin(self):
        driver=self.driver
        driver.get('https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=110') 
        time.sleep(3) 

        username_box = driver.find_element_by_id('email') 
        username_box.send_keys(self.username) 
        time.sleep(1)
  
        password_box = driver.find_element_by_id('pass') 
        password_box.send_keys(self.password) 
        login_box = driver.find_element_by_id('loginbutton') 
        login_box.click() 
        time.sleep(3)

    def Flike(self,tag):
        driver=self.driver
        driver.get('https://www.facebook.com/search/top/?q='+tag+"&epa=SEARCH_BOX")
        time.sleep(3)

#password="@mytestingpwd1"
tag="quote"
username=input("enter the username : ")
password=input("enter the password : ")
ed=liker_Bot(username,password)
#tag=input("enter the hashtag (eg.quote,happy) : ")   
ed.Flogin()  
ed.Flike(tag)
 



