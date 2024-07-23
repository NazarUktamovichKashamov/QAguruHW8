from selene import browser, have
import os
from pathlib import Path
from test_data.user import User


class RegistrationPage:
    def open_page(self):
        browser.open('/automation-practice-form')
        return self

    def first_name(self, first_name):
        browser.element('#firstName').type(first_name)
        return self

    def last_name(self, last_name):
        browser.element('#lastName').type(last_name)
        return self

    def user_email_adress(self, mail):
        browser.element('#userEmail').type(mail)
        return self

    def choose_gender(self):
        browser.element('[for="gender-radio-1').click()
        return self

    def phone_number(self, number):
        browser.element('#userNumber').type(number)
        return self

    def birthday(self):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element('.react-datepicker__year-select').element('[value="1977"]').click()
        browser.element('.react-datepicker__month-select').element('[value="7"]').click()
        browser.element('.react-datepicker__day--020').click()
        return self

    def subject(self, chem):
        browser.element('#subjectsInput').type(chem).press_enter()
        return self

    def photo(self, photo):
        browser.element('#uploadPicture').send_keys(os.path.abspath('../resources/photo.jpg'))
        return self

    def hobbies(self):
        browser.element('[for="hobbies-checkbox-2"]').click()
        return self

    def person_address(self, address):
        browser.element('#currentAddress').type(address)

    def type_state(self, state):
        browser.element('#react-select-3-input').type('Raja').press_enter()
        return(self)

    def type_city(self, city):
        browser.element('#react-select-4-input').type('Jaip').press_enter()
        return self

    def submit(self):
        browser.element('#submit').click()
        return self

    def check_result_of_registration(self):
        browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
        browser.element('.table').all('td').even.should(have.exact_texts
                                                        ('Walther White', 'heisenberg@drugs.com', 'Male', '8999999999',
                                                         '20 August,1977', 'Chemistry', 'Reading', 'photo.jpg',
                                                         'Albukerke, 39', 'Rajasthan Jaipur')
                                                        )
        return self


    def register_user(self, student: User):
        self.first_name(student.first_name)
        self.last_name(student.last_name)
        self.user_email_adress(student.email)
        self.choose_gender()
        self.phone_number(student.phone)
        self.birthday()
        self.subject(student.subject)
        self.hobbies()
        self.photo(student.photo)
        self.person_address(student.address)
        self.type_state(student.state)
        self.type_city(student.city)
        self.submit()
        self.check_result_of_registration()

