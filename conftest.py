import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name e.g.chrome OR firefox")


@pytest.fixture(scope='class')
def test_setup(request):

    browser = request.config.getoption("--browser")

    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="/home/prashant/PycharmProjects/AutomationFramework_1/drivers/chromedriver")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path="/home/prashant/PycharmProjects/AutomationFramework_1/drivers/geckodriver")

    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    yield

    driver.close()
    driver.quit()
    print("\nTest Completed")