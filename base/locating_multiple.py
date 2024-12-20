
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

path = "C:\\Program Files (x86)\\chromedriver.exe"
service = Service(path)
driver = webdriver.Chrome(service=service)

query = "laptop"
for i in range(1,11):
    driver.get(f"https://www.flipkart.com/search?q={query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}")
    try:
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "_75nlfW"))
        )
        elements = driver.find_elements(By.CLASS_NAME, "_75nlfW")
        print(f"{len(elements)} items found")
        for elem in elements:
            print(elem.text)

    except Exception as e:
        print("Error:", e)
    time.sleep(10)
    driver.quit()
