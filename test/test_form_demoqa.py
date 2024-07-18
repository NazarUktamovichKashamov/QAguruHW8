import os

from selene import browser, be, have

from page.page import registration

def test_form():
    registration.open_page()
    registration.first_name()
    registration.last_name()
    registration.user_email_adress()
    registration.choose_gender()
    registration.phone_number()
    registration.birthday()
    registration.choose_subject()
    registration.upload_image()
    registration.choose_hobby()
    registration.person_address()
    registration.submit()
    registration.check_result_of_registration()
