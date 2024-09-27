"""
Selenium - Automating tasks in the browser (Login and logout github)
"""
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

class ChromeAuto:
    def __init__(self):
        self.driver_path = "chromedriver.exe"
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--profile-directory=1')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def click_sign_in(self):
        try:
            btn_sign_in = self.chrome.find_element(By.LINK_TEXT,'Sign in')
            btn_sign_in.click()

        except Exception as e:
            print('Error when clicking Sign in:', e)


    def acess(self, site):
        self.chrome.get(site)

    def exiting(self):
        self.chrome.quit()

    def click_profile(self):
        try:
            profile = self.chrome.find_element(By.CSS_SELECTOR, 'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details')
            profile.click()
        except Exception as e:
            print('Error when clicking profile:', e)

    def do_logout(self):

        try:
            logout = self.chrome.find_element(By.CSS_SELECTOR, 'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > form > button')
            logout.click()
        except Exception as e:
            print('Error when logging out:', e)

    def verify_user(self, user):
        profile_link = self.chrome.find_element(By.CLASS_NAME, 'user-profile-link')
        profile_link_html = profile_link.get_attribute('innerHTML')
        assert user in profile_link_html

    def do_login(self):
        try:
            input_login = self.chrome.find_element(By.ID, 'login_field')
            input_password = self.chrome.find_element(By.ID, 'password')
            btn_login = self.chrome.find_element(By.NAME, 'commit')
            input_login.send_keys('YOUR_LOGIN')
            input_password.send_keys('YOUR_PASSWORD')
            sleep(3)
            btn_login.click()

        except Exception as e:
            print('Error when logging in:',e)


if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acess('https://github.com/')

    chrome.click_profile()
    chrome.do_logout()

    chrome.click_profile()

    chrome.click_sign_in()
    chrome.do_login()
    chrome.verify_user('YOUR_USER')


    sleep(30)
    chrome.exiting()
