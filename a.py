from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\k_sur\8056\Sample\Driver\chromedriver.exe")
driver.get("http://demo.guru99.com/test/drag_drop.html")
driver.maximize_window()

src = driver.find_element(By.ID, "credit2")

des = driver.find_element(By.ID, "bank")

acc = ActionChains(driver)

acc.drag_and_drop(src, des).perform()

print("dgfhf")
