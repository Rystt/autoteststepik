import os
from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select



browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

input1 = browser.find_element_by_name("firstname")
input1.send_keys("Kostya")
input2 = browser.find_element_by_name("lastname")
input2.send_keys("Su")
input3 = browser.find_element_by_name("email")
input3.send_keys("yadro@ya.ru")
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')
element = browser.find_element_by_name("file")
element.send_keys(file_path)

input4 = browser.find_element_by_xpath("//button[text()='Submit']")
input4.click()

time.sleep(10)
browser.quit()

# current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
# file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
# element.send_keys(file_path)