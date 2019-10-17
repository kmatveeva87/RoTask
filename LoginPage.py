import female as female
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait



driver = webdriver.Firefox(executable_path='C:\Users\kmatveeva\PycharmProjects\TestCasesForRo\drivers\geckodriver.exe')
# driver = webdriver.Chrome(executable_path='C:\Users\kmatveeva\PycharmProjects\TestCasesForRo\drivers\chromedriver.exe')
driver.maximize_window()

# to work with cookies the next command can be used
driver.delete_all_cookies()
driver.refresh()




driver.get('https://start.ro.co/rory/vaginal-dryness')



time.sleep(5)

# fill out all requested fields

email = driver.find_element_by_xpath("//form/div/div/input[@id='temporaryEmail']")
email.send_keys('first_name@gmail.com')
first_name = driver.find_element_by_id('firstName').send_keys('Ksenia')
last_name = driver.find_element_by_id('lastName').send_keys('Lastname')
password = driver.find_element_by_name('password')
password.send_keys('oriental25')
time.sleep(1)
agree = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div/div[2]/div/form/div[5]/div/div/label/div').click()
start_visit = driver.find_element_by_css_selector('.sc-bxivhb').click()

# when client redirected to the next page verify clients name and welcome text
assert driver.page_source.find("Hi Ksenia, thanks for starting your online visit.")

time.sleep(3)

# to continue
continue_my_visit = driver.find_element_by_xpath("//button[@class='button start-button button--primary']").click()

time.sleep(2)

# specify your gender
male = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/form/div[1]/div[2]/div[1]").click()

time.sleep(1)
# when client select gender "male" the website will notify him with following text
assert driver.page_source.find("Unfortunately, our prescription treatment for vaginal dryness is only available to women.")

# click got it and you will be redirected to the main page where user can select other options
got_it = driver.find_element_by_xpath("//button[@class='button button--block button--primary button--big']").click()

main_menu= driver.find_element_by_xpath("//ul[@id='menu-main-navigation']/li[@id='menu-item-4984']/a[@class='main-nav__link']").text
print main_menu

# female = driver.find_element_by_xpath("//form[@class='form basics']/div[@class='form-item'][1]/div[@class='choice']/div[@class='choice-item'][2]").click()
# date_of_birth = driver.find_element_by_id('dateOfBirth').send_keys('10/25/1987')
# zipcode = driver.find_element_by_id('zipcode').send_keys('99577')
# phone_number = driver.find_element_by_id('phone').send_keys('0000000000')
# time.sleep(2)
# btn_next = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/form/div[5]/button').click()











# driver.quit()



