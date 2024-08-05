from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import os


def test_admin_enter():
    driver = webdriver.Chrome()
    driver.get('https://forms-s9jo.onrender.com/')

    driver.find_element('xpath', '/html/body/main/form[1]/button').click()
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('administratorLesko')
    driver.find_element(By.XPATH, '/html/body/main/form/button').click()

    assert driver.current_url == 'https://forms-s9jo.onrender.com/formsadmin'
    driver.quit()

# def check_exists_by_selector(driver, selector):
#     return len(driver.find_elements(By.CSS_SELECTOR, f'{selector}')) > 0
#
# def test_admin_replace_pic():
#     driver = webdriver.Chrome()
#     driver.get("https://forms-s9jo.onrender.com/")
#
#     driver.find_element('xpath', '/html/body/main/form[1]/button').click()
#     driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("administratorLesko")
#     driver.find_element(By.XPATH, '/html/body/main/form/button').click()
#
#     assert driver.current_url == 'https://forms-s9jo.onrender.com/formsadmin'
#
#     assert check_exists_by_selector(driver, 'img[src="https://academy.softclub.by/japan_new.jpg"]') == True
#     driver.find_element(By.XPATH, '/html/body/div/header/ul/li[2]/form/button').click()
#
#     assert driver.current_url == 'https://forms-s9jo.onrender.com/update'
#     number_element = driver.find_element(By.XPATH, '//img[@src="https://academy.softclub.by/japan_new.jpg"]/preceding-sibling::strong')
#     strong_text = number_element.text
#     picture_number = strong_text.strip('.')
#     select_pic = Select(driver.find_element(By.XPATH, '//*[@id="template-num"]'))
#     select_pic.select_by_value(f'{picture_number}')
#
#     # element = driver.find_element(By.XPATH, '//*[@id="template-form"]/button')
#     url_field = driver.find_element(By.XPATH, '//*[@id="new-url"]')
#     url_field.send_keys('https://as2.ftcdn.net/v2/jpg/03/29/19/59/1000_F_329195928_B2Gr0zA5DrREZ1GTWrxVNsT59H818Y9A.jpg')
#     url_field.send_keys(Keys.ENTER)
#
#     assert check_exists_by_selector(driver, 'img[src="https://academy.softclub.by/japan_new.jpg"]') == False
#     driver.quit()
#
# def wait_for_file(filename, directory, timeout=10):
#     file_path = os.path.join(directory, filename)
#
#     start_time = time.time()
#     while time.time() - start_time < timeout:
#         if os.path.exists(file_path):
#             return True
#         time.sleep(0.5)
#
#     return False
#
# def delete_file(filename, directory):
#     file_path = os.path.join(directory, filename)
#     try:
#         os.remove(file_path)
#     except OSError as e:
#         print(f"Ошибка при удалении файла: {e}")
#
#
# def test_download_stat():
#     driver = webdriver.Chrome()
#     driver.get("https://forms-s9jo.onrender.com/")
#
#     driver.find_element('xpath', '/html/body/main/form[1]/button').click()
#     driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("administratorLesko")
#     driver.find_element(By.XPATH, '/html/body/main/form/button').click()
#
#     assert driver.current_url == 'https://forms-s9jo.onrender.com/formsadmin'
#     time.sleep(5)
#     directory = 'C:\\Users\\vikak\\Downloads'
#     filename = 'data.xlsx'
#     driver.find_element(By.XPATH, '/html/body/div/header/ul/li[1]/button').click()
#     assert wait_for_file(filename, directory) == True
#     delete_file(filename, directory)
#
# def test_refrash_stat():
#     driver = webdriver.Chrome()
#
#     driver.get("https://forms-s9jo.onrender.com/")
#
#     driver.find_element('xpath', '/html/body/main/form[1]/button').click()
#     driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("administratorLesko")
#     driver.find_element(By.XPATH, '/html/body/main/form/button').click()
#
#     #Обнуление статистики
#     driver.find_element(By.XPATH, '/html/body/div/header/ul/li[3]/form/button').click()
#
#     #Заходим в пользователя
#     driver.get("https://forms-s9jo.onrender.com/")
#     driver.find_element(By.XPATH, '/html/body/main/form[2]/button').click()
#
#     assert driver.current_url == 'https://forms-s9jo.onrender.com/forms'
#
#     for i in range(1, 46):  # Генерация XPath для 45 выпадающих списков
#         xpath = f'//*[@id="myForm"]/select[{i}]'
#         select_element = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, xpath))
#         )
#         select = Select(select_element)
#         select.select_by_index(0)  # Выбрать первый вариант
#
#
#     button = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, '//*[@id="myForm"]/button'))
#     )
#     driver.execute_script("arguments[0].scrollIntoView(true);", button)
#     actions = ActionChains(driver)
#     actions.move_to_element(button).click().perform()
#
#     #Админка
#     driver.get("https://forms-s9jo.onrender.com/")
#     driver.find_element('xpath', '/html/body/main/form[1]/button').click()
#     driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("administratorLesko")
#     driver.find_element(By.XPATH, '/html/body/main/form/button').click()
#
#     for j in range(1, 46):
#         xpath = f'/html/body/div/div/table[{j}]/tbody/tr/th[2]'
#         voices = driver.find_element(By.XPATH, f'{xpath}')
#         assert voices.text == '1'
#
#     driver.find_element(By.XPATH, '/html/body/div/header/ul/li[3]/form/button').click()
#
#     for j in range(1, 46):
#         xpath = f'/html/body/div/div/table[{j}]/tbody/tr/th[2]'
#         voices = driver.find_element(By.XPATH, f'{xpath}')
#         assert voices.text == '0'
#
#     driver.quit()