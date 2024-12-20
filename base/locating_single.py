# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# path = "C:\\Program Files (x86)\\chromedriver.exe"  # Ensure proper escaping of backslashes
# service = Service(path)

# driver = webdriver.Chrome(service=service)

# # WebDriverWait(driver,5).until(
# #     EC.presence_of_all_elements_located((By.CSS_SELECTOR,"cPHDOP col-12-12"))
# # )
# query="laptop"
# driver.get(f"https://www.flipkart.com/search?q={query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
# input_element=driver.find_element(By.CSS_SELECTOR,"cPHDOP col-12-12")
# print(input_element.text)

# # input_element.send_keys("tech with tim" + Keys.ENTER)


# time.sleep(10)

# driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Define the path to the ChromeDriver executable
path = "C:\\Program Files (x86)\\chromedriver.exe"
service = Service(path)

# Initialize the WebDriver
driver = webdriver.Chrome(service=service)

# Navigate to the Flipkart search page
query = "laptop"
driver.get(f"https://www.flipkart.com/search?q={query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")

try:
    # Wait for the search result container to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "_75nlfW"))
    )
    input_element = driver.find_element(By.CLASS_NAME, "_75nlfW")
    print(input_element.text)
    print(input_element.get_attribute("outerHTML"))
except Exception as e:
    print("Error:", e)

# Pause for a few seconds before closing the browser
time.sleep(10)

# Quit the browser
driver.quit()
