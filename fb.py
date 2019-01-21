#!usr/bin/ python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
usr="kaustubhsharma97"
pwd="qwertyuiop"
driver=webdriver.Firefox()
driver.get("http://facebook.com")
assert "Facebook" in driver.title
element=driver.find_element_by_id("email")
element.send_keys(usr)
element=driver.find_element_by_id("pass")
element.send_keys(pwd)
element.send_keys(Keys.RETURN)
