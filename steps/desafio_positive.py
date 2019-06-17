from behave import given, when, then
from framework.webapp import webapp
from pages.challenge import challenge
import time 

#### POSITIVE 1 ####

@given('load the website for required fields fill')
def open_site(context):
    webapp.load_website()

@when('fill in the required fields')
def use_commad(context):
    time.sleep(2)
    challenge.enter_form()
    time.sleep(1)
    challenge.typing_first_name()
    time.sleep(1)
    challenge.typing_email()
    time.sleep(1)
    challenge.page_down()
    time.sleep(1)
    challenge.data_send()
    time.sleep(1)

@then('required fields sent successfully')
def validated_send(context):
    challenge.validated_send()
    challenge.tearDown()

#### POSITIVE 2 ####

@given('load the website for fill all fields')
def open_site(context):
    webapp.load_website()

@when('fill all fields')
def use_commad(context):
    time.sleep(2)
    challenge.enter_form()
    time.sleep(1)
    challenge.typing_first_name()
    time.sleep(1)
    challenge.typing_last_name()
    time.sleep(1)
    challenge.typing_email()
    time.sleep(1)
    challenge.select_born()
    time.sleep(1)
    challenge.data_send()
    time.sleep(1)

@then('all fields sent successfully')
def validated_send(context):
    challenge.validated_send()
    challenge.tearDown()

#### POSITIVE 3 ####

@given('load the website for click next questions')
def open_site(context):
    webapp.load_website()

@when('I go through all the questions')
def use_commad(context):
    time.sleep(2)
    challenge.enter_form()
    time.sleep(1)
    challenge.next_question()
    time.sleep(1)
    challenge.next_question()
    time.sleep(1)
    challenge.next_question()
    time.sleep(1)
    
@then('I see the questions available')
def validated_send(context):
    challenge.tearDown()

#### POSITIVE 4 ####

@given('load the website for access Powered by typeform')
def open_site(context):
    webapp.load_website()

@when('I click on Powered by typeform')
def use_commad(context):
    time.sleep(2)
    challenge.enter_form()
    time.sleep(1)
    challenge.access_powered_by_typeform()
    
@then('login page opens')
def validated_send(context):
    challenge.tearDown()

#### POSITIVE 5 ####

@given('load the website for Access Report abuse')
def open_site(context):
    webapp.load_website()

@when('I click on Report abuse')
def use_commad(context):
    time.sleep(2)
    challenge.enter_form()
    time.sleep(1)
    challenge.access_report_abuse()
    
@then('Report abuse page opens')
def validated_send(context):
    challenge.tearDown()