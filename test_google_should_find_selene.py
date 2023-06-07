from selene.support.shared import browser
from selene import be, have

def test_check_chrome():
    browser.open('')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
    browser.quit()

def test_check_wrong_result():
    browser.open('')
    browser.element('[name="q"]').should(be.blank).type('rjsefldsjfljsd').press_enter()
    browser.element('[class="card-section"]').should(have.text("По запросу rjsefldsjfljsd ничего не найдено"))
    browser.quit()
