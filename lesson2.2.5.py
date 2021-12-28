from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"
browser.get(link)

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

input1 = browser.find_element_by_id("answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
input1.send_keys(y)
input2 = browser.find_element_by_id("robotCheckbox")
input2.click()
input3 = browser.find_element_by_id("robotsRule")
input3.click()
input4 = browser.find_element_by_xpath("//button[text()='Submit']")
input4.click()

time.sleep(10) #задержка на 10 секунд
browser.quit() #закрываем браузер