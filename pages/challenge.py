from framework.webapp import webapp
from selenium.webdriver.common.keys import Keys
import random
import time 

class Challenge():
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Challenge()
        return cls.instance

    def __init__(self):
        self.driver = webapp.get_driver()
        
    def enter_form(self):
        button_enter = self.driver.find_element_by_xpath('//button[@data-qa="start-button"]')
        button_enter.click()

    def typing_first_name(self):
        first_name = self.driver.find_element_by_xpath('//label[contains(text(), "What\'s your")]/ancestor-or-self::section//input')
        first_name.send_keys('Test')
        button_ok = self.driver.find_element_by_xpath('//button[@data-qa="ok-button-visible deep-purple-ok-button-visible"]')
        button_ok.click()

    def typing_last_name(self):
        number = random.randrange(1000)
        last_name = self.driver.find_element_by_xpath('//label[contains(text(), "Hey Test, nice to meet you.")]/ancestor-or-self::section//input')
        last_name.send_keys(number.__str__())
        button_ok = self.driver.find_element_by_xpath('//button[@data-qa="ok-button-visible deep-purple-ok-button-visible"]')
        button_ok.click()

    def typing_email(self):
        number = random.randrange(1000)
        email = self.driver.find_element_by_xpath('//label[contains(text(), "Which ")]/ancestor-or-self::section//input')
        email.send_keys('jsoaresme+' + number.__str__() +  '@gmail.com')
        button_ok = self.driver.find_element_by_xpath('//button[@data-qa="ok-button-visible deep-purple-ok-button-visible"]')
        button_ok.click()

    def typing_email_error(self):
        email = self.driver.find_element_by_xpath('//label[contains(text(), "Which ")]/ancestor-or-self::section//input')
        email.send_keys('jsoaresme')
        button_ok = self.driver.find_element_by_xpath('//button[@data-qa="ok-button-visible deep-purple-ok-button-visible"]')
        button_ok.click()    

    def select_born(self):
        born = self.driver.find_element_by_xpath('//label[contains(text(), "Where were you born, Test?")]/ancestor-or-self::section//input')
        born.send_keys('Brazil')
        born_brazil = self.driver.find_element_by_xpath('//strong[contains(text(),"Brazil")]')
        born_brazil.click()

    def select_born_error(self):
        born = self.driver.find_element_by_xpath('//label[contains(text(), "Where were you born,")]/ancestor-or-self::section//input')
        born.send_keys('abc123')   

    def data_send(self):
        button_register = self.driver.find_element_by_xpath('//button[@data-qa="submit-button deep-purple-submit-button"]')
        button_register.click()

    def validated_send(self):
        text_sucess = self.driver.find_element_by_xpath('//h1//strong').text
        print(text_sucess)
        assert text_sucess == "create your own"

    def validated_alert_error(self):
        text_error = self.driver.find_element_by_xpath('//section[@data-qa="unfixed-footer"]//div[@font-weight="regular"]').text
        print(text_error)
        assert text_error == "2 answers need completing"

    def error_message_email(self):
        message_error = self.driver.find_element_by_xpath('//div[@data-qa="error-message-visible"]').text
        print(message_error)
        assert message_error == "Hmm…that email doesn't look valid"

    def error_message_born(self):
        message_error = self.driver.find_element_by_xpath('//div[@data-qa="error-message-visible"]').text
        print(message_error)
        assert message_error == "No suggestions found"

    def next_question(self):
        next_question = self.driver.find_element_by_xpath('//button[@data-qa="fixed-footer-navigation-next"]//span')
        next_question.click

    def previous_question(self):
        previous_question = self.driver.find_element_by_xpath('//button[@data-qa="fixed-footer-navigation-previous"]')
        previous_question.click

    def access_powered_by_typeform(self):
        page = self.driver.find_element_by_xpath('//button[@data-qa="fixed-footer-brand-button"]')
        page.click

    def access_report_abuse(self):
        first_name = self.driver.find_element_by_xpath('//label[contains(text(), "What\'s your")]/ancestor-or-self::section//input')
        first_name.send_keys(Keys.PAGE_DOWN)
        email = self.driver.find_element_by_xpath('//label[contains(text(), "Which ")]/ancestor-or-self::section//input')
        email.send_keys(Keys.PAGE_DOWN)
        link = self.driver.find_element_by_link_text('Report abuse')
        link.click
        time.sleep(5)

    def page_down(self):
        page = self.driver.find_element_by_xpath('//label[contains(text(), "Where were you born,")]/ancestor-or-self::section//input')
        page.send_keys(Keys.PAGE_DOWN)

    def tearDown(self):
       self.driver.quit()

challenge = Challenge.get_instance()