from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id("num1")
y_element = browser.find_element_by_id("num2")
x = int(x_element.text) + int(y_element.text)
y = str(x)
select = Select(browser.find_element_by_id("dropdown"))
select.select_by_visible_text(y)

input4 = browser.find_element_by_xpath("//button[text()='Submit']")
input4.click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()
#x = x_element.get_attribute("valuex")
#y = calc(x)
# input1 = browser.find_element_by_id("answer")
# input1.send_keys(x)
# input2 = browser.find_element_by_id("robotCheckbox")
# input2.click()
# input3 = browser.find_element_by_id("robotsRule")
# input3.click()

