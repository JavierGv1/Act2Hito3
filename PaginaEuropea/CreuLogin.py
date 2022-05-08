import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

BD = open("UsersCreu.txt","r").read()
lines = BD.splitlines()
line = random.choice(lines)
split = line.split(',')
email = split[0]
psw = split[1]

driver = webdriver.Chrome(executable_path="./chromedriver")
driver.maximize_window()
driver.get("https://www.creushop.com/es/")

Wait5 = WebDriverWait(driver,5)
Wait20 = WebDriverWait(driver,20)

element = Wait5.until(EC.element_to_be_clickable((By.XPATH,"/html/body/main/header/div/div[2]/div/div/div[3]/div[3]/a/i")))
driver.find_element(By.XPATH,"/html/body/main/header/div/div[2]/div/div/div[3]/div[3]/a/i").click()

element = Wait5.until(EC.element_to_be_clickable((By.XPATH,"/html/body/main/header/div/div[2]/div/div/div[3]/div[3]/div/ul/li[1]/a/span")))
driver.find_element(By.XPATH,"/html/body/main/header/div/div[2]/div/div/div[3]/div[3]/div/ul/li[1]/a/span").click()

element = Wait5.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div/div[2]/div[1]/div[1]/form/div[3]/input")))
driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[1]/div[1]/form/div[3]/input").send_keys(email)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[1]/div[1]/form/div[4]/input").send_keys(psw)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[1]/div[1]/form/div[6]/button/span[2]").click()

sleep(3)

element = Wait5.until(EC.element_to_be_clickable((By.XPATH,"/html/body/main/header/div/div[2]/div/div/div[3]/div[3]/a/i")))
driver.find_element(By.XPATH,"/html/body/main/header/div/div[2]/div/div/div[3]/div[3]/a/i").click()