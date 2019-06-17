from behave import given, when, then
from framework.webapp import webapp
from pages.challenge import challenge
import time 

#### NEGATIVE 1 ####

@given('load the website for register without filling in required fields')
def open_site(context):
    webapp.load_website()

@when('I click Register without filling fields')
def use_commad(context):
    time.sleep(2)
    challenge.enter_form()
    time.sleep(1)
    challenge.page_down()
    time.sleep(1)
    challenge.data_send()
    time.sleep(1)

@then('I see the error message')
def validated_send(context):
    challenge.validated_alert_error()
    challenge.tearDown()

#### NEGATIVE 2 ####

@given('load the website for fill in wrong email')
def open_site(context):
    webapp.load_website()

@when('fill in wrong email')
def use_commad(context):
    time.sleep(2)
    challenge.enter_form()
    time.sleep(1)
    challenge.typing_email_error()
    time.sleep(1)

@then('I see the error message about in wrong email')
def validated_send(context):
    challenge.error_message_email()
    challenge.tearDown()

#### NEGATIVE 3 ####

@given('load the website for fill in wrong filds born')
def open_site(context):
    webapp.load_website()

@when('fill in wrong filds born')
def use_commad(context):
    time.sleep(2)
    challenge.enter_form()
    time.sleep(1)
    challenge.select_born_error()
    time.sleep(1)
    
@then('I see the error message about in wrong filds born')
def validated_send(context):
    challenge.error_message_born()
    challenge.tearDown()