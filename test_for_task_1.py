import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def get_barcode(product_name: str):
    driver = webdriver.Chrome()
    driver.get('https://dusty.pandemonium.itqc.ru/')

    input_product = driver.find_element(By.CSS_SELECTOR, 'input[name="prodname"]')
    input_product.clear()
    input_product.send_keys(product_name)

    button_order = driver.find_element(By.CSS_SELECTOR, 'button[class="btn-request"]')
    button_order.click()
    time.sleep(4)

    button_barcode = driver.find_element(By.CSS_SELECTOR, 'button[class="request__btn"]')
    button_barcode.click()
    time.sleep(22)

    field_barcode = driver.find_element(By.CSS_SELECTOR, 'input[class="request__field"]')
    field_barcode_value = field_barcode.get_attribute("value")
    return field_barcode_value



