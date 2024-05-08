from selenium import webdriver
from bs4 import BeautifulSoup
import getpass
import requests
from selenium.webdriver.common.keys import Keys
import pprint

userid = str(input("Enter email address or number with country code: "))
password = getpass.getpass("Enter your password:")

driver = webdriver.Firefox()
driver.get("https://www.linkedin.com")
driver.implicitly_wait(6)
driver.find_element_by_xpath("""//*[@id="login-email"]""").send_keys(userid)
driver.find_element_by_xpath("""//*[@id="login-password"]""").send_keys(password)
driver.find_element_by_xpath("""//*[@id="login-submit"]""").click()
driver.get(
    "https://www.linkedin.com/in/andriyburkov/"
)  # Enter any of your connection profile Link

connectionName = driver.find_element_by_class_name(
    "pv-top-card-section__name"
).get_attribute("innerHTML")
print(connectionName)
driver.find_element_by_css_selector("button.contact-see-more-less").click()
content = driver.find_element_by_css_selector(
    ".pv-profile-section.pv-contact-info.artdeco-container-card.ember-view"
)
data = BeautifulSoup(content.get_attribute("innerHTML"), "lxml")
driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + "t")
for section in data.find_all("section"):
    for header in section.find_all("header"):
        if header.contents[0] == "Email":
            section.find_all("a")
            print("Email Address" + section.a.contents[0])
        if header.contents[0] == "Phone":
            section.find_all("a")
            print("Phone Number :" + section.a.contents[0])
        if header.contents[0] == "Website":
            section.find_all("a")
            print("Phone Number :" + section.a.contents[0])
