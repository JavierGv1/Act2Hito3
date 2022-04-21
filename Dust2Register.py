from operator import length_hint
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="chromedriver")
driver.maximize_window()
driver.get("https://yopmail.com/es/email-generator")

email = driver.find_element(By.ID,"egen").text
split = email.split('@')
psw = split[0]
driver.get("https://dust2.gg/mi-cuenta/")
driver.find_element(By.ID,"reg_email").send_keys(email)
driver.find_element(By.ID ,"reg_password").send_keys(psw)
driver.find_element(By.NAME,"register").send_keys(Keys.ENTER)

BD = open("UsersD2.txt","a")
BD.write(email+','+psw+'\n')
BD.close()
sleep(3)
driver.quit()