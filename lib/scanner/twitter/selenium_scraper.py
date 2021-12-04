import urllib.parse as tourl

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver import Safari

displayname = "Jayan Smart"

with Safari() as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("https://twitter.com/search?q=" +
               tourl.quote_plus(displayname) + "&src=typed_query&f=user")
