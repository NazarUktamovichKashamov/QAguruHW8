from selene import browser, command, have
import os


class RegistrationPage:
    def open_page(self):
        browser.open('/automation-practice-form')
        return self

    def first_name(self):
        browser.element('#firstName').type('Walther')
        return self

    def last_name(self):
        browser.element('#lastName').type('White')
        return self

    def user_email_adress(self):
        browser.element('#userEmail').type('heisenberg@drugs.com')
        return self

    def choose_gender(self):
        browser.element('[for="gender-radio-1').click()
        return self

    def phone_number(self):
        browser.element('#userNumber').type('89999999999')
        return self

    def birthday(self):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element('.react-datepicker__year-select').element('[value="1977"]').click()
        browser.element('.react-datepicker__month-select').element('[value="7"]').click()
        browser.element('.react-datepicker__day--020').click()
        return self

    def choose_subject(self):
        browser.element('#subjectsInput').type('chem').press_enter()
        return self

    def upload_image(self):
        browser.element('#uploadPicture').send_keys(os.path.abspath('../resources/photo.jpg'))
        return self

    def choose_hobby(self):
        browser.element('[for="hobbies-checkbox-2"]').click()
        return self

    def person_address(self):
        browser.element('#currentAddress').type('Albukerke, 39')
        browser.element('#react-select-3-input').type('Raja').press_enter()
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

registration = RegistrationPage()
