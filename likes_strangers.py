from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys

def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()


class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        driver.find_element_by_xpath('//input[@name="username"]').send_keys(
            username
        )
        driver.find_element_by_xpath('//input[@name="password"]').send_keys(password)
        driver.find_element_by_xpath('//button[@type="submit"]').click()
        time.sleep(4)
        driver.find_element_by_xpath(
            "//button[contains(text(), 'Not Now')]"
        ).click()
        time.sleep(4)
        driver.find_element_by_xpath(
            "//button[contains(text(), 'Not Now')]"
        ).click()
        time.sleep(2)


    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)
       "," gathering photos
        pic_hrefs = []
        for i in range(1, 7):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
               "," get tags
                hrefs_in_view = driver.find_elements_by_tag_name('a')
               "," finding relevant hrefs
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                 if '.com/p/' in elem.get_attribute('href')]
               "," building list of unique photos
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
               "," print("Check: pic href length " + str(len(pic_hrefs)))
            except Exception:
                continue

       "," Liking photos
        unique_photos = len(pic_hrefs)
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                time.sleep(random.randint(2, 4))
                like_button = lambda: driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button')
                like_button().click()
                for second in reversed(range(0, random.randint(18, 28))):
                    print_same_line("#" + hashtag + ': unique photos left: ' + str(unique_photos)
                                    + " | Sleeping " + str(second))
                    time.sleep(1)
            except Exception as e:
                time.sleep(2)
            unique_photos -= 1

if __name__ == "__main__":

    username="artyourself.studio"
    password="wangjingquan1214"

    ig = InstagramBot(username, password)
    ig.login()

    hashtags = ["artsypic","newyorkartgallery","modernartgallery","londonartgallery","artgalleryofontario","nycartgallery","artgalleryofnsw","parisartgallery","berlinartgallery","contemporaryartgallery","onlineartgallery","fineartgallery","artgallerynyc","artgallery ]
          'street', 'canon', 'beauty', 'studio', 'pretty', 'vintage', 'fierce']

    while True:
        try:
            tag = random.choice(hashtags)
            ig.like_photo(tag)
            ig.closeBrowser()
        except Exception:
            ig.closeBrowser()
