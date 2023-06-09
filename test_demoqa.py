import os
import allure
from selene import be, have, by


@allure.title("Successful fill form")
def test_successful(setup_browser):
    browser = setup_browser

    with allure.step("Open registrations form"):
        browser.open('https://demoqa.com/automation-practice-form')
        browser.element('.practice-form-wrapper').should(have.text('Student Registration Form'))
        browser.driver.execute_script("$('#fixedban').remove()")

    with allure.step("Fill form"):
       browser.element("#firstName").type('Sergey')
       browser.element("#lastName").type('Petrov')
       browser.element("#userEmail").type('Petrov@mail.ru')
       browser.element("[value=Male]").double_click()
       browser.element("#userNumber").type('8999777777')
       browser.element('[id=dateOfBirthInput]').click()
       browser.element('.react-datepicker__month-select').click()
       browser.element('.react-datepicker__month-select').element('[value = "9"]').click()
       browser.element('.react-datepicker__year-select').click()
       browser.element('.react-datepicker__year-select').element('[value = "1991"]').click()
       browser.element('.react-datepicker__day--019').click()
       browser.element("#subjectsInput").type('History').press_enter()
       browser.element("#hobbiesWrapper").element(by.text("Sports")).click()
       # browser.element('#uploadPicture').send_keys(os.getcwd() + '/picture.jpg')
       browser.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
       browser.element('#currentAddress').type('Moscow')
       browser.element('#state').click()
       browser.element('#react-select-3-input').set_value('NCR').press_tab()
       browser.element('#react-select-4-input').type('Delhi').press_enter()
       browser.driver.execute_script("$('footer').remove()")
       browser.driver.execute_script("$('#submit').click()")

    with allure.step("Check form results"):
       browser.element('.modal-title').should(have.text('Thanks for submitting the form'))
       browser.all('tbody tr').should(have.exact_texts('Student Name Sergey Petrov', 'Student Email Petrov@mail.ru',
                                                    'Gender Male', 'Mobile 8999777777',
                                                    'Date of Birth 19 October,1991', 'Subjects History',
                                                    'Hobbies Sports', 'Picture',
                                                    'Address Moscow', 'State and City NCR Delhi'))
    #browser.driver.execute_script("$('#closeLargeModal').click()")


"""
registration_page.fill_first_name('Sergey')
    registration_page.fill_last_name('Petrov')
    registration_page.fill_email('Petrov@mail.ru')
    registration_page.fill_gender('Male')
    registration_page.fill_mobile('8999777777')
    registration_page.fill_date_of_birth('19', 'October', '1991')

    registration_page.fill_subjects('History')
    registration_page.fill_hobbie('Sports')
    registration_page.upload_picture('test.jpg')

    registration_page.fill_address('Moscow')
    registration_page.fill_state('NCR')
    registration_page.fill_city('Delhi')
"""




"""
import allure
from selene import have, by


@allure.title("Successful fill form")
def test_successful(setup_browser):
    browser = setup_browser
    first_name = "Alex"
    last_name = "Egorov"

    with allure.step("Open registrations form"):
        browser.open("https://demoqa.com/automation-practice-form")
        browser.element(".practice-form-wrapper").should(have.text("Student Registration Form"))
        browser.driver.execute_script("$('footer').remove()")
        browser.driver.execute_script("$('#fixedban').remove()")

    with allure.step("Fill form"):
        browser.element("#firstName").set_value(first_name)
        browser.element("#lastName").set_value(last_name)
        browser.element("#userEmail").set_value("alex@egorov.com")
        browser.element("#genterWrapper").element(by.text("Other")).click()
        browser.element("#userNumber").set_value("1231231230")
        # browser.element("#dateOfBirthInput").click()
        # browser.element(".react-datepicker__month-select").s("July")
        # browser.element(".react-datepicker__year-select").selectOption("2008")
        # browser.element(".react-datepicker__day--030:not(.react-datepicker__day--outside-month)").click()
        browser.element("#subjectsInput").send_keys("Maths")
        browser.element("#subjectsInput").press_enter()
        browser.element("#hobbiesWrapper").element(by.text("Sports")).click()
        # browser.element("#uploadPicture").uploadFromClasspath("img/1.png")
        browser.element("#currentAddress").set_value("Some street 1")
        browser.element("#state").click()
        browser.element("#stateCity-wrapper").element(by.text("NCR")).click()
        browser.element("#city").click()
        browser.element("#stateCity-wrapper").element(by.text("Delhi")).click()
        browser.element("#submit").click()

    with allure.step("Check form results"):
        browser.element("#example-modal-sizes-title-lg").should(have.text("Thanks for submitting the form"))
        # browser.element(".table-responsive").should(
        #     have.texts(first_name, last_name, "alex@egorov.com", "Some street 1"))

"""


