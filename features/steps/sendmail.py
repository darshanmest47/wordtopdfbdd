import time

import autoit
from behave import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@given(u'User is already on the outlook website')
def step_impl(context):
    context.driver.get('https://outlook.live.com/')


@then(u'User clicks on the login from navigation links')
def step_impl(context):
    context.wt = WebDriverWait(context.driver, 200)
    context.wt.until(
        expected_conditions.presence_of_element_located((By.XPATH, "//nav[@class='auxiliary-actions']/ul/li[2]")))
    context.driver.find_element(By.XPATH, "//nav[@class='auxiliary-actions']/ul/li[2]").click()


@then(u'User lands on a page to enter email')
def step_impl(context):
    context.wt.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[contains(text(),'Sign')]")))


@then(u'User enters the email address into the email field {email}')
def step_impl(context, email):
    context.driver.find_element(By.XPATH, "//input[@type='email']").send_keys(email)


@then(u'User clicks on the Next Button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@value='Next']").click()


@then(u'User lands on the page to enter password')
def step_impl(context):
    context.wt.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[contains(@title,'dars')]")))


@then(u'User enters the password {password}')
def step_impl(context, password):
    context.driver.find_element(By.XPATH, "//input[@name='passwd']").send_keys(password)


@then(u'Clicks on the next button')
def step_impl(context):
    context.ele = context.driver.find_element(By.XPATH, "//div[@class='inline-block']/input[@id='idSIButton9']")
    context.driver.execute_script("arguments[0].click();", context.ele)


@then(u'User gets a popup to stay signed in and user sets value to Yes by clicking it')
def step_impl(context):
    print('Bypassed')





@then(u'User lands on the home page of oulook')
def step_impl(context):
    context.wt.until(expected_conditions.title_contains('Email - Darshan'))
    print('User is on the Outlook Homepage')


@then(u'User clicks on New email button')
def step_impl(context):
    context.wt.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[contains(text(),'New')]")))
    context.driver.find_element(By.XPATH, "//span[contains(text(),'New')]").click()


@then(u'User clicks on attach browsers a file and attaches the file')
def step_impl(context):
    context.wt.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//input[@aria-label='To']")))
    time.sleep(5)
    context.att = context.driver.find_element(By.XPATH,
                                "//span[@data-automationid='splitbuttonprimary']/span/span[text()='Attach']")

    time.sleep(5)
    context.att.click()
    context.wt.until(
        expected_conditions.presence_of_element_located((By.XPATH, "//span[contains(text(),'Browse this')]")))
    context.brows =context.driver.find_element(By.XPATH, "//span[contains(text(),'Browse this')]")

    time.sleep(5)
    context.brows.click()

    time.sleep(5)
    autoit.run("E:\\wordtopdfbdd\\resumes\\fileup.exe")
    time.sleep(5)


@then(u'User enters the value in to field {to}')
def step_impl(context, to):
    context.driver.find_element(By.XPATH, "//input[@aria-label='To']").send_keys(to)


@then(u'User clicks on cc button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//span[text()='Cc']").click()


@then(u'User enters value in cc field {cc}')
def step_impl(context, cc):
    context.driver.find_element(By.XPATH, "//input[@aria-label='Cc']").send_keys(cc)


@then(u'User clicks on Bcc field')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//span[text()='Bcc']").click()


@then(u'User sends value into Bcc field {bcc}')
def step_impl(context, bcc):
    context.driver.find_element(By.XPATH, "//input[@aria-label='Bcc']").send_keys(bcc)


@then(u'User enters the subject')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[contains(@aria-label,'subject')]").send_keys("Sent Converted Pdf")


@then(u'User enters the message into textbox')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[@role='textbox']").send_keys("Hi,\n"
                                                                              "Good Day Team Here is your converted pdf resume file.\n"
                                                                              "\n"
                                                                              "Thanks,\n"
                                                                              "Automated Team")


@then(u'User clicks on send to send an email')
def step_impl(context):
    time.sleep(30)
    context.driver.find_element(By.XPATH, "//span[text()='Send']").click()
    time.sleep(20)
