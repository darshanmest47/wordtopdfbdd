from selenium import webdriver
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
import autoit
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import allure
from allure_commons.types import AttachmentType

def before_scenario(context,scenario):
    fp = FirefoxProfile()
    fp.set_preference("browser.download.manager.showWhenStarts", False)
    fp.set_preference("browser.download.manager.showAlertOnComplete", False)
    fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
    fp.set_preference("browser.download.dir", "E:\\wordtopdfbdd\\resumes")
    fp.set_preference("browser.download.folderList", 2)
    fp.set_preference("pdfjs.disabled", True)

    context.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=fp)


def after_scenario(context,scenario):
    if context.failed:
        print(context.scenario)

        allure.attach(context.driver.get_screenshot_as_png(), name="testfail", attachment_type=AttachmentType.PNG)
        context.driver.quit()
    else:

        context.driver.quit()