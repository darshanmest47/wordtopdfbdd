import time

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@given(u'The User is already on the pdf conversion page')
def step_impl(context):
    context.driver.get("https://docupub.com/pdfconvert/")


@when(u'User successfully lands on the page')
def step_impl(context):
    context.wc = WebDriverWait(context.driver, 50)
    context.wc.until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@type='file']")))


@then(u'User uploads the word document to be converted')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@type='file']").send_keys(
        "E:\\wordtopdfbdd\\resumes\\Darshan_Resume.docx")


@then(u'User clicks on the upload button')
def step_impl(context):
    context.wc.until(expected_conditions.element_to_be_clickable((By.XPATH, "//input[@id='uploadBtn']")))
    context.driver.find_element(By.XPATH, "//input[@id='uploadBtn']").click()


@then(u'User recieves the link to the converted pdf file')
def step_impl(context):
    context.wc.until(expected_conditions.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Da')]")))


@then(u'User clicks on the link and downloads the converted file')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[contains(text(),'Da')]").click()
    time.sleep(20)
