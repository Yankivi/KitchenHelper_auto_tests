from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import globals


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(globals.main_page)
    yield driver
    driver.quit()

@pytest.fixture
def admin_enter(driver):
    driver.get(globals.main_page)

    driver.find_element('xpath', '/html/body/main/form[1]/button').click()
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(globals.admin_pass)
    driver.find_element(By.XPATH, '/html/body/main/form/button').click()

    yield driver
    driver.quit()
