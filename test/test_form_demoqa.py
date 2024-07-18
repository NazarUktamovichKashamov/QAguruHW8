import os

from selene import browser, be, have

def test_form():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Walther')
    browser.element('#lastName').type('White')
    browser.element('#userEmail').type('heisenberg@drugs.com')
    browser.element('[for="gender-radio-1').click()
    browser.element('#userNumber').type('89999999999')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select').element('[value="1977"]').click()
    browser.element('.react-datepicker__month-select').element('[value="7"]').click()
    browser.element('.react-datepicker__day--020').click()
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#subjectsInput').type('chem').press_enter()
    browser.element('#uploadPicture').send_keys(os.path.abspath('photo.jpg'))
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#currentAddress').type('Albukerke, 39')
    browser.element('#react-select-3-input').type('Raja').press_enter()
    browser.element('#react-select-4-input').type('Jaip').press_enter()
    browser.element('#submit').click()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table').all('td').even.should(have.exact_texts
        ('Walther White','heisenberg@drugs.com','Male','8999999999','20 August,1977','Chemistry','Reading','photo.jpg','Albukerke, 39','Rajasthan Jaipur')
    )
