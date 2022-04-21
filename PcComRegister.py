from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="chromedriver")
driver.maximize_window()
driver.get("https://yopmail.com/es/email-generator")

email = driver.find_element(By.ID,"egen").text
split = email.split('@')
psw = split[0]

driver.get("https://www.pccomponentes.com/login")
driver.find_element(By.XPATH,"//a[@href='/signup']").click()

sleep(3)
driver.find_element(By.ID,"name").send_keys("Bender")
sleep(1)
driver.find_element(By.ID,"email").send_keys(email)
sleep(2)
driver.find_element(By.ID ,"password").send_keys(psw)
sleep(3)
driver.find_element(By.ID ,"repeatPassword").click()
sleep(1)
driver.find_element(By.ID ,"repeatPassword").send_keys(psw)
sleep(3)
driver.find_element(By.ID,"policy").click()
sleep(3)
driver.find_element(By.XPATH,"//button[@type='submit']").click()
BD = open("UsersPC.txt","a")
BD.write(email+','+psw+'\n')
BD.close()
    