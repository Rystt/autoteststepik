import os
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)
input1 = browser.find_element_by_xpath("//button[text()='I want to go on a magical journey!']")
input1.click()
confirm = browser.switch_to.alert
confirm.accept()

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

input2 = browser.find_element_by_id("answer")
input2.send_keys(y)
input4 = browser.find_element_by_xpath("//button[text()='Submit']")
input4.click()

time.sleep(1)
browser.quit()
