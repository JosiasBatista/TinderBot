from selenium import webdriver
from time import sleep

from login import email
from login import password


class TinderBot(): 
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
         self.driver.get('https://tinder.com')

         sleep(4)

         fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')
         fb_btn.click()

         base_window = self.driver.window_handles[0]
         popup = self.driver.switch_to_window(self.driver.window_handles[1])

         sleep(1)
         email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
         email_in.send_keys(login())
         
         pw = bot.driver.find_element_by_xpath('//*[@id="pass"]')
         pw.send_keys(password())

         login_btn = bot.driver.find_element_by_xpath('//*[@id="u_0_0"]')
         login_btn.click()
         
         self.driver.switch_to_window(base_window)

         sleep(2)
         popup_1 = bot.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
         popup_1.click()
         
         popup_2 = bot.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
         popup_2.click()


    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
        like_btn.click()


    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
        dislike_btn.click()


    def auto_swipe(self):
        from random import random
        left_count, right_count = 0, 0

        while True:
            sleep(2)

            try:
                rand = random()

                if rand < .63:
                    self.like()
                    right_count += 1
                    print('{}th right swipe'.format(right.count))
                    break
                else:
                    self.dislike()
                    left_count += 1
                    print('{}th left swipe'.format(left_count))
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    try:
                        self.close_match()
                    except Exception:
                        pass

    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()


    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

bot = TinderBot()
bot.login()
