import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Определяем путь к HTML-файлу
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML_PATH = "file://" + os.path.join(BASE_DIR, "index.html")


@pytest.fixture
def driver():
    """Фикстура для создания и закрытия драйвера"""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Запуск без графического интерфейса
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_page_title(driver):
    """Тест 1: Проверка заголовка страницы"""
    driver.get(HTML_PATH)
    h1 = driver.find_element(By.TAG_NAME, "h1")
    assert h1.text == "Обратная связь"


def test_form_fields_exist(driver):
    """Тест 2: Проверка наличия всех полей формы"""
    driver.get(HTML_PATH)
    assert driver.find_element(By.ID, "name") is not None
    assert driver.find_element(By.ID, "email") is not None
    assert driver.find_element(By.ID, "message") is not None
    assert driver.find_element(By.ID, "submitBtn") is not None


def test_form_submission(driver):
    """Тест 3: Проверка отправки формы"""
    driver.get(HTML_PATH)
    
    # Заполняем форму
    driver.find_element(By.ID, "name").send_keys("Тестов Пользователь")
    driver.find_element(By.ID, "email").send_keys("test@example.com")
    driver.find_element(By.ID, "message").send_keys("Тестовое сообщение")
    
    # Отправляем форму
    driver.find_element(By.ID, "submitBtn").click()
    
    # Ждём появления сообщения об успехе
    wait = WebDriverWait(driver, 5)
    success = wait.until(
        EC.visibility_of_element_located((By.ID, "successMessage"))
    )
    
    assert success.is_displayed()
    assert "Спасибо!" in success.text


def test_button_text(driver):
    """Тест 4: Проверка текста на кнопке"""
    driver.get(HTML_PATH)
    button = driver.find_element(By.ID, "submitBtn")
    assert button.text == "Отправить"