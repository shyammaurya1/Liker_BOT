from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys




class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
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


    def I_like(self,hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(3)

        #collect posts.......
        lst = []
        for i in range(1, 7):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                
                hv = driver.find_elements_by_tag_name('a')
               
                hv = [elem.get_attribute('href') for elem in hv
                                 if '.com/p/' in elem.get_attribute('href')]
              
                # [lst.append(href) for href in hv if href not in lst]
                for href in hv:
                    if href not in lst:
                        lst.append(href)

            except Exception:
                continue

        # Like posts....
        photos = len(lst)
        for pic in lst:
            driver.get(pic)
            time.sleep(3)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                time.sleep(random.randint(2, 4))
                like_button = driver.find_element_by_xpath('//span[@aria-label="Like"]').click()
               
                
            except Exception as e:
                time.sleep(3)
            photos -= 1


if __name__ == "__main__":

    username = "humble__bubble"
    password = "@mytestingpwd1"


    ig = InstagramBot(username, password)
    ig.I_login()


    while True:
        try:
            
            tag="AI"
            ig.I_like(tag)
        except Exception:
            ig.closeBrowser()
            time.sleep(60)
            ig = InstagramBot(username, password)
            ig.I_login()
