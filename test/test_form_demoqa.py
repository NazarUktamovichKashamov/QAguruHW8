import os

from selene import browser, be, have

from page.pages import RegistrationPage
from test_data.user import User

def test_registration():
    student = User(first_name='Walther', last_name='White', email='heisenberg@drugs.com', gender='Male', phone='89999999999', birthday='20 July,1977', subject='Chemistry', hobbies='Reading', photo='photo.jpg', address='Albukerke, 39', state='Rajahstan', city='Jaipur')
    form_page = RegistrationPage()
    form_page.open_page()
    form_page.register_user(student)

