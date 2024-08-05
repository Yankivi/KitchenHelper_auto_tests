from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import globals


def test_admin_enter(admin_enter, driver):
    assert driver.current_url == globals.admin_page


def test_user_enter(driver):
    driver.find_element(By.XPATH, '/html/body/main/form[2]/button').click()
    assert driver.current_url == globals.user_page


def check_exists_by_selector(driver, selector):
    return len(driver.find_elements(By.CSS_SELECTOR, f'{selector}')) > 0


def get_file_path(filename_for_uls):
    # путь к файлу относительно корня проекта
    return os.path.join(os.path.dirname(__file__), filename_for_uls)


def read_urls(file_path):
    with open(file_path, 'r') as file:
        urls = [line.strip() for line in file if line.strip()]
    return urls


def test_admin_replace_pic(admin_enter, driver):
    assert driver.current_url == globals.admin_page
    # Получение листа urls
    file_path = get_file_path("pic_urls")
    urls_list = read_urls(file_path)

    driver.find_element(By.XPATH, '/html/body/div/header/ul/li[2]/form/button').click()
    assert driver.current_url == globals.update_pic_page
    counter = 1
    for url in urls_list:
        select_pic = Select(driver.find_element(By.XPATH, '//*[@id="template-num"]'))
        select_pic.select_by_value(f'{str(counter)}')
        url_field = driver.find_element(By.XPATH, '//*[@id="new-url"]')
        url_field.send_keys(
            f'{urls_list[counter - 1]}')
        url_field.send_keys(Keys.ENTER)
        assert check_exists_by_selector(driver, f'img[src="{urls_list[counter - 1]}"]') is not False
        if counter == len(urls_list):
            break
        counter += 1
        driver.get(globals.update_pic_page)


def wait_for_file(filename, directory, timeout=10):
    file_path = os.path.join(directory, filename)

    start_time = time.time()
    while time.time() - start_time < timeout:
        if os.path.exists(file_path):
            return True
        time.sleep(0.5)

    return False


def delete_file(filename, directory):
    file_path = os.path.join(directory, filename)
    try:
        os.remove(file_path)
    except OSError as e:
        print(f"Ошибка при удалении файла: {e}")


def test_download_stat(admin_enter, driver):
    time.sleep(5)
    directory = globals.local_directory
    filename = 'data.xlsx'
    driver.find_element(By.XPATH, '/html/body/div/header/ul/li[1]/button').click()
    assert wait_for_file(filename, directory) == True
    delete_file(filename, directory)


def admin_log(driver):
    driver.get(globals.main_page)
    driver.find_element('xpath', '/html/body/main/form[1]/button').click()
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(globals.admin_pass)
    driver.find_element(By.XPATH, '/html/body/main/form/button').click()


def test_refresh_stat(admin_enter, driver):
    # Обнуление статистики
    driver.find_element(By.XPATH, '/html/body/div/header/ul/li[3]/form/button').click()
    # Заходим в пользователя
    driver.get(globals.main_page)
    driver.find_element(By.XPATH, '/html/body/main/form[2]/button').click()

    assert driver.current_url == globals.user_page

    for i in range(1, 46):  # Генерация XPath для 45 выпадающих списков
        xpath = f'//*[@id="myForm"]/select[{i}]'
        select_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        select = Select(select_element)
        select.select_by_index(0)  # Выбрать первый вариант

    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="myForm"]/button'))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", button)
    actions = ActionChains(driver)
    actions.move_to_element(button).click().perform()

    assert driver.current_url == globals.success_vote_page

    # Админка
    admin_log(driver)

    for j in range(1, 46):
        xpath = f'/html/body/div/div/table[{j}]/tbody/tr/th[2]'
        voices = driver.find_element(By.XPATH, f'{xpath}')
        assert voices.text == '1'

    driver.find_element(By.XPATH, '/html/body/div/header/ul/li[3]/form/button').click()

    for j in range(1, 46):
        xpath = f'/html/body/div/div/table[{j}]/tbody/tr/th[2]'
        voices = driver.find_element(By.XPATH, f'{xpath}')
        assert voices.text == '0'
