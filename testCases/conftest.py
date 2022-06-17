from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching Chrome browser..........")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox browser..........")
    else:
        driver = webdriver.Edge()
    return driver


def pytest_addoption(parser):               # This will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):           # This will return the browser value to setup method
    return request.config.getoption("--browser")

#####################Pytest HTML Reports#################################

# It is a hook for adding environment info to HTML report
def pytest_configure(config):
    config._metadata["Project Name"] = "nop Commerce"
    config._metadata["Module Name"] = "Customer"
    config._metadata["Tester"] = "Deepak"

# It is a hook for delete/modify environment info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA HOME", None)
    metadata.pop("Plugins", None)