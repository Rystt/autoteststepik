from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

button = WebDriverWait(browser, 12).until (
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
button1 = browser.find_element_by_id("book")
button1.click()

browser.quit()

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

input1 = browser.find_element_by_id("answer")
input1.send_keys(y)
input4 = browser.find_element_by_xpath("//button[text()='Submit']")
input4.click()
